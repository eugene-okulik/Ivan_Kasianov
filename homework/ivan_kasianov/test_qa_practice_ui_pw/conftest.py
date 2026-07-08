import pytest
from test_qa_practice_ui_pw.pages.cart_page import CartPage
from test_qa_practice_ui_pw.pages.desks_page import DesksPage
from test_qa_practice_ui_pw.pages.product_page import ProductPage


@pytest.fixture
def cart_page(page):
    return CartPage(page)


@pytest.fixture
def desks_page(page):
    return DesksPage(page)


@pytest.fixture
def product_page(page):
    return ProductPage(page)
