#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __author__ = 'zhang.c.m'

# __str__ 用于print()类实例时显示的字符串
class Student(object):
    def __init__(self, name='Bob'):
        self.__name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.__name
    __repr__ = __str__

print(Student('Michael'))

# __iter__ 用于for...in循环
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 30:
            raise StopIteration()
        return self.a

for n in Fib():
    print(n)

# __getitem__ 用于实现下标取元素
class Fib_new(object):
    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b  = b, a + b
            return L

f = Fib_new()
print(f[10:100])

# __getattr__ 动态返回属性和方法
class Student_new(object):
    def __init__(self, name='Adam'):
        self.__name = name
        self.__score = 100

    def __getattr__(self, item):
        if item == 'score':
            return self.__score
        if item == 'age':
            return lambda : 18
        raise AttributeError('Student object has no attribute: %s' % item)

adam = Student_new()
print(adam.score)
print(adam.age())
# print(adam.other)  # 调用不存在的方法属性，产生错误

class Chain(object):
    def __init__(self, path=''):
        self.__path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self.__path, path))
    def __call__(self, *args, **kwargs):
        return Chain('/%s' % (args[0]))
    def __str__(self):
        return self.__path
    __repr__ = __str__

print(Chain().status.user.timeline.list)
print(Chain().status.user('adam').timeline.list('now_list'))