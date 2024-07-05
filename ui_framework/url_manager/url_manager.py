class URLManager:
    """Base class for URL management in Selenium tests."""

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url


class YandexURLManager(URLManager):
    """Navigates to Yandex's main page."""

    def yandex_search_page(self):
        self.driver.get(self.url)
