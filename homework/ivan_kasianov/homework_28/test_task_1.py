from playwright.sync_api import Page, expect


def test_get_by_role(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    link = page.get_by_role("link", name="Form Authentication")
    link.click()
    field_username = page.get_by_role("textbox", name="username")
    field_username.fill("tomsmith")
    field_password = page.get_by_role("textbox", name="password")
    field_password.fill(" SuperSecretPassword!")
    button_login = page.get_by_role("button", name="login")
    button_login.click()
    expect(page.get_by_role("heading", name=" Secure Area"))
