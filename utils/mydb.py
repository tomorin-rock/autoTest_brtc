import pymysql


class Db():
    def __init__(self):
        # 连接数据库
        try:
            self.con = pymysql.connect(
                user='root',
                password='Admin@888',
                host='192.168.1.93',
                database='brtc_api',
                port=3306
            )
        except Exception as e:
            print("数据库连接失败,原因是：\n {}".format(e))
            raise
        self.cursor = self.con.cursor()
    # 查询一条数据
    def get_one(self,sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print("查询失败\n {}".format(e))
        result = self.cursor.fetchone()
        return result

    def operate(self,sql):
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as e:
            print("<UNK>\n {}".format(e))
            raise
        return True

mydb = Db()
if __name__ == "__main__":
    print(mydb.get_one("select * from UserName"))
    # sql = "update dept set dname='压力'where deptno=61;"
    # print(mydb.operate(sql))