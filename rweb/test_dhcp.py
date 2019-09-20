#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/20 19:08
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
from rweb.path.staticDhcpLease import StaticDHCPLeaseLocators
from rweb.path.dmzHost import DmzHostLocators
from rweb.path.dhcp import DhcpLocators

"""DHCP"""

class Dhcp(Base):
    def setUp(self):
        super(Dhcp, self).setUp()
        # 鼠标模拟移动到：高级设置
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_AdvancedSettings))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_AdvancedSettings)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 Dhcp
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.DHCP))
        ).click()
        time.sleep(2)


    # @unittest.skip("跳过")
    def test_A_dhcp_auto_change(self):
        """DHCP-自动更改网段"""
        # 更改Lan IP
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DhcpLocators.Lan_Ip))
        ).clear()
        self.driver.find_element_by_xpath(DhcpLocators.Lan_Ip).send_keys("192.168.120.254")
        # 模拟鼠标移开焦点，移动到地址池开始ip处
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DhcpLocators.IpPool_StartIp))
        ).click()

        # 断言：地址池开始ip是否自动更改网段
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, DhcpLocators.IpPool_Start_NetwordSegment))
        )
        assert self.driver.find_element_by_xpath(DhcpLocators.IpPool_Start_NetwordSegment).get_attribute("value") == "192.168.120."

        # 断言：地址池结束ip是否自动更改网段
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, DhcpLocators.IpPool_End_NetwordSegment))
        )
        assert self.driver.find_element_by_xpath(DhcpLocators.IpPool_End_NetwordSegment).get_attribute("value") == "192.168.120."




    # @unittest.skip("跳过")
    def test_B_dhcp_save(self):
        """DHCP-保存"""
        # 更改地址池开始IP
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DhcpLocators.IpPool_StartIp))
        ).clear()
        self.driver.find_element_by_xpath(DhcpLocators.IpPool_StartIp).send_keys("110")
        # 更改地址池结束IP
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DhcpLocators.IpPool_EndIp))
        ).clear()
        self.driver.find_element_by_xpath(DhcpLocators.IpPool_EndIp).send_keys("150")
        # 更改租赁时间为1天
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DhcpLocators.Lease_Time))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DhcpLocators.Lease_Time_1day))
        ).click()

        # 保存
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DhcpLocators.Save))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DhcpLocators.Save_Ok))
        ).click()

        # 断言:toast提示：重启成功
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 重启成功后在主页，此时再次进入到DHCP页，目的：检验是否修改成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_AdvancedSettings))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_AdvancedSettings)
        ActionChains(self.driver).move_to_element(mouse).perform()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.DHCP))
        ).click()

        # 断言：地址池开始ip是否已修改为：192.168.127.110
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, DhcpLocators.IpPool_StartIp))
        )
        assert self.driver.find_element_by_xpath(DhcpLocators.IpPool_StartIp).get_attribute("value") == "110"

        # 断言：地址池结束ip是否已修改为：192.168.127.150
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, DhcpLocators.IpPool_EndIp))
        )
        assert self.driver.find_element_by_xpath(DhcpLocators.IpPool_EndIp).get_attribute("value") == "150"

        # 断言：租赁时间是否已修改为：1天
        self.driver.refresh()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, DhcpLocators.Lease_Time))
        )
        Lease_Time_value = self.driver.find_element_by_xpath(DhcpLocators.Lease_Time).get_attribute('value')
        assert Lease_Time_value == "1 day", Lease_Time_value