import requests


def all_objects():
    response = requests.get("http://objapi.course.qa-practice.com/object")
    assert response.status_code == 200, (
        f"Expected 200, "
        f"but got {response.status_code}"
    )
    assert len(response.json()["data"]) != 0, (
        "The objects have not yet been created"
    )


def one_object():
    object_id = new_an_object()
    response = requests.get(
        f"http://objapi.course.qa-practice.com/object/{object_id}"
    )
    assert response.status_code == 200, (
        f"Expected 200, "
        f"but got {response.status_code}"
    )
    assert response.json()["id"] == object_id, (
        "No object exists with that id"
    )


def creation_an_object():
    name = "First object"
    body = {
        "name": name,
        "data": {
            "color": "black",
            "size": "small"
        }
    }
    response = requests.post(
        "http://objapi.course.qa-practice.com/object", json=body)
    assert response.status_code == 200, "The object has not been created"
    assert response.json()["name"] == "First object", (
        f"The object is not named {name}"
    )


def new_an_object():
    name = "First object"
    body = {
        "name": name,
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
    return response.json()["id"]


def clear(object_id):
    response = requests.delete(
        f"http://objapi.course.qa-practice.com/object/{object_id}"
    )
    assert response.status_code == 200, (
        "The object has not been deleted"
    )


def put_an_object():
    object_id = new_an_object()
    body = {
        "name": "First object",
        "data": {
            "color": "black-UPD",
            "size": "small-UPD"
        }
    }
    response = requests.put(
        f"http://objapi.course.qa-practice.com/object/{object_id}",
        json=body
    )
    assert response.status_code == 200, (
        "The object has not been updated"
    )
    assert response.json()["data"]["color"] == "black-UPD", (
        "The color has not been updated"
    )
    assert response.json()["data"]["size"] == "small-UPD", (
        "The size has not been updated"
    )
    clear(object_id)


def patch_an_object():
    object_id = new_an_object()
    body = {
        "name": "First object",
        "data": {
            "size": "small-UPD"
        }
    }
    response = requests.patch(
        f"http://objapi.course.qa-practice.com/object/{object_id}",
        json=body
    )
    assert response.status_code == 200, (
        "The object has not been updated"
    )
    assert response.json()["data"]["size"] == "small-UPD", (
        "The size has not been updated"
    )
    clear(object_id)


def delete_an_object():
    object_id = new_an_object()
    response = requests.delete(
        f"http://objapi.course.qa-practice.com/object/{object_id}"
    )
    assert response.status_code == 200, (
        "The object has not been deleted"
    )


all_objects()
one_object()
creation_an_object()
new_an_object()
put_an_object()
patch_an_object()
delete_an_object()
