import { test, expect } from '@playwright/test';

const BASE = process.env.PAGE_URL || 'https://maugx3.github.io/ai-tools';

test.describe('Mermaid diagram rendering', () => {
    test('mermaid diagrams render on information-sharing-workflow page', async ({ page }) => {
        await page.goto(BASE + '/docs/guides/information-sharing-workflow');
        
        // Wait for page to load
        await expect(page.locator('h1')).toBeVisible();
        
        // Check that mermaid script is loaded
        const mermaidScript = page.locator('script[src*="mermaid"]');
        await expect(mermaidScript).toHaveCount(1, { timeout: 10000 });
        
        // Check for mermaid diagram containers
        // Mermaid diagrams are rendered inside <svg> elements with class "mermaid"
        const mermaidDiagrams = page.locator('svg.mermaid, pre.mermaid svg, .mermaid svg');
        const diagramCount = await mermaidDiagrams.count();
        
        // The information-sharing-workflow page should have 5 mermaid diagrams
        expect(diagramCount).toBeGreaterThanOrEqual(1);
        console.log(`Found ${diagramCount} mermaid diagrams on information-sharing-workflow page`);
        
        // Verify at least one diagram is visible and has content
        const firstDiagram = mermaidDiagrams.first();
        await expect(firstDiagram).toBeVisible({ timeout: 15000 });
        
        // Check that the SVG has actual content (paths, rects, text elements)
        const svgContent = page.locator('svg.mermaid path, svg.mermaid rect, svg.mermaid text, .mermaid svg path, .mermaid svg rect, .mermaid svg text');
        const contentCount = await svgContent.count();
        expect(contentCount).toBeGreaterThan(0);
        console.log(`Mermaid diagram contains ${contentCount} SVG elements`);
    });

    test('mermaid diagrams render on memory-bank instructions page', async ({ page }) => {
        await page.goto(BASE + '/instructions/memory-bank');
        
        // Wait for page to load
        await expect(page.locator('h1')).toBeVisible();
        
        // Check that mermaid script is loaded
        const mermaidScript = page.locator('script[src*="mermaid"]');
        await expect(mermaidScript).toHaveCount(1, { timeout: 10000 });
        
        // Check for mermaid diagram containers
        const mermaidDiagrams = page.locator('svg.mermaid, pre.mermaid svg, .mermaid svg');
        const diagramCount = await mermaidDiagrams.count();
        
        // The memory-bank instructions page should have 6 mermaid diagrams
        expect(diagramCount).toBeGreaterThanOrEqual(1);
        console.log(`Found ${diagramCount} mermaid diagrams on memory-bank instructions page`);
        
        // Verify diagrams are visible
        if (diagramCount > 0) {
            const firstDiagram = mermaidDiagrams.first();
            await expect(firstDiagram).toBeVisible({ timeout: 15000 });
        }
    });

    test('mermaid diagrams render on llm-information-flow page', async ({ page }) => {
        await page.goto(BASE + '/docs/explain/llm-information-flow');
        
        // Wait for page to load
        await expect(page.locator('h1')).toBeVisible();
        
        // Check that mermaid script is loaded
        const mermaidScript = page.locator('script[src*="mermaid"]');
        await expect(mermaidScript).toHaveCount(1, { timeout: 10000 });
        
        // Check for mermaid diagram containers
        const mermaidDiagrams = page.locator('svg.mermaid, pre.mermaid svg, .mermaid svg');
        const diagramCount = await mermaidDiagrams.count();
        
        // The llm-information-flow page should have at least 1 mermaid diagram
        expect(diagramCount).toBeGreaterThanOrEqual(1);
        console.log(`Found ${diagramCount} mermaid diagrams on llm-information-flow page`);
        
        // Verify diagrams are visible
        if (diagramCount > 0) {
            const firstDiagram = mermaidDiagrams.first();
            await expect(firstDiagram).toBeVisible({ timeout: 15000 });
        }
    });

    test('mermaid diagrams have proper styling and are interactive', async ({ page }) => {
        await page.goto(BASE + '/docs/guides/information-sharing-workflow');
        
        // Wait for mermaid to render
        await page.waitForSelector('svg.mermaid, .mermaid svg', { timeout: 15000 });
        
        const mermaidDiagrams = page.locator('svg.mermaid, .mermaid svg').first();
        
        // Check that diagram has proper dimensions (not 0x0)
        const boundingBox = await mermaidDiagrams.boundingBox();
        expect(boundingBox).not.toBeNull();
        if (boundingBox) {
            expect(boundingBox.width).toBeGreaterThan(50);
            expect(boundingBox.height).toBeGreaterThan(50);
            console.log(`Mermaid diagram dimensions: ${boundingBox.width}x${boundingBox.height}`);
        }
        
        // Check for typical mermaid flowchart elements
        const hasNodes = await page.locator('svg.mermaid .node, .mermaid svg .node, svg.mermaid rect, .mermaid svg rect').count();
        const hasText = await page.locator('svg.mermaid text, .mermaid svg text').count();
        
        expect(hasNodes).toBeGreaterThan(0);
        expect(hasText).toBeGreaterThan(0);
        console.log(`Diagram has ${hasNodes} nodes and ${hasText} text elements`);
    });

    test('mermaid configuration is correct in _config.yml', async ({ page }) => {
        // This test verifies that mermaid is properly loaded on any page
        await page.goto(BASE + '/');
        
        // Check that mermaid library is loaded
        const hasMermaid = await page.evaluate(() => {
            return typeof (window as any).mermaid !== 'undefined';
        });
        
        expect(hasMermaid).toBe(true);
        console.log('Mermaid library is loaded and available');
    });

    test('no broken mermaid code blocks remain unrendered', async ({ page }) => {
        // Test multiple pages to ensure no raw mermaid code is showing
        const pagesToCheck = [
            '/docs/guides/information-sharing-workflow',
            '/instructions/memory-bank',
            '/docs/explain/llm-information-flow'
        ];
        
        for (const pagePath of pagesToCheck) {
            await page.goto(BASE + pagePath);
            await page.waitForLoadState('networkidle');
            
            // Check that there are no unrendered mermaid code blocks
            // (looking for ```mermaid fenced code blocks that weren't processed)
            const pageContent = await page.content();
            const hasUnrenderedMermaid = pageContent.includes('```mermaid') || 
                                          pageContent.includes('class="language-mermaid"');
            
            expect(hasUnrenderedMermaid).toBe(false);
            console.log(`Page ${pagePath} has no unrendered mermaid blocks`);
        }
    });
});
