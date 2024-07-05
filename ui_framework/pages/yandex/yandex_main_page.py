from selenium.webdriver.common.by import By

from ui_framework.pages.base_page import BasePage


class YandexMainPage(BasePage):
    """Class for main yandex's page"""
    @property
    def search_input(self):
        return self.driver.find_element(By.XPATH, '//input[@class = "arrow__input mini-suggest__input"]')

    @property
    def search_suggestions_popup(self):
        return self.driver.find_element(By.XPATH, '//ul[@class="mini-suggest__popup-content"]')

