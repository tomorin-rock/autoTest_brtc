import allure
import pytest

from autoTest_brtcApi.api.usermanage import userApi
from autoTest_brtcApi.utils.readFile import read_yaml


class TestRegister:
    register_result = read_yaml('userInfo.yml')['register']

    # @pytest.mark.skip
    @pytest.mark.parametrize('username,password,phone,code,message', register_result)
    @allure.epic("brtc_api")
    @allure.feature("用户管理")
    @allure.story("注册")
    def test_register(self, username, password, phone, code, message):
        allure.dynamic.title(f"输入用户名{username},密码{password},手机号{phone}注册")
        res = userApi.register_api(username, password, phone)
        assert code == res.json()["code"]
        assert message in res.json()["message"]
