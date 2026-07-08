def test_cart_is_empty(cart_page):
    cart_page.open_page()
    cart_page.check_cart_empty_text("Your cart is empty!")


def test_support_number(cart_page):
    cart_page.open_page()
    cart_page.check_phone_number_is_correct("+1 555-555-5556")


def test_check_button_login_background_color(cart_page):
    cart_page.open_page()
    color_on_hover = cart_page.hover_to_button()
    cart_page.check_button_color_is_correct(color_on_hover)
