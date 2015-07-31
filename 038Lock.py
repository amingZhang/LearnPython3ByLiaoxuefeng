#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __author__ = 'zhang.c.m'

import time, threading

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):  # 次数达到绝对多的时候，不加锁的操作就会把全局变量改乱
        lock.acquire()  # 先要获取锁:
        try:
            change_it(n)  # 放心地改吧:
        finally:
            lock.release()  # 改完了一定要释放锁:

t1 = threading.Thread(target=run_thread, args=(5005,))
t2 = threading.Thread(target=run_thread, args=(8008,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
