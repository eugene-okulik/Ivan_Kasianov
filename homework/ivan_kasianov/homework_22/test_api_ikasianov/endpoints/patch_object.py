import requests

from homework_22.test_api_ikasianov.endpoints.endpoint import Endpoint


class PatchObject(Endpoint):
    def patch_object(self, body, new_object):
        self.response = requests.patch(f"{self.url}/{new_object}", json=body)
        self.response_json = self.response.json()
        return self.response
