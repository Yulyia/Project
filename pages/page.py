import time

from selenium.webdriver.common.keys import Keys

from locators.locator import MainPageLocators


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.timeout = 30


class MainPage(BasePage):

    def set_email(self):
        emailElement = self.driver.find_element(*MainPageLocators.main_game_button)
        emailElement.send_keys("Limon")
        emailElement.send_keys(Keys.ENTER)
        time.sleep(3)

