import decimal

import pytest
import allure_pytest
import allure
import decimal
test_user_data = ['Tome','Jerry']
@pytest.fixture(scope='module')
def login_r(request):
    user = request.param
    print(f"\n 打开首页准备登录， 登录用户为 {user}")
    return user
#indirect=True 可以把传过来的参数当函数执行
@pytest.mark.parametrize('login_r',test_user_data,indirect=True)
@allure.feature("测试")
def test_login(login_r):
    a = login_r
    with allure.step("步骤二"):
        print(f"测试用例中login的返回值; {a}")
        assert  a !=''


