import unittest
from page.page_clac import PageClac
from parameterized import parameterized
from tools.read_txt import read_txt
from base.get_driver import GetDriver
import pytest
import allure


class TestClac(unittest.TestCase):
    driver = None
    str = "../data/data.txt"

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.clac = PageClac(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    @parameterized.expand(read_txt(str))
    def test_add_clac(self, username, password, captcha_code):
        self.clac.login(username, password, captcha_code)


if __name__ == '__main__':
    pytest.main()
