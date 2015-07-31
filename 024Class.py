#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __author__ = 'zhang.c.m'

class Student(object):
    "student document"

    # 只有下面槽中允许的属性和方法才可以被绑定到类的实例中
    __slots__ = ('__name', '__score', 'age', 'gender', 'set_age', 'set_gender')

    def __init__(self, name, score):
        self.__name = name  # __两个下划线表示private变量
        self.__score = score

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, new_score):
        if not isinstance(new_score, int):
            raise ValueError('score must be integer!')
        if new_score < 0 and new_score > 100:
            raise  ValueError('score must between 0 ~ 100')
        self.__score = new_score

    def print_info(self):
        print(self.__name, self.__score)

class Person():
    def run(self):
        print('person is running...')

class dog():
    def run(self):
        print('dog is running')

class cat():
    def run(self):
        print('cut is running')

def do_run(some_obj):
    some_obj.run()

from types import MethodType

def test():
    # 这里体现了一种假的多态。注意这里的Person,dog,cat之间并不存在继承关系
    # 但是只要它们有run函数，就可以被do_run调用
    do_run(Person())
    do_run(dog())
    do_run(cat())

    adam = Student('adam', 99)
    adam.score = 100  # 利用@property, 实际相当于调用了set_score
    print(adam.get_name(), '\'s new score is :', adam.score)  # 利用@property, 实际相当于调用了get_score

    if hasattr(adam, 'print_info'):  # hasattr返回true表示有print_info方法
        adam.print_info()
    print(hasattr(adam, '__name'))  # hasattr返回false表示没有__name属性
    # print(adam.__name)  #不能访问private变量

    # 给实例绑定一个方法：
    adam.set_age = MethodType(set_age, adam)  # 绑定
    print(hasattr(adam, 'set_age'))  # hasattr返回true表示有set_age方法
    adam.set_age(25)  # 调用实例方法
    print(adam.age)  # 测试

    make = Student('make', 98)
    print(hasattr(make, 'set_age'))  # hasattr返回false表示没有set_age方法

    # 给类绑定一个方法：
    Student.set_gender = MethodType(set_gender, Student)
    print(hasattr(make, 'set_gender'))  # hasattr返回true表示有set_gender方法
    make.set_gender()  # 实例可以使用新绑定的方法了
    print(make.gender)

def set_age(self, age):
    self.age = age

def set_gender(self, gender='male'):
    self.gender = gender

if __name__ == '__main__':
    test()
