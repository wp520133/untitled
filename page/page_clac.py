from selenium.webdriver.common.by import By
import page
from base.base import Base
<<<<<<< HEAD
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
        self.page_login_out()
=======
import allure

class PageClac(Base):
    # 点击数字
    num = 12

    @allure.step(title="点击数字")
    def page_click_num(self, num):
        for n in str(num):
            loc = By.CSS_SELECTOR, "#simple{}".format(n)
            self.base_click(loc)
        # self.base_click(page.clac_num)

    # 点击加号
    @allure.step(title="点击加号")
    def page_click_add(self):
        self.base_click(page.clac_add)

    # 点击等号
    @allure.step(title="点击等号")
    def page_click_eq(self):
        self.base_click(page.clac_eq)

    # 获取结果方法
    @allure.step(title="获取结果")
    def page_click_result(self):
        self.base_click(page.clac_result)

    # 点击清屏
    def page_click_clear(self):
        self.base_click(page.clac_clear)

    # 组装业务方法
    def page_add_clac(self, a, b):
        self.page_click_num(a)
        self.page_click_add()
        self.page_click_num(b)
        self.page_click_eq()
>>>>>>> 83eb904d582eaa572a7943167d71ce2c55cfa4b6
