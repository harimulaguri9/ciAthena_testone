
from playwright.async_api import Page, expect
from ciathena.pages.BasePage import BasePage
#import pytest_check as check


class AuthenticationPage(BasePage):
    def __init__(self, page: Page, step_logger=None):
        super().__init__(page, step_logger)

#Authentication
        self.authentication_nav_button = page.get_by_role("button", name="Authentication")
        self.authentication_page_title = page.locator("//h1[contains(text(),'Authentication')]")
        self.authentication_search_box = page.get_by_placeholder("Search...")
        self.add_new_authentication_button = page.get_by_role("button", name="Add new")

# Add new / Properties
        self.auth_properties_page_title = page.get_by_role("heading", name="Add new / Properties")
        self.auth_properties_tab = page.get_by_role("tab", name="Properties")
        self.auth_properties_users_tab = page.get_by_role("tab", name="Users")
        self.auth_properties_cancel_button = page.locator("//button[text()='Cancel']")
        self.auth_properties_save_proceed_button = page.get_by_role("button", name="Save & Proceed")

# Setup-sections
        self.auth_properties_setup_tab = page.get_by_role("button", name="Setup")
        self.auth_properties_app_info_tab = page.get_by_role("button", name="App Information")
        self.auth_properties_sso_provider_tab = page.get_by_role("button", name="SSO Provider")
        self.auth_properties_advanced_tab = page.get_by_role("button", name="Advanced")

        self.auth_properties_auth_name = page.get_by_placeholder("Enter name")
        self.auth_properties_auth_description = page.get_by_placeholder("Enter description")
        self.auth_protocol_dropdown = page.get_by_role("button", name="OpenID Connect")
        self.auth_properties_enabled_toggle = page.locator("input[type='checkbox']")

#App Information section
        # self.auth_properties_appInfo_tab = page.get_by_role("button", name="App Information")
        # self.auth_properties_appInfo_redirect_URL = page.get_by_placeholder("https://dummy.url")
        # self.auth_properties_appInfo_logout_URL = page.locator("//*[@id=':r88:']")
        # self.auth_properties_appInfo_back_channel_logout_URL = page.locator("//*[@id=':r89:']")

#SSO Provider section
        self.sso_provider_tab = page.get_by_role("button", name="SSO Provider")
        self.sso_authority_url = page.locator('//input[contains(@placeholder,"Enter URL")]')
        self.sso_client_id = page.locator('//input[contains(@placeholder,"Enter client ID")]')
        self.sso_client_secret = page.locator('//input[contains(@placeholder,"Enter client secret")]')
        self.sso_scope = page.locator('//input[contains(@placeholder,"Enter scope")]')

#Advanced
        self.advanced_tab = page.get_by_role("button", name="Advanced")
        self.post_logout_url = page.get_by_placeholder("https://dummy.url")




# ---------- VALIDATION METHODS ----------
#Authentication page
    async def validate_authentication_page_options(self):
        await self.authentication_nav_button.click()
        await expect(self.authentication_page_title).to_be_visible()
        await expect(self.authentication_search_box).to_be_visible()
        await expect(self.add_new_authentication_button).to_be_visible()
        print("authentication_")

#authentication_page_sections
    async def validate_new_authentication_page_options(self):
        await self.add_new_authentication_button.click()
        # await expect(self.auth_properties_page_title).to_be_visible()
        await expect(self.auth_properties_tab).to_be_visible()
        await expect(self.auth_properties_users_tab).to_be_visible()
        await expect(self.auth_properties_setup_tab).to_be_visible()
        await expect(self.auth_properties_app_info_tab).to_be_visible()
        await expect(self.auth_properties_advanced_tab).to_be_visible()
        await expect(self.auth_properties_cancel_button).to_be_visible()
        await expect(self.auth_properties_save_proceed_button).to_be_visible()
        # expect(self.auth_properties_setup_tab).to_be_visible()
        print("authentication_properties_")

#auth_setup_details
    async def auth_setup_details(self):
        await self.auth_properties_auth_name.fill("AuthTest1")
        await self.auth_properties_auth_description.fill("AuthTest1")
        # await self.select_authentication_protocol("SAML 2.0")

#auth_appInfo_details auth_appinfo_details
    # async def auth_appinfo_details(self):
        # await self.auth_properties_appInfo_tab.click()
        # await self.auth_properties_appInfo_redirect_URL.fill("https:/testciai-reditrect.com")
        # await self.auth_properties_appInfo_logout_URL.fill("https:/testciai-logout.com")
        # await self.auth_properties_appInfo_back_channel_logout_URL.fill("https:/testciai-channel.com")

#auth_SSO_provider
    async def auth_sso_provider_details(self):
        await self.auth_properties_sso_provider_tab.click()
        await self.sso_authority_url.fill("https:/testciai-authority_url.com")
        await self.sso_client_id.fill("1234567890")
        await self.sso_client_secret.fill("987654321")
        await self.sso_scope.fill("987654321")


    #auth_Advanced_details
    async def auth_advanced_details(self):
        await self.advanced_tab.click()
        await self.post_logout_url.fill("https:/testciai-post_logout_url.com")
        await self.auth_properties_cancel_button.click()















# ---------- ACTIONS ----------
    async def search_authentication(self, value):
        self.fill(self.search_box, value)

    async def click_add_new_authentication_button(self):
        await self.add_new_authentication_button.click()

    async def select_authentication_protocol(self, protocol_name: str):
        """
        protocol_name:
        - 'OpenID Connect'
        - 'Email/Password'
        - 'SAML 2.0'
        """
        # Open dropdown
        await self.auth_protocol_dropdown.click()
        await self.page.wait_for_timeout(2000)
        # Select option dynamically
        await self.page.get_by_role("option", name=protocol_name).click()
        await self.page.wait_for_timeout(2000)
