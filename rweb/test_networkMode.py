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

"""工作方式"""


class NetworkMode(Base):
    def setUp(self):
        super(NetworkMode, self).setUp()
        # 鼠标模拟移动到：高级设置
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_AdvancedSettings))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_AdvancedSettings)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 工作方式
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Network_Mode))
        ).click()
        time.sleep(2)

    # @unittest.skip("跳过")
    def test_A_set_bridge_mode(self):
        """工作方式-切换到桥模式"""
        # 点击 桥模式
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, NetworkModeLocators.Bridge_Mode))
        ).click()
        # 保存
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, NetworkModeLocators.Save))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, NetworkModeLocators.Save_Ok))
        ).click()

        # 断言:toast提示：切换桥模式成功
        WebDriverWait(self.driver, 130).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 重新登录路由器
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "has-icon"))
        ).send_keys(const.PASSWORD)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[1]/div[1]/div[2]/div/div[2]/button"))
        ).click()
        time.sleep(0.5)
        # time.sleep(10)

        # 桥模式下，部分功能不可用。以下只判断三个模块不可用：接入设备、黑名单、端口转发
        # 断言：接入设备 不可用
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Devices))
        )
        print(1111111111)
        print(self.driver.find_element_by_xpath(CommonLocators.Devices).get_attribute('class'))
        assert self.driver.find_element_by_xpath(CommonLocators.Devices).get_attribute(
            'class') == "nav-child__text disabled"

        # 断言：黑名单 不可用
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Blacklist))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Blacklist).get_attribute(
            'class') == "nav-child__text disabled"

        # 断言：端口转发 不可用
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.PortForwarding))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.PortForwarding).get_attribute(
            'class') == "nav-child__text disabled"

    # @unittest.skip("跳过")
    def test_B_set_router_mode(self):
        """工作方式-切换到路由器模式"""
        # 点击 路由器模式
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, NetworkModeLocators.Router_Mode))
        ).click()
        # 保存
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, NetworkModeLocators.Save))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, NetworkModeLocators.Save_Ok))
        ).click()

        # 断言:toast提示：切换路由器模式成功
        WebDriverWait(self.driver, 130).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 重新登录路由器
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "has-icon"))
        ).send_keys(const.PASSWORD)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[1]/div[1]/div[2]/div/div[2]/button"))
        ).click()
        time.sleep(0.5)

        # 路由器模式下，所有功能均可用。以下只判断三个模块可用：接入设备、黑名单、端口转发
        # 断言：接入设备 可用
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Devices))
        )
        print(222222222222)
        print(self.driver.find_element_by_xpath(CommonLocators.Devices).get_attribute('class'))
        assert self.driver.find_element_by_xpath(CommonLocators.Devices).get_attribute('class') == "nav-child__text"

        # 断言：黑名单 可用
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Blacklist))
        )
        print(222222222222)
        print(self.driver.find_element_by_xpath(CommonLocators.Blacklist).get_attribute('class'))
        assert self.driver.find_element_by_xpath(CommonLocators.Blacklist).get_attribute('class') == "nav-child__text"

        # 断言：端口转发 可用
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.PortForwarding))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.PortForwarding).get_attribute(
            'class') == "nav-child__text"
