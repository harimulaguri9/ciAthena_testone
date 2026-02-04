import allure

from ciathena.pages.BasePage import BasePage
from playwright.async_api import Page


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.SSO_signin_button=page.get_by_text("Sign in with Microsoft")
        self.sso_email_input = page.locator("#i0116")
        self.sso_password_input =  page.locator("//input[@placeholder='Password']")
        # placeholder = "username@domain.ai"
        self.sso_signin_button = page.locator("#idSIButton9")
        self.email_input = page.locator("//input[@placeholder='username@domain.ai']")
        self.signin_button =page.locator("//button[normalize-space()='Sign in']")
        self.next_button = page.get_by_role("button", name="Next")
        self.password_input =  page.locator("//input[@placeholder='Enter password']")
        self.phone_number_button=page.get_by_role("button", name="Text +XX XXXXXXXX73")
        self.verify_button=page.get_by_role("button", name="Verify")
        self.yes_button=page.get_by_role("button", name="Yes")
        self.welcome_text=page.locator("#welcome-prefix")

    async def login_with_email_password(self):
        await self.email_input.fill("harimulaguri9@gmail.com")
        await self.page.wait_for_timeout(2000)
        await self.signin_button.click()
        await self.page.wait_for_timeout(2000)
        await self.password_input.wait_for(state="visible")
        await self.page.wait_for_timeout(2000)
        await self.password_input.fill("Android@123")
        await self.page.wait_for_timeout(2000)
        await self.signin_button.click()
        await self.page.wait_for_timeout(5000)

    async def login_with_sso_email(self):
        await self.email_input.fill("hari.mulaguri@customerinsights.ai")
        await self.signin_button.click()
        await self.page.wait_for_timeout(5000)
        await self.sso_email_input.wait_for(state="visible")
        await self.sso_email_input.fill("hari.mulaguri@customerinsights.ai")
        await self.next_button.click()
        await self.sso_password_input.wait_for(state="visible")
        await self.sso_password_input.fill("Android@123")
        await self.sso_signin_button.click()
        await self.phone_number_button.wait_for(state="visible")
        await self.phone_number_button.click()
        await self.page.wait_for_timeout(20000)
        await self.verify_button.click()
        await self.page.wait_for_timeout(5000)
