import time

import pytest

from pages import page
from tests.base import BaseTest


class Test1(BaseTest):

    def test_1(self):
        self.driver.get("https://www.google.ru")
        main_page = page.MainPage(self.driver)
        main_page.set_email()
        assert False
