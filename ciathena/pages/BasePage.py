from playwright.async_api import Page, expect


class BasePage:
    def __init__(self, page: Page, step_logger=None):
        """
        Base class for all pages.
        :param page: Playwright Page object
        :param step_logger: Optional logging function for test step logs
        """
        self.page = page
        self.step_logger = step_logger  # injected from pytest fixture or passed manually

    async def launch(self):
        """Launch the base URL and verify the Microsoft Sign-in page is visible."""
        await self.page.goto("https://ciathena-qa.customerinsights.ai/")
        await expect(self.page.get_by_text("Sign in with Microsoft")).to_be_visible(timeout=20000)
        if self.step_logger:
            self.step_logger("✅ Navigated to sign-in page successfully")

    async def navigate(self, url: str, timeout: int = 60000):
        """Navigate to a given URL."""
        if self.step_logger:
            self.step_logger(f"🌐 Navigating to URL: {url}")
        await self.page.goto(url, timeout=timeout, wait_until="domcontentloaded")

    # async def initialise(self):
    #     browser = await p.chromium.launch(headless=False)
    #     page = await browser.new_page()
    #     basepage = BasePage(page, step_logger)
    #     await basepage.navigate("https://ciathena-qa.customerinsights.ai/")

    async def click(self, locator, description: str = ""):
        """
        Custom click method with logging and auto-wait.
        :param locator: Playwright locator object
        :param description: Description for logs (e.g., 'Login button')
        """
        try:
            if self.step_logger:
                self.step_logger(f"🖱️ Clicking on {description or locator}")

            await locator.wait_for(state="visible")
            await locator.click()

            if self.step_logger:
                self.step_logger(f"✅ Clicked successfully on {description or locator}")

        except Exception as e:
            if self.step_logger:
                self.step_logger(f"❌ Failed to click on {description or locator}: {e}")
            raise

    async def assert_visible(self, locator, description: str = ""):
        """
        Common assertion to check element visibility with logging.
        """
        try:
            if self.step_logger:
                self.step_logger(f"👀 Verifying visibility of {description}")


            await expect(locator).to_be_visible(timeout=3000)

            if self.step_logger:
                self.step_logger(f"✅ {description} is visible")

        except Exception as e:
            if self.step_logger:
                self.step_logger(f"❌ {description} is NOT visible: {e}")
            raise
