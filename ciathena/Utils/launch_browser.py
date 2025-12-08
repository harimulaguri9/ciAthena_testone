from playwright.sync_api import expect, sync_playwright


def launch():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://ciathena-qa.customerinsights.ai")
        expect(page.get_by_text("Sign in with Microsoft")).to_be_visible(timeout=10000)
        page.get_by_text("Sign in with Microsoft").click()
