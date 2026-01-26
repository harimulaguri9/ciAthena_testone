import re
from datetime import time
from playwright.async_api import Page, expect
import time
from ciathena.pages.BasePage import BasePage


class CollabSpacePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.collab_space_navbar=page.locator("#sidebar-nav-label-container-collaboration-space")
        self.proceed_button = page.locator("//button[contains(text(), 'Proceed')]")
        self.spaceTitleInput = page.locator("#spaceTitleInput")
        self.spaceDescriptionInput = page.locator("#spaceDescriptionInput")
        self.saveSpaceButton = page.locator("//button[contains(text(), 'Save')]")
        self.MySpace_header=page.locator("//p[contains(text(),'My Spaces')]")

        self.space_name_elements=page.locator("//p[contains(text(),'My Spaces')]//parent::div/following-sibling::div/div/div/div")

        self.rename_space=page.locator("//span[text()='Rename']")
        self.rename_input=page.locator("#rename-input-field")
        self.rename_button=page.locator("#rename-confirm-button")
        self.Delete_space=page.locator("//span[text()='Delete']")
        self.Delete_confirm_button=page.locator("//*[@id='delete-confirm-button']")
        self.Pin_button=page.locator("//img[@alt='Pin']")
        self.view_button=page.locator("//img[@alt='View']")
        self.collab_panel_pin_button=page.locator("#collab-panel-pin-button")
        self.search_spaces=page.get_by_placeholder("Search spaces")
        self.members_space=page.locator("//span[text()='Members']")
        self.members_dialog_title_text=page.locator("#members-dialog-title-text")
        self.members_dialog_user_dropdown=page.locator("#members-dialog-user-dropdown")
        self.members_dialog_user_search_input=page.locator("#members-dialog-user-search-input")
        self.members_dialog_user_checkbox=page.locator("#members-dialog-user-checkbox-0")
        self.members_dialog_add_button=page.locator("#members-dialog-add-button")
        self.members_dialog_member_container=page.locator("#members-dialog-member-container-1")
        self.members_dialog_close_button=page.locator("#members-dialog-close-button")
        self.members_dialog_member_info=page.locator("#members-dialog-member-info-1")
        self.members_dialog_member_remove_button=page.locator("#members-dialog-member-remove-button-1")
        self.members_dialog_member_info=page.locator("#members-dialog-member-info-1")
        self.members_dialog_member_info=page.locator("#members-dialog-member-info-1")
        self.view_dashboard_button=page.locator("#view-button")
        self.generate_dashboard_button=page.locator("//*[@id='generate-dashboard-button']/p")
        self.infographic_checkbox_button=page.locator("#infographic-checkbox-0")
        self.kpi_checkbox_button=page.locator("#kpi-checkbox-0")
        self.generate_dashboard_header=page.locator("//*[@id='dashboard-generator-back-button-container']/h3")
        self.infographics_header=page.locator("#dashboard-generator-tab-infographics")
        self.kpi_cards_header=page.locator("#dashboard-generator-tab-kpi-cards")
        self.save_proceed_button=page.locator("#save-and-proceed-button")
        self.dashboard_input=page.locator("#dashboard-name-input")
        self.dashboard_desc_input=page.locator("#dashboard-description-input")
        self.save_dialog_button=page.locator("#save-dialog-save-button")
        self.dashboard_edit_icon=page.locator("#collaboration-space-dashboard-edit-icon")
        self.dashboard_title_edit_input=page.locator("#collaboration-space-dashboard-title-edit-input")
        self.dashboard_save_button=page.locator("#collaboration-space-dashboard-save-button")

    async def create_new_space(self):
        title1="qa1space"
        title1desc="qa1spacedesc"
        spacename1="testHari_space1"
        time.sleep(5)
        await self.collab_space_navbar.click()
        await self.page.evaluate("document.body.style.zoom='60%'")
        await self.proceed_button.click()
        await self.spaceTitleInput.fill(title1)
        await self.spaceDescriptionInput.fill(title1desc)
        await self.saveSpaceButton.click()
        time.sleep(2)
        expect(self.page.locator("text=Space created successfully")).to_be_visible()

    #async def member_sharing(self):
        # space_name = "qa1space"
        # user2="Gireesh"
        #
        # await self.collab_space_navbar.hover()
        # time.sleep(3)
        # # self.page.wait_for_locator(self.search_spaces, timeout=2000)
        # await self.page.wait_for_selector("//input[@placeholder='Search spaces']", timeout=3000)
        # await self.search_spaces.click()
        # time.sleep(2)
        # await self.Pin_button.click()
        # await self.MySpace_header.wait_for(state="visible", timeout=2000)
        # time.sleep(2)
        #
        # spaces_count = await self.space_name_elements.count()
        # time.sleep(2)
        #
        # print(f"Total spaces found: {spaces_count}")
        # for i in range(spaces_count):
        #     # Get text of the i-th space
        #     time.sleep(3)
        #     current_space_name = (await self.space_name_elements.nth(i).text_content()).strip()
        #     print(current_space_name)
        #     time.sleep(3)
        #     if current_space_name == space_name:
        #         print(f"Found space '{space_name}' at index {i}")
        #         time.sleep(5)
        #         await self.page.locator("//img[@id='collab-panel-my-space-menu-icon-0']").click()
        #         time.sleep(2)
        #         # more_button.click()
        #         print(f"Clicked 'More' button for space '{space_name}' at index {i}")
        #         time.sleep(2)
        #         await self.members_space.click()
        #         time.sleep(2)
        #         await self.assert_visible(self.members_dialog_title_text, "members_dialog_title  displayed")
        #         await self.members_dialog_user_dropdown.click()
        #         await self.members_dialog_user_search_input.fill(user2)
        #         await self.members_dialog_user_checkbox.click()
        #         time.sleep(2)
        #         await self.members_dialog_add_button.scroll_into_view_if_needed()
        #         await self.members_dialog_add_button.wait_for(state="visible")
        #         await self.members_dialog_add_button.click(force=True)
        #         time.sleep(2)
        #         success_message = self.page.locator("text=Members added successfully")
        #         expect(success_message).to_be_visible(timeout=2000)
        #         time.sleep(2)
        #         await self.members_dialog_member_container.hover()
        #         time.sleep(2)
        #         await self.members_dialog_member_remove_button.click()
        #         time.sleep(2)
        #         await self.members_dialog_close_button.click()
        #         time.sleep(3)


    async def rename_spaces(self):
        space_name = "hari_space1"
        space_desc_name = "qa1space_desc"
        new_space_name ="hari_space1_Updated"

        # Wait for the "My Spaces" section to be visible
        time.sleep(3)
        await self.collab_space_navbar.hover()
        time.sleep(3)
       # self.page.wait_for_locator(self.search_spaces, timeout=2000)
        await self.page.wait_for_selector("//input[@placeholder='Search spaces']", timeout=3000)
        await self.search_spaces.click()

        time.sleep(2)
        await self.MySpace_header.wait_for(state="visible", timeout=2000)
        time.sleep(2)

        spaces_count = await self.space_name_elements.count()
        time.sleep(2)

        print(f"Total spaces found: {spaces_count}")
        for i in range(spaces_count):
            # Get text of the i-th space
            time.sleep(3)
            current_space_name = (await self.space_name_elements.nth(i).text_content()).strip()
            print(current_space_name)
            time.sleep(3)
            if current_space_name == space_name:
                print(f"Found space '{space_name}' at index {i}")
                time.sleep(5)
                await self.page.locator("//img[@id='collab-panel-my-space-menu-icon-0']").click()


                print(f"Clicked 'More' button for space '{space_name}' at index {i}")
                time.sleep(2)

                # Click 'Delete' option in the menu that appears
                await self.rename_space.click()
                time.sleep(3)
                await self.rename_input.press("End")
                await self.rename_input.fill(new_space_name)
                await self.rename_button.click()

                print(f"Renamed '{space_name}' to '{new_space_name}'")

                # ✅ Validation — look for updated name in same locator list
                time.sleep(3)  # wait for DOM update
                updated_found = False
                spaces_after = await self.space_name_elements.count()

                for j in range(spaces_after):
                    name_after = (await self.space_name_elements.nth(j).text_content()).strip()
                    if name_after == new_space_name:
                        updated_found = True
                        print(f"✅ Rename successful — found updated name: '{new_space_name}'")
                        break

                if not updated_found:
                    print(f"❌ Rename failed — '{new_space_name}' not found after update.")

                break
            else:
                print(f"⚠️ Space '{space_name}' not found in the list.")



    async def delete_spaces(self):
        new_space_name ="hari_space1_Updated"

        # Wait for the "My Spaces" section to be visible
        time.sleep(3)
        await self.collab_space_navbar.hover()
        time.sleep(3)
       # self.page.wait_for_locator(self.search_spaces, timeout=2000)
        await self.page.wait_for_selector("//input[@placeholder='Search spaces']", timeout=3000)
        await self.search_spaces.click()
        #self.page.wait_for_selector(self.Pin_button, timeout=2000)
        #self.Pin_button.click()
        time.sleep(3)
        await self.MySpace_header.wait_for(state="visible", timeout=2000)
        space_name_elements=self.page.locator("//p[contains(text(),'My Spaces')]//parent::div/following-sibling::div/div/div/div")

        spaces_count = await self.space_name_elements.count()
        time.sleep(3)

        print(f"Total spaces found: {spaces_count}")
        for i in range(spaces_count):
            # Get text of the i-th space
            time.sleep(3)
            current_space_name = (await self.space_name_elements.nth(i).text_content()).strip()
            print(current_space_name)
            time.sleep(3)
            if current_space_name == new_space_name:
                print(f"Found space '{new_space_name}' at index {i}")

                await self.page.locator("//img[@id='collab-panel-my-space-menu-icon-0']").click()
                time.sleep(3)
                #more_button.click()
                print(f"Clicked 'More' button for space '{new_space_name}' at index {i}")
                time.sleep(3)

                # Click 'Delete' option in the menu that appears
                await self.Delete_space.click()
                time.sleep(3)
                await self.Delete_confirm_button.click()
                await self.collab_panel_pin_button.click()

                print(f"Deleted space '{new_space_name}'")

                # ✅ Validation: ensure space name no longer exists
                time.sleep(4)  # wait for UI refresh
                remaining_spaces = [
                    await self.pace_name_elements.nth(j).text_content().strip()
                    for j in range(await self.space_name_elements.count())
                ]

                print("Remaining spaces:", remaining_spaces)

                if new_space_name in remaining_spaces:
                    print(f"❌ Deletion failed — '{new_space_name}' still visible.")
                else:
                    print(f"✅ Deletion successful — '{new_space_name}' not found in My Spaces.")
                break
            else:
                print(f"⚠️ Space '{new_space_name}' not found — nothing to delete.")


    async def create_Dashboard(self):
        dashboard1="qa1Dashboard"
        dashboard1desc="qa1DashboardDesc"
        rename_dashboard="qa1Dashboard_updated"
        time.sleep(5)
        await self.collab_space_navbar.click()
        time.sleep(3)
        await self.page.evaluate("document.body.style.zoom='80%'")
        time.sleep(2)
        await self.assert_visible(self.view_button,"Collab Hub displayed")
        time.sleep(2)
        await self.view_button.click()
        time.sleep(2)
        await self.generate_dashboard_button.click()
        time.sleep(2)
        await self.infographics_header.click()
        await self.infographic_checkbox_button.click()
        time.sleep(2)
        await self.kpi_cards_header.click()
        await self.kpi_checkbox_button.click()
        await self.save_proceed_button.click()
        time.sleep(2)
        await self.dashboard_input.fill(dashboard1)
        time.sleep(2)

        await self.dashboard_desc_input.fill(dashboard1desc)
        time.sleep(2)
        await self.save_dialog_button.click()
        time.sleep(2)
        await self.dashboard_edit_icon.click()
        time.sleep(2)
        await self.dashboard_title_edit_input.fill(rename_dashboard)
        time.sleep(2)
        await self.dashboard_save_button.click()
