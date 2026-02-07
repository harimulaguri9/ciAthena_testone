import re
from datetime import time
from playwright.async_api import Page, expect
import time
from ciathena.pages.BasePage import BasePage


class InsightsHubPage(BasePage):
    def __init__(self, page: Page ):
        super().__init__(page)
        self.insights_hub_nav_label = page.locator("#sidebar-icon-insights-hub")
        # self.insights_hub_nav_label=page.locator("#sidebar-nav-icon-container-insights-hub")
        self.insights_hub_title = page.get_by_text("Insights Hub")
        self.executive_insights_tab = page.locator("#text_executive_insights")
        self.personalized_insights_tab = page.locator("#text_personalized_insights")

        self.executive_insights_card_title1 = page.locator("//h6[contains(@id,'executive-insight-title-')]")
        self.executive_insights_cards_title2 = page.locator("//*[@id='dashboard-header']/p")
        self.executive_insights_cards_details_button = page.locator(
            "//button[contains(@id,'executive-insight-details-btn-')]")
        # self.titles = page.locator('[id^="executive-insight-title-"]')
        self.executive_insights_cards_summary = page.locator("#answer-text-paragraph")
        self.insights_graph_info_button = page.locator("//button[contains(@id,'info-btn-')]")
        # self.insights_tabular_view=page.locator("#toggle-label-0-0")
        self.insights_tabular_toggle_button = page.locator("//div[contains(@id,'toggle-btn-')]")
        self.insights_download_button = page.locator("//button[contains(@id,'download-btn')]")
        self.chart_section_title = page.locator("//div[@data-name='section-header-container']")
        self.detailed_page_back_button = page.locator("#back-button-icon")

        self.personalized_insights_header_content = page.locator("#header-title-content")
        self.personalized_insight_card_content = page.locator(
            "//*[@id='insight-card-data-trends-and-exploration-0']/div[1]/p")
        self.personalized_insight_segmentation_card_content = page.locator(
            "//*[@id='insight-card-segmentation-0']/div[1]/p")
        self.personalized_insight_channels_card_content = page.locator(
            "//*[@id='insight-card-face-to-face-vs-virtual-calls-0']/div[1]/p")
        self.personalized_insight_budget_card_content = page.locator(
            "//*[@id='insight-card-budget-optimization-0']/div[1]/p")

        self.personalized_insight_card_full_content = page.locator(
            "//*[@id='insight-card-data-trends-and-exploration-3']")
        # self.personalized_insight_card_msg_icon = page.locator("#conversation-icon-data-trends-and-exploration-0")
        self.navigate_left_icon = page.locator("#navigate-left-icon")
        self.navigate_right_icon = page.locator("#navigate-right-icon")
        self.personalized_insight_card_title = page.locator("")
        self.tabular_view_toggle = page.locator("#conversation-icon-segmentation-1")
        self.navigate_more_option = page.locator("#more-options-icon-segmentation-0")
        self.go_to_conversation = page.locator("#conversation-icon-data-trends-and-exploration-0")
        self.card_more_option=page.locator("//*[@id='more-options-icon-data-trends-and-exploration-0']")


        self.personalized_insight_card_full_content = page.locator(
            "#insight-card-customer-engagement-1")
        self.tabular_view_toggle = page.locator("#conversation-icon-segmentation-1")
        self.navigate_more_option = page.locator("#more-options-icon-segmentation-0")
        self.go_to_conversation = page.locator("#conversation-icon-data-trends-and-exploration-0")
        self.card_more_option=page.locator("//*[@id='more-options-icon-data-trends-and-exploration-0']")


        self.rename_insights_option = self.page.locator('[data-name="rename-action-icon"]')
        self.rename_popup = self.page.locator("#rename-dialog-title-text")
        self.rename_input_field = self.page.locator("#rename-input-field")
        self.rename_confirm_button = self.page.locator("#rename-confirm-button")
        self.collab_space_navbar = page.locator("#sidebar-nav-label-container-collaboration-space")
        self.proceed_button = page.locator("//button[contains(text(), 'Proceed')]")
        self.spaceTitleInput = page.locator("#spaceTitleInput")
        self.spaceDescriptionInput = page.locator("#spaceDescriptionInput")
        self.saveSpaceButton = page.locator("//button[contains(text(), 'Save')]")
        self.MySpace_header = page.locator("//p[normalize-space()='My Spaces']")
        self.rename_space = page.locator("//span[text()='Rename']")
        self.rename_input = page.locator("#rename-input-field")
        self.rename_button = page.locator("#rename-confirm-button")
        self.Delete_space = page.locator("//span[text()='Delete']")
        self.Delete_button = page.locator("//*[@id='delete-confirm-button']")
        self.ongoing_threads_title = page.get_by_text("Ongoing Threads")

    async def create_space(self):
        title1 = "qa1space"
        title1desc = "qa1spacedesc"
        spacename1 = "testHari_space1"
        time.sleep(5)
        await self.collab_space_navbar.click()
        await self.page.evaluate("document.body.style.zoom='80%'")
        time.sleep(3)
        await self.proceed_button.click()
        await self.spaceTitleInput.fill(title1)
        await self.spaceDescriptionInput.fill(title1desc)
        await self.saveSpaceButton.click()
        await self.page.locator("text=Space created successfully").wait_for(state="visible", timeout=10000)
        await self.collab_space_navbar.hover()
        await self.MySpace_header.wait_for(state="visible", timeout=4000)
        await self.page.locator("div").filter(has_text=re.compile(r"^space⋯$")).get_by_role("button").click()

        # self.page.locator().click()
        await self.Delete_space.click()
        await self.Delete_button.click()
        await self.Rename_space.click()
        await self.rename_input.press("End")
        await self.rename_input.type("_Updated")
        await self.rename_button.click()

    async def verify_insightshub_UI(self):
        await self.insights_hub_nav_label.wait_for(state="visible", timeout=10000)
        await self.insights_hub_nav_label.click()
        await self.insights_hub_title.wait_for(state="visible", timeout=2000)
        # await check.is_true(self.executive_insights_tab.is_visible(), "Executive Insights tab should be visible")
        # await check.is_true(self.personalized_insights_tab.is_visible(), "personalized  Insights tab should be visible")
        await self.personalized_insights_tab.wait_for(state="visible", timeout=2000)
        await self.assert_visible(self.personalized_insights_tab, "Personalized insights")

    async def verify_executive_cards(self):
        count = await self.executive_insights_card_title1.count()
        print(f"🔍 Found {count} executive insights.")

        for i in range(count):

            title_element = self.executive_insights_card_title1.nth(i)

            # ✅ Capture text BEFORE clicking
            try:
                title_text = title_element.text_content(timeout=5000)
                title_text = title_text.strip() if title_text else "N/A"
            except Exception:
                title_text = "N/A"
            print(f"{i + 1}. {title_text}")
            # optional hover (for tooltip/animation)
            await title_element.hover()
            await self.click(self.executive_insights_cards_details_button.nth(i), "Details button")

            # print(f"{i + 1}. {title_text}")

            await self.verify_chart_details()
            time.sleep(3)
            await self.click(self.detailed_page_back_button, "detailed_page_back_button_")

    async def verify_chart_details(self):
        charts = await self.chart_section_title.count()

        for i in range(charts):
            time.sleep(3)

            await self.assert_visible(self.insights_graph_info_button.nth(i), f"Info icon for chart {i + 1}")
            # await self.assert_visible(self.insights_tabular_toggle_button.nth(i), f"Tabular toggle icon for chart {i + 1}")
            await self.assert_visible(self.insights_download_button.nth(i), f"Download icon for chart {i + 1}")

            # Click safely using nth(i)
            await self.click(self.insights_graph_info_button.nth(i), f"insights_graph_info_button_{i}")
            # await self.click(self.insights_tabular_toggle_button.nth(i), f"tabular_toggle_button_{i}")
            # await self.click(self.insights_tabular_toggle_button.nth(i), f"tabular_toggle_button_{i}_back")
            await self.click(self.insights_download_button.nth(i), f"download_button_{i}")

            print(f"✅ Chart {i + 1} verified successfully.\n")

    async def verify_personalized_insights_all_cards(self):
        """
        Navigate through Insights sections (Data Trends, Segmentation, etc.),
        perform rename + message icon click on first visible card in each section.
        """

        # --- Step 1: Navigate to Personalized Insights tab ---
        await self.insights_hub_nav_label.wait_for(state="visible", timeout=5000)
        await self.insights_hub_nav_label.click()
        await self.personalized_insights_tab.wait_for(state="visible", timeout=5000)
        await self.click(self.personalized_insights_tab, "personalized_insights_tab")
        time.sleep(30)
        # --- Step 2: Define all section headers to iterate through ---
        headers = [
            "Customer Engagement",
            "Operational Efficiency",
            "Market Trends"


            # "Access Favorability Landscape",
            # "Market Access Landscape",
            # "Access vs Performance Dynamics",
            # "Competitive Access Comparison",
            # "Payer Mix & Differentiation",
            # "FAST vs Traditional Benchmarks",
            # "HCP Opportunity Segmentation"
        ]

        # --- Step 3: Loop through each section header ---
        for index, header_name in enumerate(headers, start=1):
            print(f"\n➡️ Navigating to Section {index}: {header_name}")

            # try:
            # Wait for section header to be visible
            await self.page.wait_for_timeout(5000)

            header_locator = self.page.locator(f"//h2[text()='{header_name}']")

            #self.click(header_locator, f'{header_locator}')
            await header_locator.wait_for(state="visible", timeout=5000)
            print(f"✅ Section '{header_name}' loaded.")

            # --- Step 4: Get the first visible insight card under this section ---
            trx_card = self.page.locator(
                f"//div[contains(@id, 'insight-card-{header_name.lower().replace(' ', '-')}')]"
            ).first

            await trx_card.wait_for(state="visible", timeout=5000)
            trx_text = await trx_card.text_content()
            trx_text = trx_text.strip() if trx_text else "N/A"
            print(f"📈 Found Card: {trx_text}")

            await trx_card.hover()

            # --- Step 5: Click more → rename ---
            # more_icon = self.page.locator(
            #     f"//*[@id='more-options-icon-{header_name.lower().replace(' ', '-').replace('&', 'and')}-0']"
            # )
            # await more_icon.wait_for(state="visible", timeout=10000)
            # await more_icon.click()
            # time.sleep(2)
            # await self.rename_insights_option.click()
            # await self.rename_input_field.click()
            # await self.rename_input_field.press("End")
            # await self.rename_input_field.type("_Updated")
            # await self.rename_confirm_button.click()
            # print("✅ Successfully renamed insight.")
            #
            # # --- Step 6: Hover again and click message icon ---
            # await trx_card.hover()

            await self.page.wait_for_timeout(3000)

            msg_icon = self.page.locator(
                f"//*[@id='conversation-icon-{header_name.lower().replace(' ', '-').replace('&', 'and')}-0']"
            )

            await msg_icon.wait_for(state='visible', timeout=3000)
            await msg_icon.click()

            # await self.click(self.page.go_back(), "personalized_insights_tab")
           # await self.page.go_back(wait_until="domcontentloaded")
            await self.ongoing_threads_title.wait_for(state="visible", timeout=5000)
            await self.insights_hub_nav_label.click()
            # Reopen tab (some apps reload page)
            await self.click(self.personalized_insights_tab, "personalized_insights_tab")

        # except Exception as e:
        #     print(f"⚠️ Error in section '{header_name}': {e}")

        # --- Step 7: Click right arrow to move to next section (except last one) ---
            time.sleep(2)
            if index < len(headers):
                for i in range(0,index):
                    await self.navigate_right_icon.click()
                time.sleep(2)
    print("\n✅ Completed all Insight sections successfully.")


def verify_data_trends_and_cards(self):
    time.sleep(5)
    self.insights_hub_nav_label.click()
    self.personalized_insights_tab.wait_for(state="visible", timeout=5000)
    self.click(self.personalized_insights_tab, "personalized_insights_tab")
    time.sleep(10)
    # --- STEP 1: Read Header ---
    # try:
    header_locator = self.page.locator('//*[@id="header-title-content"]/h2')
    header_text = header_locator.text_content(timeout=3000).strip()
    print(f"\n📊 Header: {header_text}")
    time.sleep(2)
    # card_text = self.personalized_insight_card_content.text_content(timeout=5000)
    # time.sleep(2)
    # card_text = card_text.strip() if card_text else "N/A"
    # print(f" card_element_info: {card_text}")

    card_count = self.personalized_insight_card_full_content.count()
    for i in range(card_count):
        card_text1 = self.personalized_insight_card_full_content.text_content(timeout=5000)
        card_item = self.personalized_insight_card_full_content.nth(i)
        card_text1 = card_item.text_content(timeout=3000)
        card_text1 = card_text1.strip().replace("\n", " ") if card_text1 else "N/A"
        print(f"   • Card {i + 1}: {card_text1}")

    print("\n✅ Completed reading header and visible card info...\n")
