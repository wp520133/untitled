from selenium.webdriver.common.by import By
import page
from base.base import Base
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
