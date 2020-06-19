import unittest
from page.page_clac import PageClac
from parameterized import parameterized
from tools.read_json import read_json
from base.get_driver import GetDriver
import pytest
import allure
import page


class TestClac(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.clac = PageClac(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    @parameterized.expand(read_json("data.json"))
    def test_add_clac(self, username, password, captcha_code,success):
        self.clac.login(username, password, captcha_code)
        if success:
            try:
                # 断言是否登录成功
                self.assertTrue(self.clac.page_is_login_success())
            except:
                self.clac.base_get_image()
            else:
                self.clac.page_login_out()
                try:
                    # 断言是否退出成功
                    self.assertTrue(self.clac.page_is_login_out_success())
                except:
                    self.clac.base_get_image()
                else:
                    self.clac.page_login_out()

        else:
            try:
                self.assertTrue(self.clac.page_is_login_success())
            except:
                self.clac.base_get_image()



if __name__ == '__main__':
    pytest.main()
