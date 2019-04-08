#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-1-24 08:18
# @Author  : zhdya@zhdya.cn
# @File    : salt_client.py


import json
import requests
# from conf.settings import SALT_API_CON
from Mydjangoapp.salt_api.conf.settings import SALT_USERNAME
from Mydjangoapp.salt_api.conf.settings import SALT_PASSWORD


class SaltApi:

    def __init__(self, url, params):        ##定义salt api接口的类，初始化获得token
        self.url = url
        self.username = SALT_USERNAME
        self.password = SALT_PASSWORD
        self.params = params
        self.headers = {        ##设置初始化header头信息
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
            "Content-type": "application/json"
        }
        self.login_url = url + "login"      ##地址拼接
        self.login_params = {'username': self.username, 'password': self.password, 'eauth': 'pam'}
        # self.token = self.get_data(self.login_url, self.login_params)['token']
        self.token = self.get_data(self.login_url, self.login_params).get('token')
        self.headers['X-Auth-Token'] = self.token

    def get_data(self, url, params):
        send_data = json.dumps(params)
        # print('-----send_data>>', send_data)
        request = requests.post(url, data=send_data, headers=self.headers, verify=False)
        response = request.json()
        result = dict(response)
        # print result
        return result['return'][0]

    def salt_command(self):
        """远程执行命令，相当于salt 'client1' cmd.run 'free -m'"""
        # if arg:
        #     params = {'client': 'local', 'fun': method, 'tgt': tgt, 'arg': arg}
        # else:
        #     params = {'client': 'local', 'fun': method, 'tgt': tgt}
        result = self.get_data(self.url, self.params)
        return result