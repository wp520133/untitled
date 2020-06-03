from selenium.webdriver.support.wait import WebDriverWait
import time


class Base:
    def __init__(self, driver):
        self.driver = driver

    # 查找元素方法
    def base_find_element(self, loc, timeout=30, poll_frequency=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).until(
            lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 输入方法
    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)

    # 获取文本方法
    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    # 获取value的属性方法
    def base_get_value(self, loc):
        # 使用get_attribute获取指定的元素值
        self.base_find_element(loc).get_attribute("value")

    # 获取截图
    def base_get_image(self):
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))

    # 判断元素是否存在
    def base_element_is_exist(self,loc):
        try:
            self.base_find_element(loc,timeout=2)
            return True # 代表元素存在
        except:
            return False # 代表元素不存在