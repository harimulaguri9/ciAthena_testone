from datetime import time
import time
# import allure
import pytest
# #import pytest_check as check
#
#
# # @pytest.mark.order(2)
# # @pytest.mark.smoke
# # @pytest.mark.wip
# @pytest.mark.asyncio
# @pytest.mark.asyncio
# @pytest.mark.branding
# async def test_branding_configuration(setup):
#     brandingPage = setup["brandingPage"]
#
#     await brandingPage.click_on_Settings()
#     await brandingPage.validate_Configuration_tabs()
#     await brandingPage.validate_branding_tabs()
#     await brandingPage.validate_company_name()
#     await brandingPage.update_branding_logos()
#     await brandingPage.upload_login_background_image()


@pytest.mark.asyncio
@pytest.mark.auth
@pytest.mark.openid
async def test_openid_authentication_flow(setup):
    brandingPage = setup["brandingPage"]
    authenticationPage = setup["authenticationPage"]

    await brandingPage.validate_Configuration_tabs()
    await authenticationPage.verify_authentication_page_ui()
    await authenticationPage.verify_new_SSO_OpenID_Connect_page()
    await authenticationPage.fill_openID_auth_setup()
    await authenticationPage.fill_auth_appinfo_details()
    await authenticationPage.fill_auth_sso_provider_details()
    await authenticationPage.fill_auth_advanced_details()
    await authenticationPage.add_users_to_the_group()
    await authenticationPage.search_for_created_authentication_type()
    await authenticationPage.sso_auth_type_edit()
    await authenticationPage.sso_auth_type_delete()


@pytest.mark.asyncio
@pytest.mark.auth
@pytest.mark.saml
async def test_saml_authentication_flow(setup):
    ongoingthreadsPage = setup["ongoingthreadsPage"]
    brandingPage = setup["brandingPage"]
    authenticationPage = setup["authenticationPage"]

    # await ongoingthreadsPage.goto_Settings()
    await brandingPage.validate_Configuration_tabs()
    await authenticationPage.verify_authentication_page_ui()
    await authenticationPage.verify_new_saml_page_properties()
    await authenticationPage.fill_saml_auth_setup()
    await authenticationPage.select_auth_protocol()
    await authenticationPage.fill_saml_auth_appinfo_details()
    await authenticationPage.fill_saml_auth_sso_provider_details()
    await authenticationPage.fill_saml_auth_field_mapping_details()
    await authenticationPage.fill_saml_auth_advanced_details()
    await authenticationPage.add_users_to_the_group()
    await authenticationPage.search_for_saml_authentication_type()
    await authenticationPage.sso_auth_type_edit()
    await authenticationPage.sso_auth_type_delete()


@pytest.mark.asyncio
@pytest.mark.auth
@pytest.mark.email
async def test_email_authentication_flow(setup):
    ongoingthreadsPage = setup["ongoingthreadsPage"]
    brandingPage = setup["brandingPage"]
    authenticationPage = setup["authenticationPage"]

    await ongoingthreadsPage.goto_Settings()
    await brandingPage.validate_Configuration_tabs()
    await authenticationPage.verify_authentication_page_ui()
    await authenticationPage.verify_email_authentication_page_properties()
    await authenticationPage.fill_email_auth_setup()
    await authenticationPage.fill_password_policy_fields()
    await authenticationPage.add_users_to_the_group()
    await authenticationPage.search_for_email_authentication_type()
    await authenticationPage.sso_auth_type_edit()
    await authenticationPage.sso_auth_type_delete()

# @pytest.mark.asyncio
# @pytest.mark.users
# # async def test_users_management(setup):
#     brandingPage = setup["brandingPage"]
#     usersPage = setup["usersPage"]
#
#     await brandingPage.click_on_Settings()
#     await brandingPage.validate_Configuration_tabs()
#     await usersPage.validate_users_page_options()
#     await usersPage.verify_users_table_columns()
#     await usersPage.verify_adduser_fields()
#     await usersPage.fill_user_details(
#         first_name="Hari",
#         last_name="Mulaguri",
#         email="hari1@test.com",
#         title="QA",
#         phone="9999999999"
#     )
# async def test_search_edit_users(setup):
#     usersPage = setup["usersPage"]
#     brandingPage = setup["brandingPage"]
#
#     await brandingPage.click_on_Settings()
#     await brandingPage.validate_Configuration_tabs()
#     await usersPage.validate_users_page_options()
#     await usersPage.verify_users_table_columns()
#     await usersPage.verify_user_search_edit()
#     await usersPage.verify_user_search_delete()

#
# async def test_search_edit_user_sections(setup):
#     usersPage = setup["usersPage"]
#     brandingPage = setup["brandingPage"]
#
#     await brandingPage.click_on_Settings()
#     await brandingPage.validate_Configuration_tabs()
#     await usersPage.validate_users_page_options()
#     await usersPage.verify_users_table_columns()
#     await usersPage.verify_user_search_edit()
#     await usersPage.verify_user_search_delete()


