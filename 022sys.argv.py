#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __author__ = 'zhang.c.m'

'显示启动参数'

import sys

def say_hello():
    args = sys.argv
    for i in args:
        print(i)

if __name__ == '__main__':
    say_hello()