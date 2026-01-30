from datetime import time
import time
import allure
import pytest
#import pytest_check as check


# @pytest.mark.order(2)
# @pytest.mark.smoke
# @pytest.mark.wip
@pytest.mark.asyncio
# @allure.epic("BrandingPage validation")
# @allure.story("brandingPages_Features")
# @allure.title("Verify brandingPage UI elements")
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
#     await brandingPage.validate_Configuration_tabs()
#     await brandingPage.validate_branding_tabs()
#     await brandingPage.validate_company_name()
#     await brandingPage.update_branding_logos()
#     await brandingPage.upload_login_background_image()


#SSO_openID_authentication_valdaition
    await brandingPage.validate_Configuration_tabs()
    await authenticationPage.verify_authentication_page_ui()
    await authenticationPage.verify_new_SSO_OpenID_Connect_page()
    await authenticationPage.fill_openID_auth_setup()
    time.sleep(2)
    await authenticationPage.fill_auth_appinfo_details()
    await authenticationPage.fill_auth_sso_provider_details()
    await authenticationPage.fill_auth_advanced_details()

    time.sleep(3)
    await authenticationPage.add_users_to_the_group()
    time.sleep(3)
    await authenticationPage.search_for_created_authentication_type()
    time.sleep(3)
    await authenticationPage.sso_auth_type_edit()
    time.sleep(2)
    await authenticationPage.sso_auth_type_delete()
    time.sleep(2)


#SAML_authentication_valdaition
    # await brandingPage.validate_Configuration_tabs()
    # await authenticationPage.verify_authentication_page_ui()
    # await authenticationPage.validate_new_auth_properties_page()
    # await authenticationPage.fill_auth_setup_details()
    # await authenticationPage.create_SAML_auth_type()
    # await authenticationPage.fill_auth_appinfo_details()
    # await authenticationPage.fill_auth_sso_provider_details()
    # await authenticationPage.fill_auth_advanced_details()
    # await authenticationPage.perform_auth_edit_delete()


#users_valdaition
    # await usersPage.validate_users_page_options()
    # await usersPage.verify_users_table_columns()
    # await usersPage.verify_adduser_fields()
    # await usersPage.fill_user_details(
    #         first_name="Hari",
    #         last_name="Mulaguri",
    #         email="hari@test.com",
    #         title="QA",
    #         phone="9999999999")
    # await usersPage.users_search(first_name="Hari")

            # use_case="Analytics",
                    # role="Admin",
                    # team="QA",
                    # licensed=True)

