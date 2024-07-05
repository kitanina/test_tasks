import pytest
from selenium import webdriver

from config.config import URL_YANDEX
from ui_framework.pages.yandex.yandex_main_page import YandexMainPage
from ui_framework.url_manager.url_manager import YandexURLManager


@pytest.fixture(name='browser')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def get_yandex_search_page(browser):
    driver = browser
    yandex_url_manager = YandexURLManager(driver, URL_YANDEX)
    yandex_url_manager.yandex_search_page()
    return YandexMainPage(browser)
