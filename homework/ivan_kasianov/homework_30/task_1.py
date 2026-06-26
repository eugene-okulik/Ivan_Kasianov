from playwright.sync_api import Page, expect, Route
import re
import json


def test_apple_API(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        product_name = body["body"]["digitalMat"][0]["familyTypes"][0]
        product_name["productName"] = "яблокофон 17 про"
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )
    page.route(re.compile("digital-mat"), handle_route)
    page.goto("https://www.apple.com/shop/buy-iphone")
    page.locator(".rf-hcard").locator("nth=0").click()
    title = page.locator("#rf-digitalmat-overlay-label-0").locator("nth=0")
    expect(title).to_have_text("яблокофон 17 про")
