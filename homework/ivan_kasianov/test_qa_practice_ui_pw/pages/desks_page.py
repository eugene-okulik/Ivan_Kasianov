from playwright.sync_api import expect
from test_qa_practice_ui_pw.pages.base_page import BasePage
from test_qa_practice_ui_pw.pages.locators import desks_locator as DL
from test_qa_practice_ui_pw.utils import test_data as TL


class DesksPage(BasePage):
    page_url = "/shop/category/desks-1"

    def check_desks_on_page(self):
        desks = self.find(DL.desks_loc)
        expect(desks).to_have_count(9)

    def find_desks_titles_locators(self):
        return self.find(DL.desks_titles_loc)

    def find_desks_titles_texts(self):
        return self.find(DL.desks_titles_loc).all_inner_texts()

    def check_all_titles(self, actual_titles):
        expect(actual_titles).to_have_text(TL.desk_titles)

    def select_sort_by_name_a_z(self):
        dropdown_button = self.find(DL.dropdown_button_loc)
        dropdown_button.click()
        button_sort_list = self.find(DL.dropdown_button_list_loc)
        button_sort_list.click()

    def check_titles_are_sorted(self, actual_titles, expected_titles):
        expect(actual_titles).to_have_text(expected_titles)
