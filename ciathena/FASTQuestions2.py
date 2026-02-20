"""
MMM Chatbot Automation Framework
---------------------------------
Validations:
    1. Stream Completion
    2. SQL Match
    3. Backend raw_sql_result Match
    4. Chart Match
Final Output:
    Clean PASS / FAIL report
"""

import re
import json
import math
import asyncio
from playwright.async_api import async_playwright

from ciathena.Utils.ExcelReader2 import ExcelReader
from ciathena.Utils.ExcelWriter2 import ExcelWriter


# ============================================================
# CONFIGURATION
# ============================================================

INPUT_PATH = r"C:\HARI\ciATHENA_Backup\ciathena_autoamtion\MMM_Questions.xlsx"
OUTPUT_PATH = r"C:\HARI\ciATHENA_Backup\ciathena_autoamtion\MMM_Report.xlsx"
SHEET_NAME = "Questions"
BASE_URL = "https://ciathena-qa.customerinsights.ai/"

USERNAME = "harimulaguri9@gmail.com"
PASSWORD = "Android@123"


# ============================================================
# UTILITY FUNCTIONS
# ============================================================

def normalize_sql(sql: str) -> str:
    """Normalize SQL string for safe comparison."""
    if not sql:
        return ""
    sql = sql.lower()
    sql = re.sub(r"\s+", " ", sql).strip()
    return sql


def compare_be_response(actual, expected, tolerance=0.0001):
    """Compare backend raw_sql_result with expected dataset."""
    if not actual or not expected:
        return False

    if isinstance(expected, str):
        try:
            expected = json.loads(expected)
        except:
            return False

    if len(actual) != len(expected):
        return False

    actual_sorted = sorted(actual, key=lambda x: x[0])
    expected_sorted = sorted(expected, key=lambda x: x[0])

    for act, exp in zip(actual_sorted, expected_sorted):
        if act[0] != exp[0]:
            return False
        if not math.isclose(float(act[1]), float(exp[1]), rel_tol=tolerance):
            return False

    return True


def is_chart_match(expected_chart, actual_chart):
    """Validate chart name."""
    if not expected_chart or not actual_chart:
        return False
    return expected_chart.lower() in actual_chart.lower()


# ============================================================
# PLAYWRIGHT ACTIONS
# ============================================================

async def login(page):
    """Perform application login."""
    await page.goto(BASE_URL)
    await page.wait_for_timeout(5000)

    await page.locator("input[placeholder='username@domain.ai']").fill(USERNAME)
    await page.get_by_role("button", name="Sign in").click()

    await page.get_by_placeholder("Enter password").fill(PASSWORD)
    await page.get_by_role("button", name="Sign in").click()

    await page.wait_for_timeout(15000)


async def send_question(page, question):
    """Send chatbot question."""
    await page.wait_for_timeout(3000)
    await page.locator("#welcome-search-input").click(force=True)
    await page.locator("#welcome-app-name-mmm").click()
    await page.wait_for_timeout(3000)
    chat_input = page.locator("[placeholder='Type something here...']")
    await chat_input.wait_for(state="visible", timeout=2000)
    await chat_input.fill(question)
    await page.locator("#send-icon").click()


async def wait_for_final_stream(responses, timeout=60):
    """Wait until final stream payload is received."""
    for _ in range(timeout):
        for resp in responses:
            if resp.get("is_final"):
                return resp
        await asyncio.sleep(1)
    return None


# ============================================================
# MAIN EXECUTION FLOW
# ============================================================

async def main():

    # Initialize Excel
    reader = ExcelReader(INPUT_PATH, SHEET_NAME)
    writer = ExcelWriter(OUTPUT_PATH)
    test_data = reader.get_test_data()

    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Login
        await login(page)

        # Stream Response Collector
        responses = []

        async def handle_response(response):
            if "/v1/query/stream" in response.url:
                text = await response.text()
                for line in text.splitlines():
                    if line.startswith("data:"):
                        try:
                            payload = json.loads(line[5:].strip())
                            responses.append(payload)
                        except:
                            continue

        page.on("response", handle_response)

        # ====================================================
        # TEST EXECUTION LOOP
        # ====================================================
        for item in test_data:
            question = item["question"]
            expected_sql = item["expected_sql"]
            expected_be = item["expected_be_response"]
            expected_chart = item["chart"]

            print(f"\nExecuting: {question}")
            await send_question(page, question)
            final_payload = await wait_for_final_stream(responses)

            # -----------------------------
            # Extract Stream Data
            # -----------------------------
            if final_payload:
                stream_completed = final_payload.get("status") == "completed"
                actual_sql = final_payload.get("sql_query")
                raw_sql_result = final_payload.get("final_response", {}).get("raw_sql_result", [])
            else:
                stream_completed = False
                actual_sql = None
                raw_sql_result = []

            # -----------------------------
            # VALIDATIONS
            # -----------------------------
            sql_match = normalize_sql(actual_sql) == normalize_sql(expected_sql)
            be_match = compare_be_response(raw_sql_result, expected_be)

            try:
                actual_chart = await page.locator("button[aria-label*='Chart']").get_attribute("aria-label")
            except:
                actual_chart = None

            chart_match = is_chart_match(expected_chart, actual_chart)

            # -----------------------------
            # FINAL STATUS DECISION
            # -----------------------------
            if not stream_completed:
                status = "FAIL - Stream Incomplete"
            elif not be_match:
                status = "FAIL - Backend Mismatch"
            elif not sql_match:
                status = "FAIL - SQL Mismatch"
            elif not chart_match:
                status = "FAIL - Chart Mismatch"
            else:
                status = "PASS"

            # -----------------------------
            # Write Clean Report
            # -----------------------------
            writer.write_row(
                question,
                sql_match,
                be_match,
                chart_match,
                stream_completed,
                status
            )

            writer.save()
            responses.clear()

        await browser.close()


# ============================================================
# RUN ENTRY POINT
# ============================================================

if __name__ == "__main__":
    asyncio.run(main())