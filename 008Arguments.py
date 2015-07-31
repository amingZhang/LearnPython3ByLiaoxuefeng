#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  __author__ = 'zhang.c.m'

print('现在展示函数的多种参数：')
print('*'*20)

print('1. 位置参数')
print('def power(x, n):')
def power(x, n):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s
x = float(input('输入x：'))
n = float(input('输入n：'))
print(power(x, n))

print('\n' + '*'*20)
print('2. 默认参数')
print('def enroll(name, gender, age=6, city=\'Beijing\'):')
def enroll(name, gender, age=6, city='Shanghai'):
    print('name:%s; gender:%s; age:%d; city:%s' % (name, gender, age, city))
name = input('请输入名字：')
gender = input('请输入性别（M/F）：')
age = input('请输入年龄（直接回车使用缺省值）：')
city = input('请输入城市（直接回车使用缺省值）：')

if len(age) == 0 and len(city) == 0:
    enroll(name, gender)
elif len(age) == 0 and len(city) > 0:
    enroll(name, gender, city=city)
elif len(age) > 0 and len(city) == 0:
    enroll(name, gender, int(age))
else:
    enroll(name, gender, int(age), city)

print('*'*20)
print('默认参数有一个特别需要注意的地方：\n默认参数必须指向不变对象')
print('错误的使用：def add_end(L=[]):')
def add_end(L=[]):
    L.append('END')
    return L
print(add_end())
print(add_end())

print('正确的使用：def add_end(L=None):')
def add_end_none(L=None):
    if L is None:
        L = ['default', 'value']  # 在这里设置缺省值
    L.append('END')
    return L
print(add_end_none())
print(add_end_none())

print('\n' + '*'*20)
print('3. 可变参数')
print('def calc(*numbers):')
def calc(*numbers):
    sum = 0
    for n in numbers:
        if isinstance(n, str):
            n = int(n)
        sum  = sum + n * n
    return sum
print('calc(1,2,3)')
print(calc(1,2,3))
print('calc(1,3,5,7)')
print(calc(1,3,5,7))
nums = tuple(input('输入需要计算的数字：'))
print('在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去')
print('nums = ', nums)
print('calc(*nums)')
print(calc(*nums))

print('\n' + '*'*20)
print('4. 关键字参数')
print('利用**指定关键字参数（dict类型）：def person(name, age, **kw):')
def person(name, age, **kw):
    print('name:', name, '; age:', age, '; key_word:', kw)
person('Adam', 45, gender='M', job='Engineer')
print('在dict前面加2个*号，把dict的元素变成可变关键字参数传进去')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

print('\n' + '*'*20)
print('5. 命名关键字参数')
print('限制关键字参数的名字，只接收指定的关键字参数：def person(name, age, *, city, job):')
def person_new(name, age, *, city, job):
    print('name:', name, '; age:', age, '; city:', city, '; job:', job)
person_new('angel baby', 23, city='tokyo', job='player')
