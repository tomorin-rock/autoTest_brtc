from autoTest_brtcApi.core.executeReq import Request
from autoTest_brtcApi.utils.readFile import read_yaml
from autoTest_brtcApi.utils.writeFile import write_file


class UserApi(Request):
    # 注册api
    def register_api(self, username, password, phone):
        file_name = "/register"
        url = self.pre_url + file_name
        headers = read_yaml('common.yml')['headers']
        params = {
            "user_name": username,
            "passwd": password,
            "phone": phone,
        }
        res = self.request("POST", url=url, headers=headers, json=params)
        return res

    # 登录api
    def login_api(self, phone, passwd):
        file_name = "/login"
        url = self.pre_url + file_name
        headers = read_yaml('common.yml')['headers']
        params = {
            "phone": phone,
            "passwd": passwd,
        }
        res = self.request("POST", url=url, headers=headers, json=params)
        if res.json()['code'] == 0:
            userId = res.json()['data']['userId']
            token = res.json()['data']['token']
            data = {
                "headers": {
                    'userId': userId,
                    'token': token,
                }
            }
            write_file(data)
            return res
        return 0

    # 获取用户api
    def getUser_api(self):
        file_name = "/getUserById"
        url = self.pre_url + file_name
        data = read_yaml('tmp.yml')
        headers = {
            "token": data['headers']['token'],
            "userId": str(data['headers']['userId']),
        }
        res = self.request("GET", url=url, headers=headers)
        return res

    def createOrder_api(self):
        file_name = "/createOrder"
        data = read_yaml('tmp.yml')
        url = self.pre_url + file_name
        headers = read_yaml('common.yml')['headers']
        params = {"token": data['headers']['token'],
                  "userId": str(data['headers']['userId']),
                  "productId": "1000",
                  "productName": "Toyama Kasumi",
                  "quantity": 200,
                  "shippingAddress": "划小船中专",
                  "buyerPhone": "11100888811",
                  }
        res = self.request("POST", url=url, headers=headers, json=params)
        return res


if __name__ == '__main__':
    api = UserApi()
    res = api.getUser_api()
    print(res)

# 实例化userApi对象
userApi = UserApi()
