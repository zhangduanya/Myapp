#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-1-24 08:16
# @Author  : zhdya@zhdya.cn
# @File    : mem.py


from Mydjangoapp.salt_api.func.hosts.main import Base              #加载自定义的一个类

class Mem(Base):
    def run(self):
        self.method = 'cmd.run'
        self.tgt = '*'
        self.arg = 'dmidecode -q -t 17 2>/dev/null'     #类似于：free -m|grep Mem |awk -F ' ' '{print $2}'

        return {'client': 'local', 'fun': self.method, 'tgt': self.tgt, 'arg': self.arg}
