#!/usr/bin/python3
# Author: Chunk

from src.calendar.TimeUtil import *
from src.util.db.DBExecutor import DbUtils

# 将工作日和非工作日日期，周位置导入到mysql
#
if __name__ == '__main__':
    vacations = get_vacations_by_api_from('2018')
    all_days = getAllDayPerYear(2018)
    weekday_of_1st_day = get_day_of_week_from(all_days[0])
    print(weekday_of_1st_day)
    my_cal = []
    for yr_mon_day in all_days:
        my_cal.append([yr_mon_day, weekday_of_1st_day % 7, yr_mon_day in vacations])
        weekday_of_1st_day += 1
    # 得到所有日期数据,prepared for inserting
    print(my_cal)
    dbut = DbUtils("10.16.94.25", "onesdk", "Nt6TNmWd", "onesdk", 14051)
    for date_arr in my_cal:
        # date_arr[2] is True 则为假期，db对应0,否则1

        res = dbut.insert_one('INSERT INTO `onesdk`.`working_calendar` '
                              ' (`date`, `week`, `is_work_day`) '
                              ' VALUES ("%s", "%s", "%s") ' % (
                              date_arr[0], date_arr[1], 0 if (date_arr[2] is True) else 1))
        print(res)
