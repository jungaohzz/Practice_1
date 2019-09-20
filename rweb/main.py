#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun


from BeautifulReport import BeautifulReport
import unittest
import os
from unittest import TestLoader
from .test_timeZone import TimeZone
from .test_language import Language
from .test_limit import Limit
from .test_portForwarding import PortForwarding
from .test_staticDhcpLease import StaticDHCPLease
from .test_dmzHost import DmzHost
from .test_fireWall import FireWall
from .test_dhcp import Dhcp
from .test_cloneMacAddress import CloneMacAddress
from .test_ddns import DDNS
from .test_networkMode import NetworkMode
from .test_networkDiagnosis import NetworkDiagnosis
from .test_systemLog import SystemLog
from .test_wifiSettings import WifiSettings



def core():
    s = []
    class_tests = [
        # 注：模式切换最好最后执行，因为如果失败将导致其它用例全部出错
        WifiSettings
    ]
    
    
    
    for t in class_tests:
        suite = TestLoader().loadTestsFromTestCase(t)
        s.append(suite)
    t_s = unittest.TestSuite(s)
    return t_s


if __name__ == "__main__":
    t_suites = core()
    result = BeautifulReport(t_suites)
    log_path = 'report/api/rweb'
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    result.report(filename="路由器UI自动化测试",
                  description="路由器UI自动化测试报告",
                  log_path=log_path)
