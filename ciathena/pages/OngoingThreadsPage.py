
from playwright.async_api import Page, expect
from ciathena.pages.BasePage import BasePage

class OngoingThreadsPage(BasePage):
    def __init__(self, page: Page, step_logger=None):
        super().__init__(page, step_logger)
        self.ongoing_threads_navbar=page.locator("#sidebar-nav-label-ongoing-threads")
        self.sidebar_nav_item_newchat=page.locator("#sidebar-nav-item-new-chat")

        self.ongoing_threads_title = page.get_by_text("Ongoing Threads")
        self.search_input = page.locator("//*[@id='search-input']")
        #self.search_input = page.locator("#search-input")
        self.pin_icon = page.locator("#pin-icon")
        self.today_header = page.locator("//*[@id='group-label-0']")
        self.response_question_text = page.locator("#question-text")
        self.today_history_section=page.locator("//p[contains(text(),'Today')]//parent::div/div/div/div/div[2]")
        self.mmx_title = page.get_by_text("Market Mix Modeling")
        self.home_icon = page.locator("#navbar-home-button")
        self.settings_icon = page.locator("#navbar-settings-button")
        self.app_overview_icon = page.locator("#navbar-app-overview-button")
        self.main_input = page.locator("#main-input")
        self.mic_icon = page.locator("#question-response-mic-button")
        self.show_thinking_button = page.locator("#show-thinking-button")
        self.send_button1 = page.locator("#send-btn")
        self.send_button2 = page.locator("#question-response-send-button")
        self.data_category_section = page.locator("#categories-wrapper")
        self.answer_response = page.locator("#answer-text")
        self.share_visualization_button = page.locator("#share-visualization-button")
        self.save_insights_button = page.locator("#save-visualization-button")
        self.next_button = page.locator("#nextButton")
        self.save_button = page.get_by_role("button", name="Save")
        self.submit_button = page.get_by_role("button", name="Submit")
        self.insight_saved_msg = page.get_by_text("Insight saved successfully")
        self.insight_unsaved_msg = page.get_by_text("Insight removed successfully.")
        self.insight_shared_msg = page.get_by_text("Insight shared successfully")
        self.download_button = page.locator("#download-visualization-button")
        self.download_visual_button = page.locator("#download-visuals-option")
        self.download_data_button = page.locator("#download-data-option")

        self.sql_button = page.locator("#sql-toggle-button")
        self.info_button = page.locator("#info-button")
        self.like_button = page.locator("#like-button")
        self.like_msg = page.locator("#like-icon")
        self.dislike_button = page.locator("#dislike-button")
        self.unlike_feedback_dialog = page.locator("#feedback-dialog-textarea")
        self.feedback_submit_button = page.locator("#feedback-dialog-submit-button")
        self.unlike_msg = page.locator("#like-icon")
        self.tag_containers = page.locator("[id^='tagItem-']")
        self.cancel_button = page.locator("#cancelButton")
        self.space_containers = page.locator("[id^='spaceInfoContainer-']")

        self.create_space_button = page.locator("//*[@id='mainContentContainer']/button")
        self.space_title_input = page.locator("#spaceTitleInput")
        self.space_desc_input = page.locator("#spaceDescriptionInput")
        self.save_space_Button = page.locator("#saveSpaceButton")
        self.tag_items = page.locator("#tagItem-")
        self.space_cancel_input = page.locator("#cancelSpaceCreationButton")
        self.space_create_space_popup = page.locator("#spaceTitleInput")
        self.save_to_Space_button = page.locator("#saveToSpaceButton")

        self.categories_header = page.locator("#categories-header")
        self.suggested_category_headers = page.locator("[data-name^='suggested-header-'][data-name$='-text']")
        self.suggested_question = page.locator("#suggestion-text-2")
        self.suggested_question_asked=page.locator("//h2[@id='question-text']")
        self.suggested_questions_list = page.locator("#suggested-question-item-0")
        self.question_name_elements=page.locator("//p[contains(text(),'Today')]//parent::div/div/div/div/div[2]")
        self.new_chat=page.locator("//*[@id='sidebar-icon-new-chat']")

        failures = []
    # --------------------------------------------------------------------------
    # Verification of page UI
    # --------------------------------------------------------------------------
    async def verify_ongoing_threads_UI(self):
        await self.ongoing_threads_title.wait_for(state="visible", timeout=20000)
        await self.assert_visible(self.mmx_title, "MMX title")
        await self.assert_visible(self.home_icon, "home_icon")
        await self.assert_visible(self.settings_icon, "settings_icon")
        await self.assert_visible(self.app_overview_icon, "app_overview_icon")

    # --------------------------------------------------------------------------
    # Ask Question
    # --------------------------------------------------------------------------
    async def ask_question(self):
        await self.main_input.fill(
            "How does TOTAL_DIGITAL_PROMOTIONS volume last month compare to the previous month across regions?"
        )
        await self.send_button1.click()
        #await asyncio.sleep(3)
        await self.page.wait_for_timeout(35000)  # 20 seconds
        # await self.assert_visible(self.show_thinking_button, "show_thinking_button")
        # time.sleep(5)
        # await self.assert_visible(self.show_thinking_button, "show_thinking_button")

        if await self.answer_response.is_visible():
            text = await self.answer_response.text_content()
            return text.strip() if text else None
        return None

    # --------------------------------------------------------------------------
    # Tag selection
    # --------------------------------------------------------------------------
    async def tag_select(self):
        count = await self.tag_containers.count()
        target_tag_name = "hari_tag"

        for i in range(count):
            tag_element = self.tag_containers.nth(i)
            await self.page.wait_for_timeout(2000)

            tag_name_text = (await tag_element.text_content() or "").strip()
            print(f"🔹 Found tag: {tag_name_text}")

            if target_tag_name.lower() in tag_name_text.lower():
                print(f"✅ Matching tag found: {tag_name_text}")
                await tag_element.click()
                await self.page.wait_for_timeout(2000)
                print(f"✅ Matching tag: '{tag_name_text}' clicked")
                break
            else:
                print(f"⚠️ Tag: '{target_tag_name}' not found!")

    async def tag_select1(self):
        count = await self.tag_items.count()
        target_space_tag_name = "hari_tag2"

        for i in range(count):
            tag_space_element = self.tag_items.nth(i)
            await self.page.wait_for_timeout(3000)
            print(tag_space_element)
            tag_name_text = (await tag_space_element.text_content() or "").strip()
            print(f"🔹 Found space: {tag_name_text}")

            if target_space_tag_name.lower() in tag_name_text.lower():
                print(f"✅ Matching space found: {tag_name_text}")
                await tag_space_element.click()
                print(f"✅ Matching space: '{tag_name_text}' clicked")
                break
            else:
                print(f"⚠️ Space: '{target_space_tag_name}' not found!")

    async def create_new_space(self):
        space_name = "hari_space1"
        space_name_desc = "hari_space1_desc"

        await self.create_space_button.wait_for(state="visible", timeout=2000)
        await self.create_space_button.click()
        await self.page.wait_for_timeout(2000)
        await self.space_title_input.fill(space_name)
        await self.space_desc_input.fill(space_name_desc)
        await self.page.wait_for_timeout(2000)
        await self.save_space_Button.click()
        await self.page.wait_for_timeout(3000)

    # --------------------------------------------------------------------------
    # Space selection
    # --------------------------------------------------------------------------
    async def space_select(self):
        count = await self.space_containers.count()
        print("space_containers:",count)
        target_space_name = "hari_space1"

        for i in range(count):
            space_element = self.space_containers.nth(i)
            await self.page.wait_for_timeout(2000)
            space_name_text = (await space_element.text_content() or "").strip()
            print(f"🔹 Found space: {space_name_text}")

            if target_space_name.lower() in space_name_text.lower():
                print(f"✅ Matching space found: {space_name_text}")
                await space_element.click()
                print(f"✅ Matching space: '{space_name_text}' clicked")
                break
        else:
            print(f"⚠️ Space: '{target_space_name}' not found!")

    # --------------------------------------------------------------------------
    # Share Insights
    # --------------------------------------------------------------------------
    async def share_insights(self):
        await self.share_visualization_button.click()
        await self.page.wait_for_timeout(2000)
        # await self.tag_select()
        # await self.page.wait_for_timeout(4000)
        # await self.next_button.click()
        # await self.page.wait_for_timeout(3000)
        await self.create_new_space()
        await self.page.wait_for_timeout(2000)
        await self.space_select()
        await self.page.wait_for_timeout(2000)
        await self.save_to_Space_button.click()


        # await expect(self.insight_shared_msg).to_be_visible(timeout=2000)
        #await self.assert_visible(self.insight_shared_msg, "Insight shared successfully")
    # --------------------------------------------------------------------------
    # Save Insights
    # --------------------------------------------------------------------------
    async def save_insights(self):
        await self.save_insights_button.click()
        await self.page.wait_for_timeout(4000)
        await self.tag_select()
        await self.page.wait_for_timeout(3000)
        await self.submit_button.click()
        await self.page.wait_for_timeout(2000)
        #await expect(self.insight_saved_msg).to_be_visible(timeout=2000)
        #await self.assert_visible(self.insight_saved_msg, "Insight saved successfully")

    # --------------------------------------------------------------------------
    # Unsave Insights
    # --------------------------------------------------------------------------
    async def unsave_insights(self):
        await self.save_insights_button.click()
        await self.page.wait_for_timeout(3000)
        await self.assert_visible(self.insight_unsaved_msg, "Bookmark removed successfully")


    # --------------------------------------------------------------------------
    # Download Insights
    # --------------------------------------------------------------------------
    async def click_download_insights_button(self):
        await self.page.wait_for_timeout(1000)
        try:
            await self.click(self.download_button, "download_button")
            return
        except:
            print("download_button not found, trying download_visual_button...")

        try:
            await self.click(self.download_visual_button, "download_visual_button")
            return
        except:
            print("download_visual_button not found.")

        try:
            await self.click(self.download_data_button, "download_data_button")
            return
        except:
            print("download_data_button not found.")

        print("⚠️ No download button found, continuing test...")

    # --------------------------------------------------------------------------
    # Info Button
    # --------------------------------------------------------------------------
    async def click_info_button(self):
        await self.click(self.info_button, "info_button")
        await self.page.wait_for_timeout(2000)

    # --------------------------------------------------------------------------
    # SQL Button Validation
    # --------------------------------------------------------------------------
    async def validate_sql_button(self):
        await self.click(self.sql_button, "sql_button")
        await self.page.wait_for_timeout(2000)
        await expect(self.sql_button).to_have_attribute("aria-label", "Hide SQL")
        await self.page.wait_for_timeout(2000)
        await self.click(self.sql_button, "sql_button")
        await self.page.wait_for_timeout(2000)
        await expect(self.sql_button).to_have_attribute("aria-label", "Show SQL")

    # --------------------------------------------------------------------------
    # Like & Dislike Buttons
    # --------------------------------------------------------------------------
    async def click_like_button(self):
        await self.click(self.like_button, "like_button")
        await self.page.wait_for_timeout(2000)
        await expect(self.like_button).to_have_attribute("aria-label", "Undo like")
        await expect(self.like_msg).to_be_visible(timeout=5000)
        await self.page.wait_for_timeout(2000)

    async def click_dislike_button(self):
        await self.click(self.dislike_button, "unlike_button")
        await self.page.wait_for_timeout(2000)
        await self.assert_visible(self.unlike_feedback_dialog, "unlike feedback popup")
        await self.unlike_feedback_dialog.fill("test unlike feedback")
        await self.page.wait_for_timeout(2000)
        await self.click(self.feedback_submit_button, "feedback_submit_button")
        await self.page.wait_for_timeout(2000)

    # --------------------------------------------------------------------------
    # Suggested Questions
    # --------------------------------------------------------------------------
    async def verify_suggested_questions(self):
        await self.sidebar_nav_item_newchat.click()
        await expect(self.categories_header).to_be_visible(timeout=3000)
        headers_count = await self.suggested_category_headers.count()
        print("suggested_questions_headers:", headers_count)
        loops = min(headers_count, 2)
        for i in range(loops):
            await self.new_chat.click()
            await self.page.wait_for_timeout(2000)
            suggested_category_header =  self.suggested_category_headers.nth(i)
            print("suggested_category_header:-->", await suggested_category_header.text_content())
            await self.page.wait_for_timeout(2000)
            await suggested_category_header.hover()
            await self.page.wait_for_timeout(2000)
            suggested_question_name = (await self.suggested_question.text_content()).strip()
            print(f"🔹 Found question_name: {suggested_question_name}")
            await self.suggested_question.click()
            await self.page.wait_for_timeout(30000)
            assert await self.suggested_question_asked.text_content() in suggested_question_name



            # if target_suggested_question_name.lower() in suggested_question_name.lower():
            #     print(f"✅ Matching tag found: {suggested_question_name}")
            #     await suggested_question.click()
            #     await self.page.wait_for_timeout(2000)
            #     print(f"✅ Matching tag: '{suggested_question_name}' clicked")
            #     await self.page.wait_for_selector("//span[text()='call promotional']")
            #     break
            # else:
            #     print(f"⚠️ Tag: '{target_suggested_question_name}' not found!")

    async def verify_OGT_history(self):
        await self.ongoing_threads_navbar.hover()
        await self.search_input.click()
        await self.pin_icon.click()

        await self.today_header.wait_for(state="visible", timeout=5000)
        today_history_Qs = await self.today_history_section.count()

        print(f"Total today_history_Q found: {today_history_Qs}")
        for i in range(today_history_Qs):
            await self.page.wait_for_timeout(2000)
            today_history_Q1 = self.today_history_section.nth(i)
            question_text=await today_history_Q1.text_content()
            print(question_text)
            await today_history_Q1.click()
            await self.page.wait_for_timeout(5000)

            response_Q_count=await self.response_question_text.count()
            for j in range(response_Q_count):
                await self.page.wait_for_timeout(5000)

                response_Q = self.today_history_section.nth(i)
                resp_question_text = await response_Q.text_content()
                print(resp_question_text)
                await self.page.wait_for_timeout(2000)
                #assert question_text.__contains__(resp_question_text)
                #assert resp_question_text in question_text
