---
layout: default
title: Jekyll Theme Upgrade
---

## Jekyll Theme Upgrade

## New Theme: Just the Docs

The site now uses **Just the Docs** - a modern, responsive documentation theme with advanced features.

### Features

✨ **Modern Design**: Clean, professional appearance  
🔍 **Built-in Search**: Full-text search across all pages  
📱 **Responsive**: Mobile-first design that works on all devices  
🎨 **Customizable**: Light/dark mode support  
⚓ **Navigation**: Automatic heading anchors for easy linking  
🔝 **Back to Top**: Quick navigation on long pages  

### Theme Configuration

The theme is configured in `_config.yml`:

```yaml
# Theme configuration
theme: just-the-docs

# Features
search_enabled: true
heading_anchors: true
color_scheme: light
back_to_top: true
```

### Customization Options

You can customize the theme by editing `_config.yml`:

#### Color Schemes
```yaml
color_scheme: light  # or "dark"
```

#### Search
```yaml
search_enabled: true  # Enable/disable search
```

#### Navigation
```yaml
nav_sort: case_insensitive  # Sort order for navigation
```

### Documentation

For full theme documentation, see:
- [Just the Docs Documentation](https://just-the-docs.github.io/just-the-docs/)
- [Customization Guide](https://just-the-docs.github.io/just-the-docs/docs/customization/)
- [Configuration Reference](https://just-the-docs.github.io/just-the-docs/docs/configuration/)

### Migration Notes

The theme uses custom layouts in `_layouts/` which are preserved:
- `default.html` - Base layout
- `prompt.html` - Prompt pages
- `instruction.html` - Instruction pages
- `mode.html` - Mode pages
- `thought.html` - Thought pages

All existing content continues to work with the new theme.

### Building the Site

```bash
bundle install
bundle exec jekyll build
bundle exec jekyll serve
```

### Previous Theme

The site previously used the `minima` theme, which is a basic starter theme.
