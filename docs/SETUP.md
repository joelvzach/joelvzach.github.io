# Website Setup Documentation

## Site Overview

This website now uses **Jekyll** (static site generator) to manage essays and pages.

**Tech Stack:**
- Jekyll 4.3 (GitHub Pages native support)
- Markdown for essay content
- Liquid templating
- Vanilla JavaScript for search/filter

**Key Directories:**
- `_essays/` - Essay collection (auto-generated from Medium exports)
- `_layouts/` - Page templates
- `_includes/` - Reusable components (header, footer)
- `assets/images/essays/` - Essay images

## Adding Social Links

To add your social media profiles, update the following files:

### Files to Edit

1. **index.html** - Contact section (near bottom)
2. **about.html** - Connect section (near bottom)
3. **Optional: Add a footer with social links in all pages**

### Example Format

Add links in the contact/connect sections:

```html
<p>Email: <a href="mailto:jzachariah@binghamton.edu">jzachariah@binghamton.edu</a></p>
<p>
  <a href="https://linkedin.com/in/yourusername" target="_blank">LinkedIn</a> |
  <a href="https://github.com/joelvzach" target="_blank">GitHub</a> |
  <a href="https://twitter.com/joelvzach" target="_blank">Twitter</a>
</p>
```

### Recommended Links

- **LinkedIn:** `https://linkedin.com/in/yourusername`
- **GitHub:** `https://github.com/joelvzach`
- **Twitter/X:** `https://twitter.com/joelvzach`
- **Google Scholar:** (if applicable)
- **ResearchGate:** (if applicable)

---

## Adding New Essays

### Option 1: Manual Creation

1. Create a new Markdown file: `_essays/YYYY-MM-DD-slug.md`
2. Add front matter at the top:

```yaml
---
layout: essay
title: "Your Essay Title"
subtitle: "Optional subtitle"
date: 2026-01-01 00:00:00 +0000
categories: [general]
read_time: 5
---
```

3. Write content in Markdown below front matter
4. Essay automatically appears on `essays.html` listing

### Option 2: Convert from Medium Export

Use the conversion script:

```bash
python3 convert_medium_to_jekyll.py --limit 10
```

See `../docs/ESSAY_MIGRATION.md` for full details.

---

## Adding New Portfolio Projects

1. Add a new `.card` div in `portfolio.html`
2. Include title, meta (company/date), and bullet points

### Project Card Template

```html
<div class="card">
  <h3>Project Title</h3>
  <div class="meta">Company/Organization | Date Range</div>
  <ul>
    <li>Achievement or responsibility</li>
    <li>Another achievement</li>
  </ul>
</div>
```

---

## Site Structure

```
joelvzach.github.io/
├── _config.yml              (Jekyll configuration)
├── Gemfile                  (Ruby dependencies)
├── _layouts/
│   ├── default.html         (Base template)
│   └── essay.html           (Essay template)
├── _includes/
│   ├── header.html          (Navigation)
│   └── footer.html          (Footer)
├── _essays/                 (Essay collection - auto-generated)
│   └── YYYY-MM-DD-slug.md   (Individual essays)
├── index.html               (Home page)
├── about.html               (About page)
├── portfolio.html           (Portfolio/Projects page)
├── essays.html              (Essays list with search/filter)
├── resume.html              (Full resume page)
├── CNAME                    (Domain: joelvzach.com)
├── convert_medium_to_jekyll.py (Conversion script)
├── docs/
│   ├── SETUP.md             (This file)
│   ├── PORKBUN_DNS.md       (DNS setup)
│   └── ESSAY_MIGRATION.md   (Essay conversion guide)
└── assets/
    ├── css/
    │   └── style.css        (LaTeX-inspired stylesheet)
    ├── js/
    │   └── main.js          (Navigation + search)
    └── images/
        └── essays/          (Essay images)
```

---

## Deployment Workflow

### For Regular Updates (no Jekyll changes)

1. Make changes locally
2. Commit: `git add . && git commit -m "description"`
3. Push: `git push origin main`
4. GitHub Pages auto-deploys (~1-2 minutes)
5. Visit `joelvzach.com` to verify

### For Jekyll/Essay Updates

1. Convert essays if needed: `python3 convert_medium_to_jekyll.py`
2. Stage all changes: `git add .`
3. Commit: `git commit -m "Add migrated essays"`
4. Push: `git push origin main`
5. GitHub Pages builds with Jekyll (~2-3 minutes)
6. Visit `joelvzach.com/essays` to verify

**Note:** First push with Jekyll may take longer as GitHub builds the site.

---

## Porkbun DNS Configuration

See `PORKBUN_DNS.md` for DNS setup instructions.
