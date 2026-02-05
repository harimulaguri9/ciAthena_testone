import pytest


# @pytest.mark.asyncio
# @pytest.mark.users
# async def test_users_management(setup):
#     brandingPage = setup["brandingPage"]
#     usersPage = setup["usersPage"]
#
#     print("test_users_management")
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
#
# @pytest.mark.asyncio
# @pytest.mark.users
# async def test_search_edit_users(setup):
#     usersPage = setup["usersPage"]
#     brandingPage = setup["brandingPage"]
#
#     print("test_search_edit_users")
#     await brandingPage.click_on_Settings()
#     await brandingPage.validate_Configuration_tabs()
#     await usersPage.validate_users_page_options()
#     await usersPage.verify_users_table_columns()
#     await usersPage.verify_user_search_edit()
#     await usersPage.verify_user_search_delete()

# @pytest.mark.asyncio
# @pytest.mark.users
# async def test_search_edit_user_sections(setup):
#     usersPage = setup["usersPage"]
#     brandingPage = setup["brandingPage"]
#
#     print("test_search_edit_user_sections")
#     await brandingPage.click_on_Settings()
#     await brandingPage.validate_Configuration_tabs()
#     await usersPage.validate_users_page_options()
#     await usersPage.verify_users_table_columns()
#     await usersPage.verify_user_search_edit()

@pytest.mark.asyncio
@pytest.mark.users
async def test_user_filter_options(setup):
    usersPage = setup["usersPage"]
    brandingPage = setup["brandingPage"]

    print("test_search_edit_user_sections")
    await brandingPage.click_on_Settings()
    await brandingPage.validate_Configuration_tabs()
    await usersPage.validate_users_page_options()
    await usersPage.verify_user_filters()