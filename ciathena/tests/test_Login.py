
import allure
import pytest
# @pytest.mark.order(1)
# @pytest.mark.smoke
@pytest.mark.wip
@pytest.mark.asyncio

@allure.description("test_login_functionality_valid_logins")
async def test_login_functionality(setup):
    # basepage = setup["basepage"]
    # loginPage = setup["loginPage"]
    welcomePage = setup["welcomePage"]
    welcomePage.validate_welcomepage_ui()
