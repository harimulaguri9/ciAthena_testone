
import pytest
@pytest.mark.asyncio
@pytest.mark.order(2)
# @pytest.mark.wip
@pytest.mark.asyncio
async def test_ask_question(setup):
    ongoingthreadsPage = setup["ongoingthreadsPage"]
    await ongoingthreadsPage.ask_question()

# @pytest.mark.asyncio
# @pytest.mark.order(3)
# async def test_validate_generated_insights_options(setup):
#     ongoingthreadsPage = setup["ongoingthreadsPage"]
    await ongoingthreadsPage.verify_share_insights()
    await ongoingthreadsPage.verify_unsave_insights()
    await ongoingthreadsPage.verify_save_insights()
    await ongoingthreadsPage.verify_download_insights()
    await ongoingthreadsPage.verify_sql_query()
    await ongoingthreadsPage.click_like_button()
    await ongoingthreadsPage.click_dislike_button()
