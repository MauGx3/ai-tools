# GitHub Pages Testing Scripts

This directory contains scripts and documentation for testing and verifying the GitHub Pages deployment.

## Important: URL Configuration

The scripts and documentation use placeholder URLs (`YOUR_USERNAME.github.io/REPO_NAME`). 

**For this repository**, the actual URL is: `https://maugx3.github.io/ai-tools/`

To use these scripts with a different repository:
1. Update `_config.yml` with your `baseurl` and `url`
2. Set the `GITHUB_PAGES_URL` environment variable when running the verification script:
   ```bash
   GITHUB_PAGES_URL=https://yourusername.github.io/your-repo bash .github/scripts/verify-pages.sh
   ```

## Issue

The GitHub Pages site is not currently deployed because GitHub Pages is not enabled in the repository settings. The Jekyll site builds successfully, but the deployment step is being skipped.

## Solution

To fix this issue and get the GitHub Pages site live, follow these steps:

### Step 1: Enable GitHub Pages

1. Go to your repository on GitHub: https://github.com/MauGx3/ai-tools
2. Click on **Settings** (you need admin access)
3. In the left sidebar, click on **Pages**
4. Under **Source**, select **"GitHub Actions"** from the dropdown
5. Click **Save**

![GitHub Pages Settings](https://docs.github.com/assets/cb-47267/mw-1440/images/help/pages/github-actions-source.webp)

### Step 2: Wait for Deployment

After enabling GitHub Pages:

1. Go to the **Actions** tab in your repository
2. You should see a new workflow run starting automatically
3. Wait for the "Build and deploy Jekyll site to GitHub Pages" workflow to complete
4. The workflow will show a "deploy" job this time (previously it was skipped)
5. Once complete, your site will be live at: https://YOUR_USERNAME.github.io/REPO_NAME/

### Step 3: Verify the Deployment

Once GitHub Pages is enabled and deployed, run the verification script to ensure all pages are accessible:

```bash
# Make the script executable (if not already)
chmod +x .github/scripts/verify-pages.sh

# Run the verification script
.github/scripts/verify-pages.sh
```

The script will test all 24 pages and report which ones are accessible.

Expected output:
```
=========================================
GitHub Pages Verification Script
Base URL: https://YOUR_USERNAME.github.io/REPO_NAME
=========================================

Testing Main Pages...
-------------------
Checking: Home page                                            ✓ PASS (HTTP 200)
Checking: Prompts listing                                      ✓ PASS (HTTP 200)
...

=========================================
Test Results Summary
=========================================
Total pages tested: 24
Passed: 24
Failed: 0

✓ All pages are accessible!
```

## Files in this Directory

### test-github-pages.md
A comprehensive test plan document that outlines:
- All pages that should be tested
- Manual testing procedures
- Expected results
- Troubleshooting steps

Use this document for thorough manual testing of the site.

### verify-pages.sh
An automated bash script that:
- Tests all 24 pages on the site
- Verifies each page returns HTTP 200
- Provides a summary report
- Color-coded output for easy reading

Use this script for quick automated verification after deployments.

### playwright-test-guide.md
A comprehensive guide for testing with Playwright MCP server:
- Detailed test categories and procedures
- Example Playwright commands
- Interactive testing workflows
- Integration with CI/CD
- Visual regression testing

Use this guide for thorough interactive testing with Playwright MCP.

## Current Status

As of the last check:
- ✅ Jekyll site builds successfully
- ✅ GitHub Actions workflow is properly configured
- ❌ GitHub Pages is **NOT enabled** in repository settings
- ❌ Site is **NOT deployed** (deployment job is skipped)

## What's Working

The GitHub Actions workflow is intelligently handling the situation:
- It builds the Jekyll site successfully
- It detects that Pages is not enabled
- It uploads the built site as an artifact for preview
- It skips the deployment step
- It provides clear instructions in the workflow logs

## Next Steps

1. **Enable GitHub Pages** (requires repository admin access)
   - Follow Step 1 above

2. **Wait for automatic deployment**
   - The workflow will run automatically after enabling Pages
   - Or manually trigger it from the Actions tab

3. **Verify deployment**
   - Run `./github/scripts/verify-pages.sh`
   - Or manually visit https://YOUR_USERNAME.github.io/REPO_NAME/

4. **Report any issues**
   - If any pages fail to load, check the workflow logs
   - Verify the base URL in `_config.yml` matches the repository name

## Additional Resources

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [GitHub Actions for Pages](https://github.com/actions/deploy-pages)

## Troubleshooting

### "404 Not Found" errors
- Ensure GitHub Pages is enabled with "GitHub Actions" as the source
- Check that the latest workflow run completed successfully
- Verify the `baseurl` in `_config.yml` matches your repository name

### "Build failed" in Actions
- Check the workflow logs for specific errors
- Verify `Gemfile` and `_config.yml` are valid
- Ensure all required files are committed

### Deployment job is skipped
- This means GitHub Pages is not enabled yet
- Follow Step 1 to enable Pages in repository settings

### Pages enabled but site not loading
- Wait 1-2 minutes for deployment to propagate
- Clear your browser cache
- Try accessing in an incognito/private window
