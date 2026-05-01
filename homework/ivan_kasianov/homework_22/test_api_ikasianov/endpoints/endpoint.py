import allure


class Endpoint:
    url = "http://objapi.course.qa-practice.com/object"
    response = None
    response_json = None

    @allure.step("Checking that status code is 200")
    def check_response_status_code_is_200(self):
        assert self.response.status_code == 200, "Status code is not 200"

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

    @allure.step("Checking that all objects have been received")
    def check_response_data_length_is_correct(self):
        assert (
            len(self.response_json["data"]) != 0
        ), "The objects have not yet been created"

    @allure.step("Checking that object id is new_object")
    def check_response_object_id_is_correct(self, new_object):
        assert (
            self.response_json["id"] == new_object
        ), "No object exists with that id"

    @allure.step("Check that object name")
    def check_response_name_is_correct(self, name):
        assert (
            self.response_json["name"] == name
        ), "The object has not been created"
