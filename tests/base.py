import unittest

from selenium import webdriver


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(desired_capabilities={"browserName": "chrome"})
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()


