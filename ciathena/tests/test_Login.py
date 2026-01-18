
import allure
import pytest
@pytest.mark.order(1)
# @pytest.mark.usefixtures("step_logger")
@pytest.mark.smoke
@pytest.mark.asyncio
@allure.epic("LoginPage")
@allure.story("Login functionality")
@allure.title("SSO-Login")
@allure.description("test_login with valid logins")
async def test_login_functionality(setup):
    basepage = setup["basepage"]
    loginPage = setup["loginPage"]

    with allure.step("login into the application"):
        await loginPage.login_success()
