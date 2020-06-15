import unittest
from page.page_clac import PageClac
from parameterized import parameterized
from tools.read_txt import read_txt
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

    @parameterized.expand(read_txt("data.txt"))
    def test_add_clac(self, username, password, captcha_code,success):
        self.clac.login(username, password, captcha_code)
        if success:
            try:
                # 断言是否登录成功,如果是点击退出,如果不是,截图
                self.assertTrue(self.clac.page_is_login_success())
                # 点击退出
                self.clac.page_login_out()
                try:
                    # 断言是否退出成功
                    self.assertTrue(self.clac.page_is_login_out_success())
                except:
                    self.clac.base_get_image()
                self.clac.page_login_click()
            except:
                # 获取不是登录成功的截图
                self.clac.base_get_image()
        else:
            msg=self.clac.page_login_username_null()
            msg2=self.clac.page_login_password_null()
            try:
                self.assertEqual(msg,"请输入会员登录名称！") or self.assertEqual(msg2,"请输入密码！")
            except:
                self.clac.base_get_image()


if __name__ == '__main__':
    pytest.main()
