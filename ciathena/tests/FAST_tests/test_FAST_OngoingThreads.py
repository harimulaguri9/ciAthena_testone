
import pytest
@pytest.mark.asyncio
@pytest.mark.order(2)
# @pytest.mark.wip
@pytest.mark.asyncio
async def test_ask_fast_question(setup):

    welcomePage = setup["welcomePage"]
    fast_ongoingthreadsPage = setup["fast_ongoingthreadsPage"]

    await welcomePage.select_fast_usecase()
    await fast_ongoingthreadsPage.ask_fast_question()

# async def goto_Settings(setup):
#     ongoingthreadsPage = setup["ongoingthreadsPage"]
#     await ongoingthreadsPage.goto_Settings()

    # @pytest.mark.asyncio
# @pytest.mark.order(3)
# async def test_validate_generated_insights_options(setup):
#     ongoingthreadsPage = setup["ongoingthreadsPage"]
    await fast_ongoingthreadsPage.verify_fast_share_insights()
    await fast_ongoingthreadsPage.verify_fast_unsave_insights()
    await fast_ongoingthreadsPage.verify_fast_save_insights()
    await fast_ongoingthreadsPage.verify_fast_download_insights()
    await fast_ongoingthreadsPage.verify_fast_sql_query()
    await fast_ongoingthreadsPage.click_fast_like_button()
    await fast_ongoingthreadsPage.click_dislike_button()
