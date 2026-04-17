import requests
import pytest
import allure


test_body_objects = [
    (
        {
            "name": "First object_1",
            "data": {
                "color": "black",
                "size": "small"
            }
        },
        "First object_1"
    ),
    (
        {
            "name": "Second object_1",
            "data": {
                "color": "red",
                "size": "medium"
            }
        },
        "Second object_1"
    ),
    (
        {
            "name": "Third object_1",
            "data": {
                "color": "white",
                "size": "large"
            }
        },
        "Third object_1"
    ),
]


@pytest.fixture(scope="session")
def start_and_finish_test_run():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture()
def before_and_after_test():
    print("before test")
    yield
    print("after test")


@pytest.fixture()
def new_object():
    body = {
        "name": "Test first object",
        "data": {
            "color": "black",
            "size": "small"
        }
    }
    response = requests.post(
        "http://objapi.course.qa-practice.com/object", json=body)
    assert response.status_code == 200, (
        "Failed to create test data"
    )
    object_id = response.json()["id"]
    yield object_id
    response = requests.delete(
        f"http://objapi.course.qa-practice.com/object/{object_id}"
    )


@allure.feature("Objects")
@allure.story("Manipulate objects")
@allure.title("Получение всех объектов")
@pytest.mark.critical
def test_get_all_objects(start_and_finish_test_run, before_and_after_test):
    with allure.step("Get all objects"):
        response = requests.get("http://objapi.course.qa-practice.com/object")
    with allure.step("Checking that status code is 200"):
        assert response.status_code == 200, (
            f"Expected 200, "
            f"but got {response.status_code}"
        )
    with allure.step("Checking that all objects have been received"):
        assert len(response.json()["data"]) != 0, (
        "The objects have not yet been created"
        )


@allure.feature("Objects")
@allure.story("Manipulate objects")
@allure.title("Получение одного объекта по id")
@pytest.mark.medium
def test_get_one_object(new_object, before_and_after_test):
    with allure.step(f"Get one object with id {new_object}"):
        response = requests.get(
            f"http://objapi.course.qa-practice.com/object/{new_object}"
        )
    with allure.step(f"Checking that status code is 200"):
        assert response.status_code == 200, (
            f"Expected 200, "
            f"but got {response.status_code}"
        )
    with allure.step(f"Check that object id is {new_object}"):
        assert response.json()["id"] == new_object, (
            "No object exists with that id"
        )


@allure.feature("Objects")
@allure.story("Manipulate objects")
@allure.title("Создание одного объекта")
@pytest.mark.parametrize("body, expected_name", test_body_objects)
def test_creation_an_object(body, expected_name):
    with allure.step("Create an object"):
        response = requests.post(
            "http://objapi.course.qa-practice.com/object", json=body)
    with allure.step("Checking that status code is 200"):
        assert response.status_code == 200, "The object has not been created"
    with allure.step(f"Check that object name is {expected_name}"):
        assert response.json()["name"] == expected_name, (
            f"The object is not named {expected_name}"
        )


@allure.feature("Objects")
@allure.story("Manipulate objects")
@allure.title("Обновление данных объекта")
def test_put_an_object(before_and_after_test, new_object):
    with allure.step("Prepare test data"):
        body = {
            "name": "First object",
            "data": {
                "color": "black-UPD",
                "size": "small-UPD"
            }
        }
    with allure.step("Updating object data"):
        response = requests.put(
            f"http://objapi.course.qa-practice.com/object/{new_object}",
            json=body
        )
    with allure.step("Checking that status code is 200"):
        assert response.status_code == 200, (
            "The object has not been updated"
        )
    with allure.step("Check that object color is black-UPD"):
        assert response.json()["data"]["color"] == body["data"]["color"], (
            "The color has not been updated"
        )
    with allure.step("Check that object size is small-UPD"):
        assert response.json()["data"]["size"] == body["data"]["size"], (
            "The size has not been updated"
        )


@allure.feature("Objects")
@allure.story("Manipulate objects")
@allure.title("Обновление размера объекта")
def test_patch_an_object(before_and_after_test, new_object):
    with allure.step("Prepare test data"):
        body = {
            "name": "First object",
            "data": {
                "size": "small-UPD"
            }
        }
    with allure.step("Updating object size"):
        response = requests.patch(
            f"http://objapi.course.qa-practice.com/object/{new_object}",
            json=body
        )
    with allure.step("Checking that status code is 200"):
        assert response.status_code == 200, (
            "The object has not been updated"
        )
    with allure.step("Check that object size is small-UPD"):
        assert response.json()["data"]["size"] == body['data']['size'], (
            "The size has not been updated"
        )


@allure.feature("Objects")
@allure.story("Manipulate objects")
@allure.title("Удаление объекта")
def test_delete_an_object(before_and_after_test, new_object):
    with allure.step("Delete object"):
        response = requests.delete(
            f"http://objapi.course.qa-practice.com/object/{new_object}"
        )
    with allure.step("Checking that status code is 200"):
        assert response.status_code == 200, (
            "The object has not been deleted"
        )
