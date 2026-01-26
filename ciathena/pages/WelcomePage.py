from datetime import time
from playwright.async_api import Page
import time
from ciathena.pages.BasePage import BasePage

class WelcomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.welcome_text=page.locator("#welcome-prefix")
        self.welcome_search_input=page.locator("#welcome-search-input")
        self.search_button=page.locator("#welcome-search-submit-button")
        self.mmm_usecase_icon=page.locator("#icon-app-mmm")
        self.navbar=page.locator("#navbar-deepdive-text-section")

    async def select_mmm_usecase(self):
        await self.welcome_search_input.click()
        await self.mmm_usecase_icon.wait_for(state="visible", timeout=10000)
        await self.mmm_usecase_icon.scroll_into_view_if_needed()
        await self.mmm_usecase_icon.click()
        await self.page.wait_for_timeout(10000)
