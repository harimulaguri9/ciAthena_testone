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
        self.input_companyName = page.locator("#branding-tab-field-input-companyName")
        self.save_button = page.locator("#branding-save-button")

        # Primary  logo
        self.primary_logo_image = page.locator("#image-upload-card-primary-logo-image")
        self.primary_logo_upload_icon = page.locator("#image-upload-card-primary-logo-placeholder")
        self.primary_logo_delete_icon = page.locator("#image-upload-card-primary-logo-upload-button")
        self.primary_logo_upload_input = page.locator("input[type='file'][data-name='branding-tab-primary-logo-input']")

        # Branding logo
        self.brand_logo_image = page.locator("#image-upload-card-brand-logo-image")
        self.brand_logo_upload_icon = page.locator("#image-upload-card-brand-logo-placeholder")
        self.brand_logo_delete_icon = page.locator("#image-upload-card-brand-logo-delete-button")
        self.brand_logo_upload_input = page.locator("input[type='file'][data-name='branding-tab-brand-logo-input']")

        # Favicon logo
        self.favicon_logo = page.locator("input[type='file']").nth(2)
        self.favicon_logo_image = page.locator("#image-upload-card-favicon-image")
        self.favicon_logo_upload_icon = page.locator("#image-upload-card-favicon-preview")
        self.favicon_logo_delete_icon = page.locator("#image-upload-card-favicon-delete-button")
        self.favicon_logo_upload_input = page.locator("input[type='file'][data-name='branding-tab-favicon-input']")

        self.Background_image_choosefile = page.locator("#login-screen-tab-background-input")
        self.login_screen_banner_save_button = page.locator("#login-screen-tab-save-button")

    async def click_on_Settings(self):
        await self.page.wait_for_timeout(3000)  # 3 seconds
        await self.Settings.click()
    async def validate_Configuration_tabs(self):
        await self.page.wait_for_timeout(3000)  # 3 seconds
        await self.Configuration.click()
        await expect(self.Branding_nav_bar).to_be_visible()
        print("config page tabs")

    async def validate_branding_tabs(self):
        await self.Branding_nav_bar.click()
        await expect(self.branding_tab).to_be_visible()
        await expect(self.login_screen_tab).to_be_visible()

    async def validate_company_name(self):
        await expect(self.input_companyName).to_be_visible()
        await self.input_companyName.clear()
        await expect(self.page.locator("text=Company name cannot be blank")).to_be_visible()
        await self.input_companyName.fill("CustomerInsights")
        await self.save_button.click()

        # ---------- BRANDING ACTIONS ----------
    async def update_branding_logos(self):
        await self.branding_tab.click()
        await self.delete_upload_primary_logo()
        await self.delete_upload_brand_logo()
        await self.delete_upload_favicon_logo()

    # ---------- LOGIN SCREEN ACTIONS ----------

    async def delete_upload_primary_logo(self):
        await self.primary_logo_upload_input.wait_for(state="attached")
        # await self.primary_logo_image.hover()
        # await self.primary_logo_delete_icon.click()
        # expect(self.page.locator("text=Primary logo deleted successfully")).to_be_visible()
        await self.primary_logo_upload_input.set_input_files("tests/data/fast-icon.svg")
        # await expect(self.page.locator("text=Primary logo uploaded successfully")).to_be_visible()

    async def delete_upload_brand_logo(self):
        await self.brand_logo_upload_input.wait_for(state="attached")
        # await self.brand_logo_image.hover()
        # await self.brand_logo_delete_icon.click()
        # expect(self.page.locator("text=Brand logo deleted successfully")).to_be_visible()
        await self.brand_logo_upload_input.set_input_files("tests/data/340b-icon.svg")
        # await expect(self.page.locator("text=Brand logo uploaded successfully")).to_be_visible()


    async def delete_upload_favicon_logo(self):
        await self.favicon_logo_upload_input.wait_for(state="attached")
        # await self.favicon_logo_image.hover()
        # await self.favicon_logo_delete_icon.click()
        # expect(self.page.locator("text=Favicon deleted successfully")).to_be_visible()
        await self.favicon_logo_upload_input.set_input_files("tests/data/app-icon.svg")
        # await expect(self.page.locator("text=Favicon uploaded successfully")).to_be_visible()

    async def upload_login_background_image(self):
        await self.login_screen_tab.click()
        await self.Background_image_choosefile.set_input_files("tests/data/baner.svg")
        await self.login_screen_banner_save_button.click()

