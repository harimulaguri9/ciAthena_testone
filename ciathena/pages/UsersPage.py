import re
from datetime import time
from playwright.async_api import Page, expect
from ciathena.pages.BasePage import BasePage


class UsersPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.user_nav_button = page.locator("//span[normalize-space()='Users']")
        self.user_adduser_button = page.get_by_role("button", name="Add User Add user")
        self.user_search_field = page.get_by_placeholder('//input[@placeholder="Search by name/role name..."]')
        self.user_filter_icon=page.locator("//img[@alt='Filter']")
        self.user_edit_icon=page.locator("//img[@alt='Action']")
        self.users_adduser_button=page.locator("//button[.//p[text()='Add user']]")
        self.user_first_name = page.get_by_role("textbox", name="Enter first name")
        self.user_last_name = page.get_by_role("textbox", name="Enter last name")
        self.user_email = page.get_by_role("textbox", name="Enter email address")
        self.user_title = page.locator("#general-tab-title-input")
        self.user_phone = page.locator("#general-tab-phone-input")
        self.user_usecases_dropdown = page.locator("//p[text()='Role']/following::div[@role='combobox'][1]")

        self.designation = page.get_by_role("textbox", name="Enter designation")
        self.phone_number = page.get_by_role("textbox", name="Enter phone number")

        # ========== Language ==========
        self.language_dropdown = page.get_by_text("English")
        self.language_option_english = page.get_by_role("option", name="English")

        # ========== Use Cases ==========
        self.use_cases_dropdown = page.get_by_text("Select use cases", exact=True)
        self.use_case_mmx = page.get_by_text("MMX", exact=True)
        self.use_case_fast = page.get_by_role("option", name="FAST")
        self.minimise_usecase_dropdown = page.get_by_role("#ArrowDropDownIcon")


        self.user_licensed_toggle=page.locator("//p[text()='Licensed']/following::div[@role='switch'][1]")
        # ========== Role ==========
        self.role_dropdown = page.get_by_role("combobox").filter(has_text="Select role")
        self.role_analyst = page.get_by_role("option", name="Analyst", exact=True)

        # ========== Team ==========
        self.team_dropdown = page.get_by_role("combobox").filter(has_text="Select team")
        self.team_alpha = page.get_by_text("Team Alpha")
        self.licensed_toggle = page.locator("#general-tab-licensed-toggle")
        self.personalised_toggle = page.locator("#general-tab-personalized-insights-toggle")


        # ========== Save ==========
        self.save_button = page.get_by_role("button", name="Save")
        self.save_and_proceed_button = page.get_by_role("button", name="Save & proceed")

        # ========== Toast Messages ==========
        self.user_added_msg = page.get_by_text("User Added")
        self.user_deleted_msg = page.get_by_text("User Deleted")

        # ========== User Row ==========
        self.user_email_text = page.get_by_text("hari1@gmail.com")
        self.user_row_checkbox = page.get_by_role("row", name="User Profile Hari M hari1@").get_by_role("checkbox")

        self.user_row_action_btn = page.get_by_role("row", name="User Profile Hari M hari1@").locator("button")

        # ========== Edit User ==========
        self.edit_user_option = page.get_by_text("Edit user")

        # ========== Tabs ==========
        self.general_tab = page.get_by_role("tab", name="General")

        # ========== Delete ==========
        self.more_actions_btn = page.get_by_role("button").nth(4)
        self.delete_option = page.get_by_text("Delete")
        self.confirm_delete_button = page.get_by_role("button", name="Delete")

        # ========== Overlay / Backdrop ==========
        self.backdrop = page.locator(".MuiBackdrop-root.MuiBackdrop-invisible")


        # ========== Users list ==========
        self.users_search_input = page.locator("#users-search-input")


    # -------- METHODS --------
    async def validate_users_page_options(self):
        print("users")
        await self.user_nav_button.click()
        await self.page.wait_for_timeout(3000)  # 20 seconds
        await self.user_search_field.is_visible()
        await self.user_filter_icon.is_visible()
        await self.user_edit_icon.is_visible()
        await self.user_adduser_button.is_visible()
        await self.verify_users_table_columns()
        print("users table_columns")


    async def verify_users_table_columns(self):
        columns = ["Name", "License", "2FA", "Personalized Insights", "Role", "Team", "Last login1"]
        for columnname in columns:
            await self.page.locator(f"th:has-text('{columnname}')").is_visible()
            print(columnname)

    async def verify_adduser_fields(self):
        await self.users_adduser_button.click()
        await self.page.wait_for_timeout(2000)  # 20 seconds

    async def fill_user_details(self,
                                first_name: str,
                                last_name: str,
                                email: str,
                                title: str,
                                phone: str
                                ):
        await self.user_first_name.fill(first_name)
        await self.user_last_name.fill(last_name)
        await self.user_email.fill(email)
        await self.user_title.fill(title)
        await self.user_phone.fill(phone)

        # Select language
        await self.select_user_langugae_dropdown()
        # Select Use Case
        await self.select_user_usecases_dropdown()

        # Select licensed_toggle
        await self.enable_licensed_toggle()
        # Select Team
        await self.select_team_dropdown()

        # Select Role
        await self.select_user_role_dropdown()
        #personalised_toggle
        await self.personalised_toggle.click()

        # # Toggle Licensed
        # if licensed:
        #     if not await self.licensed_toggle.is_checked():
        #         await self.licensed_toggle.check()
        # else:
        #     if await self.licensed_toggle.is_checked():
        #         await self.licensed_toggle.uncheck()

        # Save should be enabled now
        await expect(self.save_button).to_be_enabled()
        await self.save_button.click()

    # ==================================================
    # SAVE USER
    # ==================================================

    async def select_user_langugae_dropdown(self):
        await self.language_dropdown.click()
        await self.language_option_english.click()

    async def enable_licensed_toggle(self):
        if await self.licensed_toggle.get_attribute("aria-checked") == "false":
            await self.licensed_toggle.click()

    async def select_user_usecases_dropdown(self):
        await self.use_cases_dropdown.click()
        await self.use_case_mmx.click()
        await self.page.wait_for_timeout(2000)  # 20 seconds


    async def select_user_role_dropdown(self):
        await self.role_dropdown.click()
        await self.role_analyst.click()

    async def select_team_dropdown(self):
        await self.team_dropdown.click()
        await self.team_alpha.click()

    async def select_personalised_toggle(self):
        if await self.personalised_toggle.get_attribute("aria-checked") == "false":
            await self.personalised_toggle.click()

    async def verify_user_search(self,first_name: str):
        await self.users_search_input.fill(first_name)
