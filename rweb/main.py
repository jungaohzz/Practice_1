#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun


from BeautifulReport import BeautifulReport
import unittest
import os
from unittest import TestLoader
from .test_language import Language
from .test_routerManagement import RouterManagement
from .test_timeZone import TimeZone
from .test_limitTime import LimitTime
from .test_limitRate import LimitRate
from .test_limitWebsiteBlacklist import LimitWebsiteBlacklist
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
from .test_internetSettings import InternetSettings
from .test_adminPassword import AdminPassword
from .test_blacklist import Blacklist
from .test_guestWifi import GuestWifi
from .test_vpn import VPN
from .test_devices import Devices


def core():
    s = []
    class_tests = [
        # 建议执行顺序（倒序排如下）：
        # 管理路由器、管理密码、工作方式、限时（？如果被限制住未删掉情况怎么处理）
        # LimitTime, LimitRate,LimitWebsiteBlacklist
        GuestWifi, VPN, RouterManagement
    ]
    for t in class_tests:
        suite = TestLoader().loadTestsFromTestCase(t)
        s.append(suite)
    t_s = unittest.TestSuite(s)
    return t_s


if __name__ == "__main__":
    t_suites = core()
    result = BeautifulReport(t_suites)
    log_path = 'report/rweb'
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    result.report(filename="路由器Web自动化测试",
                  description="路由器Web自动化测试报告",
                  log_path=log_path)
