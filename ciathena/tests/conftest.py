import pytest
from playwright.async_api import async_playwright
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

@pytest.fixture(scope="function")
async def setup(step_logger):
    async with async_playwright() as p:
        print("🚀 Launching Chromium browser...")
        browser = await p.chromium.launch(headless=False, slow_mo=100)
        context = await browser.new_context()
        """Create a new page and initialize all page objects."""
        page = await context.new_page()
        print(f"🧩 New Page Created: {id(page)}")

    # Initialize all your page objects
        basepage = BasePage(page, step_logger)
        loginPage = LoginPage(page, step_logger)
        welcomePage = WelcomePage(page, step_logger)
        ongoingthreadsPage = OngoingThreadsPage(page, step_logger)
        insightshubPage = InsightsHubPage(page, step_logger)
        collabspacePage = CollabSpacePage(page, step_logger)
        brandingPage = BrandingPage(page, step_logger)
        authenticationPage =AuthenticationPage(page, step_logger)
        usersPage =UsersPage(page, step_logger)

        print(f"🧩 BasePage Using Page: {id(basepage.page)}")
        print("🔹 Starting navigation--")
        await basepage.navigate("https://ciathena.customerinsights.ai/")
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
        # print("🧹 Closing page after test--")
        #
        # await page.close()



@pytest.fixture
async def step_logger(request):
    request.node.step_logs = []

    async def log_step(message: str):
        print(f"[STEP] {message}")
        request.node.step_logs.append(f"➡️ {message}")

    return log_step

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if hasattr(item, "step_logs") and rep.when == "call":
        html_steps = "<br>".join(item.step_logs)
        extra = getattr(rep, "extra", [])
        extra.append(extras.html(f"<div><strong>Steps:</strong><br>{html_steps}</div>"))
        rep.extra = extra

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()