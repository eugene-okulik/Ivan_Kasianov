import requests
import pytest

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
        f"Expected 200, "
        f"but got {response.status_code}"
    )
    object_id = response.json()["id"]
    yield object_id
    response = requests.delete(
        f"http://objapi.course.qa-practice.com/object/{object_id}"
    )
    assert response.status_code in [200, 204, 404], (
        "The object has not been deleted"
    )


@pytest.mark.critical
def test_get_all_objects(start_and_finish_test_run, before_and_after_test):
    response = requests.get("http://objapi.course.qa-practice.com/object")
    assert response.status_code == 200, (
        f"Expected 200, "
        f"but got {response.status_code}"
    )
    assert len(response.json()["data"]) != 0, (
        "The objects have not yet been created"
    )


@pytest.mark.medium
def test_get_one_object(new_object, before_and_after_test):
    response = requests.get(
        f"http://objapi.course.qa-practice.com/object/{new_object}"
    )
    assert response.status_code == 200, (
        f"Expected 200, "
        f"but got {response.status_code}"
    )
    assert response.json()["id"] == new_object, (
        "No object exists with that id"
    )


@pytest.mark.parametrize("body, expected_name", test_body_objects)
def test_creation_an_object(body, expected_name):
    response = requests.post(
        "http://objapi.course.qa-practice.com/object", json=body)
    assert response.status_code == 200, "The object has not been created"
    assert response.json()["name"] == expected_name, (
        f"The object is not named {expected_name}"
    )


def test_put_an_object(before_and_after_test, new_object):
    body = {
        "name": "First object",
        "data": {
            "color": "black-UPD",
            "size": "small-UPD"
        }
    }
    response = requests.put(
        f"http://objapi.course.qa-practice.com/object/{new_object}",
        json=body
    )
    assert response.status_code == 200, (
        "The object has not been updated"
    )
    assert response.json()["data"]["color"] == body["data"]["color"], (
        "The color has not been updated"
    )
    assert response.json()["data"]["size"] == body["data"]["size"], (
        "The size has not been updated"
    )


def test_patch_an_object(before_and_after_test, new_object):
    body = {
        "name": "First object",
        "data": {
            "size": "small-UPD"
        }
    }
    response = requests.patch(
        f"http://objapi.course.qa-practice.com/object/{new_object}",
        json=body
    )
    assert response.status_code == 200, (
        "The object has not been updated"
    )
    assert response.json()["data"]["size"] == body['data']['size'], (
        "The size has not been updated"
    )


def test_delete_an_object(before_and_after_test, new_object):
    response = requests.delete(
        f"http://objapi.course.qa-practice.com/object/{new_object}"
    )
    assert response.status_code == 200, (
        "The object has not been deleted"
    )
