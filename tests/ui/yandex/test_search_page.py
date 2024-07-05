import pytest
from selenium.webdriver import Keys

def test_search_field(get_yandex_search_page):
    search_page = get_yandex_search_page
    search_input = search_page.search_input
    search_input.js_click(search_input)
    assert search_input.is_displayed()
    search_input.send_keys('ozon')
    suggest_table = search_page.search_suggestions_popup
    assert suggest_table.is_displayed()
    search_input.send_keys(Keys.ENTER)

