#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-1-24 08:15
# @Author  : zhdya@zhdya.cn
# @File    : settings.py


HOST_FUNC_DIC = {
    # 'disk': 'func.hosts.disk.Disk',
    'mem': 'Mydjangoapp.salt_api.func.hosts.mem.Mem',
    'cpu': 'Mydjangoapp.salt_api.func.hosts.cpu.Cpu',
    # 'os': 'func.hosts.os.Os',
    # 'ip': 'func.hosts.ip.Ip',
}

HOST_LI = ['mem']       ##,'cpu'

SALT_API_CON = "https://192.168.171.173:8001/"
SALT_USERNAME = 'saltapi'
SALT_PASSWORD = 'zhangDUANya.'