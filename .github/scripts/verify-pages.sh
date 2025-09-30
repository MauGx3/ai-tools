#!/bin/bash

# GitHub Pages Verification Script
# This script verifies that all pages on the GitHub Pages site are accessible

set -e

# Configuration
BASE_URL="https://maugx3.github.io/ai-tools"
TOTAL_PAGES=0
PASSED_PAGES=0
FAILED_PAGES=0

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "========================================="
echo "GitHub Pages Verification Script"
echo "Base URL: $BASE_URL"
echo "========================================="
echo ""

# Function to check if a page exists
check_page() {
    local path=$1
    local url="${BASE_URL}${path}"
    local description=$2
    
    TOTAL_PAGES=$((TOTAL_PAGES + 1))
    
    printf "Checking: %-60s " "$description"
    
    # Use curl to check if page returns 200
    HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$url" 2>/dev/null || echo "000")
    
    if [ "$HTTP_CODE" = "200" ]; then
        echo -e "${GREEN}✓ PASS${NC} (HTTP $HTTP_CODE)"
        PASSED_PAGES=$((PASSED_PAGES + 1))
        return 0
    else
        echo -e "${RED}✗ FAIL${NC} (HTTP $HTTP_CODE)"
        FAILED_PAGES=$((FAILED_PAGES + 1))
        return 1
    fi
}

echo "Testing Main Pages..."
echo "-------------------"
check_page "/" "Home page"
check_page "/prompts/" "Prompts listing"
check_page "/instructions/" "Instructions listing"
check_page "/modes/" "Modes listing"
check_page "/thoughts/" "Thoughts listing"
check_page "/docs/" "Documentation home"
echo ""

echo "Testing Prompt Pages..."
echo "----------------------"
check_page "/prompts/brainstorming-facilitator/" "Brainstorming Facilitator"
check_page "/prompts/code-review-assistant/" "Code Review Assistant"
check_page "/prompts/data-analysis-assistant/" "Data Analysis Assistant"
check_page "/prompts/project-planning-assistant/" "Project Planning Assistant"
check_page "/prompts/technical-documentation-writer/" "Technical Documentation Writer"
echo ""

echo "Testing Instruction Pages..."
echo "---------------------------"
check_page "/instructions/code-review-instructions/" "Code Review Instructions"
check_page "/instructions/copilot-instructions/" "Copilot Instructions"
check_page "/instructions/github-actions-copilot-setup/" "GitHub Actions Copilot Setup"
check_page "/instructions/github-mcp-server-tools/" "GitHub MCP Server Tools"
echo ""

echo "Testing Mode Pages..."
echo "--------------------"
check_page "/modes/advanced-coding-assistant/" "Advanced Coding Assistant"
check_page "/modes/research-assistant/" "Research Assistant"
echo ""

echo "Testing Thought Pages..."
echo "-----------------------"
check_page "/thoughts/ai-documentation-workflow-experiment/" "AI Documentation Workflow"
echo ""

echo "Testing Documentation Pages..."
echo "-----------------------------"
check_page "/docs/guides/getting-started/" "Getting Started Guide"
check_page "/docs/guides/jekyll-github-pages-setup/" "Jekyll Setup Guide"
check_page "/docs/guides/prompt-engineering-best-practices/" "Prompt Engineering Guide"
check_page "/docs/references/prompt-templates/" "Prompt Templates Reference"
echo ""

echo "Testing Additional Resources..."
echo "------------------------------"
check_page "/feed.xml" "RSS Feed"
check_page "/sitemap.xml" "Sitemap"
echo ""

echo "========================================="
echo "Test Results Summary"
echo "========================================="
echo "Total pages tested: $TOTAL_PAGES"
echo -e "Passed: ${GREEN}$PASSED_PAGES${NC}"
echo -e "Failed: ${RED}$FAILED_PAGES${NC}"

if [ $FAILED_PAGES -eq 0 ]; then
    echo -e "\n${GREEN}✓ All pages are accessible!${NC}"
    exit 0
else
    echo -e "\n${RED}✗ Some pages failed to load. Please check the logs above.${NC}"
    echo ""
    echo "Common issues:"
    echo "1. GitHub Pages not enabled in repository settings"
    echo "2. Recent deployment still in progress"
    echo "3. Incorrect base URL configuration"
    echo ""
    echo "To enable GitHub Pages:"
    echo "1. Go to repository Settings → Pages"
    echo "2. Under 'Source', select 'GitHub Actions'"
    echo "3. Save and wait for deployment to complete"
    exit 1
fi
