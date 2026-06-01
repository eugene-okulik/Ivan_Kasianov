import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(3)
    chrome_driver.set_window_size(1920, 1080)
    return chrome_driver


def test_add_to_cart_2(driver):
    driver.get("http://testshop.qa-practice.com/")
    desk = driver.find_element(
        By.CSS_SELECTOR, '[alt="Customizable Desk"]'
    )
    cart_button = driver.find_element(
        By.CSS_SELECTOR, '[title="Shopping cart"]'
    )
    actions = ActionChains(driver)
    actions.move_to_element(desk)
    actions.move_to_element(cart_button)
    actions.click()
    actions.perform()
    assert "Customizable Desk" in driver.find_element(
        By.CLASS_NAME, "product_display_name"
    ).text
