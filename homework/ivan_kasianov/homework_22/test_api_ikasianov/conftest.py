import pytest
from homework_22.test_api_ikasianov.endpoints.create_object import CreateObject
from homework_22.test_api_ikasianov.endpoints.delete_object import DeleteObject
from homework_22.test_api_ikasianov.endpoints.get_objects import GetObjects
from homework_22.test_api_ikasianov.endpoints.patch_object import PatchObject
from homework_22.test_api_ikasianov.endpoints.update_object import UpdateObject
from homework_22.test_api_ikasianov.endpoints.get_object import GetObject


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def get_objects_endpoint():
    return GetObjects()


@pytest.fixture()
def get_one_object_endpoint():
    return GetObject()


@pytest.fixture()
def patch_object_endpoint():
    return PatchObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture(scope="session", autouse=True)
def start_and_finish_test_run():
    print("\n---------- Start testing ----------")
    yield
    print("---------- Testing completed ----------")


@pytest.fixture()
def before_and_after_test():
    print("\nBefore test")
    yield
    print("\nAfter test")
