import logging
import time

from selenium.common import TimeoutException


class BasePage:
    """ Default class for any web page interactions"""
    def __init__(self, browser_driver):
        self.driver = browser_driver

    def refresh(self):
        self.driver.refresh()
        time.sleep(4)

    def back(self):
        self.driver.back()

    def get_current_url(self):
        return self.driver.current_url

    def open_url(self, url):
        return self.driver.get(url)

    def close_window(self):
        return self.driver.close()

    def js_click(self, element):
        try:
            self.driver.execute_script("arguments[0].click();", element)
        except TimeoutException:
            print(f"Element {element} not clickable or not found on the page.")




