#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-1-24 08:18
# @Author  : zhdya@zhdya.cn
# @File    : get_data.py


import requests
import json
try:
    import cookielib
except:
    import http.cookiejar as cookielib

# 使用urllib2请求https出错，做的设置
import ssl
context = ssl._create_unverified_context()

from Mydjangoapp.salt_api.func.task.salt_client import SaltApi
from Mydjangoapp.salt_api.conf.settings import SALT_API_CON

# 使用requests请求https出现警告，做的设置
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def send_main(params):
    salt = SaltApi(SALT_API_CON, params)
    # print('----BB>>', params)
    # salt_client = '*'
    # salt_test = 'test.ping'
    # salt_method = 'grains.get'
    # salt_params = ['ip_interfaces',]
    # result2 = salt.salt_command(salt_client, salt_method, salt_params)
    # for k, v in params.items():
    #     fun = v
    #     tgt = v
    #     arg = v
    result_data = salt.salt_command()
    # print(result_data)


    JG_dic = {}
    for host, value in result_data.items():
        if not value:
            print(host, '内存信息获取失败，请检查dmidecode工具')
            continue
        if host not in JG_dic.keys():
            JG_dic[host] = {}
        memory = 0
        # print(value)
        li = value.split('\n\t')
        # print('li-->', li)
        for item in li:
            # print('---item--->>', item)
            if 'Memory Device' in item:
                continue
            k, v = item.split(':')
            if k == 'Size':
                num, company = v.rsplit(' ', maxsplit=1)
                # print('num--->', num)
                try:
                    num = int(num)      ##/1024
                except ValueError:
                    continue
                memory += num
            JG_dic[host]['memory'] = memory
    return JG_dic
