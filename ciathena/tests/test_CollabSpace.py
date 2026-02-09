# import pytest
# import allure
#
# @pytest.mark.wip
# @pytest.mark.asyncio
# # @allure.epic("Collabspace")
# # @allure.story("CollabspaceUI")
# # @allure.title("Verify Collabspace UI")
# @allure.description("Validate that the UI of Collabspace loads correctly")
# async def test_create_new_collabspace(setup):
#     basepage = setup["basepage"]
#     loginPage = setup["loginPage"]
#     welcomePage = setup["welcomePage"]
#     collabspacePage = setup["collabspacePage"]
#
#     await collabspacePage.create_new_collabspace()
#     await collabspacePage.rename_collabspace()
#     await collabspacePage.delete_collabspace()
#     await collabspacePage.create_Dashboard()
#     await collabspacePage.edit_Dashboard()
#     await collabspacePage.delete_Dashboard()


import pytest
import allure

@pytest.mark.order(1)
@pytest.mark.wipx
@pytest.mark.asyncio
@allure.description("Validate that the UI of Collabspace loads correctly")
async def test_create_new_collabspace(setup):
    basepage = setup["basepage"]
    loginPage = setup["loginPage"]
    welcomePage = setup["welcomePage"]
    collabspacePage = setup["collabspacePage"]

    await collabspacePage.create_new_collabspace()
    await collabspacePage.rename_collabspace()
    await collabspacePage.delete_collabspace()
    await collabspacePage.create_Dashboard()
    await collabspacePage.edit_Dashboard()
    await collabspacePage.delete_Dashboard()


# @pytest.mark.order(2)
# @pytest.mark.wipx
# @pytest.mark.asyncio
# async def test_rename_collabspace(setup):
#     collabspacePage = setup["collabspacePage"]
#     await collabspacePage.rename_collabspace()
#
#
# @pytest.mark.order(3)
# @pytest.mark.wipx
# @pytest.mark.asyncio
# async def test_delete_collabspace(setup):
#     collabspacePage = setup["collabspacePage"]
#     await collabspacePage.delete_collabspace()
#
#
# @pytest.mark.order(4)
# @pytest.mark.wipx
# @pytest.mark.asyncio
# async def test_create_Dashboard(setup):
#     collabspacePage = setup["collabspacePage"]
#     await collabspacePage.create_Dashboard()
#
# @pytest.mark.order(5)
# @pytest.mark.wipx
# @pytest.mark.asyncio
# async def test_delete_Dashboard(setup):
#     collabspacePage = setup["collabspacePage"]
#     await collabspacePage.delete_Dashboard()