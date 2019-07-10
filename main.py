# # -*-coding:utf8 -*-
import unittest
from BeautifulReport import BeautifulReport

from a import Test1

from a import Test2


if __name__ == "__main__":

    # 先构造测试集，即实例化测试套件
    suite = unittest.TestSuite()

    #将用例加载到测试套件中，顺序：1 -> 3 -> 2 -> 4
    suite.addTest(Test1('test_1_status_code'))
    suite.addTest(Test1('test_3_url'))
    suite.addTest(Test1('test_2_reason'))

    suite.addTest(Test2('test_1_username'))
    suite.addTest(Test2('test_3_connection'))



    result = BeautifulReport(suite)
    result.report(filename='测试报告', description='测试deafult报告', log_path='report')