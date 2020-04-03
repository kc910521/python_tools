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

    def fetch_list(self, sql):
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.db.connect()
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
        except Exception as e:
            print(e)
            return None
        finally:
            cursor.close()
            self.db.close()
        return data

    def insert_one(self, sql):
        self.db.connect()
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
            self.db.commit()
            return 1
        except Exception as e:
            print(e)
            self.db.rollback()
            return -1
        finally:
            cursor.close()
            self.db.close()
        return 0


if __name__ == '__main__':
    dbut = DbUtils("10.xx.xx.xx", "xxx", "Nt6TNmxxxWd", "onesdk", 14051)
    res1 = dbut.fetch_one('SELECT * FROM onesdk.working_calendar where date = "%s" order by date desc ' % (
        str("2019-08-19").replace("\n", "")))
    res2 = dbut.fetch_one('SELECT * FROM onesdk.working_calendar where date = "%s" order by date desc ' % (
        str("2019-08-18").replace("\n", "")))

    res3 = dbut.insert_one('INSERT INTO `onesdk`.`working_calendar` '
                           ' (`date`, `week`, `is_work_day`) '
                           ' VALUES ("%s", "%s", "%s") ' % ("2019-08-20", "2", "1"))

    print(res1, res2, res3)
