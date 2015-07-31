#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __author__ = 'zhang.c.m'

'''
Decorator装饰器可以理解为包在函数外面，增加现有函数功能
参考http://www.cnblogs.com/rhcad/archive/2011/12/21/2295507.html
Python装饰器学习（九步入门）
'''

print('*'*10, 1, '*'*10)
'''示例1: 最简单的函数,表示调用了两次'''
def myfunc1():
    print("myfunc1() called.")

myfunc1()
myfunc1()

print('*'*10, 2, '*'*10)
'''示例2: 替换函数(装饰)
装饰函数的参数是被装饰的函数对象，返回原函数对象
装饰的实质语句: myfunc = deco(myfunc)'''

def deco2(func):
    print('before myfunc2() called.')
    func()
    print('after myfunc2() called.')
    return func

def myfunc2():
    print('myfunc2() called.')

myfunc = deco2(myfunc2)  # 在这里执行了装饰的实质语句

myfunc()
myfunc()

print('*'*10, 3, '*'*10)
'''示例3: 使用语法糖@来装饰函数，相当于“myfunc = deco(myfunc)”
但发现新函数只在第一次被调用，且原函数多调用了一次'''
def deco3(func):
    print('before myfunc3() called.')
    func()
    print('after myfunc3() called.')
    return func

@deco3  # 在这里执行了装饰的实质语句
def myfunc3():
    print('myfunc3() called.')

myfunc3()
myfunc3()

print('*'*10, 4, '*'*10)
'''示例4: 使用内嵌包装函数来确保每次新函数都被调用，
内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象'''
def deco4(func):
    def _deco():
        print('before myfunc4() called.')
        func()
        print('after myfunc4() called')
        # 不需要返回func，实际上应返回原函数的返回值
    return _deco

@deco4  # 此处不执行装饰的实质语句
def myfunc4():
    print('myfunc4() called.')
    return 'ok'

myfunc4()  # 此处执行完整的第一次
myfunc4()  # 此处执行完整的第二次

print('*'*10, 5, '*'*10)
'''示例5: 对带参数的函数进行装饰，
内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象'''
def deco5(func):
    def _deco(a, b):
        print('before myfunc5() called.')
        ret = func(a, b)
        print('after myfunc5() called')
        return ret
    return _deco

@deco5
def myfunc5(a, b):
    print('myfunc5(%s, %s) called.' % (a, b))
    return a + b

print(myfunc5(1, 2))
print(myfunc5(3, 4))

print('*'*10, 6, '*'*10)
'''示例6: 对参数数量不确定的函数进行装饰，
参数用(*args, **kwargs)，自动适应变参和命名参数'''
def deco6(func):
    def _deco(*args, **kwargs):
        print('before %s called.' % func.__name__)
        ret = func(*args, **kwargs)
        print('after %s called. result:%s' % (func.__name__, ret))
        return ret
    return _deco

@deco6
def myfunc6(a, b):
    print('myfunc6(%s, %s) called.' % (a, b))
    return a + b

@deco6
def myfunc6_2(a, b, c):
    print('myfunc6_2(%s, %s, %s) called.' % (a, b, c))
    return a + b + c

myfunc6(1, 2)
myfunc6(3, 4)
myfunc6_2(1, 2, 3)
myfunc6_2(3, 4, 5)

print('*'*10, 7, '*'*10)
'''示例7: 在示例4的基础上，让装饰器带参数，
和上一示例相比在外层多了一层包装。
装饰函数名实际上应更有意义些'''
def deco7(arg):
    def _deco(func):
        def __deco():
            print("before %s called [%s]." % (func.__name__, arg))
            func()
            print("after %s called [%s]." % (func.__name__, arg))
        return __deco
    return _deco

@deco7("mymodule")
def myfunc7():
    print(" myfunc7() called.")

@deco7("module2")
def myfunc7_2():
    print(" myfunc7_2() called.")

myfunc7()
myfunc7_2()

print('*'*10, 8, '*'*10)
'''示例8: 装饰器带类参数'''
class locker:
    def __init__(self):
        print("locker.__init__() should be not called.")

    @staticmethod
    def acquire():
        print("locker.acquire() called.（这是静态方法）")

    @staticmethod
    def release():
        print("locker.release() called.（不需要对象实例）")

def deco8(cls):
    '''cls 必须实现acquire和release静态方法'''
    def _deco(func):
        def __deco():
            print("before %s called [%s]." % (func.__name__, cls))
            cls.acquire()
            try:
                return func()
            finally:
                cls.release()
        return __deco
    return _deco

@deco8(locker)
def myfunc8():
    print(" myfunc8() called.")

myfunc8()
myfunc8()

print('*'*10, 9, '*'*10)
'''示例9: 装饰器带类参数，并分拆公共类到其他py文件中
同时演示了对一个函数应用多个装饰器'''
from mylockerForDecorator import *

class example:
    @lockhelper(mylocker)
    def myfunc9(self):
        print(" myfunc9() called.")

    @lockhelper(mylocker)
    @lockhelper(lockerex)
    def myfunc9_2(self, a, b):
        print(" myfunc9_2() called.")
        return a + b

if __name__=="__main__":
    a = example()
    a.myfunc9()
    print(a.myfunc9())
    print(a.myfunc9_2(1, 2))
    print(a.myfunc9_2(3, 4))
