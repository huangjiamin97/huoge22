
from selenium import webdriver
from selenium.webdriver import ActionChains
import pytest
from selenium.webdriver.common.by import By
import time


class Test_actionchains:
    def setup(self):
        self.driver = webdriver.Chrome()
    def teardown(self):
        self.driver.quit()

    def test_actionchains(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.ID,'kw').send_keys('webdriver api')
        click = self.driver.find_element(By.ID,'su')
        actions = ActionChains(self.driver)
        actions.click(click)


        actions.perform()
        time.sleep(3)


# if __name__ == "__main__":
#     pytest.main(['-vs','test_actionchains'])