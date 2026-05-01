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
