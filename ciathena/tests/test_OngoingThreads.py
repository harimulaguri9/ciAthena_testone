
import pytest
@pytest.mark.asyncio
@pytest.mark.order(2)
@pytest.mark.smoke
async def test_ask_question(setup):
    ongoingthreadsPage = setup["ongoingthreadsPage"]
    await ongoingthreadsPage.ask_question()

    await ongoingthreadsPage.verify_share_insights()
    await ongoingthreadsPage.verify_unsave_insights()
    await ongoingthreadsPage.verify_save_insights()
    await ongoingthreadsPage.verify_download_insights()
    await ongoingthreadsPage.verify_sql_query()
    await ongoingthreadsPage.click_like_button()
    await ongoingthreadsPage.click_dislike_button()
