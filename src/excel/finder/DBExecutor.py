#!/usr/bin/python3

import pymysql


class DbUtils:

    def __init__(self, host, user, passwd, db, port=3306):
        self.host = host
        self.user = user
        self.db = db
        self.port = port
        self.db = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
        self.db.close()
        print("ready to connect 2 db")

    def fetch_one(self, sql):
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.db.connect()
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
            data = cursor.fetchone()
        except Exception as e:
            print(e)
            return None
        finally:
            cursor.close()
            self.db.close()
        return data


if __name__ == '__main__':
    dbut = DbUtils("192.168.6.1", "java_user", "SFzsxjidz1aa2HjA", "gamesdk_ios", 14051)
    res1 = dbut.fetch_one('SELECT 1 FROM standalone_orders WHERE transaction_id = "%s" ' % (str("100000572839220").replace("\n", "")))
    res2 = dbut.fetch_one('SELECT 1 FROM standalone_orders WHERE transaction_id = "%s" ' % (str("100000572861936").replace("\n", "")))
    res3 = dbut.fetch_one('SELECT 1 FROM standalone_orders WHERE transaction_id = "%s" ' % (str("100000572871862").replace("\n", "")))

    print(res1, res2, res3)
    # for itemId in text_list:
        #     if itemId is not None:
        #         sql = 'SELECT 1 FROM standalone_orders WHERE transaction_id = "%s" ' % (str(itemId).replace("\n", ""))
        #
        #         # print(sql)
        #         # 使用 execute()  方法执行 SQL 查询
        #         cursor.execute(sql)
        #         # 使用 fetchone() 方法获取单条数据.
        #         data = cursor.fetchone()
        #         if data is None:
        #             print(itemId, data)
        # # 关闭数据库连接
        # db.close()



