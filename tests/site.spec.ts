import { test, expect } from '@playwright/test';

const BASE = process.env.PAGE_URL || 'https://maugx3.github.io/ai-tools';

test.describe('AI Tools site', () => {
    test('home page loads', async ({ page }) => {
        await page.goto(BASE + '/');
        await expect(page).toHaveTitle(/AI Tools Collection/i);
        await expect(page.locator('h1')).toBeVisible();
    });

    test('navigation to collection pages works', async ({ page }) => {
        await page.goto(BASE + '/');

        // Test Prompts navigation
        const promptsLink = page.locator('a', { hasText: 'Prompts' }).first();
        await promptsLink.click();
        await expect(page).toHaveURL(/\/prompts\//);
        await expect(page.locator('h1', { hasText: 'Prompts Collection' })).toBeVisible();

        // Go back to home
        await page.goto(BASE + '/');

        // Test Instructions navigation
        const instructionsLink = page.locator('a', { hasText: 'Instructions' }).first();
        await instructionsLink.click();
        await expect(page).toHaveURL(/\/instructions\//);
        await expect(page.locator('h1', { hasText: 'Instructions Collection' })).toBeVisible();

        // Go back to home
        await page.goto(BASE + '/');

        // Test Modes navigation
        const modesLink = page.locator('a', { hasText: 'Modes' }).first();
        await modesLink.click();
        await expect(page).toHaveURL(/\/modes\//);
        await expect(page.locator('h1', { hasText: 'Modes Collection' })).toBeVisible();

        // Go back to home
        await page.goto(BASE + '/');

        // Test Thoughts navigation
        const thoughtsLink = page.locator('a', { hasText: 'Thoughts' }).first();
        await thoughtsLink.click();
        await expect(page).toHaveURL(/\/thoughts\//);
        await expect(page.locator('h1', { hasText: 'Thoughts Collection' })).toBeVisible();

        // Go back to home
        await page.goto(BASE + '/');

        // Test Documentation navigation
        const docsLink = page.locator('a', { hasText: 'Documentation' }).first();
        await docsLink.click();
        await expect(page).toHaveURL(/\/docs\//);
        await expect(page.locator('h2', { hasText: 'Documentation' })).toBeVisible();
    });

    test('individual collection items are accessible', async ({ page }) => {
        // Check if a prompt item is accessible
        await page.goto(BASE + '/prompts/');
        const promptLink = page.locator('a', { hasText: 'Code Review Assistant' }).first();
        if (await promptLink.count() > 0) {
            await promptLink.click();
            await expect(page).toHaveURL(/code-review-assistant/);
            await expect(page.locator('h1')).toBeVisible();
        }

        // Check if an instruction item is accessible
        await page.goto(BASE + '/instructions/');
        const instructionLink = page.locator('a').filter({ hasText: /python/i }).first();
        if (await instructionLink.count() > 0) {
            await instructionLink.click();
            await expect(page.locator('h1')).toBeVisible();
        }

        // Check if a mode item is accessible
        await page.goto(BASE + '/modes/');
        const modeLink = page.locator('a', { hasText: 'Research Assistant' }).first();
        if (await modeLink.count() > 0) {
            await modeLink.click();
            await expect(page).toHaveURL(/research-assistant/);
            await expect(page.locator('h1')).toBeVisible();
        }
    });

    test('all collection pages have proper structure', async ({ page }) => {
        const collections = [
            { url: '/prompts/', heading: 'Prompts Collection' },
            { url: '/instructions/', heading: 'Instructions Collection' },
            { url: '/modes/', heading: 'Modes Collection' },
            { url: '/thoughts/', heading: 'Thoughts Collection' }
        ];

        for (const collection of collections) {
            await page.goto(BASE + collection.url);
            await expect(page.locator('h1', { hasText: collection.heading })).toBeVisible();

            // Check for category sections
            await expect(page.locator('h2, h3').first()).toBeVisible();

            // Check for "All" section or table
            const allSection = page.locator('h2', { hasText: /All/ });
            if (await allSection.count() > 0) {
                await expect(allSection).toBeVisible();
            }
        }
    });
});
