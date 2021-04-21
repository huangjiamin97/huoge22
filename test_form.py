
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
    @pytest.mark.skip
    @pytest.mark.parametrize('name,password',[('1099202868','Huanglove1997'),('11','22')])
    def test_actionchains(self,name,password):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.ID,'kw').send_keys('qq邮箱')
        time.sleep(3)
        self.driver.find_element(By.ID,'su').click()
        self.driver.find_element(By.XPATH,"//*[@id = '1']//a[1]"). click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        self.driver.switch_to.frame("login_frame")  # 切换到name为login_frame_qq的iframe中
        self.driver.find_element(By.ID,'u').send_keys(name)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID,'p').send_keys(password)
        self.driver.find_element(By.ID, 'p_low_login_enable').click()
        #self.driver.find_element(By.ID, 'login_button').click()

        time.sleep(3)

    def test_button(self):
        self.driver.get("https://www.12306.cn/index/")
        time.sleep(1)
        self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2021-04-11' ")
        time.sleep(3)


# if __name__ == "__main__":
#     pytest.main(['-vs','test_actionchains'])