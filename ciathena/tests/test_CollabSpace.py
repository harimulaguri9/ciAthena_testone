import pytest
import allure

@pytest.mark.order(1)
@pytest.mark.asyncio
@pytest.mark.smoke
async def test_create_new_collabspace(setup):
    basepage = setup["basepage"]
    loginPage = setup["loginPage"]
    welcomePage = setup["welcomePage"]

    collabspacePage = setup["collabspacePage"]
    await collabspacePage.create_new_collabspace()


@pytest.mark.order(2)
@pytest.mark.asyncio
@pytest.mark.smoke
async def test_rename_collabspace(setup):
    collabspacePage = setup["collabspacePage"]
    await collabspacePage.rename_collabspace()

@pytest.mark.order(3)
@pytest.mark.asyncio
@pytest.mark.smoke
async def test_delete_collabspace(setup):
    collabspacePage = setup["collabspacePage"]
    await collabspacePage.delete_collabspace()


@pytest.mark.order(4)
@pytest.mark.asyncio
@pytest.mark.smoke
async def test_create_Dashboard(setup):
    collabspacePage = setup["collabspacePage"]
    await collabspacePage.create_Dashboard()

@pytest.mark.order(4)
@pytest.mark.asyncio
@pytest.mark.smoke
async def test_edit_Dashboard(setup):
    collabspacePage = setup["collabspacePage"]
    await collabspacePage.edit_Dashboard()


@pytest.mark.order(5)
@pytest.mark.asyncio
@pytest.mark.smoke
async def test_delete_Dashboard(setup):
    collabspacePage = setup["collabspacePage"]
    await collabspacePage.delete_Dashboard()