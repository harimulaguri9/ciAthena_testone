import re
import asyncio
from difflib import SequenceMatcher
import json

from playwright.async_api import async_playwright
from ciathena.Utils.ExcelReader2 import ExcelReader
from ciathena.Utils.ExcelWriter2 import ExcelWriter

# -------------------- CONFIG --------------------
INPUT_PATH = r"C:\HARI\ciATHENA_Backup\ciathena_autoamtion\MMM_Questions.xlsx"
OUTPUT_PATH = r"C:\HARI\ciATHENA_Backup\ciathena_autoamtion\MMM_Report.xlsx"
SHEET_NAME = "Questions"

# ------------------ UI CLASS --------------------
class ChatbotAutomation:
    def __init__(self, page):
        self.page = page
        self.mmm_usecase = page.locator("#welcome-app-name-mmm")
        self.valid_response_locator = page.locator("#answer-text")
        self.chart_button = page.locator("button[aria-label*='Chart']")
        self.ask_question_input = page.get_by_placeholder("Type something here...")
        self.send_button = page.locator("#send-icon")

    async def get_valid_response(self):
        if await self.valid_response_locator.is_visible(timeout=90000):
            return (await self.valid_response_locator.text_content()).strip()
        return None

    async def get_actual_chart_name(self):
        try:
            await self.chart_button.wait_for(state="visible", timeout=30000)
            return await self.chart_button.get_attribute("aria-label")
        except:
            return "None"

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

# -------------------- MAIN ----------------------
async def main():
    reader = ExcelReader(INPUT_PATH, SHEET_NAME)
    writer = ExcelWriter(OUTPUT_PATH)
    questions_sqlquery = reader.get_questions_with_expected_sql()

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=1500)
        page = await browser.new_page()
        await page.goto("https://ciathena-qa.customerinsights.ai/")
        await page.wait_for_timeout(5000)

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
                await asyncio.sleep(1)

            if final_payload:
                print("\n✅ Final stream response captured:")
                # raw_sql_result = final_payload.get("final_response", {}).get("raw_sql_result", [])

                # print("Extracted SQL Query:\n", sql_query)
                # print("Raw SQL Result:\n", raw_sql_result)
            else:
                # raw_sql_result = []
                print("\n❌ No final response found in stream")

            print("--------------------------------------------")

            # ---------- EXTRACT AND VALIDATE ----------
            answer_text = await bot.get_valid_response()

            if final_payload:
                # Validate status completed
                stream_status = final_payload.get("status")
                is_completed = stream_status == "completed" and final_payload.get("is_final")
                print(f"Stream Completed: {is_completed}")
                print("--------------------------------------------")
                # Extract raw_sql_result
                raw_sql_result = final_payload.get("final_response", {}).get("raw_sql_result", [])
                if raw_sql_result:
                    print(f"Raw SQL Result rows: {len(raw_sql_result)}")
                    print("Raw SQL Result:\n", raw_sql_result)

                else:
                    print("No raw_sql_result found")
            else:
                is_completed = False
                raw_sql_result = []

            print("--------------------------------------------")

            # ---------- SQL & Chart Validation ----------
            if answer_text:
                sql_query = None  # Can extract from final_payload if needed
                sql_match = normalize_sql(sql_query) == normalize_sql(expected_sql) if sql_query else False
                similarity_score = sql_similarity(sql_query, expected_sql) if sql_query else 0.0
                actual_chart = await bot.get_actual_chart_name()
                chart_match = is_chart_match(expected_chart_name, actual_chart)
                status = "PASS" if sql_match and chart_match and is_completed else "FAIL"
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
                status
            )

            writer.save()
            await page.click("img[alt='Home']")
            responses.clear()  # clear for next question

        await browser.close()

# -------------------- RUN -----------------------
if __name__ == "__main__":
    asyncio.run(main())
