import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(5)
    chrome_driver.set_window_size(1920, 1080)
    return chrome_driver


def test_add_to_cart(driver):
    driver.get("http://testshop.qa-practice.com/")
    product = driver.find_element(
        By.CSS_SELECTOR, '[alt="Customizable Desk"]'
    )
    (ActionChains(driver)
     .key_down(Keys.COMMAND)
     .click(product)
     .key_up(Keys.COMMAND)
     .perform())
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    button_add_to_card = driver.find_element(
        By.ID, "add_to_cart"
    )
    button_add_to_card.click()
    button_continue_shopping = driver.find_element(
        By.CLASS_NAME, "btn-secondary"
    )
    button_continue_shopping.click()
    wait_second = WebDriverWait(driver, 5)
    wait_second.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".my_cart_quantity"), "1"
        )
    )
    driver.close()
    driver.switch_to.window(tabs[0])
    button_card = driver.find_elements(
        By.CLASS_NAME, "o_wsale_my_cart"
    )
    button_card[0].click()
    wait = WebDriverWait(driver, 5)
    wait.until(
        EC.text_to_be_present_in_element((
            By.CLASS_NAME,
            "d-inline"
        ),
            "Customizable Desk (Steel, White)"
        )
    )
    assert "Customizable Desk" in driver.find_element(
        By.CLASS_NAME, "d-inline"
    ).text
