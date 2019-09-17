#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun

import unittest
from selenium import webdriver
import time
from BeautifulReport import BeautifulReport
from .test_my_wifi import MyWifi
from unittest import TestLoader



def core():
    s = []
    class_tests = [MyWifi]
    for t in class_tests:
        suite = TestLoader().loadTestsFromTestCase(t)
        s.append(suite)

    t_s = unittest.TestSuite(s)
    return t_s


if __name__ == '__main__':
    t_suites = core()
    result = BeautifulReport(t_suites)
    result.report(filename="WebUI-调试",
                  description='Router-UiAuto测试报告',
                  log_path='report/')
