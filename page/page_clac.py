from selenium.webdriver.common.by import By
import page
from base.base import Base
import time

class PageClac(Base):
    # 点击登录
    def page_login_click(self):
        self.base_click(page.login_click)

    # 输入用户名
    def page_login_username(self, username):
        self.base_input(page.login_username, username)

    # 输入密码
    def page_login_password(self, password):
        self.base_input(page.login_password, password)

    # 输入验证码
    def page_login_captcha_code(self, captcha_code):
        self.base_input(page.login_captcha_code, captcha_code)

    # 点击登录
    def page_login(self):
        self.base_click(page.login_button)

    # 点击退出
    def page_login_out(self):
        self.base_click(page.login_out)

    # 判断登录是否成功
    def page_is_login_success(self):
        return self.base_element_is_exist(page.login_out)

    # 判断退出成功
    def page_is_login_out_success(self):
        return self.base_element_is_exist(page.login_click)

    # 获取空用户名输入提示语
    def page_login_username_null(self):
        self.base_get_text(page.login_username_null)

    # 获取空密码输入提示语
    def page_login_password_null(self):
        self.base_get_text(page.login_password_null)
    """
        组装
    """
    def login(self,username,password,captcha_code):
        self.page_login_click()
        self.page_login_username(username)
        self.page_login_password(password)
        self.page_login_captcha_code(captcha_code)
        self.page_login()
        time.sleep(3)
