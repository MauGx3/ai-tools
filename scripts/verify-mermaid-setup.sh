#!/bin/bash
# Verification script for mermaid diagram setup
# This script checks the local repository configuration for mermaid support

set -e

echo "🔍 Mermaid Diagram Setup Verification"
echo "======================================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check 1: Jekyll configuration
echo "1. Checking Jekyll configuration (_config.yml)..."
if grep -q "mermaid:" _config.yml; then
    echo -e "${GREEN}✓${NC} Mermaid configuration found in _config.yml"
    MERMAID_VERSION=$(grep -A1 "mermaid:" _config.yml | grep "version:" | awk '{print $2}' | tr -d '"')
    echo "  Version: $MERMAID_VERSION"
else
    echo -e "${RED}✗${NC} Mermaid configuration NOT found in _config.yml"
    exit 1
fi
echo ""

# Check 2: Custom head include
echo "2. Checking custom head include (_includes/head_custom.html)..."
if [ -f "_includes/head_custom.html" ]; then
    echo -e "${GREEN}✓${NC} Custom head include exists"
    if grep -q "mermaid" _includes/head_custom.html; then
        echo -e "${GREEN}✓${NC} Mermaid initialization code found"
    else
        echo -e "${YELLOW}⚠${NC}  Custom head include exists but doesn't contain mermaid code"
    fi
else
    echo -e "${YELLOW}⚠${NC}  Custom head include not found (may rely on theme defaults)"
fi
echo ""

# Check 3: Count mermaid diagrams
echo "3. Counting mermaid diagrams in markdown files..."
MERMAID_COUNT=$(grep -r "^\`\`\`mermaid" --include="*.md" . | wc -l)
echo -e "${GREEN}✓${NC} Found $MERMAID_COUNT mermaid code blocks"
echo ""

# Check 4: List files with mermaid diagrams
echo "4. Files containing mermaid diagrams:"
grep -r "^\`\`\`mermaid" --include="*.md" . -l | while read file; do
    COUNT=$(grep "^\`\`\`mermaid" "$file" | wc -l)
    echo "   - $file ($COUNT diagrams)"
done
echo ""

# Check 5: Test files
echo "5. Checking test files..."
if [ -f "tests/mermaid.spec.ts" ]; then
    echo -e "${GREEN}✓${NC} Mermaid-specific tests found (tests/mermaid.spec.ts)"
    TEST_COUNT=$(grep -c "test(" tests/mermaid.spec.ts || echo "0")
    echo "  Number of tests: $TEST_COUNT"
else
    echo -e "${RED}✗${NC} Mermaid-specific tests NOT found"
fi
echo ""

# Check 6: Node dependencies
echo "6. Checking Node.js test dependencies..."
if [ -f "package.json" ]; then
    echo -e "${GREEN}✓${NC} package.json found"
    if [ -d "node_modules" ]; then
        echo -e "${GREEN}✓${NC} node_modules directory exists"
    else
        echo -e "${YELLOW}⚠${NC}  node_modules not found. Run: npm install"
    fi
else
    echo -e "${RED}✗${NC} package.json NOT found"
fi
echo ""

# Check 7: Jekyll dependencies
echo "7. Checking Jekyll dependencies..."
if [ -f "Gemfile" ]; then
    echo -e "${GREEN}✓${NC} Gemfile found"
    if [ -d "vendor/bundle" ] || command -v bundle &> /dev/null; then
        echo -e "${GREEN}✓${NC} Bundler is available"
    else
        echo -e "${YELLOW}⚠${NC}  Bundler not found. Run: gem install bundler && bundle install"
    fi
else
    echo -e "${RED}✗${NC} Gemfile NOT found"
fi
echo ""

# Summary
echo "======================================"
echo "Summary:"
echo "- Configuration: ✓"
echo "- Diagrams found: $MERMAID_COUNT"
echo "- Tests: $([ -f 'tests/mermaid.spec.ts' ] && echo '✓' || echo '✗')"
echo ""
echo "To verify mermaid rendering:"
echo "1. Build site locally: bundle exec jekyll serve"
echo "2. Visit: http://localhost:4000/ai-tools/"
echo "3. Navigate to pages with mermaid diagrams"
echo "4. Run tests: npm test -- tests/mermaid.spec.ts"
echo ""
echo "For detailed verification steps, see: MERMAID_VERIFICATION.md"
