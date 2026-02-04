from datetime import time
import time
import allure
import pytest
#import pytest_check as check


# @pytest.mark.order(2)
# @pytest.mark.smoke
@pytest.mark.wip
@pytest.mark.asyncio

# @allure.title("Verify test_Configurations")
# @allure.description("Validate brandingPage")
async def test_Configurations(setup):
    basepage = setup["basepage"]
    loginPage = setup["loginPage"]
    welcomePage = setup["welcomePage"]
    ongoingthreadsPage = setup["ongoingthreadsPage"]
    brandingPage = setup["brandingPage"]
    authenticationPage = setup["authenticationPage"]
    usersPage = setup["usersPage"]


    failures = []
# brandingPage_valdaition
#     await brandingPage.click_on_Settings()
#     await brandingPage.validate_Configuration_tabs()
#     await brandingPage.validate_branding_tabs()
#     await brandingPage.validate_company_name()
#     await brandingPage.update_branding_logos()
#     await brandingPage.upload_login_background_image()


#SSO_openID_authentication_valdaition
    # await brandingPage.validate_Configuration_tabs()
    # await authenticationPage.verify_authentication_page_ui()
    # await authenticationPage.verify_new_SSO_OpenID_Connect_page()
    # await authenticationPage.fill_openID_auth_setup()
    # await authenticationPage.fill_auth_appinfo_details()
    # await authenticationPage.fill_auth_sso_provider_details()
    # await authenticationPage.fill_auth_advanced_details()
    # await authenticationPage.add_users_to_the_group()
    # await authenticationPage.search_for_created_authentication_type()
    # await authenticationPage.sso_auth_type_edit()
    # await authenticationPage.sso_auth_type_delete()


#SAML_authentication_valdaition
    # await brandingPage.validate_Configuration_tabs()
    # await authenticationPage.verify_authentication_page_ui()
    # await authenticationPage.verify_new_saml_page_properties()
    # await authenticationPage.fill_saml_auth_setup()
    # await authenticationPage.select_auth_protocol()
    # await authenticationPage.fill_saml_auth_appinfo_details()
    # await authenticationPage.fill_saml_auth_sso_provider_details()
    # await authenticationPage.fill_saml_auth_field_mapping_details()
    # await authenticationPage.fill_saml_auth_advanced_details()
    # await authenticationPage.add_users_to_the_group()
    # await authenticationPage.search_for_saml_authentication_type()
    # await authenticationPage.sso_auth_type_edit()
    # await authenticationPage.sso_auth_type_delete()

#users_valdaition

    await brandingPage.click_on_Settings()
    await brandingPage.validate_Configuration_tabs()
    await usersPage.validate_users_page_options()
    await usersPage.verify_users_table_columns()
    await usersPage.verify_adduser_fields()
    await usersPage.fill_user_details(
            first_name="Hari",
            last_name="Mulaguri",
            email="hari1@test.com",
            title="QA",
            phone="9999999999")


