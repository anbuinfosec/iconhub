# GitHub Pages Deployment Guide

## Overview

This project uses **GitHub Actions** to automatically build and deploy your icon gallery to GitHub Pages. The build process uses Python to scan your icon folders and generate a JSON file with all categories and icon information.

## How It Works

### 1. Build Script (`build.py`)

The Python script:
- Scans the `icons/` directory for category folders
- Counts all icon files in each category (SVG, PNG, JPG, GIF, WebP)
- Generates `categories.json` with complete category data
- Assigns appropriate icons to each category

**Run locally:**
```bash
python3 build.py
```

**Output:** `categories.json` containing:
```json
{
  "cloud": {
    "name": "Cloud",
    "icon": "bi-cloud-fill",
    "count": 23,
    "files": ["amazon.svg", "aws.svg", ...]
  },
  ...
}
```

### 2. GitHub Actions Workflow (`.github/workflows/deploy.yml`)

The workflow automatically runs on every push to `main` branch:

**Steps:**
1. **Checkout** - Gets your code
2. **Setup Python** - Installs Python 3.11
3. **Build** - Runs `build.py` to generate `categories.json`
4. **Deploy** - Publishes to GitHub Pages

### 3. Frontend (`script.js`)

The JavaScript now:
- Loads categories from `categories.json` instead of trying to parse directories
- Works perfectly on GitHub Pages (no directory listing needed)
- Fast and reliable

## Setup Instructions

### First Time Setup

1. **Push your code to GitHub:**
   ```bash
   git add .
   git commit -m "Add GitHub Actions workflow"
   git push origin main
   ```

2. **Enable GitHub Pages:**
   - Go to your repository on GitHub
   - Click **Settings** → **Pages**
   - Under "Build and deployment" source, select **GitHub Actions**

3. **Wait for deployment:**
   - Go to **Actions** tab
   - Watch the workflow run
   - When complete, your site is live!

### Your Site URL

After deployment, your site will be available at:
```
https://yourusername.github.io/repository-name/
```

For example:
```
https://anbuinfosec.github.io/iconhub/
```

## Adding New Icons

1. **Add icon files:**
   ```bash
   # Add icons to existing category
   cp new-icon.svg icons/cloud/
   
   # Or create new category
   mkdir icons/my-category
   cp *.svg icons/my-category/
   ```

2. **Test locally:**
   ```bash
   python3 build.py
   python3 -m http.server 8000
   # Open http://localhost:8000
   ```

3. **Deploy:**
   ```bash
   git add icons/
   git commit -m "Add new icons"
   git push origin main
   ```

4. **Automatic rebuild:**
   - GitHub Actions automatically runs
   - Regenerates `categories.json`
   - Deploys updated site

## Manual Workflow Trigger

You can manually trigger the workflow:

1. Go to **Actions** tab in GitHub
2. Click "Build and Deploy to GitHub Pages"
3. Click "Run workflow" button
4. Select `main` branch
5. Click "Run workflow"

## Workflow Configuration

The workflow file `.github/workflows/deploy.yml` contains:

```yaml
name: Build and Deploy to GitHub Pages

on:
  push:
    branches: [ main ]    # Runs on push to main
  workflow_dispatch:      # Allows manual trigger

permissions:
  contents: read
  pages: write
  id-token: write
```

## Troubleshooting

### Categories not showing?

**Check:**
1. Is `categories.json` being generated? Run `python3 build.py` locally
2. Are icon files in the correct folders?
3. Check GitHub Actions logs for errors

### Workflow failing?

**Common issues:**
1. **Python version** - Workflow uses Python 3.11
2. **File permissions** - Ensure `build.py` is committed
3. **Syntax errors** - Test `build.py` locally first

### Icons not loading?

**Check:**
1. Are icon files committed to git?
2. Is the `icons/` folder in the repository?
3. Check browser console for 404 errors

## Local Development

**Start development server:**
```bash
# Generate categories
python3 build.py

# Start server
python3 -m http.server 8000

# Open browser
open http://localhost:8000
```

**Or with Node.js:**
```bash
python3 build.py
npx serve
```

## Benefits of This Approach

✅ **Works on GitHub Pages** - No directory listing needed  
✅ **Fast** - JSON loads instantly  
✅ **Automatic** - Rebuilds on every push  
✅ **Reliable** - No HTML parsing required  
✅ **Scalable** - Handles hundreds of icons efficiently  
✅ **Maintainable** - Simple Python script, easy to modify  

## Files Overview

| File | Purpose |
|------|---------|
| `build.py` | Scans icons and generates JSON |
| `categories.json` | Generated category data |
| `.github/workflows/deploy.yml` | GitHub Actions workflow |
| `script.js` | Loads categories from JSON |
| `index.html` | Main page |
| `styles.css` | Styling |

## Next Steps

1. Customize `build.py` if needed (add more file types, custom logic)
2. Add more icons to `icons/` folders
3. Push to GitHub and watch automatic deployment
4. Share your icon gallery URL!

---

**Need Help?**
- Check GitHub Actions logs in the **Actions** tab
- Test locally with `python3 build.py`
- Verify `categories.json` is generated correctly
