from test_qa_practice_ui_pw.utils.helpers import sorted_desk_titles


def test_product_list_is_not_empty(desks_page):
    desks_page.open_page()
    desks_page.check_desks_on_page()


def test_all_products_have_titles(desks_page):
    desks_page.open_page()
    titles = desks_page.find_desks_titles_locators()
    desks_page.check_all_titles(titles)


def test_sort_by_name(desks_page):
    desks_page.open_page()
    initial_titles = desks_page.find_desks_titles_texts()
    expected_titles = sorted_desk_titles(initial_titles)
    desks_page.select_sort_by_name_a_z()
    actual_titles = desks_page.find_desks_titles_locators()
    desks_page.check_titles_are_sorted(actual_titles, expected_titles)
