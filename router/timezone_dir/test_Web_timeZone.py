#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun


from ..base import Base
import unittest
from rweb import const
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from rweb.path.common import CommonLocators
from rweb.path.timeZone import TimeZoneLocators
from .timezone_testcase import Test_timezone


class TimeZone(Base):

    def setUp(self):
        super(TimeZone, self).setUp()
        # 鼠标移动到切换“设置”按钮上
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 时区
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Timezone))
        ).click()
        self.driver.refresh()

    # @unittest.skip("跳过")
    def test_A_timeZone_Chinese(self):
        """操作步骤：修改时区为中国时区"""
        # 点击 时区框
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, TimeZoneLocators.TimeZone))
        ).click()
        # 选择 中国时区
        TimeZone_Chinese = TimeZoneLocators.TimeZone_All.format(num=49)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, TimeZone_Chinese))
        ).click()
        # 点击 保存
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, TimeZoneLocators.Save))
        ).click()
        # 断言:toast提示：保存成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
        time.sleep(1)

    # @unittest.skip("跳过")
    def test_B_timeZone_1(self):
        """【检验】用例-4833 : 修改系统时区为时区A后，系统时间为时区A时间"""
        # 前提条件：将时区修改为中国时区：(GMT+08:00)北京、重庆、香港、乌鲁木齐

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))
        )
        Timezone_Value = self.driver.find_element_by_tag_name("input").get_attribute('value')
        if Timezone_Value != "(GMT+08:00)Beijing, Chongqing, Hong Kong, Urumqi":
            print("【备注】该用例无法验证，原因：Web端时区未修改为：(GMT+08:00)北京、重庆、香港、乌鲁木齐")
            assert False

        # 前提检验完成，开始检验用例
        time.sleep(5)
        result = Test_timezone.test_timezone_1()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    # @unittest.skip("跳过")
    def test_C_timeZone_Eastern(self):
        """操作步骤：将时区恢复默认的东部时间"""
        # 点击 时区框
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, TimeZoneLocators.TimeZone))
        ).click()
        # 选择 东部时间
        TimeZone_Eastern = TimeZoneLocators.TimeZone_All.format(num=12)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, TimeZone_Eastern))
        ).click()
        # 点击 保存
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, TimeZoneLocators.Save))
        ).click()
        # 断言:toast提示：保存成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
        time.sleep(1)

    # 路由器未实现该功能
    # #@unittest.skip("跳过")
    # def test_D_timeZone_1(self):
    #     """【检验】用例-4834：默认情况下，系统时间正确"""
    #
    #     # 前提条件：Web端时区默认应该是：(GMT-05:00)东部时间(美国和加拿大)
    #     WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.TAG_NAME, "input"))
    #     )
    #     Timezone_Value = self.driver.find_element_by_tag_name("input").get_attribute('value')
    #     assert Timezone_Value == "(GMT-05:00)Eastern Time (US & Canada)", Timezone_Value
    #
    #     if Timezone_Value != "(GMT-05:00)Eastern Time (US & Canada)":
    #         print("【备注】该用例无法验证，原因：Web端时区默认不是：(GMT-05:00)东部时间(美国和加拿大)")
    #         assert False
    #
    #     # 前提检验完成，开始检验用例
    #     time.sleep(5)
    #     result = Test_timezone.test_timezone_1()
    #     if result == 1:
    #         print("【成功】")
    #         assert True
    #     else:
    #         print("【失败】")
    #         assert False
