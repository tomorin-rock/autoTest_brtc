import pytest

from autoTest_brtcApi.utils.mydb import mydb


@pytest.fixture(scope="session", autouse=True)
def fixture():
    # 环境预置
    print('......')
    yield 0
    # 环境恢复 --> 删除注册的用户
    sql = "delete from UserName where u_nickname = 'snake'"
    mydb.operate(sql)
    # sql2 = "delete from brtc_orders where username = 'snake'"
    # mydb.operate(sql2)
