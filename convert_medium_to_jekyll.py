#!/usr/bin/env python3
"""
Medium to Jekyll Essay Converter

Converts Medium HTML exports to Jekyll-compatible Markdown essays.
Automatically extracts title, date, subtitle, content, and downloads images.

Usage:
    python convert_medium_to_jekyll.py [options]

Options:
    --input-dir     Directory containing Medium HTML exports (default: ../essays/old_essays_from_medium/posts)
    --output-dir    Directory for Jekyll essays (default: _essays)
    --images-dir    Directory for downloaded images (default: assets/images/essays)
    --limit         Number of essays to convert (default: all)
    --dry-run       Show what would be converted without making changes
"""

import os
import re
import sys
import argparse
import requests
from html.parser import HTMLParser
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
import hashlib

class MediumHTMLParser(HTMLParser):
    """Parse Medium HTML exports and extract content."""
    
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.in_subtitle = False
        self.in_body = False
        self.in_footer = False
        self.in_time = False
        self.title = ""
        self.subtitle = ""
        self.body_html = ""
        self.date_str = ""
        self.author = ""
        self.medium_link = ""
        self.images = []
        self.current_tag = None
        self.body_depth = 0
        self.skip_tags = {'footer', 'script', 'style'}
        self.skip_depth = 0
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        if tag == 'h1' and 'class' in attrs_dict and 'p-name' in attrs_dict['class']:
            self.in_title = True
            
        elif tag == 'section' and attrs_dict.get('data-field') == 'subtitle':
            self.in_subtitle = True
            
        elif tag == 'section' and attrs_dict.get('data-field') == 'body':
            self.in_body = True
            self.body_depth = 1
            
        elif self.in_body and tag in self.skip_tags:
            self.skip_depth += 1
            
        elif self.in_body and self.skip_depth == 0:
            if tag == 'time' and 'class' in attrs_dict and 'dt-published' in attrs_dict['class']:
                self.in_time = True
            elif tag == 'img':
                src = attrs_dict.get('src', '')
                if src and src.startswith('http'):
                    self.images.append(src)
            elif tag == 'a' and 'class' in attrs_dict and 'p-canonical' in attrs_dict['class']:
                self.medium_link = attrs_dict.get('href', '')
            elif tag == 'a' and 'class' in attrs_dict and 'h-card' in attrs_dict['class']:
                self.in_author = True
            else:
                # Reconstruct HTML for body content
                if tag in ['p', 'h2', 'h3', 'h4', 'blockquote', 'ul', 'ol', 'li', 'pre', 'code', 'strong', 'em', 'a', 'img', 'figure', 'figcaption', 'hr']:
                    attrs_str = ' '.join([f'{k}="{v}"' for k, v in attrs_dict.items() if k not in ['class', 'data-field']])
                    if attrs_str:
                        self.body_html += f'<{tag} {attrs_str}>'
                    else:
                        self.body_html += f'<{tag}>'
                    
        elif self.in_footer and tag == 'a' and 'class' in attrs_dict and 'h-card' in attrs_dict['class']:
            self.in_author = True
            
        if tag == 'footer':
            self.in_footer = True
            
    def handle_endtag(self, tag):
        if tag == 'h1':
            self.in_title = False
            
        elif tag == 'section':
            if self.in_subtitle:
                self.in_subtitle = False
            elif self.in_body:
                self.body_depth -= 1
                if self.body_depth == 0:
                    self.in_body = False
                    
        elif self.in_body and tag in self.skip_tags:
            self.skip_depth -= 1
            
        elif self.in_body and self.skip_depth == 0:
            if tag in ['p', 'h2', 'h3', 'h4', 'blockquote', 'ul', 'ol', 'li', 'pre', 'code', 'strong', 'em', 'a', 'figure', 'figcaption']:
                self.body_html += f'</{tag}>'
                
        elif tag == 'time':
            self.in_time = False
            
        elif tag == 'footer':
            self.in_footer = False
            
    def handle_data(self, data):
        if self.in_title:
            self.title += data
        elif self.in_subtitle:
            self.subtitle += data
        elif self.in_time:
            self.date_str += data
        elif self.in_body and self.skip_depth == 0:
            self.body_html += data
            
    def get_data(self):
        return {
            'title': self.title.strip(),
            'subtitle': self.subtitle.strip(),
            'body_html': self.body_html.strip(),
            'date_str': self.date_str.strip(),
            'medium_link': self.medium_link,
            'images': self.images
        }


def parse_medium_html(html_content):
    """Parse Medium HTML and return extracted data."""
    parser = MediumHTMLParser()
    parser.feed(html_content)
    return parser.get_data()


def extract_date_from_filename(filename):
    """Extract date from Medium export filename."""
    match = re.match(r'(\d{4}-\d{2}-\d{2})_', filename)
    if match:
        return match.group(1)
    return None


def parse_medium_date(date_str):
    """Parse Medium date string to datetime."""
    try:
        # Format: 2019-10-22T13:57:06.337Z
        return datetime.fromisoformat(date_str.replace('Z', '+00:00'))
    except:
        return None


def slugify(text):
    """Convert text to URL-safe slug."""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


def download_image(url, output_dir, essay_slug):
    """Download image from URL and save locally."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Extract filename from URL
        parsed = urlparse(url)
        filename = os.path.basename(parsed.path)
        if not filename:
            filename = f'image_{hashlib.md5(url.encode()).hexdigest()[:8]}.jpg'
        
        # Ensure unique filename
        base, ext = os.path.splitext(filename)
        output_path = output_dir / f"{essay_slug}_{base}{ext}"
        
        # Write file
        with open(output_path, 'wb') as f:
            f.write(response.content)
        
        # Return relative path for Markdown
        return f"/assets/images/essays/{output_path.name}"
        
    except Exception as e:
        print(f"  ⚠️  Failed to download image: {url} - {e}")
        return url  # Return original URL if download fails


def html_to_markdown(html):
    """Simple HTML to Markdown conversion."""
    markdown = html
    
    # Convert common HTML tags to Markdown
    markdown = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1\n', markdown, flags=re.DOTALL)
    markdown = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1\n', markdown, flags=re.DOTALL)
    markdown = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1\n', markdown, flags=re.DOTALL)
    markdown = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1\n', markdown, flags=re.DOTALL)
    markdown = re.sub(r'<strong>(.*?)</strong>', r'**\1**', markdown, flags=re.DOTALL)
    markdown = re.sub(r'<b>(.*?)</b>', r'**\1**', markdown, flags=re.DOTALL)
    markdown = re.sub(r'<em>(.*?)</em>', r'_\1_', markdown, flags=re.DOTALL)
    markdown = re.sub(r'<i>(.*?)</i>', r'_\1_', markdown, flags=re.DOTALL)
    markdown = re.sub(r'<a href="([^"]+)"[^>]*>(.*?)</a>', r'[\2](\1)', markdown, flags=re.DOTALL)
    markdown = re.sub(r'<blockquote[^>]*>(.*?)</blockquote>', r'> \1\n', markdown, flags=re.DOTALL | re.MULTILINE)
    markdown = re.sub(r'<pre[^>]*>(.*?)</pre>', r'```\n\1\n```', markdown, flags=re.DOTALL)
    markdown = re.sub(r'<code>(.*?)</code>', r'`\1`', markdown, flags=re.DOTALL)
    markdown = re.sub(r'<ul[^>]*>(.*?)</ul>', r'\1', markdown, flags=re.DOTALL)
    markdown = re.sub(r'<ol[^>]*>(.*?)</ol>', r'\1', markdown, flags=re.DOTALL)
    markdown = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', markdown, flags=re.DOTALL)
    markdown = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n', markdown, flags=re.DOTALL)
    markdown = re.sub(r'<br\s*/?>', r'\n', markdown)
    markdown = re.sub(r'<hr\s*/?>', r'---\n', markdown)
    
    # Remove remaining HTML tags
    markdown = re.sub(r'<[^>]+>', '', markdown)
    
    # Clean up whitespace
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)
    
    return markdown.strip()


def calculate_read_time(markdown_text):
    """Calculate estimated read time in minutes."""
    words = len(markdown_text.split())
    read_time = max(1, round(words / 200))  # 200 words per minute
    return read_time


def convert_essay(input_path, output_dir, images_dir, dry_run=False):
    """Convert a single Medium HTML file to Jekyll Markdown."""
    print(f"Processing: {input_path.name}")
    
    # Read HTML file
    with open(input_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Parse HTML
    data = parse_medium_html(html_content)
    
    # Skip if no title found
    if not data['title']:
        print(f"  ⚠️  No title found, skipping")
        return None
    
    # Extract date from filename if not in HTML
    date_from_file = extract_date_from_filename(input_path.name)
    
    # Parse date
    if data['date_str']:
        pub_date = parse_medium_date(data['date_str'])
    elif date_from_file:
        pub_date = datetime.strptime(date_from_file, '%Y-%m-%d')
    else:
        pub_date = datetime.now()
    
    # Generate slug from title
    slug = slugify(data['title'])
    if len(slug) > 60:
        slug = slug[:60].rstrip('-')
    
    # Add date prefix to slug
    date_prefix = pub_date.strftime('%Y-%m-%d')
    output_filename = f"{date_prefix}-{slug}.md"
    
    # Download images
    image_map = {}
    if data['images'] and not dry_run:
        print(f"  Downloading {len(data['images'])} images...")
        for i, img_url in enumerate(data['images']):
            local_path = download_image(img_url, images_dir, f"{slug}_{i:02d}")
            image_map[img_url] = local_path
    
    # Convert HTML to Markdown
    markdown_content = html_to_markdown(data['body_html'])
    
    # Replace image URLs with local paths
    for original_url, local_path in image_map.items():
        markdown_content = markdown_content.replace(original_url, local_path)
    
    # Calculate read time
    read_time = calculate_read_time(markdown_content)
    
    # Determine categories based on title/filename
    categories = []
    filename_lower = input_path.name.lower()
    title_lower = data['title'].lower()
    
    if 'twtw' in filename_lower or 'tw---' in filename_lower:
        categories.append('tw')
    if 'pycon' in filename_lower or 'hackathon' in filename_lower or 'conference' in title_lower:
        categories.append('events')
    if 'freshman' in title_lower or 'student' in title_lower or 'university' in title_lower:
        categories.append('student-life')
    if 'community' in title_lower or 'foss' in title_lower or 'overboard' in title_lower:
        categories.append('community')
    if 'disprove' in title_lower or 'opinion' in title_lower or 'think' in title_lower:
        categories.append('opinion')
    
    if not categories:
        categories.append('general')
    
    # Generate front matter
    front_matter = f"""---
layout: essay
title: "{data['title'].replace('"', '\\"')}"
"""
    
    if data['subtitle']:
        front_matter += f"""subtitle: "{data['subtitle'].replace('"', '\\"')}"
"""
    
    front_matter += f"""date: {pub_date.strftime('%Y-%m-%d %H:%M:%S %z')}
categories: [{', '.join(categories)}]
read_time: {read_time}
medium_link: "{data['medium_link']}"
---

"""
    
    # Write output file
    output_path = output_dir / output_filename
    
    if not dry_run:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(front_matter)
            f.write(markdown_content)
            f.write('\n')
        
        print(f"  ✅ Created: {output_path.name}")
    else:
        print(f"  [DRY RUN] Would create: {output_path.name}")
    
    return {
        'title': data['title'],
        'date': pub_date,
        'output_file': output_filename,
        'categories': categories
    }


def main():
    parser = argparse.ArgumentParser(description='Convert Medium HTML exports to Jekyll essays')
    parser.add_argument('--input-dir', type=str, default='../essays/old_essays_from_medium/posts',
                        help='Directory containing Medium HTML exports')
    parser.add_argument('--output-dir', type=str, default='_essays',
                        help='Directory for Jekyll essays')
    parser.add_argument('--images-dir', type=str, default='assets/images/essays',
                        help='Directory for downloaded images')
    parser.add_argument('--limit', type=int, default=None,
                        help='Number of essays to convert (default: all)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Show what would be converted without making changes')
    
    args = parser.parse_args()
    
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    images_dir = Path(args.images_dir)
    
    # Validate input directory
    if not input_dir.exists():
        print(f"Error: Input directory does not exist: {input_dir}")
        sys.exit(1)
    
    # Create output directories
    if not args.dry_run:
        output_dir.mkdir(parents=True, exist_ok=True)
        images_dir.mkdir(parents=True, exist_ok=True)
    
    # Find HTML files (exclude drafts)
    html_files = [f for f in input_dir.glob('*.html') if not f.name.startswith('draft_')]
    html_files.sort(key=lambda f: f.name)
    
    # Apply limit if specified
    if args.limit:
        html_files = html_files[:args.limit]
    
    print(f"Found {len(html_files)} essays to convert")
    if args.limit:
        print(f"Limited to first {args.limit} essays")
    if args.dry_run:
        print("DRY RUN - No files will be written\n")
    
    # Convert essays
    converted = []
    for html_file in html_files:
        result = convert_essay(html_file, output_dir, images_dir, args.dry_run)
        if result:
            converted.append(result)
    
    # Summary
    print(f"\n{'='*60}")
    print(f"Conversion complete!")
    print(f"  Processed: {len(html_files)} files")
    print(f"  Converted: {len(converted)} essays")
    if converted:
        print(f"  Output directory: {output_dir.absolute()}")
        print(f"  Images directory: {images_dir.absolute()}")
    
    # Show converted essays
    if converted:
        print(f"\nConverted essays:")
        for essay in sorted(converted, key=lambda x: x['date'], reverse=True):
            print(f"  - {essay['date'].strftime('%Y-%m-%d')} | {essay['title'][:60]}")


if __name__ == '__main__':
    main()
