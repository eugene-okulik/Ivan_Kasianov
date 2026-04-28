import allure
import requests

from homework_22.test_api_ikasianov.endpoints.endpoint import Endpoint


class UpdateObject(Endpoint):

    @allure.step("Updating object data")
    def make_changes_in_object(self, body, new_object):
        self.response = requests.put(
            f"{self.url}/{new_object}",
            json=body
        )
        self.response_json = self.response.json()
        return self.response

    @allure.step("Check that object color is black-UPD")
    def check_response_color_is_correct(self, color):
        assert (
            self.response_json["data"]["color"] == color
        ), "The color has not been updated"

    @allure.step("Check that object size is small-UPD")
    def check_response_size_is_correct(self, size):
        assert (
            self.response_json["data"]["size"] == size
        ), "The size has not been updated"
