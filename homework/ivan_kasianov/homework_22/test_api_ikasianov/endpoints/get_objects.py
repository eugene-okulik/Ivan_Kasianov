import allure
import requests
from homework_22.test_api_ikasianov.endpoints.endpoint import Endpoint


class GetObjects(Endpoint):
    def get_all_objects(self):
        self.response = requests.get(self.url)
        self.response_json = self.response.json()
        return self.response_json

    @allure.step("Checking that all objects have been received")
    def check_response_data_length_is_correct(self):
        assert (
            len(self.response_json["data"]) != 0
        ), "The objects have not yet been created"
