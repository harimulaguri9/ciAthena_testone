
from playwright.async_api import Page, expect
from ciathena.pages.BasePage import BasePage


class TeamsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.teams_nav_button = page.locator("#configurations-nav-label-teams")
        self.teams_search_field = page.locator('#teams-search-input')
        self.teams_filter_icon=page.locator("#teams-filter-icon")
        self.teams_filter_usecase=page.locator("#teams-filter-select-use-case-dropdown")
        self.teams_delete_icon=page.locator("#teams-delete-button-icon")
        self.teams_add_button = page.locator("#teams-add-button")

        self.teams_edit_icon=page.locator("//img[@alt='Action']")
        # self.teams_namee_input=page.locator("#teams-general-name-input")
        self.teams_name = page.locator("#teams-general-name-input")
        self.teams_desc_name = page.locator("#teams-general-description-input")
        self.usecase_teams_select = page.locator("#teams-general-use-cases-select")
        self.use_case_fast = page.locator("#teams-general-use-case-option-fast")


        self.teams_general_tab = page.locator("#add-team-tab-general")
        self.teams_tab_users = page.locator("#add-team-tab-users")
        self.teams_users_add_button = page.locator("#teams-users-add-button")

        self.teams_user_search_add_team = page.locator("#teams-users-search-input")
        self.teams_addteam_users_checkbox = page.locator("input[type='checkbox'][id^='teams-users-table-row-checkbox']")
        self.save_proceed_button = page.locator("#add-team-save-button")
        # self.team_created_success = page.locator("#add-team-save-button")
        self.addusers_search_input = page.locator("#teams-add-new-users-modal-search-input")
        self.addusers_checkbox = page.locator("#teams-add-new-users-modal-user-checkbox-0")
        self.teams_user_submit = page.locator("#teams-add-new-users-modal-submit-button")
        self.teams_user_delete_button_icon = page.locator("#teams-users-delete-button-icon")

        self.teams_user_confirm_dialog_confirm_button = page.locator("#teams-user-action-confirm-dialog-confirm-button")
        self.teams_user_confirm_dialog_cancel_button = page.locator("#teams-user-action-confirm-dialog-cancel-button")

        self.users_more_button = page.locator("#user-context-menu-button-57f067d0-7a74-4be3-ae05-fbcc013c1485 > svg")
        self.teams_properties_option = page.locator("#context-menu-option-0")
        self.teams_delete_option = page.locator("#context-menu-option-1")
        self.teams_rename_option = page.locator("#context-menu-option-2")
        self.teams_users_delete_button = page.locator("#user-context-menu-delete")
        self.teams_delete_confirmation = page.locator("#delete-confirm-button")
        self.teams_delete_cancel_button = page.locator("#delete-cancel-button")
        self.teams_save_button = page.locator("#edit-team-save-button")

        self.teams_rename_input = page.locator("#rename-input-field-label")
        self.teams_rename_cancel_button = page.locator("#rename-cancel-button")
        self.teams_rename_confirm_button = page.locator("#rename-confirm-button")


        self.teams_edit_general_tab = page.locator("#edit-team-tab-general")
        self.teams_edit_users_tab = page.locator("#edit-team-tab-users")
        self.teams_edit_logs_tab = page.locator("#edit-team-tab-logs")
        self.teams_general_name_input = page.locator("#teams-general-name-input")
        self.teams_teams_general_description_input = page.locator("#teams-general-description-input")

        self.teams_general_usecases_select = page.locator("#teams-general-use-cases-select")
        self.teams_user_table_emails = page.locator("[data-testid='teams-users-row-email']")
        # self.teams_user_table_email = page.locator("#teams-users-table-row-email-0")
        self.teams_user_log_entrys = page.locator("[data-testid='teams-logs-row-action']")



    async def validate_teams_page_options(self):
        print("users")
        await self.teams_nav_button.click()
        await self.teams_search_field.is_visible()
        await self.teams_filter_icon.is_visible()
        await self.teams_delete_icon.is_visible()
        await self.teams_add_button.is_visible()
        await self.verify_teams_table_columns()
        print("teams table_columns")


    async def verify_teams_table_columns(self):
        columns = ["Name", "Description", "Use Case", "Users"]
        for columnname in columns:
            await self.page.locator(f"th:has-text('{columnname}')").is_visible()
            print(columnname)



    async def fill_team_details(self,team_name: str,team_desc_name: str):
        await self.teams_add_button.click()
        await self.teams_name.fill(team_name)
        await self.teams_desc_name.fill(team_desc_name)
        await self.usecase_teams_select.click()
        await self.use_case_fast.click()
        await self.page.mouse.click(150, 150)

    async def add_users_create_team(self):
        await self.teams_tab_users.click()
        await self.teams_users_add_button.click()
        await self.addusers_search_input.fill("harivocera@gmail.com")
        await self.addusers_checkbox.click()
        await self.teams_user_submit.click()
        await self.save_proceed_button.click()
        await self.page.wait_for_timeout(2000)  # 20 seconds

    async def validate_created_team_properties(self):
        await self.page.wait_for_timeout(2000)  # 20 seconds
        await self.select_created_team_quick_options()
        await self.page.wait_for_timeout(2000)  # 20 seconds
        await self.teams_properties_option.click()
        await self.page.wait_for_timeout(2000)  # 20 seconds
        await self.valdiate_teams_general_section()
        await self.valdiate_teams_users_section()
        await self.valdiate_teams_logs_section("Team created")
        await self.teams_save_button.click()


    async def select_created_team_quick_options(self):
        created_team_name="TeamsABC"
        rows = self.page.locator("tr[data-testid='teams-table-row']")
        row_count = await rows.count()
        for i in range(row_count):
            row = rows.nth(i)
            team_name = await row.locator("[data-testid='teams-row-name-content']").inner_text()
            if team_name.strip() == created_team_name:
                # ✅ Select checkbox
                checkbox = row.locator("input[type='checkbox']")
                await checkbox.check()
                # ✅ Click context menu (three dots)
                await row.locator("[data-testid='teams-row-context-menu-icon']").click()
                break

        await self.page.wait_for_timeout(2000)



    async def select_updated_team_quick_options(self):
        updated_team_name="TeamsABCD"
        rows = self.page.locator("tr[data-testid='teams-table-row']")
        row_count = await rows.count()
        for i in range(row_count):
            row = rows.nth(i)
            team_name = await row.locator("[data-testid='teams-row-name-content']").inner_text()
            if team_name.strip() == updated_team_name:
                # ✅ Select checkbox
                checkbox = row.locator("input[type='checkbox']")
                await checkbox.check()
                # ✅ Click context menu (three dots)
                await row.locator(
                    "[data-testid='teams-row-context-menu-icon']"
                ).click()
                break
        await self.page.wait_for_timeout(2000)




    # async def validate_created_team_properties(self):
    #     created_team_name="TeamsABC"
    #     await self.select_created_team_properties(created_team_name)
    #     await self.teams_users_add_button.click()
    #     await self.addusers_search_input.fill("haritest1@gmail.com")
    #     await self.page.wait_for_timeout(2000)
    #     await self.addusers_checkbox.click()
    #     await self.teams_user_submit.click()

    async def valdiate_teams_general_section(self):
        await self.teams_edit_general_tab.is_visible()
        await expect(self.teams_general_name_input).to_have_value("TeamsABC")
        await expect(self.teams_teams_general_description_input).to_have_value("TeamsABC")
        await expect(self.usecase_teams_select).to_have_text("FAST")

    async def valdiate_teams_users_section(self):
        user_email="harivocera@gmail.com"
        await self.teams_edit_users_tab.click()
        await expect(self.teams_user_table_emails).to_have_text(user_email)

    async def valdiate_teams_logs_section(self, action_text: str):
        await self.teams_edit_logs_tab.click()
        await expect(self.page.locator("[data-testid='teams-logs-row-action']")
                .filter(has_text=action_text)).to_be_visible(timeout=5000)
        print("logs- done")

    async def teams_delete_linked_users(self):
        user_email="harivocera@gmail.com"

        await self.teams_edit_users_tab.click()
        await self.teams_addteam_users_checkbox.click()
        await self.teams_user_delete_button_icon.click()
        await self.teams_user_confirm_dialog_confirm_button.click()
        await self.teams_save_button.click()
        await self.valdiate_teams_user_removed_log()
        await self.teams_save_button.click()

    async def valdiate_teams_user_removed_log(self):
        await self.teams_edit_logs_tab.is_visible()
        # await expect(self.teams_user_log_entrys).to_contain_text("User removed from team")
        await expect(self.teams_user_log_entrys.first).to_contain_text("User removed from team")
        print("User removed - done")


    async def validate_delete_team(self):
        await self.select_updated_team_quick_options()
        await self.teams_properties_option.click()
        await self.teams_delete_linked_users()
        await self.select_updated_team_quick_options()
        await self.teams_delete_option.click()
        await self.teams_delete_confirmation.click()


    async def validate_rename_team(self):
        await self.select_created_team_quick_options()
        await self.teams_rename_option.click()
        await self.teams_rename_input.fill("TeamsABCD")
        await self.teams_rename_confirm_button.click()
        await self.valdiate_updated_team_name("TeamsABCD")

    async def valdiate_updated_team_name(self, updated_team_name:str):
        await expect(self.page.locator("[data-testid='teams-row-name-content']",
                                       has_text=updated_team_name)).to_be_visible()