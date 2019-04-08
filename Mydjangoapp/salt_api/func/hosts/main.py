#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-1-24 08:30
# @Author  : zhdya@zhdya.cn
# @File    : main.py

class Base(object):

    def __init__(self):
        self.method = ''
        self.tgt = ''
        self.arg = ''

    def run(self):
        raise NotImplementedError('Not run func')