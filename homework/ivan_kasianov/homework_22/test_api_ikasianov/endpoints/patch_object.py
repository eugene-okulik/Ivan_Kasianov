import allure
import requests

from homework_22.test_api_ikasianov.endpoints.endpoint import Endpoint


class PatchObject(Endpoint):
    def patch_object(self, body, new_object):
        self.response = requests.patch(f"{self.url}/{new_object}", json=body)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Check that object size is small-UPD")
    def check_response_size_upd_is_correct(self, size):
        assert (
            self.response_json["data"]["size"] == size
        ), "The size has not been updated"
