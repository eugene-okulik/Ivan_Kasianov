import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(10)
    chrome_driver.set_window_size(1920, 1080)
    return chrome_driver


def test_id_name(driver):
    input_data = "Hello"
    driver.get("https://www.qa-practice.com/elements/input/simple")
    text_string = driver.find_element(By.ID, "id_text_string")
    text_string.send_keys(input_data)
    text_string.submit()
    result_text = driver.find_element(By.ID, "result-text")
    assert result_text.text == input_data
    print(input_data)


def test_the_form(driver):
    first_name_text = "Ivan"
    last_name_text = "Ivanov"
    email_text = "ivanov@gmail.com"
    mobile_number_text = "1234567890"
    address_text = "Washington str, 10"
    driver.get("https://demoqa.com/automation-practice-form")
    firs_name = driver.find_element(By.ID, "firstName")
    last_name = driver.find_element(By.ID, "lastName")
    email = driver.find_element(By.ID, "userEmail")
    gender = driver.find_element(By.CSS_SELECTOR, '[value="Male"]')
    mobile_number = driver.find_element(By.ID, "userNumber")
    date_of_birth = driver.find_element(By.ID, "dateOfBirthInput")
    firs_name.send_keys(first_name_text)
    last_name.send_keys(last_name_text)
    email.send_keys(email_text)
    gender.click()
    mobile_number.send_keys(mobile_number_text)
    date_of_birth.click()
    month_of_birth_list = driver.find_element(
        By.CSS_SELECTOR, ".react-datepicker__month-select"
    )
    dropdown_month = Select(month_of_birth_list)
    dropdown_month.select_by_value("0")
    year_of_birth = driver.find_element(
        By.CSS_SELECTOR, ".react-datepicker__year-select"
    )
    dropdown_year = Select(year_of_birth)
    dropdown_year.select_by_value("1989")
    day_of_birth = driver.find_element(
        By.CSS_SELECTOR, '[aria-label="Choose Friday, January 20th, 1989"]'
    )
    day_of_birth.click()
    subjects_input = driver.find_element(
        By.ID, "subjectsInput"
    )
    subjects_input.send_keys("comp")
    subjects_variant_1 = driver.find_element(
        By.CLASS_NAME, "subjects-auto-complete__menu"
    )
    subjects_variant_1.click()
    subjects_input.send_keys("eco")
    subjects_variant_2 = driver.find_element(
        By.CLASS_NAME, "subjects-auto-complete__menu"
    )
    subjects_variant_2.click()
    hobbies_checkbox = driver.find_element(
        By.ID, "hobbies-checkbox-1"
    )
    hobbies_checkbox.click()
    current_address_input = driver.find_element(
        By.ID, "currentAddress"
    )
    current_address_input.send_keys(address_text)
    select_state = driver.find_element(
        By.ID, "react-select-3-input"
    )
    select_state.send_keys("NCR")
    select_state.send_keys(Keys.ENTER)
    select_city = driver.find_element(
        By.ID, "react-select-4-input"
    )
    select_city.send_keys("Del")
    select_city.send_keys(Keys.ENTER)
    button_submit = driver.find_element(
        By.ID, "submit"
    )
    button_submit.click()
    table = driver.find_element(By.CLASS_NAME, "table")
    table_cells = table.find_elements(By.TAG_NAME, "td")
    dict_elements = {}
    for i in range(0, len(table_cells), 2):
        key = table_cells[i].text
        value = table_cells[i + 1].text
        dict_elements[key] = value
    print(dict_elements)
    # Не дочитал задание и выполнил с проверками, решил уже не удалять
    assert (
        dict_elements["Student Name"]
        == f"{first_name_text} {last_name_text}"
    )
    assert dict_elements["Student Email"] == f"{email_text}"
    assert dict_elements["Gender"] == "Male"
    assert dict_elements["Mobile"] == f"{mobile_number_text}"
    assert dict_elements["Date of Birth"] == "20 January,1989"
    assert dict_elements["Subjects"] == "Computer Science, Economics"
    assert dict_elements["Hobbies"] == "Sports"
    assert dict_elements["Address"] == f"{address_text}"
    assert dict_elements["State and City"] == "NCR Delhi"


def test_choose_language(driver):
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    select = driver.find_element(By.NAME, "choose_language")
    dropdown = Select(select)
    dropdown.select_by_value("1")
    submit_button = driver.find_element(By.ID, "submit-id-submit")
    submit_button.click()
    result = driver.find_element(By.ID, "result-text")
    result_text = result.text
    assert result_text == "Python"


def test_wait_text(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    button = driver.find_element(By.TAG_NAME, "button")
    button.click()
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.text_to_be_present_in_element(
            (By.ID, "finish"),
            "Hello World!")
    )
