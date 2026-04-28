import allure
import requests

from homework_22.test_api_ikasianov.endpoints.endpoint import Endpoint


class GetObject(Endpoint):
    def get_one_object(self, new_object):
        self.new_object = new_object
        self.response = requests.get(f"{self.url}/{self.new_object}")
        self.response_json = self.response.json()
        return self.response

    @allure.step("Checking that object id is new_object")
    def check_response_object_id_is_correct(self, new_object):
        assert (
            self.response_json["id"] == new_object
        ), "No object exists with that id"
