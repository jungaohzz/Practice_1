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

from rweb.path.common import CommonLocators
from rweb.path.devices import DevicesLocators
from rweb.path.limitTime import LimitTimeLocators
from rweb.path.limitRate import LimitRateLocators
from rweb.path.websiteBlacklist import WebsiteBlacklistLocators



class LimitWebsiteBlacklist(Base):

    def setUp(self):
        super(LimitWebsiteBlacklist, self).setUp()
        # 鼠标移动到切换“我的WiFi”按钮上
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_MyWifi))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_MyWifi)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 接入设备
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Devices))
        ).click()
        self.driver.refresh()
        # 点击主网-设置
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DevicesLocators.Set))
        ).click()
        # 切换到网址黑名单页
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Page_WebsiteBlacklist))
        ).click()


    @unittest.skip("跳过")
    def test_A_limitWebsiteBlacklist_add(self):
        """网址黑名单-新增"""
        # 点击黑名单 新增 按钮
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Add))
        ).click()
        # 输入：www.baidu.com
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).send_keys("www.baidu.com")
        # 完成添加
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Save))
        ).click()
        # 断言:toast提示：添加成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言:判断添加的网址是否是：www.baidu.com
        self.driver.refresh()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.List_Website))
        )
        assert self.driver.find_element_by_xpath(WebsiteBlacklistLocators.List_Website).text == "www.baidu.com"



    @unittest.skip("跳过")
    def test_B_limitWebsiteBlacklist_statu_on(self):
        """网址黑名单-修改状态：由关变为开"""
        # 状态理应为关闭，如果为关闭状态才进行if的启用操作
        Statu_class = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Statu).get_attribute('class')
        if Statu_class == "switch switch-animation":
            # 打开网址黑名单开关
            time.sleep(1)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Statu))
            ).click()
            # 断言:toast提示：打开开关成功
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        self.driver.refresh()
        time.sleep(2)   #用于状态按钮切换
        # 断言：判断开关是否开启
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Statu))
        )
        Statu_class = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Statu).get_attribute('class')
        assert Statu_class == "switch switch-animation checked", Statu_class



    @unittest.skip("跳过")
    def test_C_limitWebsiteBlacklist_statu_off(self):
        """网址黑名单-修改状态：由开变为关"""
        # 状态理应为开启，如果为开启状态才进行if的关闭操作
        Statu_class = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Statu).get_attribute('class')
        if Statu_class == "switch switch-animation checked":
            # 关闭网址黑名单开关
            time.sleep(1)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Statu))
            ).click()
            # 断言:toast提示：关闭开关成功
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        self.driver.refresh()
        # 断言：判断开关是否关闭
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Statu))
        )
        Statu_class = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Statu).get_attribute('class')
        assert Statu_class == "switch switch-animation", Statu_class



    #@unittest.skip("跳过")
    def test_D_limit_WebsiteBlacklist(self):
        """网址黑名单-删除"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Delete))
        ).click()

        # 断言:toast提示：删除成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"