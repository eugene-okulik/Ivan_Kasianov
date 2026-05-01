import requests

from homework_22.test_api_ikasianov.endpoints.endpoint import Endpoint


class GetObject(Endpoint):
    def get_one_object(self, new_object):
        self.new_object = new_object
        self.response = requests.get(f"{self.url}/{self.new_object}")
        self.response_json = self.response.json()
        return self.response
