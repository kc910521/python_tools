#!/usr/bin/python3
# Author: Chunk
import time
import calendar
import json
import requests
import arrow

server_path = "http://www.easybots.cn/api/holiday.php"


# from param likewise 2018-09-01, get weekday
def get_day_of_week_from(dateStr):
    dateSplit = dateStr.split('-')
    if len(dateSplit) == 3:
        return 1 + calendar.weekday(int(dateSplit[0]), int(dateSplit[1]), int(dateSplit[2]))
    print("error in calendar tools:" + dateStr)
    return -1


# {"201801":{"01":"2","06":"2","07":"2","13":"2","14":"1","20":"1","21":"2","27":"1","28":"1"}
#     ,"201802":{"03":"2","04":"2","10":"1","15":"2","16":"2","17":"2","18":"2","19":"1","20":"1","21":"2","25":"1"}
#     ,"201803":{"03":"1","04":"2","10":"2","11":"2","17":"1","18":"2","24":"2","25":"1","31":"1"}
#     ,"201804":{"01":"2","05":"2","06":"1","07":"2","14":"1","15":"2","21":"2","22":"1","29":"1","30":"2"}
#     ,"201805":{"01":"2","05":"1","06":"2","12":"2","13":"2","19":"1","20":"1","26":"1","27":"2"}
#     ,"201806":{"02":"2","03":"2","09":"2","10":"1","16":"1","17":"1","18":"2","23":"1","24":"1","30":"2"}
#     ,"201807":{"01":"1","07":"1","08":"2","14":"2","15":"1","21":"1","22":"2","28":"2","29":"2"}
#     ,"201808":{"04":"2","05":"1","11":"1","12":"2","18":"1","19":"2","25":"2","26":"2"}
#     ,"201809":{"01":"1","02":"1","08":"2","09":"2","15":"1","16":"2","22":"2","23":"2","24":"2"}
#     ,"201810":{"01":"2","02":"2","03":"2","04":"1","05":"2","06":"1","07":"1","13":"1","14":"2","20":"2","21":"1","27":"1","28":"2"}
#     ,"201811":{"03":"2","04":"2","10":"2","11":"1","17":"1","18":"2","24":"2","25":"1"},
#  "201812":{"01":"1","02":"2","08":"1","09":"1","15":"1","16":"2","22":"2","23":"2","30":"2","31":"1"}}
def get_vacations_by_api_from(year):
    #  concat path url params
    vacation_array = []
    month_array = []
    path_w_param = server_path + '?m='
    for mth in range(12):
        month_array.append(year + ('%02d' % (mth + 1)))
        path_w_param += year + ('%02d' % (mth + 1))
        if mth != 11:
            path_w_param += ','
    print(path_w_param)
    req = requests.get(path_w_param)
    payload = json.loads(req.text)
    print(payload)
    # foreach months in payload to extract vacations
    for year_mon in month_array:
        m_object = payload[year_mon]
        for day in m_object:
            if m_object[day] == "2" or m_object[day] == "1":
                vacation_array.append(year_mon[0:4] + '-' + year_mon[4:] + '-' + day)
    return vacation_array


def getAllDayPerYear(years):
    '''
    获取一年的所有日期
    :param years:年份
    :return:全部日期列表
    '''
    start_date = '%s-1-1' % years
    a = 0
    all_date_list = []
    days_sum = isLeapYear(int(years))
    print()
    while a < days_sum:
        b = arrow.get(start_date).shift(days=a).format("YYYY-MM-DD")
        a += 1
        all_date_list.append(b)
    # print(all_date_list)
    return all_date_list


def isLeapYear(years):
    '''
    通过判断闰年，获取年份years下一年的总天数
    :param years: 年份，int
    :return:days_sum，一年的总天数
    '''
    # 断言：年份不为整数时，抛出异常。
    assert isinstance(years, int), "请输入整数年，如 2018"

    if ((years % 4 == 0 and years % 100 != 0) or (years % 400 == 0)):  # 判断是否是闰年
        # print(years, "是闰年")
        days_sum = 366
        return days_sum
    else:
        # print(years, '不是闰年')
        days_sum = 365
        return days_sum


if __name__ == '__main__':
    # print(get_day_of_week_from("2019-08-19"))
    vacations = get_vacations_by_api_from('2018')
    all_days = getAllDayPerYear(2018)
    weekday_of_1st_day = get_day_of_week_from(all_days[0])
    print(weekday_of_1st_day)
    my_cal = []
    for yr_mon_day in all_days:
        my_cal.append([yr_mon_day, weekday_of_1st_day % 7, yr_mon_day in vacations])
        weekday_of_1st_day += 1
    print(my_cal)
