#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun


import unittest
from BeautifulReport import BeautifulReport


def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def multi(a, b):
    return a * b


def divide(a, b):
    return a / b


class TestMath(unittest.TestCase):

    def test_math_add(self):
        '''加法'''
        self.assertEqual(3, add(1, 2))

    def test_math_min(self):
        '''减法'''
        self.assertEqual(1, minus(2, 1))

    def test_math_mul(self):
        '''乘法'''
        self.assertEqual(2, multi(1, 2))

    @unittest.skipIf()
    def test_math_div(self):
        '''除法'''
        self.assertEqual(1, divide(2, 1))


if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [
        TestMath("test_math_add"),
        TestMath("test_math_min"),
        TestMath("test_math_div"),
        TestMath("test_math_mul")
    ]
    suite.addTests(tests)
    result = BeautifulReport(suite)
    result.report(filename='调试报告', description='测试deafult报告', log_path='report')