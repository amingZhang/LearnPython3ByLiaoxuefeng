#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __author__ = 'zhang.c.m'

import logging
import os

print(os.name)  # 操作系统类型

try:
    print(os.uname())  # 获取详细的系统信息
except Exception as e:
    logging.exception(e)  # 注意uname()函数在Windows上不提供

print(os.environ)  # 环境变量
print(os.environ.get('PATH'))  # 要获取某个环境变量的值

print(os.path.abspath('.'))  # 查看当前目录的绝对路径

# 在当前目录下创建一个新目录，首先把新目录的完整路径表示出来:
new_dir_path = os.path.join('.', 'testdir')
print(new_dir_path)
# 然后创建一个目录:
os.mkdir(new_dir_path)
# 删掉一个目录:
os.rmdir(new_dir_path)

'''
把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，
这样可以正确处理不同操作系统的路径分隔符。
'''

'''
要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，
这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
'''
print(os.path.split('/users_path/test_dir/test_file.txt'))

'''
os.path.splitext()可以直接让你得到文件扩展名
'''
print(os.path.splitext('/path/to/file.txt'))

import shutil
# 复制文件
shutil.copyfile('./test.txt', './test_new.txt')
# 对文件重命名:
os.rename('test_new.txt', 'test.py')
# 删掉文件:
os.remove('test.py')

# 列出当前目录下的所有目录
L = [x for x in os.listdir('.') if os.path.isdir(x)]
print(L)

# 列出所有的.py文件
L = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(L)
