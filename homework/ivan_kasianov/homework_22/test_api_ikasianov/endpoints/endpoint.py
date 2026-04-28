import allure


class Endpoint:
    url = "http://objapi.course.qa-practice.com/object"
    response = None
    response_json = None

    @allure.step("Checking that status code is 200")
    def check_response_status_code_is_200(self):
        assert self.response.status_code == 200, "Status code is not 200"
