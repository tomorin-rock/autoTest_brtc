import allure
import pytest

from autoTest_brtcApi.api.usermanage import userApi
from autoTest_brtcApi.utils.readFile import read_yaml


class TestLogin:
    login_test = read_yaml('userInfo.yml')['login']

    @pytest.mark.parametrize('phone,passwd,code,msg', login_test)
    @allure.epic("brtc_api")
    @allure.feature("用户管理")
    @allure.story("登录")
    # @pytest.mark.skip
    def test_login(self, phone, passwd, code, msg):
        allure.dynamic.title(f"输入手机号{phone},密码{passwd}登录")
        res = userApi.login_api(phone, passwd)
        assert int(code) == res.json()["code"]
        assert msg in res.json()["message"]
