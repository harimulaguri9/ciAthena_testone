
from playwright.async_api import Page, expect
from ciathena.pages.BasePage import BasePage
#import pytest_check as check


class AuthenticationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

#Authentication
        self.authentication_nav_button = page.locator("#configurations-nav-button-authentication")
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
        self.auth_protocol_dropdown = page.locator("#auth-setup-protocol-select")
        self.auth_protocol_option = page.locator("#auth-setup-protocol-select")
        self.auth_properties_enabled_toggle = page.locator("input[type='checkbox']")

#App Information section
        self.auth_properties_appInfo_tab = page.locator("#auth-properties-subtab-appInformation-label")
        self.auth_properties_appInfo_redirect_URL = page.locator("#auth-app-information-redirect-input")
        self.auth_properties_appInfo_logout_URL = page.locator("#auth-app-information-logout-input")
        self.auth_properties_appInfo_back_channel_logout_URL = page.locator("#auth-app-information-backchannel-input")

#SSO Provider section
        self.sso_provider_tab = page.get_by_role("button", name="SSO Provider")
        self.sso_authority_url = page.locator('//input[contains(@placeholder,"Enter URL")]')
        self.sso_client_id = page.locator('//input[contains(@placeholder,"Enter client ID")]')
        self.sso_client_secret = page.locator('//input[contains(@placeholder,"Enter client secret")]')
        self.sso_scope = page.locator('//input[contains(@placeholder,"Enter scope")]')

#Fieldmaping
        self.fieldmapping_email = page.locator('#auth-field-mapping-email-input')
        self.fieldmapping_firstname = page.locator('#auth-field-mapping-first-name-input')
        self.fieldmapping_lastname = page.locator('#auth-field-mapping-last-name-input')
        self.fieldmapping_signin = page.locator('#auth-field-mapping-can-sign-in-input')
        self.fieldmapping_teamname = page.locator('#auth-field-mapping-team-name-input')

#Advanced
        self.advanced_tab = page.get_by_role("button", name="Advanced")
        self.post_logout_url = page.get_by_placeholder("https://dummy.url")

 #delete - confirm - button
        self.row = self.page.locator("tr", has_text="AuthTest1")
        self.edit_button=page.locator("p:has-text('Edit')")
        self.delete_button = page.locator("p:has-text('Delete')")
        self.delete_confirm = page.locator('#delete-confirm-button')

#Add new
        self.auth_users_tab_button = page.locator("#auth-form-tab-users")
        self.auth_add_users_title = page.locator("#auth-form-breadcrumb")
        self.auth_search_input = page.locator("#auth-users-search-input")
        self.auth_search_add_new_user_button = page.locator("#auth-users-add-button")
        self.auth_add_new_user_search_input = page.locator("#auth-add-users-search-input")
        self.auth_add_new_user_checkbox=page.locator("#auth-add-users-table-body input[type='checkbox']")
        self.auth_add_new_user_submit_button=page.locator(("#auth-add-users-submit-button"))
        self.auth_add_new_user_save_proceed_button = page.locator(("#auth-form-users-save-button"))

    async def add_users_to_the_group(self):
        await self.auth_users_tab_button.click()
        await expect(self.auth_add_users_title).to_be_visible()
        await self.auth_search_add_new_user_button.click()
        await self.auth_add_new_user_search_input.fill("Hari")
        await self.auth_add_new_user_checkbox.first.check()
        await self.auth_add_new_user_submit_button.click()
        await self.auth_add_new_user_save_proceed_button.click()


    # ---------- VALIDATION METHODS ----------
#Verify Authentication landing page UI
    async def verify_authentication_page_ui(self):
        await self.authentication_nav_button.click()
        await expect(self.authentication_page_title).to_be_visible()
        await expect(self.authentication_search_box).to_be_visible()
        await expect(self.add_new_authentication_button).to_be_visible()

#SSO_OpenID_Connect_authentication:
    async def verify_new_SSO_OpenID_Connect_page(self):
        await self.add_new_authentication_button.click()
        await expect(self.auth_properties_setup_tab).to_be_visible()
        await expect(self.auth_properties_tab).to_be_visible()
        await expect(self.auth_properties_users_tab).to_be_visible()
        await expect(self.auth_properties_setup_tab).to_be_visible()
        await expect(self.auth_properties_app_info_tab).to_be_visible()
        await expect(self.auth_properties_advanced_tab).to_be_visible()
        await expect(self.auth_properties_cancel_button).to_be_visible()
        await expect(self.auth_properties_save_proceed_button).to_be_visible()

    async def fill_openID_auth_setup(self):
        await self.auth_properties_auth_name.fill("AuthTest1")
        await self.auth_properties_auth_description.fill("AuthTest1_desc")

    async def fill_auth_appinfo_details(self):
        await self.auth_properties_appInfo_tab.click()
        await self.auth_properties_appInfo_redirect_URL.fill("https:/testciai-reditrect.com")
        await self.auth_properties_appInfo_logout_URL.fill("https:/testciai-logout.com")
        await self.auth_properties_appInfo_back_channel_logout_URL.fill("https:/testciai-channel.com")

        # auth_SSO_provider
    async def fill_auth_sso_provider_details(self):
            await self.auth_properties_sso_provider_tab.click()
            await self.sso_authority_url.fill("https:/testciai-authority_url.com")
            await self.sso_client_id.fill("1234567890")
            await self.sso_client_secret.fill("987654321")
            await self.sso_scope.fill("987654321")
    #auth_Advanced_details
    async def fill_auth_advanced_details(self):
        await self.advanced_tab.click()
        await self.post_logout_url.fill("https:/testciai-post_logout_url.com")
        await self.auth_properties_save_proceed_button.click()


#==================================================================================

    #auth_setup_details
    async def fill_SAML_auth_setup(self):
        await self.select_saml_authentication_protocol_type()
        await self.fill_auth_appinfo_details()
        await self.fill_auth_sso_provider_details()
        await self.fill_fieldmappig_details()
        await self.fill_auth_advanced_details()


    #auth_setup_details
    async def fill_email_passwrod_auth_setup(self):
        await self.select_saml_authentication_protocol_type()
        await self.fill_auth_appinfo_details()
        await self.fill_auth_sso_provider_details()
        await self.fill_fieldmappig_details()
        await self.fill_auth_advanced_details()


    async def select_saml_authentication_protocol_type(self):
        await self.auth_properties_auth_name.fill("AuthTest1")
        await self.auth_properties_auth_description.fill("AuthTest1_desc")
        await self.auth_protocol_dropdown.click()
        await page.get_by_role("option", name="SAML 2.0").click()

#auth_SSO_provider
    async def fill_auth_saml_sso_provider_details(self):
        await self.auth_properties_sso_provider_tab.click()
        await self.sso_authority_url.fill("https:/testciai-authority_url.com")
        await self.sso_client_id.fill("1234567890")
        await self.sso_client_secret.fill("987654321")
        await self.sso_scope.fill("987654321")


    async def fill_fieldmappig_details(self):
        await self.fieldmapping_email.fill("logout_url.com")
        await self.fieldmapping_firstname.fill("hari")
        await self.fieldmapping_lastname.fill("test11")
        await self.fieldmapping_signin.fill("signin")
        await self.fieldmapping_teamname.fill("teamA")

    async def perform_auth_edit_delete(self):
        await self.row.locator("button").last.click()
        await self.edit_button.click()
        await self.auth_properties_auth_description.fill("AuthTest1_desc1")
        await self.auth_properties_sso_provider_tab.click()
        await self.sso_authority_url.fill("https:/testciai-authority1.com")
        await self.auth_properties_save_proceed_button.click()
        await self.row.locator("button").last.click()
        await self.delete_button.click()
        await self.delete_confirm.click()


# ---------- ACTIONS ----------
    async def search_authentication(self, value):
        self.fill(self.search_box, value)

    async def click_add_new_authentication_button(self):
        await self.add_new_authentication_button.click()

    async def select_authentication_protocol(self, protocol_name: str):
        #
        # protocol_name:
        # - 'OpenID Connect'
        # - 'Email/Password'
        # - 'SAML 2.0'

        # Open dropdown
        await self.auth_protocol_dropdown.click()
        await self.page.wait_for_timeout(2000)
        # Select option dynamically
        await self.page.get_by_role("option", name=protocol_name).click()
        await self.page.wait_for_timeout(2000)
