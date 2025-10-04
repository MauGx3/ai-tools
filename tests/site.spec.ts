import { test, expect } from '@playwright/test';

const BASE = process.env.PAGE_URL || 'https://maugx3.github.io/ai-tools';

test.describe('AI Tools site', () => {
    test('home page loads and nav works', async ({ page }) => {
        await page.goto(BASE + '/');
        await expect(page).toHaveTitle(/AI Tools Collection/i);

        // Click Prompts link
        const prompts = await page.locator('a', { hasText: 'Prompts' }).first();
        await prompts.click();
        await expect(page).toHaveURL(/\/prompts\//);

        // Try to click a prompt detail if present
        const promptLink = page.locator('a', { hasText: 'Code Review Assistant' }).first();
        if (await promptLink.count() > 0) {
            await promptLink.click();
            await expect(page).toHaveURL(/code-review-assistant/);
            await expect(page.locator('h1')).toBeVisible();
        }
    });
});
