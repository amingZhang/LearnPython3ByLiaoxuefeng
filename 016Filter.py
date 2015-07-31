#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __author__ = 'zhangchangming'

"""
filter()接收一个函数和一个序列。filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
"""

def is_odd(x):
    return x % 2 == 1

list0to9 = list(range(10))
print(list0to9)

# 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
result = list(filter(is_odd, list0to9))
print(result)

# s.strip(rm)        删除s字符串中开头、结尾处，位于 rm删除序列的字符
# 当rm为空时，默认删除空白符（包括'\n', '\r',  '\t',  ' ')
def no_str_blank(s):
    return s and s.strip()

result = list(filter(no_str_blank, ['abc', None, '', 'd e f', ' ', ' ghi ']))
print(result)

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。
def is_palindrome(n):
    str1 = str(n)
    for i in range(int(len(str1)/2)):
        if str1[i] != str1[(-1)*(i+1)]:
            return False
    return True

# 更优雅的方法：
# 1.没必要一一比较每一个字符
# 2.str[::-1]可以反转str 'abc'[::-1] => 'cba'
def is_palindrome_excellent(n):
    return n == int(str(n)[::-1])

output = filter(is_palindrome_excellent, range(1, 1000))
print(list(output))
