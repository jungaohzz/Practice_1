#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/20 23:59
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

"""WiFi设置"""

class WifiSettings(Base):
    def setUp(self):
        super(WifiSettings, self).setUp()
        # 鼠标模拟移动到：设置
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 WiFi设置
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.WiFi_Settings))
        ).click()
        time.sleep(2)


    @unittest.skip("跳过")
    def test_A_wifiSetting_changePassword(self):
        """WiFi设置-修改WiFi密码为各种字符组合"""
        # 密码框，输入各种组合，如：abc~!@#$%^123
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.WiFi_Password))
        ).clear()
        self.driver.find_element_by_xpath(WifiSettingsLocators.WiFi_Password).send_keys("abc~!@#$%^123")
        # 保存
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Save))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Save_Ok))
        ).click()
        time.sleep(5)

        # 因为修改密码后没有成功的toast提示，所以不能用成功的toast提示判断是否完成reboot
        # 又因为reboot完成后，页面处于：我的WiFi-管理路由器，故可借判断管理路由器页的“mesh拓扑图”元素是否加载出来，来判断是否完成reboot
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Mesh_Topology))
        )
        time.sleep(10)
        # 断言：判断密码是否是修改的各种组合密码：abc~!@#$%^123
        # 再次进入 WiFi设置 页
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 WiFi设置
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.WiFi_Settings))
        ).click()
        time.sleep(2)
        # 判断密码
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.WiFi_Password))
        )
        assert self.driver.find_element_by_xpath(WifiSettingsLocators.WiFi_Password).get_attribute("value") =="abc~!@#$%^123"




    # @unittest.skip("跳过")
    def test_B_wifiSetting_SmartConnect(self):
        """WiFi设置-修改双频合一开关：由开->关"""

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute('class')
        # 默认状态：打开
        # 如果状态为：打开，才进行if的关闭操作
        if Smart_Connect_class == "switch switch-animation checked":
            # 点击按钮：双频合一，即由开 -> 关
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Smart_Connect))
            ).click()
            time.sleep(2)   #用于开关切换

            # 保存
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Save))
            ).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Save_Ok))
            ).click()
            time.sleep(5)

            # 因为修改密码后没有成功的toast提示，所以不能用成功的toast提示判断是否完成reboot
            # 又因为reboot完成后，页面处于：我的WiFi-管理路由器，故可借判断管理路由器页的“mesh拓扑图”元素是否加载出来，来判断是否完成reboot
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Mesh_Topology))
            )
            time.sleep(10)
            # 断言：判断开关状态是否为：关闭
            # 再次进入 WiFi设置 页
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
            )
            mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
            ActionChains(self.driver).move_to_element(mouse).perform()
            # 点击 WiFi设置
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, CommonLocators.WiFi_Settings))
            ).click()
            time.sleep(2)
        # 判断双频合一开关
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Smart_Connect))
        )
        assert self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute('class') == "switch switch-animation"
