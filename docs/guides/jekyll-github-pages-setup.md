---
title: "Setting Up Jekyll for GitHub Pages"
type: "setup"
difficulty: "beginner"
time_required: "30-45 minutes"
prerequisites: "Basic command line knowledge, Git basics"
description: "Complete guide to setting up Jekyll for GitHub Pages deployment"
---

This guide walks you through setting up Jekyll for GitHub Pages, allowing you to create a modern documentation site that automatically deploys when you push changes.

## Prerequisites

Before starting, ensure you have:
- Git installed and configured
- Ruby installed (version 2.7 or higher)
- A GitHub account
- Basic command line familiarity

## Installation Steps

### 1. Install Jekyll and Bundler

```bash
gem install jekyll bundler
```

### 2. Create a New Jekyll Site

```bash
jekyll new my-ai-tools-site
cd my-ai-tools-site
```

### 3. Configure for GitHub Pages

Create or update your `Gemfile`:

```ruby
source "https://rubygems.org"
gem "github-pages", group: :jekyll_plugins

group :jekyll_plugins do
  gem "jekyll-feed"
  gem "jekyll-sitemap"
  gem "jekyll-seo-tag"
end
```

### 4. Update `_config.yml`

```yaml
title: Your AI Tools
description: Your AI tools collection
baseurl: "/repository-name"
url: "https://username.github.io"

markdown: kramdown
highlighter: rouge
theme: minima

plugins:
  - jekyll-feed
  - jekyll-sitemap
  - jekyll-seo-tag
```

### 5. Install Dependencies

```bash
bundle install
```

### 6. Test Locally

```bash
bundle exec jekyll serve
```

Visit `http://localhost:4000` to see your site.

### 7. Deploy to GitHub Pages

1. Create a new repository on GitHub
2. Push your Jekyll site to the repository:

```bash
git init
git add .
git commit -m "Initial Jekyll site"
git branch -M main
git remote add origin https://github.com/username/repository-name.git
git push -u origin main
```

3. Enable GitHub Pages in repository settings:
   - Go to Settings → Pages
   - Select "Deploy from a branch"
   - Choose "main" branch and "/ (root)" folder
   - Click Save

## Configuration Tips

### Custom Domain (Optional)
Add a `CNAME` file with your domain name if using a custom domain.

### Security
- Keep dependencies updated with `bundle update`
- Review GitHub security alerts
- Use branch protection rules

### Performance
- Optimize images before adding
- Use Jekyll's built-in compression
- Enable caching headers

## Troubleshooting

### Common Issues

**Build fails with dependency errors:**
```bash
bundle update
bundle exec jekyll serve
```

**GitHub Pages not updating:**
- Check the Actions tab for build errors
- Ensure `_config.yml` is valid YAML
- Verify all files are committed and pushed

**Local site not matching GitHub Pages:**
- Use the same Ruby version as GitHub Pages
- Test with `bundle exec jekyll serve --livereload`

### Getting Help

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Jekyll GitHub Pages Gem](https://github.com/github/pages-gem)