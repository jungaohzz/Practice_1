#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/21 15:42
# @Author:  GaoJun

import unittest
from .test_base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from . import const
import time
from rweb.path.common import CommonLocators
from rweb.path.devices import DevicesLocators
from rweb.path.limitTime import LimitTimeLocators
from selenium.webdriver.common.action_chains import ActionChains
from rweb.path.staticDhcpLease import StaticDHCPLeaseLocators
from rweb.path.dmzHost import DmzHostLocators
from rweb.path.internetSettings import InternetSettingsLocators
from rweb.path.routerManagement import RouterManagementLocators
from rweb.path.adminPassword import AdminPasswordLocators
from rweb.path.devices import DevicesLocators
from rweb.path.blacklist import BlacklistLocators
from selenium.common.exceptions import NoSuchElementException


"""黑名单"""

class Blacklist(Base):
    def setUp(self):
        super(Blacklist, self).setUp()
        # 鼠标模拟移动到：我的WiFi
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_MyWifi))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_MyWifi)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 接入设备
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Devices))
        ).click()
        time.sleep(1)


    @unittest.skip("跳过")
    def test_A_blacklist_MyWifi(self):
        """黑名单-从主网加入黑名单"""


    @unittest.skip("跳过")
    def test_B_blacklist_Guest(self):
        """黑名单-从访客加入黑名单"""


    # @unittest.skip("跳过")
    def test_C_blacklist_Offline(self):
        """黑名单-从离线加入黑名单"""
        # 进入 离线列表
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, DevicesLocators.Offline))
        ).click()

        time.sleep(2)   #用于切换到离线列表

        try:
            # 如果离线设备列表找不到第一个设备名元素，则该列表为空
            DeviceName_First = self.driver.find_element_by_xpath(DevicesLocators.Offline_DeviceName_First).text
            # 加入黑名单
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, DevicesLocators.Offline_AddToBlacklist))
            ).click()
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, DevicesLocators.Offline_AddToBlacklist_Ok))
            ).click()

            # 断言:toast提示：加入黑名单成功
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

            time.sleep(5)

            # 断言：检验是否从离线列表消失
            """
                这里断言可能有两种情况：
                一、将该设备加入黑名单后，离线列表还有设备
                二、将该设备加入黑名单后，离线列表为空
                第一种情况对比设备名即可，而第二种情况查看设备名元素时会出现查找不到的情况，所以这里也需要try except一下
            """
            # print(DeviceName_First)
            # try:
            #
            #     print(self.driver.find_element_by_xpath(DevicesLocators.Offline_DeviceName_First).text)
            #     assert self.driver.find_element_by_xpath(DevicesLocators.Offline_DeviceName_First).text != DeviceName_First
            # except:
            #     pass
            #DeviceName_First = self.driver.find_element_by_xpath(DevicesLocators.Offline_DeviceName_First).text

            # 断言：检验是否加入黑名单列表中
            # DeviceName_First = self.driver.find_element_by_xpath(DevicesLocators.Offline_DeviceName_First).text
            # 进入 黑名单
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
            )
            mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
            ActionChains(self.driver).move_to_element(mouse).perform()
            # 点击 接入设备
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, CommonLocators.Blacklist))
            ).click()
            time.sleep(1)
            # 断言：加入黑名单前的设备名，与加入黑名单后的设备名是否一致
            print(4444444)
            print(self.driver.find_element_by_xpath(BlacklistLocators.Device_Name).text)
            assert self.driver.find_element_by_xpath(BlacklistLocators.Device_Name).text == DeviceName_First
            print(555555)


        except NoSuchElementException:
            print("离线设备列表为空，暂无法检验从离线列表加入黑名单的功能是否正常！")

            print(2222222)
            #assert 1 == 0       # 该断言用于使该用例失败


