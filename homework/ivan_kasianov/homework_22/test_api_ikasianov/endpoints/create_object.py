import requests
import allure

from homework_22.test_api_ikasianov.endpoints.endpoint import Endpoint


class CreateObject(Endpoint):
    @allure.step("Create new object")
    def create_new_object(self, body):
        self.response = requests.post(
            self.url,
            json=body)

        self.response_json = self.response.json()
        return self.response

    def returned_object_id(self):
        return self.response_json["id"]
