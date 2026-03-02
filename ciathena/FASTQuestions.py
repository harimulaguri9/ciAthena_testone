import re
from difflib import SequenceMatcher

from playwright.async_api import Page
import asyncio
from playwright.async_api import async_playwright
import json

from ciathena.Utils.ExcelReader import ExcelReader
from ciathena.Utils.ExcelWriter import ExcelWriter
from ciathena.tests.apis.beUtils import compare_trx_only

INPUT_PATH = r"C:\HARI\ciATHENA_Backup\ciathena_autoamtion\FAST_Questions.xlsx"
OUTPUT_PATH = r"C:\HARI\ciATHENA_Backup\ciathena_autoamtion\FAST_Report.xlsx"
SHEET_NAME = "Questions"


class ChatbotAutomation:
    def __init__(self, page: Page):
        self.page = page

        self.valid_response_locator = page.locator("#answer-text")
        self.invalid_response_locator = page.locator('[data-name="answer-text"]')
        self.answer_visualization_container = page.locator("//div[@id='answer-visualization-container']")
        self.answer_visualization_title = page.locator("//div[@id='visualization-actions-pill']/p")
        self.view_fullscreen_icon = page.locator("//button[@aria-label='View in fullscreen']")
        self.data_view_icon = page.locator("//button[@aria-label='Data View']")
        self.stacked_bar_chart_icon = page.locator("//button[@aria-label='Stacked Bar Chart']")
        # self.download_icon = page.locator("#//*[@aria-label='Download']")
        self.restore_icon= page.locator("#//*[@aria-label='Restore']")
        self.bubble_chart_icon = page.locator("[data-testid='BubbleChartTwoToneIcon']")
        self.chart_icon = page.locator("[aria-label$='Chart']").first

        self.sql_button_locator = page.locator("#sql-toggle-button")
        self.sql_query_response_locator = page.locator("#sql-content")

        self.show_sql_icon = page.locator("#sql-toggle-icon")
        self.show_share_icon = page.locator("#share-header-button")
        self.show_save_icon = page.locator("#save-icon")
        self.show_download_icon = page.locator("//*[@aria-label='Download']")

        self.ask_question_input = page.get_by_placeholder("Type something here...")
        self.send_button = page.locator("#send-icon")

        self.signin_button = page.locator("//button[normalize-space()='Sign in']")
        self.next_button = page.get_by_role("button", name="Next")
        self.password_input = page.locator("//input[@placeholder='Enter password']")
        self.phone_number_button = page.get_by_role("button", name="Text +XX XXXXXXXX73")
        self.verify_button = page.get_by_role("button", name="Verify")
        self.yes_button = page.get_by_role("button", name="Yes")
        self.welcome_text = page.locator("#welcome-prefix")

        self.error_messages = [
            "Empty SQL result", "Error", "no records",
            "My apologies", "cannot process requests"
        ]

        # responses should be instance-scoped (not a class variable)
        self.responses = []

    async def get_valid_response(self):
        if await self.valid_response_locator.is_visible():
            return (await self.valid_response_locator.text_content()).strip()
        return None

    async def get_error_response(self):
        if await self.invalid_response_locator.is_visible():
            text = (await self.invalid_response_locator.text_content()).strip()
            if any(err.lower() in text.lower() for err in self.error_messages):
                return text
        return None

        # ---------------- STREAM RESPONSE HANDLER ----------------
    def is_stream_response(self, response):
        """Return True if the response URL indicates it's the streaming endpoint."""
        return "/v1/query/stream" in response.url


    async def handle_response(self, response):
        """Async handler to be scheduled when a network response arrives.

        The Playwright `page.on("response", ...)` callback should schedule this
        coroutine (see usage in `main`).
        """
        if self.is_stream_response(response):
            try:
                text = await response.text()
            except Exception:
                return
            for line in text.splitlines():
                if line.startswith("data:"):
                    data_str = line[len("data:"):].strip()
                    if data_str:
                        try:
                            payload = json.loads(data_str)
                            self.responses.append(payload)
                        except json.JSONDecodeError:
                            # ignore malformed JSON chunks
                            continue

    async def get_sql_query_if_available(self):
        icon_status = {
            "show_sql_visible": False,
            "show_chart_visible": False,
            "show_share_visible": False,
            "show_save_visible": False,
            "show_download_visible": False,
            "view_fullscreen_icon":False,
            "data_view_icon":False
        }
        sql_query = None

        print("\n Checking for SQL button visibility...")

        try:
            sql_button_visible = await self.sql_button_locator.is_visible(timeout=15000)
            print(f"  SQL button visible: {sql_button_visible}")

            if sql_button_visible:
                icon_status["show_sql_visible"] = await self.show_sql_icon.is_visible()
                icon_status["show_chart_visible"] = await self.chart_icon.is_visible()
                icon_status["show_share_visible"] = await self.show_share_icon.is_visible()
                icon_status["show_save_visible"] = await self.show_save_icon.is_visible()
                icon_status["show_download_visible"] = await self.show_download_icon.is_visible()
                icon_status["view_fullscreen_icon"] = await self.view_fullscreen_icon.is_visible()
                icon_status["data_view_icon"] = await self.data_view_icon.is_visible()

                print("  📋 Clicking on show_sql_icon to expand SQL panel...")
                await self.show_sql_icon.click()
                await self.page.wait_for_timeout(2000)

                # Wait for SQL response to be visible
                sql_response_visible = await self.sql_query_response_locator.is_visible(timeout=15000)
                print(f"  SQL response visible: {sql_response_visible}")

                if sql_response_visible:
                    sql_query = (await self.sql_query_response_locator.text_content()).strip()
                    print(f"  ✓ SQL Query extracted: {sql_query[:100]}..." if len(sql_query) > 100 else f"  ✓ SQL Query: {sql_query}")
                else:
                    print("  ✗ SQL response not visible after clicking")
            else:
                print("  ✗ SQL button not visible")
        except Exception as e:
            print(f"  ✗ Error in get_sql_query_if_available: {str(e)}")

        return sql_query, icon_status

    async def get_actual_chart_name(self) -> str:
        """Extract the actual chart name from multiple sources.

        Tries: 1) chart_icon aria-label, 2) visualization title text, 3) fallback to "None"
        """
        # Attempt 1: Get aria-label from chart icon
        try:
            await self.chart_icon.wait_for(state="visible", timeout=15000)
            print(" Chart icon is visible, attempting to extract aria-label...")
            aria_label = await self.chart_icon.get_attribute("aria-label")
            if aria_label:
                return aria_label.strip()
        except Exception as e:
            print(f"Chart icon not found: {e}")

        # Attempt 2: Try to get chart name from visualization title
        try:
            if await self.answer_visualization_title.is_visible(timeout=5000):
                title_text = await self.answer_visualization_title.text_content()
                if title_text:
                    return title_text.strip()
        except Exception as e:
            print(f"Visualization title not found: {e}")

        # Attempt 3: Fallback
        print("Warning: Could not determine chart name, returning 'None'")
        return "None"

    def normalize_sql(self, sql: str) -> str:
        if not sql:
            return ""
        sql = sql.lower()
        sql = re.sub(r"'[^']*'", "''", sql)
        sql = re.sub(r"\s+", " ", sql).strip()
        return sql

    def sql_similarity(self, sql1: str, sql2: str) -> float:
        return SequenceMatcher(None, self.normalize_sql(sql1), self.normalize_sql(sql2)).ratio()

    def normalize_chart_name(self, name: str) -> str:
        words = name.lower().replace("_", " ").replace("-", " ").split()
        words = [w for w in words if w not in {"chart"}]
        return "".join(dict.fromkeys(words))

    def is_chart_match(self, expected_chart_name: str, actual_chart: str) -> bool:
        """Check if expected chart name matches actual chart.

        Returns False if either is None or "None". Normalizes both and compares.
        """
        if not expected_chart_name or not actual_chart:
            return False

        # Don't match if actual chart couldn't be determined
        if actual_chart.lower() == "none":
            return False

        # Normalize and compare
        normalized_expected = self.normalize_chart_name(expected_chart_name)
        normalized_actual = self.normalize_chart_name(actual_chart)

        match = normalized_expected == normalized_actual
        if not match:
            print(f"  Chart mismatch: expected='{normalized_expected}', actual='{normalized_actual}'")

        return match


async def main():
    reader = ExcelReader(INPUT_PATH, SHEET_NAME)
    writer = ExcelWriter(OUTPUT_PATH)
    questions_sqlquery = reader.get_questions_with_expected_values()

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("https://ciathena-qa.customerinsights.ai/")
        await page.locator("input[placeholder='username@domain.ai']").fill("harimulaguri9@gmail.com")
        await page.get_by_role("button", name="Sign in").click()
        await page.get_by_placeholder("Enter password").fill("Android@123")
        await page.get_by_role("button", name="Sign in").click()
        await page.wait_for_timeout(15000)


        bot = ChatbotAutomation(page)

        for item in questions_sqlquery:
            question = item["question"]
            expected_sql = item["expected_sql"]
            expected_chart_name = item["chart"]
            final_response_json = item["final_response_json"]

            # # Step 1: Convert string to dictionary
            # response_json = json.loads(final_response_json)
            # # Step 2: Extract raw_sql_result
            # expected_raw_sql = response_json[0]["answer"]["raw_sql_result"]
            # print("expected_raw_sql:", expected_raw_sql)
            try:
                response_json = json.loads(final_response_json)

                # If list → take first element
                if isinstance(response_json, list):
                    response_json = response_json[0] if response_json else {}

                # If dict → extract safely
                if isinstance(response_json, dict):
                    expected_raw_sql = response_json.get("answer", {}).get("raw_sql_result", [])
                else:
                    expected_raw_sql = []

            except Exception as e:
                print("JSON parsing error:", e)
                expected_raw_sql = []


            await page.locator("#welcome-search-row").click(force=True)
            # await page.locator("#icon-app-mmm").click()
            await page.locator("#icon-app-fast").click()
            # await page.locator("#app-patient_claims").click()

            # clear previous stream responses before asking a new question
            bot.responses.clear()
            await bot.ask_question_input.fill(question)
            await bot.send_button.click()
            print("\n🔍 ======START Execution=====")
            print("Asked Quesion::", question)
            page.on("response", lambda r: asyncio.create_task(bot.handle_response(r)))

            # ---------- WAIT FOR FINAL STREAM RESPONSE ----------
            final_payload = None
            for _ in range(60):  # wait up to 60 seconds
                for resp in bot.responses:
                    if resp.get("is_final"):
                        final_payload = resp
                        break
                if final_payload:
                    break
                await asyncio.sleep(3)

            answer_text = await bot.get_valid_response()

            # Initialize these variables for all code paths
            sql_query = None
            icon_status = None
            similarity_score = 0.0
            chart_match = False
            sql_match = False
            actual_chart = "None"

            if answer_text:
                await page.wait_for_timeout(15000)
                sql_query, icon_status = await bot.get_sql_query_if_available()
                # Status check based on icon visibility
                status = "PASS" if icon_status and all(icon_status.values()) else "FAIL"
            else:
                # No valid answer, try to get error response
                answer_text = await bot.get_error_response() or "No response"
                # Initialize icon_status with False values
                icon_status = {
                    "show_sql_visible": False,
                    "show_chart_visible": False,
                    "show_share_visible": False,
                    "show_save_visible": False,
                    "show_download_visible": False,
                    "view_fullscreen_icon": False,
                    "data_view_icon": False
                }
                status = "FAIL"



            if final_payload:
                # Validate status completed
                stream_status = final_payload.get("status")
                is_completed = stream_status == "completed" and final_payload.get("is_final")
                print(f"Stream Completed: {is_completed}")

                # Extract raw_sql_result
                raw_sql_result = final_payload.get("final_response", {}).get("raw_sql_result", [])
                raw_sql_comparision_result = False
                if raw_sql_result:
                    print(f"Raw SQL Result rows: {len(raw_sql_result)}")
                    print("RAW SQL Result:\n", raw_sql_result)
                    print(f"Raw SQL Result rows: {len(expected_raw_sql)}")
                    print("EXP SQL Result:\n", expected_raw_sql)

                    raw_sql_comparision_result = compare_trx_only(expected_raw_sql, raw_sql_result)
                    print("raw_sql_comparision_result:", raw_sql_comparision_result)
                else:
                    print("No raw_sql_result found")

            else:
                is_completed = False
                raw_sql_result = []

            if answer_text:
                # sql_query = None  # Can extract from final_payload if needed
                sql_match = bot.normalize_sql(sql_query) == bot.normalize_sql(expected_sql) if sql_query else False
                similarity_score = bot.sql_similarity(sql_query, expected_sql) if sql_query else 0.0

                print(f"\n📊 Extracting chart name...")
                actual_chart = await bot.get_actual_chart_name()
                print(f"  ✓ Actual chart name: '{actual_chart}'")
                print(f"  ✓ Expected chart name: '{expected_chart_name}'")

                chart_match = bot.is_chart_match(expected_chart_name, actual_chart)
                print(f"  ✓ Chart match result: {chart_match}")

                status = "PASS" if sql_match and chart_match and is_completed and raw_sql_comparision_result else "FAIL"
            else:
                sql_query = None
                similarity_score = 0.0
                chart_match = False
                sql_match = False
                actual_chart = "None"
                status = "FAIL"

            writer.write_row(
                question,
                answer_text,
                sql_query,
                icon_status["show_sql_visible"] if icon_status else False,
                expected_sql,
                sql_match,
                similarity_score,
                icon_status["show_chart_visible"] if icon_status else False,
                actual_chart,
                expected_chart_name,
                chart_match,
                raw_sql_comparision_result,
                icon_status["show_share_visible"] if icon_status else False,
                icon_status["show_save_visible"] if icon_status else False,
                icon_status["view_fullscreen_icon"] if icon_status else False,
                icon_status["data_view_icon"] if icon_status else False,
                icon_status["show_download_visible"] if icon_status else False,
                status
            )
            writer.save()
            print("✅ ====== EXECUTION DONE ======")
            await page.click("img[alt='Home']")

        await browser.close()
        print("✅ ====== EXECUTION DONE ======")


if __name__ == "__main__":
    asyncio.run(main())