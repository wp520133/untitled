import unittest
from page.page_clac import PageClac
from parameterized import parameterized
from tools.read_txt import read_txt
from base.get_driver import GetDriver
import pytest
import allure

class TestClac(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.clac = PageClac(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # @parameterized.expand(read_txt("data.txt"))
    @allure.step(title="计算")
    def test_add_clac(self):
        self.clac.page_add_clac(1, 2)


if __name__ == '__main__':
    pytest.main()
