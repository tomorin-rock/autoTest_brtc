import allure

from autoTest_brtcApi.api.usermanage import userApi


class TestCreateOrder:
    @allure.epic("brtc_api")
    @allure.feature("用户管理")
    @allure.story("创建订单")
    def test_create_order(self):
        res = userApi.createOrder_api()
        assert '恭喜你，下单成功。' in res.json()['message']
        print(res.json())
