# GitHub Pages Verification Test Plan

This document provides a comprehensive test plan to verify that all pages are properly live on GitHub Pages using the Playwright MCP server.

## Prerequisites

- GitHub Pages must be enabled in the repository settings
- The site should be accessible at: `https://maugx3.github.io/ai-tools/`
- Playwright MCP server should be available

## Test Scope

This test plan covers all generated pages from the Jekyll build:

### Main Pages (6 pages)
1. Home page (`/`)
2. Prompts listing (`/prompts/`)
3. Instructions listing (`/instructions/`)
4. Modes listing (`/modes/`)
5. Thoughts listing (`/thoughts/`)
6. Documentation home (`/docs/`)

### Prompt Pages (5 pages)
1. `/prompts/brainstorming-facilitator/`
2. `/prompts/code-review-assistant/`
3. `/prompts/data-analysis-assistant/`
4. `/prompts/project-planning-assistant/`
5. `/prompts/technical-documentation-writer/`

### Instruction Pages (4 pages)
1. `/instructions/code-review-instructions/`
2. `/instructions/copilot-instructions/`
3. `/instructions/github-actions-copilot-setup/`
4. `/instructions/github-mcp-server-tools/`

### Mode Pages (2 pages)
1. `/modes/advanced-coding-assistant/`
2. `/modes/research-assistant/`

### Thought Pages (1 page)
1. `/thoughts/ai-documentation-workflow-experiment/`

### Documentation Pages (4 pages)
1. `/docs/guides/getting-started/`
2. `/docs/guides/jekyll-github-pages-setup/`
3. `/docs/guides/prompt-engineering-best-practices/`
4. `/docs/references/prompt-templates/`

**Total: 22 pages**

## Test Procedure

### Step 1: Enable GitHub Pages

If not already enabled:

1. Go to repository Settings → Pages
2. Under "Source", select "GitHub Actions"
3. Save and wait for deployment
4. Verify the deployment URL is accessible

### Step 2: Verify Main Page

Test that the main page loads correctly:

```
1. Navigate to https://maugx3.github.io/ai-tools/
2. Verify page loads without errors (200 status)
3. Verify page title contains "AI Tools Collection"
4. Verify navigation menu is present
5. Verify main content sections are visible
```

### Step 3: Verify Collection Listing Pages

Test each collection listing page:

#### Prompts Page
```
1. Navigate to https://maugx3.github.io/ai-tools/prompts/
2. Verify page loads (200 status)
3. Verify "Prompts" heading is present
4. Verify at least 5 prompt links are listed
5. Test that clicking a prompt link navigates to the detail page
```

#### Instructions Page
```
1. Navigate to https://maugx3.github.io/ai-tools/instructions/
2. Verify page loads (200 status)
3. Verify "Instructions" heading is present
4. Verify at least 4 instruction links are listed
```

#### Modes Page
```
1. Navigate to https://maugx3.github.io/ai-tools/modes/
2. Verify page loads (200 status)
3. Verify "Modes" heading is present
4. Verify at least 2 mode links are listed
```

#### Thoughts Page
```
1. Navigate to https://maugx3.github.io/ai-tools/thoughts/
2. Verify page loads (200 status)
3. Verify "Thoughts" heading is present
```

#### Documentation Page
```
1. Navigate to https://maugx3.github.io/ai-tools/docs/
2. Verify page loads (200 status)
3. Verify "Documentation" heading is present
```

### Step 4: Verify Individual Content Pages

Test a sample of individual pages from each collection:

#### Sample Prompt Page
```
1. Navigate to https://maugx3.github.io/ai-tools/prompts/code-review-assistant/
2. Verify page loads (200 status)
3. Verify page has content
4. Verify "Back to Prompts" link is present and functional
5. Verify navigation menu works
```

#### Sample Instruction Page
```
1. Navigate to https://maugx3.github.io/ai-tools/instructions/github-actions-copilot-setup/
2. Verify page loads (200 status)
3. Verify page has content
4. Verify code blocks are properly formatted
```

#### Sample Mode Page
```
1. Navigate to https://maugx3.github.io/ai-tools/modes/advanced-coding-assistant/
2. Verify page loads (200 status)
3. Verify page has content
```

#### Sample Documentation Page
```
1. Navigate to https://maugx3.github.io/ai-tools/docs/guides/jekyll-github-pages-setup/
2. Verify page loads (200 status)
3. Verify page has content and proper formatting
```

### Step 5: Verify Navigation

Test that navigation works across the site:

```
1. Start at home page
2. Click "Prompts" in navigation → verify landing on prompts page
3. Click a prompt → verify landing on prompt detail page
4. Click "Back to Prompts" → verify returning to prompts listing
5. Click "Home" in navigation → verify returning to home page
6. Repeat for Instructions, Modes, and Documentation sections
```

### Step 6: Verify Assets and Styling

```
1. Verify CSS is loaded (check for styled elements)
2. Verify no broken images
3. Verify responsive design works (test different viewport sizes)
```

### Step 7: Verify RSS Feed

```
1. Navigate to https://maugx3.github.io/ai-tools/feed.xml
2. Verify valid XML is returned
3. Verify feed contains expected entries
```

### Step 8: Verify Sitemap

```
1. Navigate to https://maugx3.github.io/ai-tools/sitemap.xml
2. Verify valid XML is returned
3. Verify sitemap contains all major pages
```

## Expected Results

All pages should:
- Return HTTP 200 status
- Load without JavaScript errors
- Display proper content with correct formatting
- Have working navigation links
- Be accessible and usable
- Have proper SEO meta tags

## Troubleshooting

If pages are not loading:

1. **404 Errors**: Check that GitHub Pages is enabled and deployment completed
2. **Styling Issues**: Check that `baseurl` in `_config.yml` matches the repository name
3. **Broken Links**: Verify all internal links use `relative_url` filter
4. **Build Failures**: Check GitHub Actions logs for build errors

## Automated Test Execution

An automated test script can be created using the Playwright MCP server to verify all pages programmatically. See `verify-pages.sh` for a bash implementation.

## Success Criteria

✅ All 22 pages load successfully (HTTP 200)
✅ Navigation works between all sections
✅ Content is properly formatted
✅ No broken links within the site
✅ RSS feed and sitemap are accessible
✅ Mobile responsive design works correctly

## Notes

- This test plan should be executed after every major deployment
- Any failing tests should be documented and fixed before considering the deployment successful
- Consider adding automated tests to CI/CD pipeline for continuous verification
