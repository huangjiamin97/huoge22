from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time


class Test_cookie():
    def setup(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9333"
        self.driver = webdriver.Chrome(options=options)
        self.vars = {}

        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    def teardown(self):
        # self.driver.quit()
        pass


    def test_driver(self):
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame')

        print(self.driver.get_cookies())


        time.sleep(3)
