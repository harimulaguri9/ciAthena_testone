from playwright.async_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        """
        Base class for all pages.
        :param page: Playwright Page object
        :param step_logger: Optional logging function for test step logs
        """
        self.page = page
        #self.step_logger = step_logger  # injected from pytest fixture or passed manually



    async def click(self, locator, description: str = ""):
        await locator.wait_for(state="visible")
        await locator.click()
        #
        # """
        # Custom click method with logging and auto-wait.
        # :param locator: Playwright locator object
        # :param description: Description for logs (e.g., 'Login button')
        # """
        # try:
        #     # if self.step_logger:
        #     #     self.step_logger(f"🖱️ Clicking on {description or locator}")
        #
        #     # if self.step_logger:
        #     #     self.step_logger(f"✅ Clicked successfully on {description or locator}")
        #
        # except Exception as e:
        #     # if self.step_logger:
        #     #     self.step_logger(f"❌ Failed to click on {description or locator}: {e}")
        #     raise

    async def assert_visible(self, locator, description: str = ""):
        await expect(locator).to_be_visible(timeout=3000)

        # """
        # Common assertion to check element visibility with logging.
        # """
        # try:
        #     # if self.step_logger:
        #     #     self.step_logger(f"👀 Verifying visibility of {description}")
        #
        #
        #     # await expect(locator).to_be_visible(timeout=3000)
        #     #
        #     # if self.step_logger:
        #     #     self.step_logger(f"✅ {description} is visible")
        #
        # except Exception as e:
        #     # if self.step_logger:
        #     #     self.step_logger(f"❌ {description} is NOT visible: {e}")
        #     raise
