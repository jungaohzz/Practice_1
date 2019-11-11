#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/20 20:32
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
from rweb.path.cloneMacAddress import CloneMacAddressLocators
from rweb import const

"""MAC地址克隆"""

class CloneMacAddress(Base):
    def setUp(self):
        super(CloneMacAddress, self).setUp()
        # 鼠标模拟移动到：高级设置
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_AdvancedSettings))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_AdvancedSettings)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 MAC地址克隆
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Clone_MAC_Address))
        ).click()
        time.sleep(2)


    # @unittest.skip("跳过")
    def test_A_custom_mac(self):
        """MAC地址克隆-自定义Mac地址"""
        # 点击按钮 自定义MAC地址
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CloneMacAddressLocators.Custom_Mac_Button))
        ).click()

        #输入自定义的Mac地址：f8:27:2e:01:1a:e1
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CloneMacAddressLocators.Custom_Mac))
        ).clear()
        self.driver.find_element_by_xpath(CloneMacAddressLocators.Custom_Mac).send_keys("f8:27:2e:01:1a:e1")

        # 点击 保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CloneMacAddressLocators.Save))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CloneMacAddressLocators.Save_Ok))
        ).click()

        # 断言:toast提示：重启成功
        WebDriverWait(self.driver, const.REBOOT_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        self.driver.refresh()
        # 断言：是否将自定义Mac地址设置为了：f8:27:2e:01:1a:e1
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CloneMacAddressLocators.Custom_Mac))
        )
        Custom_Mac_value = self.driver.find_element_by_xpath(CloneMacAddressLocators.Custom_Mac).get_attribute('value')
        assert Custom_Mac_value == "f8:27:2e:01:1a:e1", Custom_Mac_value