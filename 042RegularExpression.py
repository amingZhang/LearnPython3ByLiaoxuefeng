#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __author__ = 'zhangchangming'

import re

def check_re(rex, item):
    result = rex.match(item)
    if result:  # 查看结果，不匹配返回None
        print(result.group(0), '格式匹配')  # group(0) = 原始字符串
        for i in result.groups():
            print(i)
        '''
        print(result.group(1))  # 第一个子串
        print(result.group(2))  # 第二个子串
        print(result.group(3))  # 第三个子串
        print(result.groups())
        '''
    else:
        print('格式错误')
    return result

input_string = input('输入要检查的时间（格式hh:mm:ss）:')  # '21:06:00'
# 如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了
# 编译:
re_check_time = re.compile(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$')
# 使用:
check_re(re_check_time, input_string)


re_check_mail = re.compile(r'[\w]+[\_\-]*[\.]?[\w\_\-]+@[\w\_\-]+.[\w\_\-\.]*[\w]')
input_string = input('输入要检查的邮件（格式x@x.x）:')  # 'q@a.o'
check_re(re_check_mail, input_string)
