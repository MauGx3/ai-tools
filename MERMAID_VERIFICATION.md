# Mermaid Diagram Verification Guide

This document explains how mermaid diagrams are configured in this repository and how to verify they are displaying properly on GitHub Pages.

## Configuration

### Jekyll Configuration (`_config.yml`)

The mermaid support is configured in `_config.yml`:

```yaml
# Mermaid diagrams support
mermaid:
  version: "10.6.1"
```

### Custom Head Include (`_includes/head_custom.html`)

A custom head include has been added to ensure mermaid is properly initialized on all pages. This file:
- Loads mermaid from CDN using ESM module format
- Initializes mermaid with proper configuration
- Makes mermaid available globally for debugging

## Pages with Mermaid Diagrams

The following pages contain mermaid diagrams:

1. **Information Sharing Workflow** (`docs/guides/information-sharing-workflow.md`)
   - 5 mermaid diagrams showing workflow patterns
   - Main page for understanding the information flow

2. **Memory Bank Instructions** (`.github/instructions/memory-bank.instructions.md` and `_instructions/memory-bank.instructions.md`)
   - 6 mermaid diagrams each
   - Shows Memory Bank structure and workflows

3. **LLM Information Flow** (`docs/explain/llm-information-flow.md`)
   - 1 mermaid diagram
   - Architecture diagram

## Manual Verification Steps

### 1. Visual Inspection

Visit the deployed GitHub Pages site and check:

1. Navigate to: https://maugx3.github.io/ai-tools/docs/guides/information-sharing-workflow
2. Verify that diagrams appear as rendered SVG graphics, not as code blocks
3. Check that diagrams are properly sized and visible
4. Verify that text in diagrams is readable
5. Confirm that flowchart arrows and connections are visible

### 2. Browser Developer Tools

Open browser developer console (F12) and:

1. Check for any JavaScript errors related to mermaid
2. Verify mermaid library is loaded:
   ```javascript
   console.log(window.mermaid);
   ```
   Should return the mermaid object, not `undefined`

3. Check for rendered SVG elements:
   ```javascript
   document.querySelectorAll('svg.mermaid').length
   ```
   Should return the number of diagrams on the page

4. Verify no unrendered code blocks:
   - Search page source (Ctrl+F) for "```mermaid"
   - Should not find any fenced code blocks in the final HTML

### 3. Network Tab Verification

In browser developer tools, Network tab:

1. Look for mermaid library loading from CDN
2. Verify it loads successfully (200 status code)
3. Check that version matches configuration (10.6.1)

## Automated Testing

### Playwright Tests

Automated tests have been created in `tests/mermaid.spec.ts` that verify:

1. **Diagram Rendering**: Mermaid diagrams render as SVG elements
2. **Content Verification**: SVG contains actual diagram content (paths, text, nodes)
3. **Multiple Pages**: All pages with mermaid diagrams are tested
4. **Library Loading**: Mermaid library is properly loaded
5. **No Unrendered Blocks**: No raw mermaid code blocks remain

### Running Tests

Tests run automatically in GitHub Actions after deployment. To run manually:

```bash
# Install dependencies
npm install

# Install Playwright browsers
npx playwright install --with-deps chromium

# Run mermaid-specific tests
npm test -- tests/mermaid.spec.ts

# Run all tests
npm test
```

**Note**: Tests require the GitHub Pages site to be accessible. They will run automatically in the CI/CD pipeline after deployment.

## Troubleshooting

### Diagrams Not Rendering

If diagrams appear as code blocks instead of rendered graphics:

1. **Check mermaid configuration**: Verify `_config.yml` has mermaid section
2. **Check custom head include**: Ensure `_includes/head_custom.html` exists
3. **Clear browser cache**: Hard refresh (Ctrl+Shift+R) or clear cache
4. **Check browser console**: Look for JavaScript errors
5. **Verify CDN access**: Ensure CDN (jsdelivr.net) is accessible

### Diagrams Partially Visible

If diagrams are cut off or not fully visible:

1. Check CSS conflicts with theme
2. Verify viewport settings
3. Try zooming out in browser
4. Check container width settings

### JavaScript Errors

Common issues and solutions:

1. **"mermaid is not defined"**: Head include not loading properly
2. **CDN timeout**: Network connectivity issue, try different CDN
3. **Syntax errors**: Check mermaid code block syntax in markdown

## Theme Compatibility

This repository uses **Just the Docs** theme (version 0.8.x), which has built-in mermaid support. The custom head include enhances this support by:

- Using ESM module format for better compatibility
- Explicit initialization with configuration
- Global availability for debugging

## GitHub Actions Workflow

The Jekyll build workflow (`.github/workflows/jekyll-gh-pages.yml`) includes:

1. **Build job**: Builds Jekyll site with mermaid support
2. **Deploy job**: Deploys to GitHub Pages
3. **Test job**: Runs Playwright tests including mermaid verification

The workflow ensures that every deployment is automatically tested for mermaid diagram rendering.

## Best Practices

When adding new mermaid diagrams:

1. **Test locally**: Build Jekyll site locally and verify rendering
   ```bash
   bundle exec jekyll serve
   ```

2. **Keep diagrams simple**: Complex diagrams may have rendering issues
3. **Use proper syntax**: Follow mermaid documentation for diagram types
4. **Add comments**: Document what each diagram shows
5. **Verify in PR**: Check GitHub Pages preview before merging

## Resources

- [Mermaid Documentation](https://mermaid.js.org/)
- [Just the Docs Theme](https://just-the-docs.github.io/just-the-docs/)
- [Mermaid Live Editor](https://mermaid.live/) - For testing diagram syntax
- [GitHub Pages Documentation](https://docs.github.com/en/pages)

## Verification Checklist

Before considering mermaid diagrams verified:

- [ ] All pages with diagrams load without errors
- [ ] Diagrams render as SVG elements (not code blocks)
- [ ] Diagram content is visible and properly formatted
- [ ] Text in diagrams is readable
- [ ] Arrows and connections are visible
- [ ] No JavaScript console errors
- [ ] Mermaid library loads from CDN
- [ ] Automated tests pass
- [ ] Works in multiple browsers (Chrome, Firefox, Safari)
- [ ] Works on mobile devices

---

**Last Updated**: 2025-11-20
**Mermaid Version**: 10.6.1
**Theme**: Just the Docs 0.8.x
