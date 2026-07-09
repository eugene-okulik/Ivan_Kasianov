from playwright.sync_api import expect
from test_qa_practice_ui_pw.pages.base_page import BasePage
from test_qa_practice_ui_pw.pages.locators import product_locators as PL
from test_qa_practice_ui_pw.utils.test_data import (
    expected_property as exp_bor_prop,
    expected_border_color as exp_bor_color)


class ProductPage(BasePage):
    page_url = "/shop/furn-9999-office-design-software-7?category=9"

    def check_product_name_on_page(self, text):
        self.verify_element_text(PL.product_name_loc, text)

    def check_add_to_cart(self):
        cart_quantity = self.find(PL.cart_quantity_loc)
        expect(cart_quantity).to_have_text("1")

    def add_product_to_cart(self):
        add_to_cart_button = self.find(PL.add_to_cart_button_loc)
        add_to_cart_button.click()

    def click_input(self):
        search_input = self.find(PL.search_input_loc)
        search_input.click()

    def check_search_input_highlight(self):
        search_input = self.find(PL.search_input_loc)
        expect(search_input).to_have_css(exp_bor_prop, exp_bor_color)
