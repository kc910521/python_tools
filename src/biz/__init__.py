#!/usr/bin/python3
# Author: Chunk
# 处理 http://sqlreview.duoku.com/

from src.net.NetUtil import NetsUtils
import src.xml.XMLFetcher as xmlf

workBench_XML_path = "/home/caikun/PycharmProjects/codeExecutor/src/resource/connection.xml"

csrftoken = 'EhO73d8DIefWIZkAAMf3NxnMlzI8b7LIn26a9OYZhmniaWFrrZ0hdLY6G7hEDoMF'

h_cookies = {'BAIDUID': 'A52D9052254343A857EDA367212DBD62', 'auth_info': 'Y2Fpa3VufDE1ODU2MjMxNDMwMDQ=',
             'auth_hash': 'a5d7fbd8588bf19af72b615c1c42e11c',
             'csrftoken': csrftoken,
             'sessionid': 'rd5q5xiqog19qa9q3g57r0hdt8pua7ft'
             }
h_header = {'Referer': 'http://sqlreview.duoku.com/sqlquery/',
            'X-CSRFToken': csrftoken,
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
            }

form_header = {'Referer': 'http://sqlreview.duoku.com/sqlquery/',
               'X-CSRFToken': csrftoken,
               'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
               }


# return { '{MysqlName}': [scheme1, scheme2, scheme3] }
def compareAndFetch():
    allDBArr = []
    allDBDict = {}
    allDBArrRaw = xmlf.fetch_from_work_bench(workBench_XML_path)

    net_getter = NetsUtils(header=h_header, cookie=h_cookies)
    net_poster = NetsUtils(header=form_header, cookie=h_cookies)

    res = net_getter.get_url("http://sqlreview.duoku.com/group/user_all_instances/?tag_codes%5B%5D=can_read")
    resJson = res.json()
    print(resJson)
    if resJson['status'] == 0:
        resDataArr = resJson['data']
        for dbInstance in resDataArr:
            print("=%s,%s" % (dbInstance['instance_name'], dbInstance['id']))
            for dbInstanceInXML in allDBArrRaw:
                # 匹配数据源导出文件的 {ip}:{port} 到 dbInstance的名字
                if dbInstance['instance_name'].find(dbInstanceInXML) == -1:
                    # print("FG:" + dbInstance['instance_name'])
                    allDBArr.append(dbInstance['instance_name'])
                    break
    print(allDBArr)
    for ins in allDBArr:
        # fetch dbs from Mysql path
        schemes = net_poster.post_form("http://sqlreview.duoku.com/instance/instance_resource/",
                                       form_data={'instance_name': ins,
                                                  'resource_type': 'database'})
        schJson = schemes.json()
        if schJson['status'] == 0:
            allDBDict[ins] = schJson['data']
            print('%s of %s' % (ins, schJson['data']))

    print(allDBDict)
    return allDBDict


if __name__ == '__main__':
    # pathWithSchemes = compareAndFetch()
    net_poster = NetsUtils(header=form_header, cookie=h_cookies)
    resSubmit = net_poster.post_form("http://sqlreview.duoku.com/query/applyforprivileges/",
                                     form_data={'title': '打包中心',
                                                'instance_name': 'cps-10.16.87.49:3306-S',
                                                'priv_type': '1',
                                                'db_name': '',
                                                'db_list[]': 'package_center',
                                                'valid_date': '2020-4-15',
                                                'limit_num': '100',
                                                'workflow_auditors': '2',
                                                'group_name': 'java资源组',
                                                })
    # resSubmitJson = resSubmit.json()
    # print(resSubmitJson)
    print("====oer============")
