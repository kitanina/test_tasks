import pytest
from ui_framework.url_manager.url_manager import YandexURLManager
from config.config import URL_YANDEX


class YandexUIPlugin:
    """Class with fixtures to open web-pages"""

    @pytest.fixture()
    def get_yandex_search_page(self, browser):
        driver = browser
        yandex_url_manager = YandexURLManager(driver, URL_YANDEX)
        yandex_url_manager.yandex_search_page()
        return driver

