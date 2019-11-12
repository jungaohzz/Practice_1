#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/20 21:34
# @Author:  GaoJun

import unittest
from .test_base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from rweb.path.common import CommonLocators
from rweb.path.devices import DevicesLocators
from rweb.path.limitTime import LimitTimeLocators
from selenium.webdriver.common.action_chains import ActionChains
from . import const
from rweb.path.staticDhcpLease import StaticDHCPLeaseLocators
from rweb.path.dmzHost import DmzHostLocators
from rweb.path.dhcp import DhcpLocators
from rweb.path.cloneMacAddress import CloneMacAddressLocators
from rweb.path.ddns import DDNSLocators
from rweb.path.networkMode import NetworkModeLocators
from rweb.path.networkDiagnosis import NetworkDiagnosisLocators

"""网络诊断"""


class NetworkDiagnosis(Base):
    def setUp(self):
        super(NetworkDiagnosis, self).setUp()
        # 鼠标模拟移动到：高级设置
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_AdvancedSettings))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_AdvancedSettings)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 网络诊断
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Network_Diagnosis))
        ).click()
        time.sleep(2)

    # @unittest.skip("跳过")
    def test_A_networkDiagnosis_ping(self):
        """网络诊断-ping"""
        # 点击 ping
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, NetworkDiagnosisLocators.Diagnostics_Tools))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, NetworkDiagnosisLocators.Ping))
        ).click()
        # 输入域名：www.baidu.com
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, NetworkDiagnosisLocators.IP_or_DomainName))
        ).send_keys("www.baidu.com")
        # 点击 开始
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, NetworkDiagnosisLocators.Start))
        ).click()
        time.sleep(2)

    # @unittest.skip("跳过")
    def test_B_networkDiagnosis_traceroute(self):
        """网络诊断-traceroute"""
        # 点击 traceroute
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, NetworkDiagnosisLocators.Diagnostics_Tools))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, NetworkDiagnosisLocators.Traceroute))
        ).click()
        # 输入域名：www.baidu.com
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, NetworkDiagnosisLocators.IP_or_DomainName))
        ).send_keys("www.baidu.com")
        # 点击 开始
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, NetworkDiagnosisLocators.Start))
        ).click()
        time.sleep(2)

    # @unittest.skip("跳过")
    def test_C_networkDiagnosis_nslookup(self):
        """网络诊断-nslookup"""
        # 点击 nslookup
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, NetworkDiagnosisLocators.Diagnostics_Tools))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, NetworkDiagnosisLocators.Nslookup))
        ).click()
        # 输入域名：www.baidu.com
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, NetworkDiagnosisLocators.IP_or_DomainName))
        ).send_keys("www.baidu.com")
        # 点击 开始
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, NetworkDiagnosisLocators.Start))
        ).click()
        time.sleep(2)
