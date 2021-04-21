from selenium import webdriver
import time

from selenium.webdriver.common.by import By


class Testdriver:
    def setup(self):

        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        self.driver.get('https://www.baidu.com/')



    def teardown(self):
        self.driver.quit()

    def test_driver(self):
        time.sleep(1)
        self.driver.find_element(By.ID,'kw').send_keys("123")
        time.sleep(2)


        self.driver.find_element(By.ID,"su").click()













# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(2)
# driver.get('https://www.taobao.com/')#模拟打开百度网页
# time.sleep(5)
# driver.quit()