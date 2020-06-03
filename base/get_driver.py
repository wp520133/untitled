from selenium import webdriver
import page


class GetDriver:
    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Firefox()
            cls.driver.maximize_window()
            cls.driver.get(page.url)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            # 一个坑,需要做dirver归Num,实现单例
            cls.driver = None
