from pydoc import visiblename

from playwright.sync_api import sync_playwright, Page
import time

from pytest_html.selfcontained_report import SelfContainedReport

from ciathena.Utils.ExcelReader import ExcelReader
from ciathena.Utils.ExcelWriter import ExcelWriter

INPUT_PATH = r"C:\Users\HariKumarMulaguri\PycharmProjects\PythonProjectTest\Questions.xlsx"
OUTPUT_PATH = r"C:\Users\HariKumarMulaguri\PycharmProjects\PythonProjectTest\Reports.xlsx"
SHEET_NAME = "Questions"

class QuestionsTest:
    def __init__(self, page: Page):
        super().__init__(page)
        self.answer_response = page.locator("#answer-text")
        self.sql_icon = page.locator("#sql-toggle-icon")
        self.sql_query_response = page.locator("#sql-query-content")
        self.show_sql_icon = page.locator("img[alt='Show SQL']")
        self.show_info_icon = page.locator("button[aria-label='Explain / More info']")
        self.show_share_icon = page.locator("img[alt='Share']")
        self.show_save_icon = page.locator("img[alt='Save']")
        self.show_download_icon = page.locator("img[alt='Download']")

        self.error_messages = [
            "Empty SQL result", "Error", "no records", "no transactions recorded",
            "request is a bit too detailed", "Empty SQL result ", "My apologies",
            "cannot process requests", "please limit your query"
        ]

    def get_answer_response(self):
        if self.answer_response.is_visible():
            return self.answer_response.text_content().strip()
        return None


    def get_sql_query_if_available(self):
        sql_query = None
        icon_status = {
            "show_sql_visible": False,
            "show_info_visible": False,
            "show_share_visible": False,
            "show_save_visible": False,
            "show_download_visible": False
        }

        if self.sql_icon.is_visible():
            print("🟢 SQL button visible")

            icon_status["show_sql_visible"] = self.show_sql_icon.is_visible()
            icon_status["show_info_visible"] = self.show_info_icon.is_visible()
            icon_status["show_share_visible"] = self.show_share_icon.is_visible()
            icon_status["show_save_visible"] = self.show_save_icon.is_visible()
            icon_status["show_download_visible"] = self.show_download_icon.is_visible()

            for key, value in icon_status.items():
                print(f"{key}: {value}")

            if self.sql_icon.is_visible():
                self.sql_icon.click()
                self.sql_query_response.wait_for(state="visible")
                sql_query = self.sql_query_response.text_content().strip()
                print(f"💾 SQL Query captured: {sql_query[:200]}...")
            else:
                print("⚠️ SQL query box not visible after clicking button")
        else:
            print("🔸 SQL button not visible for this response.")

        return sql_query, icon_status


# --- Start Playwright Session ---
reader = ExcelReader(INPUT_PATH, SHEET_NAME)
writer = ExcelWriter(OUTPUT_PATH)
questions = reader.get_questions()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # --- Login ---
    page.goto("https://ciathena-dev.customerinsights.ai/")
    page.get_by_role("button", name="Sign in with Microsoft").click()
    page.get_by_role("textbox", name="You'r Email Address").fill("hari.mulaguri@customerinsights.ai")
    page.get_by_role("button", name="Next").click()
    page.locator("#i0118").fill("Ganesha@123")
    page.locator("#i0118").press("Enter")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_role("button", name="Text +XX XXXXXXXX73").click()
    time.sleep(20)
    page.get_by_role("button", name="Verify").click()
    time.sleep(5)
    page.get_by_role("button", name="Yes").click()
    page.wait_for_selector("#welcome-search-row")
    page.locator("#welcome-search-row").click(force=True)

    bot = QuestionsTest(page)

    # --- Loop through all questions ---
    for question in questions:
        print(f"\n===============================")
        print(f"❓ Question: {question}")
        page.wait_for_selector("#welcome-search-row")
        page.locator("#welcome-search-row").click(force=True)
        page.click("#icon-app-mmx")
        page.wait_for_timeout(5000)
        page.get_by_placeholder("Type something here...").fill(question)
        page.wait_for_selector("#send-btn").click()
        page.wait_for_timeout(60000)

        answer_text = bot.get_answer_response()
        sql_query = None

        page.evaluate("document.body.style.zoom='40%'")  # Zoom out to 40%
        page.get_by_placeholder("Ask a question").fill(question)
        page.wait_for_selector("#send-btn").click()
        time.sleep(30)

        if answer_text:
            print(f"✅ Answer: {answer_text}")
            sql_query, icon_status = bot.get_sql_query_if_available()
        else:
            answer_text = "⚠️ No response found"
            icon_status = {
                "show_sql_visible": False,
                "show_info_visible": False,
                "show_share_visible": False,
                "show_save_visible": False,
                "show_download_visible": False
            }

        status = "PASS" if all(icon_status.values()) else "FAIL"
        print(f"✅ Overall Icon Status: {status}")

        # --- Write results to Excel ---
        writer.write_row(
            question,
            answer_text,
            sql_query,
            icon_status["show_sql_visible"],
            icon_status["show_info_visible"],
            icon_status["show_share_visible"],
            icon_status["show_save_visible"],
            icon_status["show_download_visible"],
            status
        )
        writer.save()

        page.wait_for_timeout(3000)
        #page.click("img[alt='Home']")

    browser.close()
    print("\n✅ All questions processed and results saved!")
