#!/usr/bin/python3
# Author: Chunk

from urllib.request import urlopen
import requests, string, random
import json
from urllib import parse


class NetsUtils:

    def __init__(self, header, cookie):
        self.header = header
        self.cookie = cookie
        if header is None:
            self.header = ""
        if cookie is None:
            self.cookie = ""

    def get_url(self, url, data={}):
        res = requests.get(url, params=data, cookies=self.cookie, headers=self.header)
        return res

    def post_form(self, url, form_data={}):
        # FormData = {"instance_name": 'onlne_game_sdk-4-192.168.6.163:14006-S', "resource_type": 'database'}
        data = parse.urlencode(form_data)
        print("====================")
        print(data)
        print("====================")
        # return requests.post(url, data=data, cookies=self.cookie, headers=self.header)


if __name__ == '__main__':
    # print("111")
    # res = get_url("http://sqlreview.duoku.com/group/user_all_instances/?tag_codes%5B%5D=can_read")
    # resJson = res.json()
    # print(resJson)
    # if resJson['status'] == 0:
    #     resDataArr = resJson['data']
    #     for dbInstance in resDataArr:
    #         print("=%s,%s" % (dbInstance['instance_name'], dbInstance['id']))
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
    # resSubmit = post_form("http://sqlreview.duoku.com/query/applyforprivileges/",
    #                       form_data={'title': '打包中心',
    #                                  'instance_name': 'cps-10.16.87.49:3306-S',
    #                                  'priv_type': '1',
    #                                  'db_name': '',
    #                                  'db_list[]': 'package_center',
    #                                  'valid_date': '2020-4-15',
    #                                  'limit_num': '100',
    #                                  'workflow_auditors': '2',
    #                                  'group_name': 'java资源组',
    #                                  })
    # resSubmitJson = resSubmit.json()
    # print(resSubmitJson)

    print("=====over=====")
