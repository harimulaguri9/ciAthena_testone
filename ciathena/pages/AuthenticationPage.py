import time

from playwright.async_api import Page, expect
from ciathena.pages.BasePage import BasePage


class AuthenticationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

#Authentication
        self.authentication_nav_button = page.locator("#configurations-nav-button-authentication")
        self.authentication_page_title = page.locator("//h1[contains(text(),'Authentication')]")
        self.authentication_search_input = page.get_by_placeholder("Search...")
        self.add_new_authentication_button = page.get_by_role("button", name="Add new")

# Add new / Properties
        self.auth_properties_page_title = page.get_by_role("heading", name="Add new / Properties")
        self.auth_properties_tab = page.get_by_role("tab", name="Properties")
        self.auth_properties_users_tab = page.get_by_role("tab", name="Users")
        self.auth_properties_cancel_button = page.locator("//button[text()='Cancel']")
        self.auth_properties_save_proceed_button = page.get_by_role("button", name="Save & Proceed")

# Setup-sections
        self.auth_properties_setup_tab = page.get_by_role("button", name="Setup")
        self.auth_properties_app_info_tab = page.locator("#auth-properties-subtab-appInformation-label")
        self.auth_properties_sso_provider_tab = page.get_by_role("button", name="SSO Provider")
        self.auth_properties_advanced_tab = page.get_by_role("button", name="Advanced")
        self.auth_password_policy_tab = page.locator("#auth-properties-subtab-passwordPolicy-label")



        self.auth_properties_auth_name = page.get_by_placeholder("Enter name")
        self.auth_properties_auth_description = page.get_by_placeholder("Enter description")
        self.auth_protocol_dropdown = page.locator("#auth-setup-protocol-select")
        self.auth_openID_protocol_option = page.locator("#auth-setup-protocol-option-openid_connect")
        self.auth_saml_protocol_option = page.locator("#auth-setup-protocol-option-saml")
        self.auth_email_protocol_option = page.locator("#auth-setup-protocol-option-email_password")
        self.auth_properties_enabled_toggle = page.locator("input[type='checkbox']")
        self.auth_email_protocol_option = page.locator("#auth-setup-protocol-option-email_password")
        self.auth_password_policy_min_chars_input = page.locator("#auth-password-policy-min-chars-input")
        self.auth_password_policy_expiry_select = page.locator("#auth-password-policy-expiry-select")
        self.auth_password_policy_expiry_30 = page.locator('//*[@id="auth-password-policy-expiry-30"]')


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

# SAML- SSO Provider section
        self.sso_provider_tab = page.get_by_role("button", name="SSO Provider")
        self.saml_saml_entity_identifier_input = page.locator('#auth-sso-provider-saml-entity-identifier-input')
        self.saml_signon_url_input = page.locator('#auth-sso-provider-saml-signon-url-input')
        self.saml_logout_url_input = page.locator('#auth-sso-provider-saml-logout-url-input')
        self.saml_certificate_input = page.locator('#auth-sso-provider-saml-certificate-input')
        self.saml_sign_auth_request_control = page.locator('#auth-sso-provider-saml-sign-auth-request-control')

#Fieldmaping
        self.fieldmapping_tab = page.locator('#auth-properties-subtab-fieldMapping')
        self.fieldmapping_email = page.locator('#auth-field-mapping-email-input')
        self.fieldmapping_firstname = page.locator('#auth-field-mapping-first-name-input')
        self.fieldmapping_lastname = page.locator('#auth-field-mapping-last-name-input')
        self.fieldmapping_signin = page.locator('#auth-field-mapping-can-sign-in-input')
        self.fieldmapping_teamname = page.locator('#auth-field-mapping-team-name-input')

#Advanced
        self.advanced_tab = page.get_by_role("button", name="Advanced")
        self.post_logout_url = page.get_by_placeholder("https://dummy.url")

 #delete - confirm - button
        auth_sso_name='AAuth_SSO_Test1'
        self.sso_auth_more_button = self.page.locator("#auth-list-row-0-more-button")
        self.auth_edit_option=page.locator("p:has-text('Edit')")
        self.auth_delete_option = page.locator("p:has-text('Delete')")
        self.auth_delete_confirm = page.locator('#delete-confirm-button')
        self.auth_remove_user_confirm=page.locator('#user-removal-dialog-remove-button')
        self.auth_discard_changes_confirm= page.locator("#unsaved-changes-dialog-confirm-button")

#Add new
        self.auth_users_tab_button = page.locator("#auth-form-tab-users")
        self.auth_add_users_title = page.locator("#auth-form-breadcrumb")
        self.auth_search_input = page.locator("#auth-users-search-input")
        self.auth_add_user_button = page.locator("#auth-users-add-button")
        self.auth_add_new_user_search_input = page.locator("#auth-add-users-search-input")
        self.auth_add_new_user_checkbox=page.locator("(//input[@type='checkbox'])[2]")
        self.auth_add_new_user_submit_button=page.locator(("#auth-add-users-submit-button"))
        self.auth_add_new_user_save_proceed_button = page.locator(("#auth-form-users-save-button"))


    async def add_users_to_the_group(self):
        await self.auth_users_tab_button.click()
        await expect(self.auth_add_users_title).to_be_visible()
        await self.auth_add_user_button.click()
        await self.auth_add_new_user_search_input.fill("hari")
        await self.auth_add_new_user_checkbox.first.check()
        await self.auth_add_new_user_submit_button.click()
        await self.auth_add_new_user_save_proceed_button.click()
        time.sleep(3)
        # await expect(self.auth_updated_toast_message).to_be_visible()


    async def delete_users_to_the_group(self):
        users_checkbox = self.page.locator("//tbody[@data-name='auth-users-table-body']//input[@type='checkbox']")
        count = await users_checkbox.count()
        for i in range(count):
            await users_checkbox.nth(i).uncheck()



    # ---------- OpenID connect----------
#Verify Authentication landing page UI
    async def verify_authentication_page_ui(self):
        await self.authentication_nav_button.click()
        await self.page.wait_for_timeout(3000)
        await expect(self.authentication_page_title).to_be_visible()
        await expect(self.authentication_search_input).to_be_visible()
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
        await self.auth_properties_auth_name.fill("AAuth_SSO_Test1")
        await self.auth_properties_auth_description.fill("AAuth_SSO_Test1_desc")

    async def fill_auth_appinfo_details(self):
        await self.auth_properties_appInfo_tab.click()
        await self.auth_properties_appInfo_redirect_URL.fill("https:/testciai-reditrect.com")
        await self.auth_properties_appInfo_logout_URL.fill("https:/testciai-logout.com")
        await self.auth_properties_appInfo_back_channel_logout_URL.fill("https:/testciai-channel.com")

        # auth_SSO_provider
    async def fill_auth_sso_provider_details(self):
        await self.auth_properties_sso_provider_tab.click()
        time.sleep(3)
        await self.sso_authority_url.fill("https:/testciai-authority_url.com")
        await self.sso_client_id.fill("1234567890")
        await self.sso_client_secret.fill("987654321")
        await self.sso_scope.fill("987654321")
    #auth_Advanced_details
    async def fill_auth_advanced_details(self):
        await self.advanced_tab.click()
        await self.post_logout_url.fill("https:/testciai-post_logout_url.com")


    #===============================SAML============
    async def verify_new_saml_page_properties(self):
        await self.add_new_authentication_button.click()
        await expect(self.auth_properties_tab).to_be_visible()
        await expect(self.auth_properties_users_tab).to_be_visible()
        await expect(self.auth_properties_setup_tab).to_be_visible()
        await expect(self.auth_properties_app_info_tab).to_be_visible()


    async def fill_saml_auth_setup(self):
        await self.auth_properties_auth_name.fill("AAuth_SAML_Test1")
        await self.auth_properties_auth_description.fill("AAuth_SAML_Test1_desc")

    async def select_auth_protocol(self):
        time.sleep(2)
        await self.auth_protocol_dropdown.click()
        await self.auth_saml_protocol_option.click()


    async def fill_saml_auth_appinfo_details(self):
        await self.page.wait_for_timeout(3000)
        await self.auth_properties_appInfo_tab.click()
        await self.auth_properties_appInfo_redirect_URL.fill("https:/testciai-reditrect.com")
        await self.auth_properties_appInfo_logout_URL.fill("https:/testciai-logout.com")
        await self.auth_properties_appInfo_back_channel_logout_URL.fill("https:/testciai-channel.com")


    async def fill_saml_auth_sso_provider_details(self):
        time.sleep(3)
        await self.auth_properties_sso_provider_tab.click()
        await self.saml_saml_entity_identifier_input.fill("https:/testciai-authority_url.com")
        await self.saml_signon_url_input.fill("https:/testciai-authority_signon.com")
        await self.saml_logout_url_input.fill("https:/testciai-authority_logout.com")
        await self.saml_certificate_input.fill("certificate test")
        await self.saml_sign_auth_request_control.click()

    async def fill_saml_auth_field_mapping_details(self):
        time.sleep(3)
        await self.fieldmapping_tab.click()
        await self.fieldmapping_email.fill("haritest@test.com")
        await self.fieldmapping_firstname.fill("hari")
        await self.fieldmapping_lastname.fill("test1")
        await self.fieldmapping_signin.fill(" yes")
        await self.fieldmapping_teamname.fill("team test")

    #auth_Advanced_details
    async def fill_saml_auth_advanced_details(self):
        time.sleep(3)
        await self.advanced_tab.click()
        await self.post_logout_url.fill("https:/testciai-post_logout_url.com")

    async def auth_type_save_proceed_button(self):
        await self.auth_properties_save_proceed_button.click()
        await self.page.wait_for_timeout(5000)

    async def search_for_saml_authentication_type(self):
        await self.page.wait_for_timeout(3000)
        await self.authentication_search_input.fill("AAuth_SAML_Test1")
        await expect(self.page.locator("#auth-list-table-body")).to_contain_text("AAuth_SAML_Test1")

    async def sso_auth_type_edit(self):
        await self.page.wait_for_timeout(3000)
        await self.sso_auth_more_button.click()
        await self.page.wait_for_timeout(2000)
        await self.auth_edit_option.click()
        await self.auth_users_tab_button.click()
        # await self.auth_add_new_user_search_input.fill("Hari")
        await self.delete_users_to_the_group()
        await self.auth_properties_save_proceed_button.click()
        await self.auth_remove_user_confirm.click()


    async def sso_auth_type_delete(self):
        await self.sso_auth_more_button.click()
        await self.page.wait_for_timeout(2000)
        await self.auth_delete_option.click()
        await self.auth_delete_confirm.click()


    #=====================================SAML_auth_setup=============================================
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
        await self.page.get_by_role("option", name="SAML 2.0").click()

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


# ---------- EMAIL -------------------------------------------------------------
    async def verify_email_authentication_page_properties(self):
        await self.add_new_authentication_button.click()
        await self.select_email_auth_protocol()
        await self.page.wait_for_timeout(3000)
        await expect(self.auth_properties_tab).to_be_visible()
        await expect(self.auth_properties_users_tab).to_be_visible()
        await expect(self.auth_properties_setup_tab).to_be_visible()
        await expect(self.auth_password_policy_tab).to_be_visible()


    async def fill_email_auth_setup(self):
        await self.auth_properties_auth_name.fill("AAuth_email_Test1")
        await self.auth_properties_auth_description.fill("AAuth_email_Test1_desc")
        await self.auth_properties_enabled_toggle.click()

    async def fill_password_policy_fields(self):
        await self.auth_password_policy_tab.click()
        await self.page.wait_for_timeout(2000)
        await self.auth_password_policy_min_chars_input.fill("15")
        await self.auth_password_policy_expiry_select.click()
        await self.page.wait_for_timeout(2000)
        await self.auth_password_policy_expiry_30.click()
        await self.page.wait_for_timeout(2000)


    async def select_email_auth_protocol(self):
        time.sleep(2)
        await self.auth_protocol_dropdown.click()
        await self.auth_email_protocol_option.click()

    async def click_add_new_authentication_button(self):
        await self.add_new_authentication_button.click()


    async def search_for_email_authentication_type(self):
        time.sleep(4)
        await self.authentication_search_input.fill("AAuth_email_Test1")
        await expect(self.page.locator("#auth-list-table-body")).to_contain_text("AAuth_email_Test1")

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
