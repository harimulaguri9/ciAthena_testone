import re
from datetime import time
from playwright.async_api import Page, expect
import time
from ciathena.pages.BasePage import BasePage
#import pytest_check as check


class BrandingPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        page.get_by_role("button", name="Teams Teams").click()
        page.get_by_role("textbox", name="Search by team name/").click()
        page.get_by_role("button", name="Add Team Add team").click()
        page.get_by_role("textbox", name="Team name").click()
        page.get_by_role("textbox", name="Team name").fill("Team1")
        page.get_by_role("textbox", name="Team name").press("ControlOrMeta+a")
        page.get_by_role("textbox", name="Input a description here...").click()
        page.get_by_role("textbox", name="Input a description here...").fill("Teams1desc")
        page.get_by_role("combobox").click()
        page.get_by_text("FAST").click()
        page.locator(".MuiBackdrop-root").click()
        page.get_by_role("tab", name="Users").click()
        page.get_by_role("textbox", name="Search by name/role name...").click()
        page.get_by_role("textbox", name="Search by name/role name...").fill("hari")
        page.get_by_role("textbox", name="Search by name/role name...").dblclick()
        page.get_by_role("textbox", name="Search by name/role name...").fill("")
        page.get_by_role("button", name="Add User Add user").click()
        page.get_by_role("textbox", name="Search by name/role name...").click()
        page.get_by_role("textbox", name="Search by name/role name...").fill("hari")
        page.get_by_role("checkbox").nth(2).check()
        page.get_by_role("button", name="Submit").click()
        page.get_by_role("checkbox").nth(1).check()
        page.get_by_role("tab", name="General").click()
        page.get_by_role("button", name="Save & Proceed").click()
        page.get_by_role("checkbox").nth(1).check()
        page.get_by_role("button", name="Submit").click()
