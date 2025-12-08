from playwright.sync_api import sync_playwright
import time
from ciathena.Utils.ExcelReader import ExcelReader
from ciathena.Utils.ExcelWriter import ExcelWriter

INPUT_PATH = r"C:\Users\HariKumarMulaguri\PycharmProjects\PythonProjectTest\QuestionsTest.xlsx"
OUTPUT_PATH = r"C:\Users\HariKumarMulaguri\PycharmProjects\PythonProjectTest\Reports.xlsx"
SHEET_NAME = "Questions"



class ChatbotAutomation:
    def __init__(self, page):
        self.page = page
        # Locators
        self.valid_response_locator = page.locator("div.MuiTypography-root.MuiTypography-body1.css-1bhq52v")
        self.error_response_locator = page.locator("div.MuiTypography-root.MuiTypography-body1.css-1qrepl8")
        self.sql_button_locator = page.locator("button[aria-label='Show SQL']")
        self.sql_query_response_locator = page.locator("div.MuiBox-root.css-18xib6f")
        self.show_sql_icon = page.locator("#sql-toggle-icon")
        self.show_info_icon = page.locator("button[aria-label='Explain / More info']")
        self.show_share_icon = page.locator("img[alt='Share']")
        self.show_save_icon = page.locator("img[alt='Save']")
        self.show_download_icon = page.locator("img[alt='Download']")

        self.error_messages = [
            "Empty SQL result", "Error", "no records", "no transactions recorded",
            "request is a bit too detailed", "Empty SQL result ", "My apologies",
            "cannot process requests", "please limit your query"
        ]

      #  show_sql_visible = show_info_visible = show_share_icon = show_save_icon = show_download_visible = False

    def get_valid_response(self):
        if self.valid_response_locator.is_visible():
            return self.valid_response_locator.text_content().strip()
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

        if self.sql_button_locator.is_visible():
            print("🟢 SQL button visible")

            icon_status["show_sql_visible"] = self.show_sql_icon.is_visible()
            icon_status["show_info_visible"] = self.show_info_icon.is_visible()
            icon_status["show_share_visible"] = self.show_share_icon.is_visible()
            icon_status["show_save_visible"] = self.show_save_icon.is_visible()
            icon_status["show_download_visible"] = self.show_download_icon.is_visible()

            for key, value in icon_status.items():
                print(f"{key}: {value}")

            self.sql_button_locator.click()
            time.sleep(3)
            if self.sql_query_response_locator.is_visible():
                sql_query = self.sql_query_response_locator.text_content().strip()
                print(f"💾 SQL Query captured: {sql_query[:200]}...")
            else:
                print("⚠️ SQL query box not visible after clicking button")
        else:
            print("🔸 SQL button not visible for this response.")

        return sql_query, icon_status

    def get_error_response(self):
        """Return chatbot error text if visible."""
        if self.error_response_locator.is_visible():
            text = self.error_response_locator.text_content().strip()
            if any(err in text for err in self.error_messages):
                return text
        return None


def main():
    reader = ExcelReader(INPUT_PATH, SHEET_NAME)
    writer = ExcelWriter(OUTPUT_PATH)
    questions = reader.get_questions()
    show_sql_visible = show_info_visible = show_share_icon = show_save_icon = show_download_visible = False

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Go to chatbot app
        page.goto("https://ciathena-qa.customerinsights.ai")
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
        page.locator("#welcome-search-row").click(force=True)  # id   - NW

        bot = ChatbotAutomation(page)

        for question in questions:
            print(f"\n===============================")
            print(f"❓ Question: {question}")
            page.wait_for_selector("#welcome-search-row")
            page.locator("#welcome-search-row").click(force=True)  # id   - NW
            page.click("#icon-app-mmx")  # search icon click
            page.wait_for_timeout(3000)
            page.get_by_placeholder("Type something here...").fill(question)
            page.wait_for_selector("#send-icon").click()
            page.wait_for_timeout(60000)
            page.locator("#navbar-home-button").wait_for(state="visible", timeout=3000)
            answer_text = bot.get_valid_response()
            sql_query = None

            #page.evaluate("document.body.style.zoom='40%'")  # Zoom out to 40%
            #page.get_by_placeholder("Ask a question").fill(question)
            #page.wait_for_timeout(3000)

            if answer_text:
                print(f"✅ Answer: {answer_text}")
                sql_query, icon_status = bot.get_sql_query_if_available()
            else:
                error_text = bot.get_error_response()
                if error_text:
                    answer_text = f"❌ Error: {error_text}"
                    print(answer_text)
                else:
                    answer_text = "⚠️ No response found"
                    print(answer_text)
                icon_status = {
                    "show_sql_visible": False,
                    "show_info_visible": False,
                    "show_share_visible": False,
                    "show_save_visible": False,
                    "show_download_visible": False
                }
            if all(icon_status.values()):
                status = "PASS"
            else:
                status = "FAIL"

            print(f"✅ Overall Icon Status: {status}")

            # --- Write to Excel ---
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
            # Back to home for next query
            page.click("img[alt='Home']")

        browser.close()
        print("\n✅ All questions processed and results saved!")


if __name__ == "__main__":
    main()
