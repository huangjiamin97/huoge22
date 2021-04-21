

import pytest

@pytest.fixture(scope='function',)
def login():
    print("这是一个fixture方法")
    yield
    print("这个方法结束了")
