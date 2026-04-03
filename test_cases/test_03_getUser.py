import allure
import pytest

from autoTest_brtcApi.api.usermanage import userApi


class TestGetUser:
    # 测试用例
    @allure.epic("brtc_api")
    @allure.feature("用户管理")
    @allure.story("获取用户信息")
    # @pytest.mark.skip
    def test_get_user(self):
        # 发送请求获取响应数据
        res = userApi.getUser_api()
        assert 0 == res.json()['code']
        assert "用户信息获取成功" in res.json()['message']
