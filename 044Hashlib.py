#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __author__ = 'zhang.c.m'

import hashlib
import re
import json
import os

db = {}

def get_md5(password):
    '''
    由于常用口令的MD5值很容易被计算出来，
    所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，
    这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”：
    :param password:
    :return: hexdigest of md5
    '''
    password += 'the-Salt'
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

def register(name, password):
    db[name] = get_md5(password)

def login(name, password):
    if db[name] == get_md5(password):
        return True
    return False

def did_name_existed(name):
    return db.get(name)

def is_name_correct(name):
    return re.match(r'[0-9a-zA-Z\_]+', name)

def test():
    print('*****先注册用户*****')
    while True:
        name = input('输入注册用户名(请使用数字、英文字母或下划线)：')
        if did_name_existed(name):
            print('用户名已经存在！')
            continue
        if not is_name_correct(name):
            print('用户名格式不对！')
            continue
        password = input('输入密码：')
        register(name, password)
        command = input('输入r，继续注册，其它任意键退出注册：')
        if command.lower() == 'r':
            continue
        else:
            break

    print('*****用户登录*****')
    while True:
        name = input('输入用户名：')
        if not did_name_existed(name):
            print('用户名不存在！')
            continue
        password = input('输入密码：')
        if login(name, password):
            print('Welcome', name)
        else:
            print('密码错误！')
        command = input('输入r，继续测试登入，其它任意键退出：')
        if command.lower() == 'r':
            continue
        else:
            break

    print('*****看看数据库中保存的数据啦*****')
    print(db)

if __name__ == '__main__':
    file_name = r'./name_pwd.txt'
    if os.path.exists(file_name):  # 文件存在
        # 先从文件载入数据库，json格式
        f = open(file_name, 'r')
        try:
            db = json.load(f)
        except:
            db = {}
        finally:
            f.close()

    # 测试：
    test()

    # 将数据库内容写入文件
    f = open(file_name, 'w')
    try:
        json.dump(db, f)
    finally:
        f.close()
