import pytest
from _testcapi import awaitType


@pytest.mark.asyncio
@pytest.mark.smoke
async def test_teams_management(setup):
    brandingPage = setup["brandingPage"]
    teamsPage = setup["teamsPage"]

    print("test_users_management")
    await brandingPage.click_on_Settings()
    await brandingPage.validate_Configuration_tabs()
    await teamsPage.validate_teams_page_options()
    await teamsPage.fill_team_details(team_name="TeamsABC",team_desc_name="TeamsABC")
    await teamsPage.add_users_create_team()
    await teamsPage.validate_created_team_properties()
    await teamsPage.validate_rename_team()
    await teamsPage.validate_delete_team()

