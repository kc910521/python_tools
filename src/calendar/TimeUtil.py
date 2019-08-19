#!/usr/bin/python3
import time
import calendar


def get_day_of_week_from(dateStr):
    dateSplit = dateStr.split('-')
    if len(dateSplit) == 3:
        return 1 + calendar.weekday(int(dateSplit[0]), int(dateSplit[1]), int(dateSplit[2]))
    print("error in calendar tools:" + dateStr)
    return -1


if __name__ == '__main__':
    print(get_day_of_week_from("2019-08-19"))
