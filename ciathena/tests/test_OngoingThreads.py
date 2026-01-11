from datetime import time
import time
import allure
import pytest
# @pytest.mark.smoke
# @pytest.mark.asyncio
# # @allure.epic("MMM_OngoingThreads")
# # @allure.story("OngoingThreads_Features")
# @allure.title("Verify OngoingThreads UI elements")
# @allure.description("Validate OngoingThreads")
# @pytest.mark.order(1)
# async def test_OngoingThreads(setup):
    # basepage = setup["basepage"]
    # loginPage = setup["loginPage"]
    # welcomePage = setup["welcomePage"]
    # ongoingthreadsPage = setup["ongoingthreadsPage"]
    #
    # failures = []
    # with allure.step("login into the application"):
    #     await loginPage.login_success()
    #
    # with allure.step("Select use case"):
    #     await welcomePage.select_usecase()

@pytest.mark.asyncio
@pytest.mark.order(1)
async def test_ongoing_threads_UI(setup):
    # basepage = setup["basepage"]
    # loginPage = setup["loginPage"]
    # welcomePage = setup["welcomePage"]
    ongoingthreadsPage = setup["ongoingthreadsPage"]
    await ongoingthreadsPage.verify_ongoing_threads_UI()

    # await setup["ongoingthreadsPage"].verify_ongoing_threads_UI()
    print("UI")

@pytest.mark.asyncio
@pytest.mark.order(2)
async def test_ask_question(setup):
    # basepage = setup["basepage"]
    # loginPage = setup["loginPage"]
    # welcomePage = setup["welcomePage"]
    ongoingthreadsPage = setup["ongoingthreadsPage"]
    await ongoingthreadsPage.ask_question()

    # await setup["ongoingthreadsPage"].ask_question()
    print("ask")


@pytest.mark.asyncio
@pytest.mark.order(3)
async def test_validate_insights_actions(setup):
    await setup["ongoingthreadsPage"].share_insights()

    #
    # async def ask_question(setup):
    #     await ongoingthreadsPage.save_insights()
    #
    # with allure.step("Click Unsave Insights button"):
    #     await ongoingthreadsPage.unsave_insights()
    #
    # with allure.step("Share insights"):
    #     await ongoingthreadsPage.share_insights()
    #
    #
    # with allure.step("Click Download Insights button"):
    #     await ongoingthreadsPage.click_download_insights_button()
    #
    # with allure.step("Validate SQL button"):
    #     await ongoingthreadsPage.validate_sql_button()
    #
    # with allure.step("Click Info button"):
    #     await ongoingthreadsPage.click_info_button()
    #
    # with allure.step("Click Like button"):
    #     await ongoingthreadsPage.click_like_button()
    #
    # with allure.step("Click Dislike button"):
    #     await ongoingthreadsPage.click_dislike_button()
    #
    # with allure.step("Verify Suggested Questions"):
    #     await ongoingthreadsPage.verify_suggested_questions()
    #
    # with allure.step("Verify verify_Threads_history"):
    #     await ongoingthreadsPage.verify_OGT_history()