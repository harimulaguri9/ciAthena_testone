from playwright.sync_api import sync_playwright
import time
from playwright.sync_api import Page, expect
from ciathena.pages.BasePage import BasePage
from playwright.sync_api import Page

from ciathena.Utils.ExcelReader import ExcelReader
from ciathena.Utils.ExcelWriter import ExcelWriter

INPUT_PATH = r"C:\HARI\ciATHENA_Backup\ciathena_autoamtion\Questions.xlsx"
OUTPUT_PATH = r"C:\HARI\ciATHENA_Backup\ciathena_autoamtion\Reports.xlsx"
SHEET_NAME = "Questions"



class ChatbotAutomation:
    def __init__(self, page):
        self.page = page
        # Locators
        self.valid_response_locator = page.locator("#answer-text")
        self.invalid_response_locator = page.locator('[data-name="answer-text"]')
        self.sql_button_locator = page.locator("#sql-toggle-button")
        self.sql_query_response_locator = page.locator("div.MuiBox-root.css-18xib6f")
        self.show_sql_icon = page.locator("#sql-toggle-icon")
        self.show_info_icon = page.locator("#info-icon")
        self.show_share_icon = page.locator("#share-header-button")
        self.show_save_icon = page.locator("#save-icon")
        self.show_regenerate_button = page.locator("#regenerate-button")
        self.show_download_icon = page.locator("#download-visualization-button")
        self.ask_question_input=page.locator("#question-response-input")
        self.view_fullscreen_icon = page.locator("//button[@aria-label='View in fullscreen']")
        self.data_view_icon = page.locator("//button[@aria-label='Data View']")
        self.stacked_bar_chart_icon = page.locator("//button[@aria-label='Stacked Bar Chart']")
        self.download_icon = page.locator("#//*[@aria-label='Download']")
        self.restore_icon= page.locator("#//*[@aria-label='Restore']")
        self.bubble_chart_icon = page.locator("[data-testid='BubbleChartTwoToneIcon']")


        self.SSO_signin_button = page.get_by_text("Sign in with Microsoft")
        self.sso_email_input = page.locator("#i0116")
        self.sso_password_input = page.locator("//input[@placeholder='Password']")
        self.sso_signin_button = page.locator("#idSIButton9")
        self.email_input = page.locator("//input[@placeholder='username@domain.ai']")
        self.signin_button = page.locator("//button[normalize-space()='Sign in']")
        self.next_button = page.get_by_role("button", name="Next")
        self.password_input = page.locator("//input[@placeholder='Enter password']")
        self.phone_number_button = page.get_by_role("button", name="Text +XX XXXXXXXX73")
        self.verify_button = page.get_by_role("button", name="Verify")
        self.yes_button = page.get_by_role("button", name="Yes")
        self.welcome_text = page.locator("#welcome-prefix")


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
            icon_status["show_sql_visible"] = self.show_sql_icon.is_visible()
            # icon_status["show_info_visible"] = self.show_info_icon.is_visible()
            icon_status["show_share_visible"] = self.show_share_icon.is_visible()
            icon_status["show_save_visible"] = self.show_save_icon.is_visible()
            icon_status["show_download_visible"] = self.show_download_icon.is_visible()

            for key, value in icon_status.items():
                print(f"{key}: {value}")

            self.sql_button_locator.click()
            if self.sql_query_response_locator.is_visible():
                sql_query = self.sql_query_response_locator.text_content().strip()
                print(f"💾 SQL Query : {sql_query[:500]}...")
            else:
                print("⚠️ SQL query box not visible after clicking button")
        else:
            print("🔸 SQL button not visible for this response.")

        return sql_query, icon_status

    def get_error_response(self):
        """Return chatbot error text if visible."""
        if self.invalid_response_locator.is_visible():
            text = self.invalid_response_locator.text_content().strip()
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

        # await self.email_input.fill("hari.mulaguri@customerinsights.ai")
        # await self.signin_button.click()
        # await self.sso_email_input.wait_for(state="visible")
        # await self.sso_email_input.fill("hari.mulaguri@customerinsights.ai")
        # await self.next_button.click()
        # await self.sso_password_input.wait_for(state="visible")
        # await self.sso_password_input.fill("Android@123")
        # await self.sso_signin_button.click()
        # await self.phone_number_button.wait_for(state="visible")
        # await self.phone_number_button.click()
        # await self.page.wait_for_timeout(20000)
        # await self.verify_button.click()
        # await self.page.wait_for_timeout(5000)
        # await self.welcome_text.wait_for(state="visible")
        # await self.page.wait_for_timeout(5000)


        page.goto("https://ciathena.customerinsights.ai/")
        page.locator("email_input").fill("hari.mulaguri@customerinsights.ai")
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
            page.wait_for_timeout(2000)

            page.click("#icon-app-mmx")  # search icon click
            page.wait_for_timeout(3000)
            page.get_by_placeholder("Type something here...").fill(question)
            page.wait_for_selector("#send-icon").click()
            page.wait_for_timeout(40000)
            page.locator("#navbar-home-button").wait_for(state="visible", timeout=3000)
            answer_text = bot.get_valid_response()
            sql_query = None

            # page.evaluate("document.body.style.zoom='40%'")  # Zoom out to 40%
            # page.get_by_placeholder("Ask a question").fill(question)
            # page.wait_for_timeout(3000)
            # page.locator("#question-response-send-button").click()
            # page.wait_for_timeout(30000)

            if answer_text:
                print(f"✅ Answer: {answer_text}")
                sql_query, icon_status = bot.get_sql_query_if_available()
            else:
                error_text = bot.get_error_response()
                if error_text:
                   # answer_text = f"❌ Error: {error_text}"
                    print(f"❌ Error: {error_text}")
                else:
                    answer_text = "⚠️ No response found"
                    print(answer_text)
            # icon_status = {
            #         "show_sql_visible": False,
            #         "show_info_visible": False,
            #         "show_share_visible": False,
            #         "show_save_visible": False,
            #         "show_download_visible": False
            #     }
            if icon_status and all(icon_status.values()):
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
