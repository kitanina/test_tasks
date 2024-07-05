class Pages:
    """ Base class for all pages."""

    def __init__(self, driver, url_manager):
        self.driver = driver
        self.url_manager = url_manager


class YandexPages(Pages):
    """ Class for Yandex pages."""

    def yadex_search_page(self):
        self.url_manager.yandex_search_page()
        TODO: "do the returnn"
