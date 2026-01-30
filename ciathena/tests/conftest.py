import allure
import pytest
import pytest_asyncio
from playwright.async_api import async_playwright, Page
import asyncio
from ciathena.pages.BasePage import BasePage
from ciathena.pages.LoginPage import LoginPage
from ciathena.pages.WelcomePage import WelcomePage
from ciathena.pages.InsightsHubPage import InsightsHubPage
from ciathena.pages.OngoingThreadsPage import OngoingThreadsPage
from ciathena.pages.CollabSpacePage import CollabSpacePage
from ciathena.pages.brandingPage import BrandingPage
from ciathena.pages.AuthenticationPage import AuthenticationPage
from ciathena.pages.UsersPage import UsersPage
from pytest_html import extras
# @pytest.fixture(scope="function")
@pytest_asyncio.fixture
async def setup():
    async with async_playwright() as p:
        print("🚀 Launching Chromium browser...")
        browser = await p.chromium.launch(headless=False, slow_mo=3000)
        context = await browser.new_context()
        """Create a new page and initialize all page objects."""
        page = await context.new_page()
        print(f"🧩 New Page Created: {id(page)}")

    # Initialize all your page objects
        basepage = BasePage(page)
        loginPage = LoginPage(page)
        welcomePage = WelcomePage(page)
        ongoingthreadsPage = OngoingThreadsPage(page)
        insightshubPage = InsightsHubPage(page)
        collabspacePage = CollabSpacePage(page)
        brandingPage = BrandingPage(page)
        authenticationPage =AuthenticationPage(page)
        usersPage =UsersPage(page)

        print(f"🧩 BasePage Using Page: {id(basepage.page)}")
        await page.goto("https://ciathena.customerinsights.ai/")
        await loginPage.login_success()
        await welcomePage.select_mmm_usecase()

        yield {
            "page": page,
            "basepage": basepage,
            "loginPage": loginPage,
            "welcomePage": welcomePage,
            "ongoingthreadsPage": ongoingthreadsPage,
            "insightshubPage": insightshubPage,
            "collabspacePage" : collabspacePage,
            "brandingPage" : brandingPage,
            "authenticationPage": authenticationPage,
            "usersPage": usersPage

        }
        print("🧹 Closing page after test--")
        await page.close()



# @pytest.fixture
# async def step_logger(request):
#     request.node.step_logs = []
#
#     async def log_step(message: str):
#         print(f"[STEP] {message}")
#         request.node.step_logs.append(f"➡️ {message}")
#     return log_step

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.failed:
        page = item.funcargs.get("page") or item.funcargs.get("setup", {}).get("page")

        if isinstance(page, Page):
            try:
                loop = asyncio.get_event_loop()
            except RuntimeError:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)

            screenshot_bytes = loop.run_until_complete(
                page.screenshot(full_page=True)
            )

            allure.attach(
                screenshot_bytes,
                name=f"Failure Screenshot ({report.when})",
                attachment_type=allure.attachment_type.PNG
            )


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#
#     if report.failed and report.when == "call":
#         page = item.funcargs.get("page", None)
#
#         # 1️⃣ Screenshot
#         if page:
#             screenshot = page.screenshot()
#             allure.attach(
#                 screenshot,
#                 name=f"{item.name} - Screenshot",
#                 attachment_type=allure.attachment_type.PNG
#             )
#
#             # 2️⃣ Current URL
#             allure.attach(
#                 page.url,
#                 name="Current URL",
#                 attachment_type=allure.attachment_type.TEXT
#             )
#
#             # 3️⃣ Page title
#             title = page.title()
#             allure.attach(
#                 title,
#                 name="Page Title",
#                 attachment_type=allure.attachment_type.TEXT
#             )
#
#         # 4️⃣ Full failure reason (test body)
#         allure.attach(
#             report.longreprtext,
#             name="Test Failure Traceback",
#             attachment_type=allure.attachment_type.TEXT
#s        )


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()