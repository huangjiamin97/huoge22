import allure
import pytest


@allure.feature('步骤一')
class Test_huogo():
    @allure.story("步骤二")
    def test_one(self,login):
        x = "this"
        assert "h" in x

    # def test_two(self):git
    #     x = "hello"
    #     assert hasattr(x, "check")
    @allure.story("步骤三")
    def test_needsfiles(tmpdir):
        # print(tmpdir)
        assert True
    @allure.story("步骤四")
    def test_demo1(self,login):
        with allure.step("shuchu"):
            print('ss')

if __name__ == '__main__':
    pytest.main(['-v','test_needsfiles'])

    #第二次kkk
