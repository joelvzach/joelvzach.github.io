# Porkbun DNS Configuration for GitHub Pages

## Step-by-Step Instructions

### 1. Login to Porkbun

Go to [porkbun.com](https://porkbun.com) and login to your account.

### 2. Access DNS Settings

1. Click on your account name (top right)
2. Select "Domains" from the dropdown
3. Find `joelvzach.com` in your domain list
4. Click the "DNS" button (or "Manage DNS")

### 3. Add/Update DNS Records

Add the following records. **Remove any existing conflicting records** (especially any existing A records or CNAME for @ or www).

| Type  | Host | Value                      | TTL     |
|-------|------|----------------------------|---------|
| A     | @    | 185.199.108.153            | Default |
| A     | @    | 185.199.109.153            | Default |
| A     | @    | 185.199.110.153            | Default |
| A     | @    | 185.199.111.153            | Default |
| CNAME | www  | joelvzach.github.io        | Default |

### 4. How to Add Each Record

For each record:

1. Click "Add Record" or the "+" button
2. Select the **Type** (A or CNAME)
3. Enter the **Host** (@ or www)
4. Enter the **Value/Answer** (IP address or domain)
5. Leave TTL as "Default" or "Auto"
6. Click "Save" or "Add Record"

### 5. Remove Conflicting Records

If you see any of these, **delete them**:

- Existing A records for `@` pointing to other IPs
- Existing CNAME for `www` pointing elsewhere
- Any URL forwarding/redirects for joelvzach.com

### 6. Verify CNAME File

Make sure the `CNAME` file in your repository contains:

```
joelvzach.com
```

(Already configured in the repo)

### 7. Enable GitHub Pages

1. Go to your repo: `https://github.com/joelvzach/joelvzach.github.io`
2. Click **Settings** (top tab)
3. Click **Pages** (left sidebar)
4. Under "Source", select:
   - **Branch:** `main`
   - **Folder:** `/ (root)`
5. Click **Save**

### 8. Wait for Propagation

- DNS changes: 15-30 minutes (can take up to 48 hours, but usually fast with Porkbun)
- GitHub Pages build: 1-2 minutes

### 9. Verify Setup

1. Visit `https://joelvzach.github.io` - should show your site
2. Visit `https://joelvzach.com` - should show your site (after DNS propagates)
3. Both should work interchangeably

### 10. Enable HTTPS (Automatic)

GitHub Pages automatically provides HTTPS via Let's Encrypt. After DNS propagates:

1. Go back to Settings → Pages
2. Check "Enforce HTTPS" (once available)
3. Your site will be accessible at `https://joelvzach.com`

---

## Troubleshooting

### Site not loading at joelvzach.com

- Wait 15-30 minutes for DNS propagation
- Clear browser cache or try incognito mode
- Use `dig joelvzach.com` or [whatsmydns.net](https://whatsmydns.net) to check DNS propagation

### GitHub Pages shows 404

- Verify GitHub Pages is enabled in Settings → Pages
- Check that files are in the `main` branch root directory
- Look at GitHub Actions tab for build errors

### SSL certificate not working

- Wait a few hours after DNS propagation
- GitHub auto-provisions SSL certificates
- Ensure "Enforce HTTPS" is checked in Pages settings

---

## Quick Reference

**GitHub Pages IPs:**
```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

**CNAME for www:**
```
joelvzach.github.io
```

**Links:**
- Porkbun DNS: https://porkbun.com/account/domains
- GitHub Pages Settings: https://github.com/joelvzach/joelvzach.github.io/settings/pages
- DNS Propagation Check: https://whatsmydns.net
