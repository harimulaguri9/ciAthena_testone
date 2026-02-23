import re
import asyncio
import time
from difflib import SequenceMatcher
import json

from playwright.async_api import async_playwright
from ciathena.Utils.ExcelReader import ExcelReader
from ciathena.Utils.ExcelWriter import ExcelWriter
from ciathena.tests.apis.beUtils import compare_nrx_only, compare_trx_only

# -------------------- CONFIG --------------------
INPUT_PATH = r"C:\HARI\ciATHENA_Backup\ciathena_autoamtion\MMM_Questions.xlsx"
OUTPUT_PATH = r"C:\HARI\ciATHENA_Backup\ciathena_autoamtion\MMM_Report.xlsx"
SHEET_NAME = "Questions"

# ------------------ UI CLASS --------------------
class ChatbotAutomation:
    def __init__(self, page):
        self.page = page
        self.sql_button_locator = page.locator("button[aria-label='Show SQL']")
        self.mmm_usecase = page.locator("#welcome-app-name-mmm")
        self.valid_response_locator = page.locator("#answer-text")
        # self.chart_button = page.locator("div[aria-label*='Chart']")
        self.chart_button = page.locator("[aria-label$='Chart']")

        self.ask_question_input = page.get_by_placeholder("Type something here...")
        self.send_button = page.locator("#send-icon")
        self.sql_icon = page.locator("#sql-toggle-icon")
        self.sql_query_response_locator = page.locator("#sql-content")
        self.show_sql_icon = page.locator("#sql-toggle-icon")
        # self.show_info_icon = page.locator("button[aria-label='Explain / More info']")
        self.show_share_icon = page.locator("img[alt='Share']")
        self.show_save_icon = page.locator("img[alt='Save']")
        self.show_download_icon = page.locator("img[alt='Download']").first
        self.view_fullscreen_icon = page.locator("//button[@aria-label='View in fullscreen']")
        self.data_view_icon = page.locator("//button[@aria-label='Data View']")

    async def get_valid_response(self):
        if await self.valid_response_locator.is_visible(timeout=60000):
            return (await self.valid_response_locator.text_content()).strip()
        return None

    async def get_actual_chart_name(self):
        try:
            await self.chart_button.wait_for(state="visible", timeout=30000)
            return await self.chart_button.get_attribute("aria-label")
        except:
            return "None"
    # async def get_error_response(self):
    #     if await self.invalid_response_locator.is_visible():
    #         text = (await self.invalid_response_locator.text_content()).strip()
    #         if any(err.lower() in text.lower() for err in self.error_messages):
    #             return text
    #     return None
    #
    # async def get_sql_query_if_available(self):
    #     icon_status = {
    #         "show_sql_visible": False,
    #         "show_share_visible": False,
    #         "show_save_visible": False,
    #         "show_download_visible": False,
    #         "view_fullscreen_icon": False,
    #         "data_view_icon": False
    #     }
    #     sql_query = ""
    #
    #     try:
    #         if await self.sql_icon.is_visible(timeout=10000):
    #             icon_status["show_sql_visible"] = True
    #             await self.sql_icon.click()
    #             await self.page.wait_for_timeout(3000)
    #
    #             # sql_element = self.page.locator("pre")  # adjust selector
    #             if await self.sql_query_response_locator.is_visible():
    #                 sql_query = await self.sql_query_response_locator.text_content()
    #                 sql_query = sql_query.strip()
    #                 print(sql_query)
    #     except Exception as e:
    #         print(f"Error fetching SQL query: {e}")
    #
    #     print("sql icon status",icon_status["show_sql_visible"])
    #     return sql_query, icon_status

    async def get_sql_query_if_available(self):

        icon_status = {
            "show_sql_visible": False,
            "show_share_visible": False,
            "show_save_visible": False,
            "show_download_visible": False,
            "view_fullscreen_icon": False,
            "data_view_icon": False
        }

        sql_query = None
        time.sleep(15)
        try:
            # ✅ Use ONE locator consistently
            if await self.sql_button_locator.is_visible():
                print("✅ SQL icon is visible")
                icon_status["show_sql_visible"] = await self.show_sql_icon.is_visible()
                icon_status["show_share_visible"] = await self.show_share_icon.is_visible()
                icon_status["show_save_visible"] = await self.show_save_icon.is_visible()
                icon_status["show_download_visible"] = await self.show_download_icon.is_visible()
                icon_status["view_fullscreen_icon"] = await self.view_fullscreen_icon.is_visible()
                icon_status["data_view_icon"] = await self.data_view_icon.is_visible()
                print("Icon visibility status:", icon_status["show_sql_visible"])
                await self.sql_icon.click()
                # time.sleep(5)
                await self.sql_query_response_locator.wait_for(state="visible", timeout=5000)
                sql_query = await self.sql_query_response_locator.text_content()
                if sql_query:
                    sql_query = sql_query.strip()
                    print("Extracted SQL Query:\n", sql_query)
                else:
                    print("SQL element visible but empty")
            else:
                print("SQL icon not visible")
        except Exception as e:
            print("Error while extracting SQL:", e)

        return sql_query, icon_status


# ------------------ UTILITIES -------------------
def normalize_sql(sql: str) -> str:
    if not sql:
        return ""
    sql = sql.lower()
    sql = re.sub(r"'[^']*'", "''", sql)
    sql = re.sub(r"\s+", " ", sql).strip()
    return sql

def sql_similarity(sql1: str, sql2: str) -> float:
    return SequenceMatcher(None, normalize_sql(sql1), normalize_sql(sql2)).ratio()

def normalize_chart_name(name: str) -> str:
    words = name.lower().replace("_", " ").replace("-", " ").split()
    words = [w for w in words if w not in {"chart"}]
    return "".join(dict.fromkeys(words))

def is_chart_match(expected_chart_name: str, actual_chart: str) -> bool:
    if not expected_chart_name or not actual_chart:
        return False
    return normalize_chart_name(expected_chart_name) == normalize_chart_name(actual_chart)


# # -------------------- MAIN ----------------------
# async def main():
#     reader = ExcelReader(INPUT_PATH, SHEET_NAME)
#     writer = ExcelWriter(OUTPUT_PATH)
#     questions_sqlquery = reader.get_questions_with_expected_values()
#
#
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False, slow_mo=1500)
#         page = await browser.new_page()
#         await page.goto("https://ciathena-qa.customerinsights.ai/")
#         await page.wait_for_timeout(10000)
#
#         # ---------- LOGIN ----------
#         await page.locator("input[placeholder='username@domain.ai']").fill("harimulaguri9@gmail.com")
#         await page.get_by_role("button", name="Sign in").click()
#         await page.get_by_placeholder("Enter password").fill("Android@123")
#         await page.get_by_role("button", name="Sign in").click()
#         await page.wait_for_timeout(15000)
#
#         bot = ChatbotAutomation(page)
#
#         # ---------------- STREAM RESPONSE HANDLER ----------------
#         responses = []
#         def is_stream_response(response):
#             return "/v1/query/stream" in response.url
#
#         async def handle_response(response):
#             if is_stream_response(response):
#                 text = await response.text()
#                 for line in text.splitlines():
#                     if line.startswith("data:"):
#                         data_str = line[len("data:"):].strip()
#                         if data_str:
#                             try:
#                                 payload = json.loads(data_str)
#                                 responses.append(payload)
#                             except json.JSONDecodeError:
#                                 continue
#
#         page.on("response", handle_response)
#
#
#
#
#         # ---------------- PROCESS QUESTIONS -----------------
#         for item in questions_sqlquery:
#             question = item["question"]
#             expected_sql = item["expected_sql"]
#             expected_chart_name = item["chart"]
#             final_response_json = item["final_response_json"]
#
#             # Step 1: Convert string to dictionary
#             response_json = json.loads(final_response_json)
#
#             # Step 2: Extract raw_sql_result
#             expected_raw_sql = response_json["answer"]["raw_sql_result"]
#
#             print("expected_raw_sql::",expected_raw_sql)
#
#             # print("Expected columns:", len(expected_raw_sql[0]))
#             # print("Actual columns:", len(raw_sql_result[0]))
#
#             await page.wait_for_timeout(3000)
#             await page.locator("#welcome-search-input").click(force=True)
#             await page.locator("#welcome-app-name-mmm").click()
#             await page.wait_for_timeout(3000)
#
#             await bot.ask_question_input.fill(question)
#             await bot.send_button.click()
#
#             # ---------- WAIT FOR FINAL STREAM RESPONSE ----------
#             final_payload = None
#             for _ in range(60):  # wait up to 60 seconds
#                 for resp in responses:
#                     if resp.get("is_final"):
#                         final_payload = resp
#                         break
#                 if final_payload:
#                     break
#                 await asyncio.sleep(1)
#
#             if final_payload:
#                 print("\n✅ Final stream response captured:")
#                 # raw_sql_result = final_payload.get("final_response", {}).get("raw_sql_result", [])
#
#                 # print("Extracted SQL Query:\n", sql_query)
#                 # print("Raw SQL Result:\n", raw_sql_result)
#             else:
#                 # raw_sql_result = []
#                 print("\n❌ No final response found in stream")
#
#             print("--------------------------------------------")
#
#             # ---------- EXTRACT AND VALIDATE ----------
#             answer_text = await bot.get_valid_response()
#             sql_query = None
#             icon_status = None
#             #
#             # if answer_text:
#             #     sql_query, icon_status = await bot.get_sql_query_if_available()
#             #     status = "PASS" if all(icon_status.values()) else "FAIL"
#             # else:
#             #     answer_text = await bot.get_error_response() or "No response"
#             #     status = "FAIL"
#
#             if final_payload:
#                 # Validate status completed
#                 stream_status = final_payload.get("status")
#                 is_completed = stream_status == "completed" and final_payload.get("is_final")
#                 print(f"Stream Completed: {is_completed}")
#                 # print("-------------final_payload start-------------------------------")
#                 # print("final_payload:",final_payload)
#                 # print("-------------final_payload end-------------------------------")
#
#                 # Extract raw_sql_result
#                 raw_sql_result = final_payload.get("final_response", {}).get("raw_sql_result", [])
#                 raw_sql_comparision_result = False
#                 if raw_sql_result:
#                     print(f"Raw SQL Result rows: {len(raw_sql_result)}")
#                     print("Raw SQL Result:\n", raw_sql_result)
#                     raw_sql_comparision_result = compare_trx_only(expected_raw_sql, raw_sql_result)
#
#                     print("-------------raw_sql_comparision_result end-------------------------------")
#                     print("raw_sql_comparision_result:", raw_sql_comparision_result)
#                 else:
#                     print("No raw_sql_result found")
#             else:
#                 is_completed = False
#                 raw_sql_result = []
#
#             print("--------------------------------------------")
#
#             # ---------- SQL & Chart Validation ----------
#             if answer_text:
#                 sql_query = None  # Can extract from final_payload if needed
#                 sql_match = normalize_sql(sql_query) == normalize_sql(expected_sql) if sql_query else False
#                 similarity_score = sql_similarity(sql_query, expected_sql) if sql_query else 0.0
#                 actual_chart = await bot.get_actual_chart_name()
#                 chart_match = is_chart_match(expected_chart_name, actual_chart)
#                 status = "PASS" if sql_match and chart_match and is_completed and raw_sql_comparision_result else "FAIL"
#             else:
#                 sql_query = None
#                 similarity_score = 0.0
#                 chart_match = False
#                 sql_match = False
#                 actual_chart = "None"
#                 status = "FAIL"
#
#             # ---------- WRITE TO EXCEL ----------
#             writer.write_row(
#                 question,
#                 answer_text,
#                 sql_query,
#                 False,
#                 expected_sql,
#                 sql_match,
#                 similarity_score,
#                 False,
#                 actual_chart,
#                 expected_chart_name,
#                 chart_match,
#                 False,
#                 False,
#                 False,
#                 False,
#                 False,
#                 False,
#                 status
#             )
#
#             writer.save()
#             await page.click("img[alt='Home']")
#             responses.clear()  # clear for next question
#
#         await browser.close()



#== Temp
async def main():
    reader = ExcelReader(INPUT_PATH, SHEET_NAME)
    writer = ExcelWriter(OUTPUT_PATH)
    questions_sqlquery = reader.get_questions_with_expected_values()


    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=1500)
        page = await browser.new_page()
        await page.goto("https://ciathena-qa.customerinsights.ai/")
        await page.wait_for_timeout(10000)

        # ---------- LOGIN ----------
        await page.locator("input[placeholder='username@domain.ai']").fill("harimulaguri9@gmail.com")
        await page.get_by_role("button", name="Sign in").click()
        await page.get_by_placeholder("Enter password").fill("Android@123")
        await page.get_by_role("button", name="Sign in").click()
        await page.wait_for_timeout(15000)

        bot = ChatbotAutomation(page)


        # ---------------- STREAM RESPONSE HANDLER ----------------
        responses = []
        def is_stream_response(response):
            return "/v1/query/stream" in response.url

        async def handle_response(response):
            if is_stream_response(response):
                text = await response.text()
                for line in text.splitlines():
                    if line.startswith("data:"):
                        data_str = line[len("data:"):].strip()
                        if data_str:
                            try:
                                payload = json.loads(data_str)
                                responses.append(payload)
                            except json.JSONDecodeError:
                                continue

        page.on("response", handle_response)

        # ---------------- PROCESS QUESTIONS -----------------
        for item in questions_sqlquery:
            question = item["question"]
            expected_sql = item["expected_sql"]
            expected_chart_name = item["chart"]
            final_response_json = item["final_response_json"]

            # Step 1: Convert string to dictionary
            response_json = json.loads(final_response_json)

            # Step 2: Extract raw_sql_result
            expected_raw_sql = response_json["answer"]["raw_sql_result"]

            print("expected_raw_sql::",expected_raw_sql)

            # print("Expected columns:", len(expected_raw_sql[0]))
            # print("Actual columns:", len(raw_sql_result[0]))

            await page.wait_for_timeout(3000)
            await page.locator("#welcome-search-input").click(force=True)
            await page.locator("#welcome-app-name-mmm").click()
            await page.wait_for_timeout(3000)

            await bot.ask_question_input.fill(question)
            await bot.send_button.click()

            # ---------- WAIT FOR FINAL STREAM RESPONSE ----------
            final_payload = None
            for _ in range(60):  # wait up to 60 seconds
                for resp in responses:
                    if resp.get("is_final"):
                        final_payload = resp
                        break
                if final_payload:
                    break
                await asyncio.sleep(3)

            # if final_payload:
            #     print("\n✅ Final stream response captured:")
                # raw_sql_result = final_payload.get("final_response", {}).get("raw_sql_result", [])

                # print("Extracted SQL Query:\n", sql_query)
                # print("Raw SQL Result:\n", raw_sql_result)
            # else:
            #     # raw_sql_result = []
            #     print("\n❌ No final response found in stream")
            #
            # print("--------------------------------------------")

            # ---------- EXTRACT AND VALIDATE ----------
            answer_text = await bot.get_valid_response()
            # sql_query = None
            # icon_status = None

            if answer_text:
                sql_query, icon_status = await bot.get_sql_query_if_available()
                status = "PASS" if all(icon_status.values()) else "FAIL"
            else:
                answer_text = await bot.get_error_response() or "No response"
                status = "FAIL"

            if final_payload:
                # Validate status completed
                stream_status = final_payload.get("status")
                is_completed = stream_status == "completed" and final_payload.get("is_final")
                print(f"Stream Completed: {is_completed}")
                # print("-------------final_payload start-------------------------------")
                # print("final_payload:",final_payload)
                # print("-------------final_payload end-------------------------------")

                # Extract raw_sql_result
                raw_sql_result = final_payload.get("final_response", {}).get("raw_sql_result", [])
                raw_sql_comparision_result = False
                if raw_sql_result:
                    print(f"Raw SQL Result rows: {len(raw_sql_result)}")
                    print("Raw SQL Result:\n", raw_sql_result)
                    raw_sql_comparision_result = compare_trx_only(expected_raw_sql, raw_sql_result)

                    print("-------------raw_sql_comparision_result end-------------------------------")
                    print("raw_sql_comparision_result:", raw_sql_comparision_result)
                else:
                    print("No raw_sql_result found")
            else:
                is_completed = False
                raw_sql_result = []

            print("--------------------------------------------")

            # ---------- SQL & Chart Validation ----------
            if answer_text:
                # sql_query = None  # Can extract from final_payload if needed
                sql_match = normalize_sql(sql_query) == normalize_sql(expected_sql) if sql_query else False
                similarity_score = sql_similarity(sql_query, expected_sql) if sql_query else 0.0
                actual_chart = await bot.get_actual_chart_name()
                print("Actual chart name:", actual_chart)
                print("Expected chart name:", expected_chart_name)

                chart_match = is_chart_match(expected_chart_name, actual_chart)
                status = "PASS" if sql_match and chart_match and is_completed and raw_sql_comparision_result else "FAIL"
            else:
                sql_query = None
                similarity_score = 0.0
                chart_match = False
                sql_match = False
                actual_chart = "None"
                status = "FAIL"

            # ---------- WRITE TO EXCEL ----------
            writer.write_row(
                question,
                answer_text,
                sql_query,
                False,
                expected_sql,
                sql_match,
                similarity_score,
                False,
                actual_chart,
                expected_chart_name,
                chart_match,
                False,
                False,
                False,
                False,
                False,
                False,
                status
            )

            writer.save()
            await page.click("img[alt='Home']")
            responses.clear()  # clear for next question

        await browser.close()



# -------------------- RUN -----------------------
if __name__ == "__main__":
    asyncio.run(main())
