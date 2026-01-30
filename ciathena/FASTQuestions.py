import re

from playwright.async_api import Page, expect
import asyncio
from playwright.async_api import async_playwright


from ciathena.Utils.ExcelReader import ExcelReader
from ciathena.Utils.ExcelWriter import ExcelWriter

INPUT_PATH = r"C:\HARI\ciATHENA_Backup\ciathena_autoamtion\FAST_Qexcel.xlsx"
OUTPUT_PATH = r"C:\HARI\ciATHENA_Backup\ciathena_autoamtion\FAST_Rexcel.xlsx"
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
        self.download_icon = page.locator("#//*[@aria-label='Download']")
        self.restore_icon= page.locator("#//*[@aria-label='Restore']")
        self.bubble_chart_icon = page.locator("[data-testid='BubbleChartTwoToneIcon']")

        self.sql_button_locator = page.locator("#sql-toggle-button")
        self.sql_query_response_locator = page.locator("#sql-query-content")

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

    async def get_sql_query_if_available(self):
        icon_status = {
            "show_sql_visible": False,
            "show_share_visible": False,
            "show_save_visible": False,
            "show_download_visible": False,
            "view_fullscreen_icon":False,
            "data_view_icon":False
        }
        sql_query = None
        if await self.sql_button_locator.is_visible():
            icon_status["show_sql_visible"] = await self.show_sql_icon.is_visible()
            icon_status["show_share_visible"] = await self.show_share_icon.is_visible()
            icon_status["show_save_visible"] = await self.show_save_icon.is_visible()
            icon_status["show_download_visible"] = await self.show_download_icon.is_visible()
            icon_status["view_fullscreen_icon"] = await self.view_fullscreen_icon.is_visible()
            icon_status["data_view_icon"] = await self.data_view_icon.is_visible()

            await self.show_sql_icon.click()
            await self.page.wait_for_timeout(5000)
            if await self.sql_query_response_locator.is_visible():
                sql_query = (await self.sql_query_response_locator.text_content()).strip()
                print("*******************************************************************")
                print("genereted sql:",sql_query)
                print("*******************************************************************")

        return sql_query, icon_status


        #     await self.show_sql_icon.click()
        #     await self.page.wait_for_timeout(5000)
        #
        #     try:
        #         # ✅ WAIT until SQL text appears
        #         await expect(self.sql_query_response_locator).to_have_text(
        #             lambda text: len(text.strip()) > 20,
        #             timeout=5000
        #         )
        #
        #         sql_query = (await self.sql_query_response_locator.text_content()).strip()
        #         print("💾 SQL captured successfully")
        #
        #     except Exception:
        #         print("⚠️ SQL panel opened but query not loaded")
        #
        # return sql_query, icon_status
#---------------------------------------------------------------------------------------------


def normalize_sql(sql: str) -> str:
    return " ".join(sql.split()).strip().lower()


async def main():
    reader = ExcelReader(INPUT_PATH, SHEET_NAME)
    writer = ExcelWriter(OUTPUT_PATH)
    questions_sqlquery = reader.get_questions_with_expected_sql()

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # --- LOGIN email ---
        # await page.goto("https://ciathena.customerinsights.ai/")
        # await page.locator("//input[@placeholder='username@domain.ai']").fill("harimulaguri9@gmail.com")
        # await page.wait_for_timeout(2000)
        # await page.locator("//button[normalize-space()='Sign in']").click()
        # await page.wait_for_timeout(2000)
        # await page.locator("//input[@placeholder='Password']").fill("Test@123")
        # await page.locator("#idSIButton9").click()
        # await page.get_by_role("button", name="Text +XX XXXXXXXX73").click()
        # await page.wait_for_timeout(5000)


        # --- LOGIN SSO ---
        await page.goto("https://ciathena.customerinsights.ai/")
        await page.locator("//input[@placeholder='username@domain.ai']").fill("hari.mulaguri@customerinsights.ai")
        await page.wait_for_timeout(2000)
        await page.locator("//button[normalize-space()='Sign in']").click()
        await page.wait_for_timeout(2000)
        await page.locator("#i0116").fill("hari.mulaguri@customerinsights.ai")
        await page.get_by_role("button", name="Next").click()
        await page.locator("//input[@placeholder='Password']").fill("Android@123")
        await page.locator("#idSIButton9").click()
        await page.get_by_role("button", name="Text +XX XXXXXXXX73").click()
        await page.wait_for_timeout(20000)
        await page.get_by_role("button", name="Verify").click()
        await page.wait_for_timeout(5000)

        bot = ChatbotAutomation(page)


        for item in questions_sqlquery:
            question = item["question"]
            expected_sql = item["expected_sql"]
            expected_sql1 = (expected_sql.text_content()).strip()

            # chart = item["chart"]


            print(f"\n❓ {question}")
            print("==============================================================================================")
            print(f"\n❓ {"EXCEL_sql:",expected_sql1}")
            # print(f"\n❓ {"chart:",chart}")

            await page.wait_for_timeout(5000)

            await page.locator("#welcome-search-input").click(force=True)
            await page.locator("#welcome-app-name-fast").click()
            await bot.ask_question_input.fill(question)
            await bot.send_button.click()
            await page.wait_for_timeout(60000)
            answer_text = await bot.get_valid_response()
            sql_query = None
            icon_status = None

            if answer_text:
                sql_query, icon_status = await bot.get_sql_query_if_available()
                status = "PASS" if all(icon_status.values()) else "FAIL"
                # assert sql_query == expected_sql1
                assert normalize_sql(sql_query) == normalize_sql(expected_sql1)

            else:
                answer_text = await bot.get_error_response() or "No response"
                status = "FAIL"

            writer.write_row(
                question,
                answer_text,
                sql_query,
                icon_status["show_sql_visible"] if icon_status else False,
                icon_status["show_share_visible"] if icon_status else False,
                icon_status["show_save_visible"] if icon_status else False,
                icon_status["view_fullscreen_icon"] if icon_status else False,
                icon_status["data_view_icon"] if icon_status else False,
                icon_status["show_download_visible"] if icon_status else False,
                status
            )
            writer.save()
            print("✅ ------- Response generated ----------")
            await page.click("img[alt='Home']")

        await browser.close()
        print("✅ Execution completed")


if __name__ == "__main__":
    asyncio.run(main())