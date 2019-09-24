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

    # @unittest.skip("跳过")
    def test_A_set_FireWall(self):
        """设置 防火墙"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, FireWallLocators.Firewall_Statu))
        )
        Firewall_Statu_class = self.driver.find_element_by_xpath(FireWallLocators.Firewall_Statu).get_attribute('class')
        # 默认状态：关闭
        # 如果状态为：关闭，才进行打开操作
        if Firewall_Statu_class == "switch switch-animation":
            # 打开防火墙
            time.sleep(1)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, FireWallLocators.Firewall_Statu))
            ).click()
            # 断言:toast提示：打开成功
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
            time.sleep(2)

        else:
            time.sleep(2)  # 用于按钮切换

        # 到这一步，无论是否执行了if，状态都为：打开

        # 断言：判断开关是否开启
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, FireWallLocators.Firewall_Statu))
        )
        Firewall_Statu_class = self.driver.find_element_by_xpath(FireWallLocators.Firewall_Statu).get_attribute('class')
        assert Firewall_Statu_class == "switch switch-animation checked", Firewall_Statu_class


        # 关闭防火墙
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, FireWallLocators.Firewall_Statu))
        ).click()
        # 断言:toast提示：关闭成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        #time.sleep(2)  # 用于按钮切换
        # 断言：判断开关是否关闭
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, FireWallLocators.Firewall_Statu))
        )
        Firewall_Statu_class = self.driver.find_element_by_xpath(FireWallLocators.Firewall_Statu).get_attribute('class')
        assert Firewall_Statu_class == "switch switch-animation", Firewall_Statu_class

    @unittest.skip("跳过")
    def test_B_set_WanPing(self):
        """设置 WAN ping"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, FireWallLocators.WAN_Ping_Statu))
        )
        WanPing_Statu_class = self.driver.find_element_by_xpath(FireWallLocators.WAN_Ping_Statu).get_attribute('class')
        # 默认状态：打开
        # 如果状态为：打开，才进行关闭操作
        if WanPing_Statu_class == "switch switch-animation checked":
            # 关闭WAN ping
            time.sleep(1)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, FireWallLocators.WAN_Ping_Statu))
            ).click()
            # 断言:toast提示：关闭成功
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
            time.sleep(2)

        else:
            time.sleep(2)  # 用于按钮切换

        # 到这一步，无论是否执行了if，状态都为：关闭

        # 断言：判断开关是否关闭
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, FireWallLocators.WAN_Ping_Statu))
        )
        WanPing_Statu_class = self.driver.find_element_by_xpath(FireWallLocators.WAN_Ping_Statu).get_attribute('class')
        assert WanPing_Statu_class == "switch switch-animation", WanPing_Statu_class

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
        WanPing_Statu_class = self.driver.find_element_by_xpath(FireWallLocators.WAN_Ping_Statu).get_attribute('class')
        assert WanPing_Statu_class == "switch switch-animation checked", WanPing_Statu_class
