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


@pytest.mark.parametrize("body", test_body_objects)
def test_creation_an_object(
    create_object_endpoint,
    body,
    before_and_after_test
):
    create_object_endpoint.create_new_object(body)
    create_object_endpoint.check_response_status_code_is_200()
    create_object_endpoint.check_response_name_is_correct(body["name"])
    create_object_endpoint.check_response_color_is_correct(body["color"])
    create_object_endpoint.check_response_size_is_correct(body["size"])


def test_get_all_objects(get_objects_endpoint, before_and_after_test):
    get_objects_endpoint.get_all_objects()
    get_objects_endpoint.check_response_status_code_is_200()
    get_objects_endpoint.check_response_data_length_is_correct()


def test_get_one_object(
    get_one_object_endpoint,
    get_object_id,
    before_and_after_test
):
    get_one_object_endpoint.get_one_object(
        get_object_id
    )
    get_one_object_endpoint.check_response_status_code_is_200()
    get_one_object_endpoint.check_response_object_id_is_correct(
        get_object_id
    )


def test_put_object(
    update_object_endpoint,
    get_object_id,
    test_body_object_put_update,
    before_and_after_test
):
    update_object_endpoint.make_changes_in_object(
        test_body_object_put_update,
        get_object_id
    )
    update_object_endpoint.check_response_status_code_is_200()
    update_object_endpoint.check_response_color_is_correct(
        test_body_object_put_update["data"]["color"]
    )
    update_object_endpoint.check_response_size_is_correct(
        test_body_object_put_update["data"]["size"]
    )
    update_object_endpoint.check_response_name_is_correct(
        test_body_object_put_update["data"]["name"]
    )


def test_patch_object(
    patch_object_endpoint,
    get_object_id,
    test_body_object_patch_update,
    before_and_after_test
):
    patch_object_endpoint.patch_object(
        test_body_object_patch_update,
        get_object_id
    )
    patch_object_endpoint.check_response_status_code_is_200()
    patch_object_endpoint.check_response_size_upd_is_correct(
        test_body_object_patch_update["data"]["size"]
    )
    patch_object_endpoint.check_response_name_is_correct(
        test_body_object_patch_update["data"]["name"]
    )
    patch_object_endpoint.check_response_color_is_correct(
        test_body_object_patch_update["data"]["color"]
    )


def test_delete_object(
    delete_object_endpoint,
    get_object_id,
    test_body_object,
    before_and_after_test
):
    delete_object_endpoint.delete_object(
        get_object_id
    )
    delete_object_endpoint.check_response_status_code_is_200()
    delete_object_endpoint.check_delete_message_is_correct(
        get_object_id
    )
