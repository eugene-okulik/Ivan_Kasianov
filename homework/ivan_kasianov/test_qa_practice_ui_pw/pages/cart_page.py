from playwright.sync_api import expect
from test_qa_practice_ui_pw.pages.locators import cart_locators as cart_loc
from test_qa_practice_ui_pw.pages.base_page import BasePage
from test_qa_practice_ui_pw.utils.test_data import expected_property as ex_prop
from test_qa_practice_ui_pw.utils.test_data import expected_value as ex_value


class CartPage(BasePage):
    page_url = "/shop/cart"

    def check_cart_empty_text(self, text):
        self.verify_element_text(cart_loc.banner_loc, text)

    def check_phone_number_is_correct(self, text):
        self.verify_element_text(cart_loc.phone_number_loc, text)

    def hover_to_button(self):
        button_login = self.find(cart_loc.button_login)
        button_login.hover()
        return button_login

    def check_button_color_is_correct(self, button_color):
        expect(button_color).to_have_css(ex_prop, ex_value)
