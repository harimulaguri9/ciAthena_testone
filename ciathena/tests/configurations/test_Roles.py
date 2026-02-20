import pytest
@pytest.mark.asyncio
@pytest.mark.wip
async def test_all_default_personas(setup):
    brandingPage = setup["brandingPage"]
    rolesPage = setup["rolesPage"]
    print("Running Roles Management Test")

    await brandingPage.click_on_Settings()
    await brandingPage.validate_Configuration_tabs()
    await rolesPage.navigate_to_roles()
    await rolesPage.validate_all_default_personas()

@pytest.mark.asyncio
@pytest.mark.wip
async def test_admin_full_access(setup):
    brandingPage = setup["brandingPage"]
    rolesPage = setup["rolesPage"]

    print("test_users_management")
    await brandingPage.click_on_Settings()
    await brandingPage.validate_Configuration_tabs()
    await rolesPage.navigate_to_roles()
    await rolesPage.validate_admin_full_access()

@pytest.mark.asyncio
@pytest.mark.wip
async def test_viewer_restricted_access(setup):
    brandingPage = setup["brandingPage"]
    rolesPage = setup["rolesPage"]

    print("test_users_management")
    await brandingPage.click_on_Settings()
    await brandingPage.validate_Configuration_tabs()
    await rolesPage.navigate_to_roles()
    await rolesPage.validate_viewer_restricted_access()

@pytest.mark.asyncio
@pytest.mark.wip
async def test_persona_selection_difference(setup):
    brandingPage = setup["brandingPage"]
    rolesPage = setup["rolesPage"]

    print("test_users_management")
    await brandingPage.click_on_Settings()
    await brandingPage.validate_Configuration_tabs()
    await rolesPage.navigate_to_roles()
    await rolesPage.validate_persona_selection_difference()