import pytest

test_body_objects = [
    {
        "name": "First object_1",
        "data": {
            "color": "black",
            "size": "small"
        }
    },
    {
        "name": "Second object_1",
        "data": {
            "color": "red",
            "size": "medium"
        }
    },
    {
        "name": "Third object_1",
        "data": {
            "color": "white",
            "size": "large"
        }
    },
]

test_body_object = {
    "name": "First object",
    "data": {
        "color": "black",
        "size": "small"
    }
}

test_body_object_put_update = {
    "name": "First object",
    "data": {
        "color": "black-UPD",
        "size": "small-UPD"
    }
}

test_body_object_patch_update = {
    "name": "First object",
    "data": {
        "size": "small-UPD"
    }
}


@pytest.mark.parametrize("body", test_body_objects)
def test_creation_an_object(
    create_object_endpoint,
    body,
    before_and_after_test
):
    create_object_endpoint.create_new_object(body)
    create_object_endpoint.check_response_status_code_is_200()
    create_object_endpoint.check_response_name_is_correct(body["name"])


def test_get_all_objects(get_objects_endpoint, before_and_after_test):
    get_objects_endpoint.get_all_objects()
    get_objects_endpoint.check_response_status_code_is_200()
    get_objects_endpoint.check_response_data_length_is_correct()


def test_get_one_object(
    get_one_object_endpoint,
    create_object_endpoint,
    before_and_after_test
):
    create_object_endpoint.create_new_object(test_body_object)
    get_one_object_endpoint.get_one_object(
        create_object_endpoint.returned_object_id()
    )
    get_one_object_endpoint.check_response_status_code_is_200()
    get_one_object_endpoint.check_response_object_id_is_correct(
        create_object_endpoint.returned_object_id()
    )


def test_put_object(
    update_object_endpoint,
    create_object_endpoint,
    before_and_after_test
):
    create_object_endpoint.create_new_object(test_body_object)
    update_object_endpoint.make_changes_in_object(
        test_body_object_put_update,
        create_object_endpoint.returned_object_id()
    )
    update_object_endpoint.check_response_status_code_is_200()
    update_object_endpoint.check_response_color_is_correct(
        test_body_object_put_update["data"]["color"]
    )
    update_object_endpoint.check_response_size_is_correct(
        test_body_object_put_update["data"]["size"]
    )


def test_patch_object(
    patch_object_endpoint,
    create_object_endpoint,
    before_and_after_test
):
    create_object_endpoint.create_new_object(test_body_object)
    patch_object_endpoint.patch_object(
        test_body_object_patch_update,
        create_object_endpoint.returned_object_id()
    )
    patch_object_endpoint.check_response_status_code_is_200()
    patch_object_endpoint.check_response_size_upd_is_correct(
        test_body_object_patch_update["data"]["size"]
    )


def test_delete_object(
    delete_object_endpoint,
    create_object_endpoint,
    before_and_after_test
):
    create_object_endpoint.create_new_object(test_body_object)
    delete_object_endpoint.delete_object(
        create_object_endpoint.returned_object_id()
    )
    delete_object_endpoint.check_response_status_code_is_200()
    delete_object_endpoint.check_delete_message_is_correct(
        create_object_endpoint.returned_object_id()
    )
