import allure
import requests

from homework_22.test_api_ikasianov.endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):
    def delete_object(self, new_object):
        self.response = requests.delete(f"{self.url}/{new_object}")
        self.response_text = self.response.text
        return self.response

    @allure.step("Check the response code")
    def check_delete_message_is_correct(self, new_object):
        expected_message = f"Object with id {new_object} successfully deleted"
        assert self.response_text == expected_message
