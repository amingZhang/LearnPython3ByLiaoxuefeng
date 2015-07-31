#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __author__ = 'zhang.c.m'

import logging

# 必要的时候可以定义我们自己的错误类型
class FooError(ValueError):
    def __init__(self, error_string):
        self.__error_string = 'there are some info has been added:' + error_string
        super().__init__(error_string)
    def print_error_info(self):
        print(self.__error_string)

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError("invalid value:%s" % s)  # 主动抛出错误
    return 10 / n

def bar(s):
    try:
        foo(s) * 2
    except FooError as e:  # 接到错误
        e.print_error_info()  # 处理错误
        raise  # 继续向上层抛出错误

def main():
    try:
        bar(0)
    except Exception as e:  # 接到错误
        logging.exception(e)  # 记下错误日志
    finally:
        print('finally always running')  # finally语句块总是会执行

main()
print('we can do something after error raised')  # 使用logging后程序不会中断，可以继续执行
