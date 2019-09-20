#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/19 23:23
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
from rweb.path.fireWall import FireWallLocators

"""防火墙"""
class FireWall(Base):

    def setUp(self):
        super(FireWall, self).setUp()
        # 鼠标模拟移动到：高级设置
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_AdvancedSettings))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_AdvancedSettings)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 防火墙
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Firewall))
        ).click()
        time.sleep(1)


    def test_A_set_FireWall(self):
        """设置 防火墙"""
        # 打开防火墙
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, FireWallLocators.Firewall_Statu))
        ).click()
        # 断言:toast提示：打开成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言：判断开关是否开启
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, FireWallLocators.Firewall_Statu))
        )
        assert self.driver.find_element_by_xpath(FireWallLocators.Firewall_Statu).get_attribute('class') == "switch switch-animation checked"


        # 关闭防火墙
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, FireWallLocators.Firewall_Statu))
        ).click()
        # 断言:toast提示：关闭成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言：判断开关是否关闭
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, FireWallLocators.Firewall_Statu))
        )
        assert self.driver.find_element_by_xpath(FireWallLocators.Firewall_Statu).get_attribute(
            'class') == "switch switch-animation"


    def test_B_set_WanPing(self):
        """设置 WAN ping"""
        # 关闭WAN ping
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, FireWallLocators.WAN_Ping_Statu))
        ).click()
        # 断言:toast提示：关闭成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言：判断开关是否关闭
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, FireWallLocators.WAN_Ping_Statu))
        )
        assert self.driver.find_element_by_xpath(FireWallLocators.WAN_Ping_Statu).get_attribute(
            'class') == "switch switch-animation"

        # 打开WAN ping
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, FireWallLocators.WAN_Ping_Statu))
        ).click()
        # 断言:toast提示：打开成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言：判断开关是否开启
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, FireWallLocators.WAN_Ping_Statu))
        )
        assert self.driver.find_element_by_xpath(FireWallLocators.WAN_Ping_Statu).get_attribute(
            'class') == "switch switch-animation checked"
