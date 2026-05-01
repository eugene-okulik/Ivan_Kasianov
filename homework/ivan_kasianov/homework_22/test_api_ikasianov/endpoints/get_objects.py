import requests
from homework_22.test_api_ikasianov.endpoints.endpoint import Endpoint


class GetObjects(Endpoint):
    def get_all_objects(self):
        self.response = requests.get(self.url)
        self.response_json = self.response.json()
        return self.response_json
