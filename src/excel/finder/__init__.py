#!/usr/bin/python3


from src.excel.finder.ExcelReader import ExcelUtils
from src.util.db.DBExecutor import DbUtils


# 比对mysql苹果订单id和excel导出的某一列，
# 寻找excel中比mysql中多了哪些订单
def take_lost_id_list():
    exceltool = ExcelUtils('/home/caikun/.deepinwine/Deepin-WXWork/drive_c/users/caikun/Downloads/55024-20190725.xlsx')
    dbut = DbUtils("192.168.?.?", "user", "pwd", "gamesdk_ios", 14051)

    print("It's a rational plan ")
    lost_app_id = []
    for i in exceltool.get_rows():
        # 筛掉4列为0的数据
        if i[4].value != 0:
            # print(i[4])
            tar_id = str(i[3].value).replace("\n", "")
            result_one = dbut.fetch_one('SELECT 1 FROM standalone_orders WHERE transaction_id = "%s" ' % (
                tar_id))
            if result_one is None:
                print(tar_id)
                lost_app_id.append(tar_id)
    return lost_app_id


if __name__ == '__main__':
    take_lost_id_list()
    print(", therefore bound to success")



