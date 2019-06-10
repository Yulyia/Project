import time

import pytest
from tests.base import BaseTest


class Test(BaseTest):
    def test_2(self):
        self.driver.get("https://selenium-python.readthedocs.io/")
        time.sleep(3)
        assert True

    def test_3(self):
        assert False

    def test_4(self):
        pytest.skip()
