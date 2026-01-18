import re
from datetime import time
from playwright.async_api import Page, expect
import time
from ciathena.pages.BasePage import BasePage
#import pytest_check as check


class BrandingPage():
    def __init__(self, page: Page):
        # super().__init__(page)
        self.page = page
        self.Settings = page.locator("//*[@id='navbar-settings-button']")
        self.Configuration = page.locator("//*[@id='sidebar-icon-configuration']")
        self.Branding_nav_bar = page.get_by_role("button", name="Branding")
        self.branding_tab = page.get_by_role("tab", name="Branding")
        self.login_screen_tab = page.get_by_role("tab", name="Login screen")

        # Primary  logo
        self.primary_logo_image = page.locator("#image-upload-card-primary-logo-placeholder")
        self.primary_logo_upload_icon = page.locator("#image-upload-card-brand-logo-placeholder")
        self.primary_logo_upload_input = page.locator("input[type='file'][data-name='branding-tab-primary-logo-input']")

        # Branding logo
        self.company_name = page.get_by_role("textbox", name="Enter company name")
        # self.brand_logo_upload_icon = page.locator("#image-upload-card-brand-logo-placeholder")
        self.brand_logo_upload_input = page.locator("input[type='file'][data-name='branding-tab-brand-logo-input']")

        # Favicon logo
        self.favicon_logo = page.locator("input[type='file']").nth(2)
        self.favicon_logo_upload_icon = page.locator("#image-upload-card-favicon-preview")
        self.favicon_logo_upload_input = page.locator("input[type='file'][data-name='branding-tab-favicon-input']")

        self.Background_image_choosefile_button = page.locator("#login-screen-tab-background-section")
        self.save_button = page.get_by_role("button", name="Save")

        brand_logo_scg_path = r"/ciathena/tests/data/340b-icon.svg"
        background_image_path= r"/ciathena/tests/data/baner.svg"

    async def validate_Configuration_tabs(self):
        print("Configuration_tabs")
        await self.page.wait_for_timeout(3000)  # 20 seconds
        await self.Settings.click()
        await self.Configuration.click()
        await self.page.wait_for_timeout(3000)  # 20 seconds
        expect(self.Branding_nav_bar).to_be_visible()
        print("config page tabs")

    async def validate_branding_tabs(self):
        await self.Branding_nav_bar.click()
        await self.page.wait_for_timeout(3000)  # 20 seconds
        expect(self.branding_tab).to_be_visible()
        await self.page.wait_for_timeout(2000)  # 20 seconds
        expect(self.login_screen_tab).to_be_visible()



        # ---------- BRANDING ACTIONS ----------
    async def update_branding_logos(self):
        await self.branding_tab.click()
        await self.page.wait_for_timeout(2000)  # 20 seconds
        await self.company_name.fill("CIAITest")
        await self.page.wait_for_timeout(2000)  # 20 seconds
        await self.upload_primary_logo()
        await self.page.wait_for_timeout(2000)  # 20 seconds
        await self.upload_brand_logo()
        await self.page.wait_for_timeout(2000)  # 20 seconds
        await self.upload_favicon_logo()
        await self.page.wait_for_timeout(2000)  # 20 seconds
        # await self.upload_login_background_image()

        # ---------- LOGIN SCREEN ACTIONS ----------

    async def upload_primary_logo(self):
            await self.primary_logo_upload_input.wait_for(state="attached")
            await self.primary_logo_upload_input.set_input_files("tests/data/fast-icon.svg")

    async def upload_brand_logo(self):
        await self.brand_logo_upload_input.wait_for(state="attached")
        await self.brand_logo_upload_input.set_input_files("tests/data/340b-icon.svg")

    async def upload_favicon_logo(self):
        await self.favicon_logo_upload_input.wait_for(state="attached")
        await self.favicon_logo_upload_input.set_input_files("tests/data/app-icon.svg")

    async def upload_login_background_image(self):
        await self.login_screen_tab.click()
        # await self.Background_image_choosefile_button.click()
        await self.Background_image_choosefile_button.set_input_files("tests/data/baner.svg")
