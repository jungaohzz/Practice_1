#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
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
from rweb.path.wifiSettings import WifiSettingsLocators
from rweb.path.routerManagement import RouterManagementLocators
from rweb.path.guestWifi import GuestWifiLocators

"""访客WiFi"""

class GuestWifi(Base):
    def setUp(self):
        super(GuestWifi, self).setUp()
        # 鼠标模拟移动到：设置
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 访客WiFi
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Guest_WiFi))
        ).click()
        time.sleep(2)


    #@unittest.skip("跳过")
    def test_A_guestWifi_on(self):
        """访客WiFi-启用"""
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        # 默认是关闭的
        # 如果是关闭的，才进行下面的if打开操作
        if Statu_class == "switch switch-animation":
            # 点击 启用 按钮

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Satatu))
            ).click()

            # 选择时长：1天
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Active_Time))
            ).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Active_Time_1day))
            ).click()

            # 修改无线名称：AutoTest
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
            ).clear()
            self.driver.find_element_by_xpath(GuestWifiLocators.Name).send_keys("AutoTest")

            # 选择加密方式：WPA/WPA2-PSK
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Encryption))
            ).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Encryption_WPA_WPA2_PSK))
            ).click()

            # 输入密码：11111111
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Password))
            ).clear()

            self.driver.find_element_by_xpath(GuestWifiLocators.Password).send_keys("11111111")

            # 保存
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Save))
            ).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Save_Ok))
            ).click()

        # 断言：保存成功后会访客WiFi的首页，则查看是否有“设置”按钮即可
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Settings))
        )

        # 断言：检查状态是否为开启：
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        assert Statu_class == "switch switch-animation checked", Statu_class



    @unittest.skip("跳过")
    def test_B_guestWifi_off(self):
        """访客WiFi-关闭"""
        time.sleep(2)  # 用于切换按钮
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        # 到这里理应是打开的
        # 如果是打开的，才进行下面的if关闭操作
        if Statu_class == "switch switch-animation checked":
            # 点击 关闭 按钮

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Satatu))
            ).click()

            # 保存
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Save_Ok))
            ).click()

            # 断言：保存成功后会访客WiFi的首页，则查看是否有“设置”按钮即可
            WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Satatu))
            )
            time.sleep(5)
            print(1111111)

        # 断言：检查状态是否为关闭：
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )

        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        print(22222)
        print(Statu_class)
        assert Statu_class == "switch switch-animation", Statu_class
