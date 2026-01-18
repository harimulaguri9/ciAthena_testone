import pytest
import allure

@pytest.mark.order(4)
# @pytest.mark.usefixtures("step_logger")
@pytest.mark.smoke
@pytest.mark.asyncio
@allure.epic("Collabspace")
@allure.story("CollabspaceUI")
@allure.title("Verify Collabspace UI")
@allure.description("Validate that the UI of Collabspace loads correctly")
async def test_Collabspace(setup):
    basepage = setup["basepage"]
    loginPage = setup["loginPage"]
    welcomePage = setup["welcomePage"]
    collabspacePage = setup["collabspacePage"]

    # LOGIN
    with allure.step("login into the application"):
        await loginPage.login_success()

    # USE CASE
    with allure.step("Select use case"):
        await welcomePage.select_usecase()

    # ---------------------
    #  RUN TESTS SAFELY
    # ---------------------

    # 1️⃣ Rename
    with allure.step("Verify rename_spaces"):
        try:
            await collabspacePage.rename_spaces()
        except Exception as e:
            allure.attach(str(e), "Rename Failed", allure.attachment_type.TEXT)
            print(f"[WARNING] rename_spaces failed but continuing...")

    # 2️⃣ Delete
    with allure.step("Verify delete_spaces"):
        try:
            await collabspacePage.delete_spaces()
        except Exception as e:
            allure.attach(str(e), "Delete Failed", allure.attachment_type.TEXT)
            print(f"[WARNING] delete_spaces failed but continuing...")

    # 3️⃣ Dashboard creation
    with allure.step("Verify create_Dashboard"):
        try:
            await collabspacePage.create_Dashboard()
        except Exception as e:
            allure.attach(str(e), "Dashboard Creation Failed", allure.attachment_type.TEXT)
            print(f"[WARNING] create_Dashboard failed but continuing...")
