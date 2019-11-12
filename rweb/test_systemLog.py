#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/20 23:08
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
from rweb.path.systemLog import SystemLogLocators

"""路由器日志"""


class SystemLog(Base):
    def setUp(self):
        super(SystemLog, self).setUp()
        # 鼠标模拟移动到：高级设置
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_AdvancedSettings))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_AdvancedSettings)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 路由器日志
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.System_Log))
        ).click()
        time.sleep(2)

    # @unittest.skip("跳过")
    def test_A_systemLog_on(self):
        """路由器日志-开启"""
        # 默认状态：关闭
        # 如果状态为：关闭，才进行if的打开操作
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, SystemLogLocators.Statu))
        )
        Statu_class = self.driver.find_element_by_xpath(SystemLogLocators.Statu).get_attribute('class')
        if Statu_class == "switch switch-animation":
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, SystemLogLocators.Statu))
            ).click()
            time.sleep(2)  # 用于切换开关

        # 到这里，无论是否执行if，开关状态都是：开启

        # 断言：开启了日志，就应该有日志内容
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, SystemLogLocators.SystemLog_Text))
        )
        assert self.driver.find_element_by_xpath(SystemLogLocators.SystemLog_Text).text != ""

    # @unittest.skip("跳过")
    def test_B_systemLog_off(self):
        """路由器日志-关闭"""
        # 如果状态为：打开，才进行if的关闭操作
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, SystemLogLocators.Statu))
        )
        Statu_class = self.driver.find_element_by_xpath(SystemLogLocators.Statu).get_attribute('class')
        if Statu_class == "switch switch-animation checked":
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, SystemLogLocators.Statu))
            ).click()
            time.sleep(2)  # 用于切换开关

        # 到这里，无论是否执行if，开关状态都是：关闭

        # 断言：开启了日志，就应该没有日志内容
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, SystemLogLocators.SystemLog_Text))
        )
        assert self.driver.find_element_by_xpath(SystemLogLocators.SystemLog_Text).text == ""
