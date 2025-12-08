from datetime import time
from playwright.async_api import Page
import time
from ciathena.pages.BasePage import BasePage

class WelcomePage(BasePage):
    def __init__(self, page: Page,step_logger=None):
        super().__init__(page,step_logger)
        self.welcome_text=page.locator("#welcome-prefix")
        self.welcome_search_input=page.locator("#welcome-search-input")
        self.search_button=page.locator("#welcome-search-submit-button")
        self.mmx_usecase_icon=page.locator("#icon-app-mmx")
        self.navbar=page.locator("#navbar-deepdive-text-section")

    async def select_usecase(self):
        await self.welcome_search_input.click()
        await self.mmx_usecase_icon.wait_for(state="visible", timeout=2000)
        await self.mmx_usecase_icon.scroll_into_view_if_needed()
        await self.mmx_usecase_icon.click()
        await self.page.wait_for_timeout(20000)
