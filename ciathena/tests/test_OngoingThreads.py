from datetime import time
import time
import allure
import pytest
#import pytest_check as check
@pytest.mark.order(2)
@pytest.mark.usefixtures("step_logger")
@pytest.mark.smoke
@pytest.mark.asyncio
@allure.epic("MMM_OngoingThreads")
@allure.story("OngoingThreads_Features")
@allure.title("Verify OngoingThreads UI elements")
@allure.description("Validate OngoingThreads")
async def test_OngoingThreads(setup):
    basepage = setup["basepage"]
    loginPage = setup["loginPage"]
    welcomePage = setup["welcomePage"]
    ongoingthreadsPage = setup["ongoingthreadsPage"]

    failures = []
    with allure.step("login into the application"):
        await loginPage.login_success()

    with allure.step("Select use case"):
        await welcomePage.select_usecase()


    with allure.step("Verify Ongoing Threads UI"):
        await ongoingthreadsPage.verify_ongoing_threads_UI()


    with allure.step("Ask a question in Ongoing Threads"):
        await ongoingthreadsPage.ask_question()

    with allure.step("Wait for insights to be generated"):
        time.sleep(30)
    with allure.step("Save insights"):
        await ongoingthreadsPage.save_insights()

    with allure.step("Click Unsave Insights button"):
        await ongoingthreadsPage.unsave_insights()

    with allure.step("Share insights"):
        await ongoingthreadsPage.share_insights()


    with allure.step("Click Download Insights button"):
        await ongoingthreadsPage.click_download_insights_button()

    with allure.step("Validate SQL button"):
        await ongoingthreadsPage.validate_sql_button()

    with allure.step("Click Info button"):
        await ongoingthreadsPage.click_info_button()

    with allure.step("Click Like button"):
        await ongoingthreadsPage.click_like_button()

    with allure.step("Click Dislike button"):
        await ongoingthreadsPage.click_dislike_button()

    with allure.step("Verify Suggested Questions"):
        await ongoingthreadsPage.verify_suggested_questions()

    with allure.step("Verify verify_Threads_history"):
        await ongoingthreadsPage.verify_OGT_history()