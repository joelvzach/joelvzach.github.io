# Website Setup Documentation

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

1. Create a new HTML file: `essay-slug.html` (use the placeholder as template)
2. Add the essay to `essays.html` list
3. Update date and content

### Essay Template Structure

```html
<article>
  <header>
    <h1>Your Essay Title</h1>
    <p class="text-muted">Month Year · X min read</p>
  </header>
  
  <section>
    <h2>Section Heading</h2>
    <p>Your content here...</p>
  </section>
  
  <!-- More sections as needed -->
</article>
```

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
├── index.html          (Home page)
├── about.html          (About page)
├── portfolio.html      (Portfolio/Projects page)
├── essays.html         (Essays list page)
├── essay-placeholder.html (Sample essay)
├── resume.html         (Full resume page)
├── CNAME               (Domain configuration: joelvzach.com)
├── docs/
│   └── SETUP.md        (This file)
└── assets/
    ├── css/
    │   └── style.css   (LaTeX-inspired stylesheet)
    └── js/
        └── main.js     (Navigation active state)
```

---

## Deployment Workflow

1. Make changes locally
2. Commit: `git add . && git commit -m "description"`
3. Push: `git push origin main`
4. GitHub Pages auto-deploys (~1-2 minutes)
5. Visit `joelvzach.com` to verify

---

## Porkbun DNS Configuration

See `PORKBUN_DNS.md` for DNS setup instructions.
