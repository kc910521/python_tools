#!/usr/bin/python3
# Author: Chunk

from src.calendar.TimeUtil import *
from src.util.db.DBExecutor import DbUtils

# 获取A表渠道id和userId
# 根据userId读取B表，获取company
# 拼接输出
#
if __name__ == '__main__':
    dbut = DbUtils("10.16.87.49", "work", "duoku2012", "cps", 3306)

    ucList = dbut.fetch_list(
        "SELECT user_id,channel_id FROM cps.oem_game_channels WHERE channel_id BETWEEN 5509661 AND 5509735 LIMIT 10000")

    # uid / companyName
    companyCache = {}

    # itm:channelId / companyName
    chanAndCompany = []

    for ucMap in ucList:
        print("uid:%s | channelId:%s" % (ucMap[0], ucMap[1]))
        companyName = companyCache.get(ucMap[0])
        if companyName is None:
            # no cached, db
            icDict = dbut.fetch_one("SELECT id, company FROM cps.oem_user WHERE id = %s LIMIT 1" % ucMap[0])
            if icDict is not None:
                print("id:%s,company:%s cache" % (icDict[0], icDict[1]))
                companyCache[icDict[0]] = icDict[1]
                chanAndCompany.append([ucMap[1], icDict[1]])
            else:
                print("warn:===============null %s" % ucMap[0])
        else:
            # fetch form cache
            chanAndCompany.append([ucMap[1], companyName])
            print("a cached value %s,%s" % (ucMap[0], companyName))
    print('############### alright!')
    print(chanAndCompany)
    print('##################### ready 4 generating sql file!###########################')
    for cc in chanAndCompany:
        print("UPDATE mcp_fr_info SET company='%s' WHERE id='%s';" % (cc[1], cc[0]))
