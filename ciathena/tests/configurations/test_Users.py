import pytest

@pytest.mark.asyncio
@pytest.mark.order(1)
@pytest.mark.wip

async def test_users_management(setup):
    brandingPage = setup["brandingPage"]
    usersPage = setup["usersPage"]

    print("test_users_management")
    await brandingPage.click_on_Settings()
    await brandingPage.validate_Configuration_tabs()
    await usersPage.validate_users_page_options()
    await usersPage.verify_users_table_columns()
    await usersPage.verify_adduser_fields()
    await usersPage.fill_user_details(
        first_name="Hari",
        last_name="Mulaguri",
        email="haritest1@test.com",
        title="QA",
        phone="9999999999"
    )
@pytest.mark.order(2)
@pytest.mark.asyncio
@pytest.mark.wip
async def test_search_edit_users(setup):
    usersPage = setup["usersPage"]
    brandingPage = setup["brandingPage"]

    print("test_search_edit_users")
    await brandingPage.click_on_Settings()
    await brandingPage.validate_Configuration_tabs()
    await usersPage.validate_users_page_options()
    await usersPage.verify_user_search_edit()

@pytest.mark.order(3)
@pytest.mark.asyncio
@pytest.mark.wip
async def verify_user_search_delete(setup):
    usersPage = setup["usersPage"]
    brandingPage = setup["brandingPage"]

    print("verify_user_search_delete")
    await brandingPage.click_on_Settings()
    await brandingPage.validate_Configuration_tabs()
    await usersPage.validate_users_page_options()
    await usersPage.verify_user_delete()


@pytest.mark.order(4)
@pytest.mark.asyncio
@pytest.mark.wip
async def test_user_filter_options(setup):
    usersPage = setup["usersPage"]
    brandingPage = setup["brandingPage"]

    print("test_search_edit_user_sections")
    await brandingPage.click_on_Settings()
    await brandingPage.validate_Configuration_tabs()
    await usersPage.validate_users_page_options()
    await usersPage.verify_user_filters()

# @pytest.mark.order(5)
# @pytest.mark.asyncio
# @pytest.mark.users1
# async def test_user_sections(setup):
#     usersPage = setup["usersPage"]
#     brandingPage = setup["brandingPage"]
#
#     print("test_search_edit_user_sections")
#     await brandingPage.click_on_Settings()
#     await brandingPage.validate_Configuration_tabs()
#     await usersPage.validate_users_page_options()

@pytest.mark.order(6)
@pytest.mark.asyncio
@pytest.mark.wip
async def test_validate_edit_user_tabs(setup):
    usersPage = setup["usersPage"]
    brandingPage = setup["brandingPage"]

    print("test_edit_user_sections")
    await brandingPage.click_on_Settings()
    await brandingPage.validate_Configuration_tabs()
    await usersPage.validate_users_page_options()
    await usersPage.validate_edit_user_tabs_validation()

@pytest.mark.order(7)
@pytest.mark.asyncio
@pytest.mark.wip

# @pytest.mark.user1
async def test_user_activity_sections(setup):
    usersPage = setup["usersPage"]
    brandingPage = setup["brandingPage"]

    print("test_search_edit_user_sections")
    await brandingPage.click_on_Settings()
    await brandingPage.validate_Configuration_tabs()
    await usersPage.validate_users_page_options()
    await usersPage.verify_user_activity_sections()
