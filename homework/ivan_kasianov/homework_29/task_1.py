from playwright.sync_api import Page, expect, Dialog


def test_alert(page: Page):
    def confirm_alert(alert: Dialog):
        alert.accept()
    page.on("dialog", confirm_alert)
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    page.get_by_role("link", name="Click").click()
    expect(page.locator("div > p")).to_contain_text(["You selected", "Ok"])
