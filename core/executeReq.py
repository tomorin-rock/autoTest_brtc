import traceback, json

import requests
from autoTest_brtcApi.utils.log_util import logger


class Request:
    def __init__(self):
        self.pre_url = "http://192.168.1.93:8899"
        # 实例化requests.Session()对象
        self.session = requests.Session()

    def request(self, method, url, headers, **kwargs):
        logger.debug(f"请求方式: {method},\n"
                     f"请求url: {url},\n"
                     f"请求头{json.dumps(headers, indent=4, ensure_ascii=False),},\n"
                     f"请求参数{json.dumps(kwargs, indent=4, ensure_ascii=False)}")
        try:
            res = self.session.request(method, url, headers=headers, **kwargs)
            logger.debug(f'接口返回的数据是:{json.dumps(res.json(), indent=4, ensure_ascii=False)}')
            return res
        except Exception as e:
            logger.error(f'接口执行出错,原因是:\n{traceback.format_exc()}')
            return None
