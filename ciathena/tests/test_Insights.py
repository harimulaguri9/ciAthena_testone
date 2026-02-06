import allure
import pytest
# @pytest.mark.order(3)
@pytest.mark.wip
@pytest.mark.asyncio
# @allure.epic("Insights Hub")
# @allure.story("InsightsHub_UI")
# @allure.title("Verify InsightsHub UI elements")
# @allure.description("Validate UI components of Insights Hub after login")
async def test_Insights(setup):
    insightshubPage = setup["insightshubPage"]

    await insightshubPage.verify_insightshub_UI()
    await insightshubPage.verify_executive_cards()
    await insightshubPage.verify_personalized_insights_all_cards()

    #
    # with allure.step("login into the application"):
    #     await loginPage.login_success()
    # with allure.step("Select use case"):
    #     await welcomePage.select_usecase()
    # ---------------------------------------------------------
    # 3️⃣ VERIFY INSIGHTS HUB UI
    # ---------------------------------------------------------
    # with allure.step("Verify InsightsHub UI"):
    #     try:
    #         await insightshubPage.verify_insightshub_UI()
    #     except Exception as e:
    #         msg = f"verify_insightshub_UI failed: {e}"
    #         failures.append(msg)
    #         allure.attach(msg, "UI Check Failed", allure.attachment_type.TEXT)
    #         print("[WARNING] InsightsHub UI verification failed but continuing...")
    # ---------------------------------------------------------
    # 4️⃣ EXECUTIVE CARDS
    # ---------------------------------------------------------
    # with allure.step("Verify Executive Cards"):
    #     try:
    #         await insightshubPage.verify_executive_cards()
    #     except Exception as e:
    #         msg = f"verify_executive_cards failed: {e}"
    #         failures.append(msg)
    #         allure.attach(msg, "Executive Cards Failed", allure.attachment_type.TEXT)
    #         print("[WARNING] Executive cards verification failed but continuing...")
    # ---------------------------------------------------------
    # 5️⃣ PERSONALIZED INSIGHTS (ALL SECTIONS)
    # # ---------------------------------------------------------
    # with allure.step("Verify Personalized Insights – All Sections"):
    #     try:
    #         await insightshubPage.verify_personalized_insights_all_cards()
    #     except Exception as e:
    #         msg = f"verify_personalized_insights_all_cards failed: {e}"
    #         failures.append(msg)
    #         allure.attach(msg, "Personalized Insights Failed", allure.attachment_type.TEXT)
    #         print("[WARNING] Personalized insights verification failed but continuing...")
    # ---------------------------------------------------------
    # FAIL TEST IF ANY STEP FAILED
    # ---------------------------------------------------------
    # if failures:
    #     pytest.fail("\n".join(failures))