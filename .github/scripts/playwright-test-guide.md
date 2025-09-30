# Playwright MCP Server Testing Guide

This guide explains how to use the Playwright MCP Server to comprehensively test your GitHub Pages site once it's deployed.

## Prerequisites

- GitHub Pages must be enabled and deployed
- Site should be accessible at: https://maugx3.github.io/ai-tools/
- Playwright MCP server should be available in your environment

## Why Use Playwright for Testing?

Playwright provides:
- **Real browser testing**: Tests in actual Chromium/Firefox/WebKit browsers
- **Visual verification**: Can take screenshots and verify UI elements
- **JavaScript execution**: Tests dynamic content and interactions
- **Network inspection**: Monitors requests and responses
- **Accessibility testing**: Can check WCAG compliance

## Test Categories

### 1. Smoke Tests (Critical Path)

Test the most important user journeys:

```
Test: Home Page → Prompts → Individual Prompt → Back to Prompts
1. Navigate to https://maugx3.github.io/ai-tools/
2. Click "Prompts" in navigation
3. Click on "Code Review Assistant"
4. Verify content loads
5. Click "Back to Prompts"
6. Verify return to prompts listing
```

### 2. Page Load Tests

Verify all pages are accessible:

```javascript
const pages = [
  '/',
  '/prompts/',
  '/instructions/',
  '/modes/',
  '/thoughts/',
  '/docs/',
  '/prompts/code-review-assistant/',
  '/instructions/github-actions-copilot-setup/',
  '/modes/advanced-coding-assistant/',
  '/docs/guides/jekyll-github-pages-setup/',
  // ... all other pages
];

for (const page of pages) {
  const url = `https://maugx3.github.io/ai-tools${page}`;
  // Navigate and verify page loads
  // Check for HTTP 200 status
  // Verify no console errors
}
```

### 3. Navigation Tests

Test that navigation works correctly:

```
Test: Main Navigation
1. Start at home page
2. For each nav item (Prompts, Instructions, Modes, Documentation, Thoughts):
   a. Click the navigation link
   b. Verify URL changes correctly
   c. Verify page loads with expected content
   d. Click "Home" to return
```

### 4. Content Validation Tests

Verify content is properly rendered:

```
Test: Prompt Page Content
1. Navigate to a prompt detail page
2. Verify:
   - Page title is present
   - "Back to Prompts" link exists
   - Category badge is displayed
   - Description is present
   - Content is rendered (not blank)
   - Code blocks are syntax highlighted (if present)
```

### 5. Responsive Design Tests

Test different viewport sizes:

```
Test: Mobile Responsiveness
1. Set viewport to 375x667 (mobile)
2. Navigate through key pages
3. Verify:
   - Navigation menu works (hamburger if applicable)
   - Content is readable
   - No horizontal scroll
   - All interactive elements are clickable

Test: Tablet View
1. Set viewport to 768x1024 (tablet)
2. Repeat verification

Test: Desktop View
1. Set viewport to 1920x1080 (desktop)
2. Repeat verification
```

### 6. Link Validation Tests

Verify all internal links work:

```
Test: Internal Links
1. Navigate to each page
2. Find all links with href starting with '/ai-tools'
3. Click each link
4. Verify destination page loads (HTTP 200)
5. Verify no 404 errors
```

## Example Playwright MCP Test Commands

### Test 1: Basic Home Page Load

```
playwright-browser_navigate: https://maugx3.github.io/ai-tools/
playwright-browser_snapshot: (capture page structure)
playwright-browser_take_screenshot: filename="home-page.png"
```

Expected: Page loads, shows "AI Tools Collection" title, navigation menu visible.

### Test 2: Navigation Flow

```
1. playwright-browser_navigate: https://maugx3.github.io/ai-tools/
2. playwright-browser_click: element="Prompts link", ref="[nav link]"
3. playwright-browser_snapshot: (verify prompts page)
4. playwright-browser_click: element="Code Review Assistant", ref="[link]"
5. playwright-browser_snapshot: (verify detail page)
6. playwright-browser_click: element="Back to Prompts", ref="[back link]"
7. playwright-browser_snapshot: (verify returned to list)
```

Expected: Smooth navigation through all pages, no errors.

### Test 3: Verify All Main Pages

```
For each URL in [/, /prompts/, /instructions/, /modes/, /thoughts/, /docs/]:
1. playwright-browser_navigate: URL
2. playwright-browser_snapshot: (check page loaded)
3. playwright-browser_console_messages: (check for errors)
```

Expected: All pages load with HTTP 200, no console errors.

### Test 4: Mobile View Test

```
1. playwright-browser_resize: width=375, height=667
2. playwright-browser_navigate: https://maugx3.github.io/ai-tools/
3. playwright-browser_take_screenshot: filename="mobile-view.png"
4. playwright-browser_snapshot: (verify mobile layout)
```

Expected: Mobile-friendly layout, readable text, functional navigation.

### Test 5: Verify Links Work

```
1. playwright-browser_navigate: https://maugx3.github.io/ai-tools/prompts/
2. playwright-browser_snapshot: (get all links)
3. For each prompt link:
   a. playwright-browser_click: link
   b. playwright-browser_snapshot: (verify page)
   c. playwright-browser_navigate_back
```

Expected: All links work, pages load correctly.

## Comprehensive Test Script

Here's a complete test sequence you can run:

### Phase 1: Smoke Test (5 minutes)
```
1. Navigate to home page
2. Take screenshot
3. Test main navigation (5 main sections)
4. Test one page from each section
5. Verify "Back" navigation works
```

### Phase 2: Full Page Verification (10 minutes)
```
1. Test all 24 pages load (HTTP 200)
2. Capture console errors
3. Take screenshots of key pages
4. Verify no broken images
```

### Phase 3: Interaction Testing (15 minutes)
```
1. Test all navigation links
2. Test internal page links
3. Test search functionality (if implemented)
4. Test form submissions (if any)
```

### Phase 4: Cross-Browser Testing (20 minutes)
```
1. Repeat smoke test in Chromium
2. Repeat smoke test in Firefox
3. Repeat smoke test in WebKit
4. Compare screenshots
```

## Running Tests with Playwright MCP

Once GitHub Pages is enabled, you can run these tests interactively:

1. **Start a test session**:
   ```
   Open your MCP-enabled environment (Claude, Copilot, etc.)
   ```

2. **Begin testing**:
   ```
   "Please use Playwright to test my GitHub Pages site at 
   https://maugx3.github.io/ai-tools/. Start by navigating to 
   the home page and taking a screenshot."
   ```

3. **Run comprehensive tests**:
   ```
   "Now test all the main pages: prompts, instructions, modes, 
   and docs. For each page, verify it loads correctly and 
   take a screenshot."
   ```

4. **Test navigation**:
   ```
   "Test the navigation by clicking through the site. Start at 
   home, go to Prompts, click on a prompt, then use back 
   navigation to return."
   ```

## Expected Results

All tests should pass with:
- ✅ All pages return HTTP 200
- ✅ No JavaScript console errors
- ✅ All navigation links work
- ✅ Content is properly rendered
- ✅ Responsive design works on all viewports
- ✅ No broken images or resources
- ✅ Back navigation functions correctly

## Test Failures and Debugging

If tests fail:

### HTTP 404 Errors
- **Issue**: Page not found
- **Check**: Verify GitHub Pages is enabled and deployed
- **Check**: Verify URL path matches file structure
- **Check**: Check `_config.yml` baseurl setting

### JavaScript Errors
- **Issue**: Console shows errors
- **Check**: Review browser console output
- **Check**: Check if external resources are loading
- **Check**: Verify Jekyll build completed without errors

### Navigation Failures
- **Issue**: Links don't work or go to wrong pages
- **Check**: Verify `relative_url` filter is used in templates
- **Check**: Verify navigation configuration in `_config.yml`
- **Check**: Test with and without trailing slashes

### Styling Issues
- **Issue**: Page loads but looks broken
- **Check**: Verify CSS files are loading
- **Check**: Check browser console for 404s on CSS files
- **Check**: Verify `baseurl` is correct in `_config.yml`

## Automated Test Execution

For automated testing, consider creating a test script that:

1. Iterates through all pages
2. Captures results for each test
3. Generates a report
4. Takes screenshots for visual regression testing
5. Logs any failures for debugging

## Integration with CI/CD

To run these tests automatically on each deployment:

1. Add a workflow file: `.github/workflows/test-pages.yml`
2. Trigger after deployment completes
3. Use Playwright in GitHub Actions
4. Fail the build if tests don't pass
5. Upload screenshots as artifacts

## Conclusion

Playwright MCP provides a powerful way to comprehensively test your GitHub Pages site. Once Pages is enabled, use this guide to verify everything works correctly. Start with the smoke tests, then move to comprehensive testing, and finally integrate automated tests into your CI/CD pipeline.

## Quick Reference: Test All Pages Command

```bash
# Use this with Playwright MCP:
"Test all pages on https://maugx3.github.io/ai-tools/. 
For each of these paths, navigate to it, take a screenshot, 
and verify it loads correctly:
/, /prompts/, /instructions/, /modes/, /thoughts/, /docs/, 
/prompts/code-review-assistant/, 
/instructions/github-actions-copilot-setup/, 
/modes/advanced-coding-assistant/, 
/docs/guides/jekyll-github-pages-setup/"
```
