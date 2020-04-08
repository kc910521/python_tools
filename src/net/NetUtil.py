#!/usr/bin/python3
# Author: Chunk

from urllib.request import urlopen
import requests, string, random
import json
from urllib import parse

csrftoken = 'VRkizSppBC0KW3mwSBaUY2EowlBri874BrkXTMovsBFfcALManG9ThBtm6leBSSt'

h_cookies = {'BAIDUID': 'A52D9052254343A857EDA367212DBD62', 'auth_info': 'Y2Fpa3VufDE1ODU2MjMxNDMwMDQ=',
             'auth_hash': 'a5d7fbd8588bf19af72b615c1c42e11c',
             'csrftoken': csrftoken,
             'sessionid': 'krnvnkhl5msb84hmmt5jnxp4zit44jlh'
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


def get_url(url, data={}):
    res = requests.get(url, params=data, cookies=h_cookies, headers=h_header)
    return res


def post_form(url, form_data={}):
    # FormData = {"instance_name": 'onlne_game_sdk-4-192.168.6.163:14006-S', "resource_type": 'database'}
    data = parse.urlencode(form_data)
    print("====================")
    print(data)
    print("====================")
    return requests.post(url, data=data, cookies=h_cookies, headers=form_header)


if __name__ == '__main__':
    print("111")
    res = get_url("http://sqlreview.duoku.com/group/user_all_instances/?tag_codes%5B%5D=can_read")
    resJson = res.json()
    print(resJson)
    if resJson['status'] == 0:
        resDataArr = resJson['data']
        for dbInstance in resDataArr:
            print("=%s,%s" % (dbInstance['instance_name'], dbInstance['id']))

    # resInstance = post_form("http://sqlreview.duoku.com/instance/instance_resource/",
    #           form_data={'instance_name': 'onlne_game_sdk-4-192.168.6.163:14006-S', 'resource_type': 'database'})
    # resJsonInstance = resInstance.json()
    # print(resJsonInstance)
    # if resJsonInstance['status'] == 0:
    #     resInsArr = resJsonInstance['data']
    #     for meta in resInsArr:
    #         print(meta)

    # resGroupInst = post_form("http://sqlreview.duoku.com/group/instances/",
    #           form_data={'group_name': 'java资源组', 'tag_code': 'can_read'})
    # print(resGroupInst.json())

    # submit
    resSubmit = post_form("http://sqlreview.duoku.com/query/applyforprivileges/",
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
    resSubmitJson = resSubmit.json()
    print(resSubmitJson)

    print("=====over=====")
