#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __author__ = 'zhang.c.m'

# Python提供了pickle模块来实现序列化。
import pickle
d = dict(name='bob', age=20, score=88)
dumped_bytes = pickle.dumps(d)  # pickle.dumps()方法把任意对象序列化成一个bytes
print(dumped_bytes)
loaded_d = pickle.loads(dumped_bytes)  # pickle.loads()方法反序列化出对象
print(loaded_d)

f = open('dump.txt', 'wb')
pickle.dump(d, f)  # pickle.dump()直接把对象序列化后写入一个file-like Object
f.close()

f = open('dump.txt', 'rb')
new_d = pickle.load(f)  # pickle.load()方法从一个file-like Object中直接反序列化出对象
f.close()
print(new_d)

# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换
import json

dumped_json = json.dumps(d)
print(dumped_json)
loaded_json = json.loads(dumped_json)
print(loaded_json)

f = open('json_dump.txt', 'w')  # 注意json是str操作，不是bytes
json.dump(d, f)
f.close()

f = open('json_dump.txt', 'r')  # 注意json是str操作，不是bytes
new_d_from_json = json.load(f)
f.close()
print(new_d_from_json)

# 对class类进行序列化
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(student):
    return {
        'name': student.name,
        'age': student.age,
        'score': student.score
    }

s = Student('adam', 18, 99)
dumped_json = json.dumps(s, default=student2dict)
print(dumped_json)

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

s = json.loads(dumped_json, object_hook=dict2student)
print(s)

# 利用class的__dict__转换class
print('利用class的__dict__转换class')
dumped_json = json.dumps(s, default=lambda obj: obj.__dict__)
print(dumped_json)
