import re
from datetime import time
from playwright.async_api import Page, expect
import time
from ciathena.pages.BasePage import BasePage
import pytest_check as check


class BrandingPage(BasePage):
    def __init__(self, page: Page, step_logger=None):
        super().__init__(page, step_logger)
        self.Settings = page.locator("//*[@id='navbar-settings-button']")
        self.Configuration = page.locator("//*[@id='sidebar-icon-configuration']")
        self.Branding_nav_bar = page.get_by_role("button", name="Branding")
        self.branding_tab = page.get_by_role("tab", name="Branding")
        self.login_screen_tab = page.get_by_role("tab", name="Login screen")
        # Branding fields
        self.company_name = page.get_by_role("textbox", name="Enter company name")
        self.brand_logo_image = page.locator("//p[normalize-space()='Brand logo']/following::img[@alt='Uploaded'][1]")
        self.brand_logo_upload_icon = page.locator("[data-testid='UploadIcon']")
        # self.brand_logo_upload = page.locator("input[type='file']").nth(1)
        self.favicon_logo = page.locator("input[type='file']").nth(2)
        # Login screen
        self.Background_image = page.get_by_role("button", name="Choose file")
        self.save_button = page.get_by_role("button", name="Save")

        brand_logo_scg_path = r"/ciathena/tests/data/340b-icon.svg"
        background_image_path= r"/ciathena/tests/data/baner.svg"

    async def validate_Configuration_tabs(self):
        await self.Settings.click()
        await self.Configuration.click()
        await self.page.wait_for_timeout(3000)  # 20 seconds
        expect(self.Branding_nav_bar).to_be_visible()

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
        await self.brand_logo_image.hover()
        time.sleep(2)
        print("hover")
        await self.update_brand_logo()
        print("path open")

        # await self.brand_logo_input.set_input_files(
        #     r"C:\HARI\ciATHENA_Backup\ciATHENA_Backup\ciathena_autoamtion\assets\340b-icon.svg"
        # )


        # ---------- LOGIN SCREEN ACTIONS ----------

    async def update_brand_logo(self):

        await self.brand_logo_image.click()
        await self.page.set_input_files(
            "[data-testid='UploadIcon']",
            "tests/data/340b-icon.svg"
        )
        # await self.page.locator("//p[normalize-space()='Brand logo']/following::img[@alt='Uploaded'][1]").set_input_files("tests/data/340b-icon.svg")

    async def update_primary_logo(self):
        await self.login_screen_tab.click()
        await self.primary_logo.click()
        await self.Background_image_file_input.set_input_files(
            r"C:\HARI\ciATHENA_Backup\ciATHENA_Backup\ciathena_autoamtion\assets\340b-icon.svg"
        )


    async def update_login_background(self):
        await self.login_screen_tab.click()
        await self.Background_image.click()
        await self.Background_image_file_input.set_input_files(
            r"C:\HARI\ciATHENA_Backup\ciATHENA_Backup\ciathena_autoamtion\assets\340b-icon.svg"
        )
