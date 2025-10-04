import { defineConfig } from '@playwright/test';

export default defineConfig({
    timeout: 30_000,
    use: {
        headless: true,
    },
    projects: [
        { name: 'chromium', use: { browserName: 'chromium' } },
        { name: 'firefox', use: { browserName: 'firefox' } },
    ],
});
