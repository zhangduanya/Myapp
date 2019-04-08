#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-1-24 08:15
# @Author  : zhdya@zhdya.cn
# @File    : run.py

import importlib
import os, sys
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASEDIR)
sys.path.append(BASEDIR)        ##将文件path加入环境变量
from Mydjangoapp.salt_api.conf.settings import HOST_FUNC_DIC
from Mydjangoapp.salt_api.conf.settings import HOST_LI
from Mydjangoapp.salt_api.func.task.get_data import send_main


for host in HOST_LI:
    path = HOST_FUNC_DIC.get(host)
    module_path, class_name = path.rsplit('.', maxsplit=1)
    module = importlib.import_module(module_path)
    disk_class = getattr(module, class_name)

    JG = disk_class()
    func = JG.run()
    # print('------>>>', func)
    JG_dic = send_main(func)
    print(JG_dic)