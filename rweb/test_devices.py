#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun


import unittest
import time
from selenium import webdriver
from .test_base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from . import const
import re  # 正则表达式

from rweb.path.common import CommonLocators
from rweb.path.devices import DevicesLocators
from rweb.path.limitTime import LimitTimeLocators
from rweb.path.limitRate import LimitRateLocators
from rweb.path.websiteBlacklist import WebsiteBlacklistLocators


class Devices(Base):

    def setUp(self):
        super(Devices, self).setUp()
        # 鼠标移动到切换“我的WiFi”按钮上
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_MyWifi))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_MyWifi)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 接入设备
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Devices))
        ).click()
        self.driver.refresh()

    @unittest.skip("跳过")
    def test_A_devices_elementCheck(self):
        """接入设备-设备列表字段检查"""
        """
        用例-1853 : 设备列表字段显示正确且完整
                    查看设备列表字段包括：设备名称、实时速率、消耗流量、IP地址/MAC地址、家长控制、操作 ： 是
        """
        # 断言：设备列表字段包括：设备名称
        Device_Name = DevicesLocators.MyWifi_Table_Head.format(num=1)
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, Device_Name))
        )
        Device_Name_Text = self.driver.find_element_by_xpath(Device_Name).text
        assert Device_Name_Text == "Device", Device_Name_Text

        # 断言：设备列表字段包括：实时速率
        Realtime_Speed = DevicesLocators.MyWifi_Table_Head.format(num=2)
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, Realtime_Speed))
        )
        Realtime_Speed_Text = self.driver.find_element_by_xpath(Realtime_Speed).text
        assert Realtime_Speed_Text == "Realtime speed", Realtime_Speed_Text

        # 断言：设备列表字段包括：消耗流量
        Device_Throughput = DevicesLocators.MyWifi_Table_Head.format(num=3)
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, Device_Throughput))
        )
        Device_Throughput_Text = self.driver.find_element_by_xpath(Device_Throughput).text
        assert Device_Throughput_Text == "Device throughput", Device_Throughput_Text

        # 断言：设备列表字段包括：IP地址/MAC地址
        Ip_Mac = DevicesLocators.MyWifi_Table_Head.format(num=4)
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, Ip_Mac))
        )
        Ip_Mac_Text = self.driver.find_element_by_xpath(Ip_Mac).text
        assert Ip_Mac_Text == "IP / MAC", Ip_Mac_Text

        # 断言：设备列表字段包括：家长控制
        Parental_Controls = DevicesLocators.MyWifi_Table_Head.format(num=5)
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, Parental_Controls))
        )
        Parental_Controls_Text = self.driver.find_element_by_xpath(Parental_Controls).text
        assert Parental_Controls_Text == "Parental controls", Parental_Controls_Text

        # 断言：设备列表字段包括：操作
        Actions = DevicesLocators.MyWifi_Table_Head.format(num=6)
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, Actions))
        )
        Actions_Text = self.driver.find_element_by_xpath(Actions).text
        assert Actions_Text == "Actions", Actions_Text

    # @unittest.skip("跳过")
    def test_A_devices_wired_elementCheck(self):
        """接入设备-有线设备接入-元素检查"""
        """
        用例-1849 : 设备有线接入，显示在列表中
        用例-1856 : 有线接入的设备，图标显示为有线图标
                    接入有线设备，查看图标显示 ： 显示为有线图标
        用例-1860 : 设备有线接入，显示“有线”标识
                    有线设备接入路由器，查看是否显示“有线”标识 ： 是
        用例-1854 : 单条设备元素检测
                    查看 设备名称 字段包含的元素：图标、连接类型标识、设备名称、接入时长、编辑按钮
                    查看 IP字段包含的元素：ip地址
                    查看 MAC 字段包含的元素：mac地址
                    查看 实时速率 字段包含的元素：上行图标 + 上行速率、下行图片 + 下行速率
                    查看 流量消耗 字段包含的元素：消耗的流量值
                    查看 限制 字段包含的元素：限时图标、限速图标、网址黑名单图标
                    查看 操作 字段包含的元素：“设置”文本、“加入黑名单”文本
        用例-1879 : IP地址显示格式为xx.xx.xx.xx
                    查看ip地址的格式 ： 显示为：xx.xx.xx.xx
        用例-1883 : MAC地址显示格式为xx.xx.xx.xx.xx.xx
                    查看mac地址的格式 ： 显示为：xx.xx.xx.xx.xx.xx（大写，有冒号）
        """
        time.sleep(1)
        # 断言：用例-1849 : 设备有线接入，显示在列表中
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='table-inner']/div[2]/div[1]"))
        )
        assert self.driver.find_element_by_xpath("//div[@class='table-inner']/div[2]/div[1]").is_displayed()

        # 断言：用例-1854 : 单条设备元素检测
        # 断言：设备名称 字段包含元素：图标
        # 断言：设备名称 字段包含元素：连接类型标识
        # 断言：用例-1856 : 有线接入的设备，图标显示为有线图标
        # 断言：用例-1860 : 设备有线接入，显示“有线”标识
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, DevicesLocators.MyWifi_Access_Icon))
        )
        MyWifi_Access_Icon_Text = self.driver.find_element_by_xpath(DevicesLocators.MyWifi_Access_Icon).text
        assert MyWifi_Access_Icon_Text == "Wired", MyWifi_Access_Icon_Text

        # 断言：设备名称 字段包含元素：设备名称
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, DevicesLocators.MyWifi_List_Name))
        )
        assert self.driver.find_element_by_xpath(DevicesLocators.MyWifi_List_Name).is_displayed()

        # 断言：设备名称 字段包含元素：接入时长 -> 未检验，因为有线连接没有接入时长

        # 断言：设备名称 字段包含元素：编辑按钮
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, DevicesLocators.MyWifi_List_Name_Edit))
        )
        assert self.driver.find_element_by_xpath(DevicesLocators.MyWifi_List_Name_Edit).is_displayed()

        # 断言：IP字段包含的元素：ip地址
        # 断言：用例-1879 : IP地址显示格式为xx.xx.xx.xx
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, DevicesLocators.MyWifi_List_Ip))
        )
        Ip = self.driver.find_element_by_xpath(DevicesLocators.MyWifi_List_Ip).text[0:15]
        assert re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", Ip), Ip

        # 断言：MAC 字段包含的元素：mac地址
        # 断言：用例-1883 : MAC地址显示格式为xx.xx.xx.xx.xx.xx
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, DevicesLocators.MyWifi_List_Mac))
        )
        Mac = self.driver.find_element_by_xpath(DevicesLocators.MyWifi_List_Mac).text
        assert re.match(r"^\s*([0-9a-fA-F]{2,2}:){5,5}[0-9a-fA-F]{2,2}\s*$", Mac), Mac

        # 断言：实时速率 字段包含元素：上行图标 + 上行速率
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='table-inner']/div[2]/div/ul/li[2]/div/div[1]/img"))
        )
        assert self.driver.find_element_by_xpath(
            "//div[@class='table-inner']/div[2]/div/ul/li[2]/div/div[1]/img").is_displayed()
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, DevicesLocators.MyWifi_List_Speed_Uplink))
        )
        assert self.driver.find_element_by_xpath(DevicesLocators.MyWifi_List_Speed_Uplink).is_displayed()

        # 断言：实时速率 字段包含元素：下行图片 + 下行速率
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='table-inner']/div[2]/div/ul/li[2]/div/div[2]/img"))
        )
        assert self.driver.find_element_by_xpath(
            "//div[@class='table-inner']/div[2]/div/ul/li[2]/div/div[2]/img").is_displayed()
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, DevicesLocators.MyWifi_List_Speed_Downlink))
        )
        assert self.driver.find_element_by_xpath(DevicesLocators.MyWifi_List_Speed_Downlink).is_displayed()

        # 断言：流量消耗 字段包含的元素：消耗的流量值
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, DevicesLocators.MyWifi_List_DeviceThroughput))
        )
        assert self.driver.find_element_by_xpath(DevicesLocators.MyWifi_List_DeviceThroughput).is_displayed()

        # 断言：限制 字段包含的元素：限时图标
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, DevicesLocators.Limit_Time_Icon))
        )
        assert self.driver.find_element_by_xpath(DevicesLocators.Limit_Time_Icon).is_displayed()

        # 断言：限制 字段包含的元素：限速图标
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, DevicesLocators.Limit_Rate_Icon))
        )
        assert self.driver.find_element_by_xpath(DevicesLocators.Limit_Rate_Icon).is_displayed()

        # 断言：限制 字段包含的元素：网址黑名单图标
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, DevicesLocators.Limit_WebsiteBlacklist_Icon))
        )
        assert self.driver.find_element_by_xpath(DevicesLocators.Limit_WebsiteBlacklist_Icon).is_displayed()

        # 断言：查看 操作 字段包含的元素：“设置”文本
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, DevicesLocators.Set))
        )
        Set_Text = self.driver.find_element_by_xpath(DevicesLocators.Set).text
        assert Set_Text == "Settings", Set_Text

        # 断言：查看 操作 字段包含的元素：“加入黑名单”文本
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, DevicesLocators.AddtoBlacklist))
        )
        AddtoBlacklist_Text = self.driver.find_element_by_xpath(DevicesLocators.AddtoBlacklist).text
        assert AddtoBlacklist_Text == "Add to Blacklist", AddtoBlacklist_Text
