from datetime import time
import time
import allure
import pytest
#import pytest_check as check


# @pytest.mark.order(2)
@pytest.mark.smoke
@pytest.mark.wip
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
    # with allure.step("login into the application"):
    #     await loginPage.login_success()
    #
    # with allure.step("Select use case"):
    #     await welcomePage.select_usecase()
    #     print("usecasesss")

    # with allure.step("validate_Configuration_tabs"):
    #     print("configgg")
    await brandingPage.validate_Configuration_tabs()
    await brandingPage.validate_branding_tabs()
    await brandingPage.update_branding_logos()

    # with allure.step("users_page_valdaition"):
    #     await usersPage.validate_users_page_options()
    #     time.sleep(3)

    #brandingPage
    # with allure.step("validate_tabs"):
    #     await brandingPage.validate_branding_tabs()
    # # with allure.step("update_branding"):
    #     await brandingPage.update_branding_logos()
    # # with allure.step("update_login_background"):
    #     await brandingPage.update_login_background()


#authentication_valdaition
    # with allure.step("validate_Configuration_tabs"):
    #     await brandingPage.validate_Configuration_tabs()
    # with allure.step("validate_authentication_page_options"):
    #     await authenticationPage.validate_authentication_page_options()
    # with allure.step("validate_new_authentication_page_options"):
    #     await authenticationPage.validate_new_authentication_page_options()
    # with allure.step("enter_auth_setup_details"):
    #     await authenticationPage.auth_setup_details()
    # # with allure.step("enter_auth_appinfo_details"):
    # #     await authenticationPage.auth_appinfo_details()
    # with allure.step("enter_auth_SSO_provider_details"):
    #     await authenticationPage.auth_sso_provider_details()
    # with allure.step("enter_auth_Advanced_details"):
    #     await authenticationPage.auth_advanced_details()


#users_valdaition
    # await brandingPage.validate_Configuration_tabs()
    # await usersPage.validate_users_page_options()
    #
    # await usersPage.verify_users_table_columns()
    # await usersPage.verify_adduser_fields()
    # await usersPage.fill_user_details(
            # first_name="Hari",
            # last_name="Mulaguri",
            # email="hari@test.com",
            # title="QA",
            # phone="9999999999")
            # use_case="Analytics",
            # role="Admin",
            # team="QA",
            # licensed=True)

