# # -*-coding:utf8 -*-
import unittest
from BeautifulReport import BeautifulReport
from .test_user import User
from unittest import TestLoader


def core():
    s = []
    class_tests = [
        User
    ]

    for t in class_tests:
        suite = TestLoader().loadTestsFromTestCase(t)
        s.append(suite)

    t_s = unittest.TestSuite(s)
    return t_s


if __name__ == "__main__":
    t_suites = core()

    result = BeautifulReport(t_suites)
    result.report(filename='新增用户-测试报告', description='测试deafult报告', log_path='report')
