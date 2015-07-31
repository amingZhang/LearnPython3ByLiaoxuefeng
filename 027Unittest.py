#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __author__ = 'zhang.c.m'

class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

import unittest

class TestDict(unittest.TestCase):
    def setUp(self):
        print('setUp:在每一个测试方法之前执行，可用于构造环境，打开数据库等功能')

    def tearDown(self):
        print('tearDown:在每一个测试方法之后执行，可用于析构环境，关闭数据库等功能')

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_key_error(self):
        d = Dict()
        with self.assertRaises(KeyError):  # 期待抛出指定类型的Error
            value = d['empty']

    def test_attr_error(self):
        d = Dict()
        with self.assertRaises(AttributeError):  # 期待抛出指定类型的Error
            value = d.empty

if __name__ == '__main__':
    unittest.main()  # 运行测试用例