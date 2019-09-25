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



class LimitRate(Base):

    def setUp(self):
        super(LimitRate, self).setUp()
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
        # 切换到限速页
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Page_RateLimit))
        ).click()

    #@unittest.skip("跳过")
    def test_A_limitRate_add(self):
        """限速-新增"""
        # 设置上下行:10KB/s
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(10)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(10)
        # 保存
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
        ).click()

        # 断言:toast提示：成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        self.driver.refresh()
        # 断言:判断上下行是否设置正确
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Upload))
        )
        assert self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value") == "10"
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
        )
        assert self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value") == "10"



    #@unittest.skip("跳过")
    def test_B_limitRate_edit_value(self):
        """限速-修改参数值"""
        # 修改上下行为：1KB/s
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(1)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(1)
        # 保存
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
        ).click()

        # 断言:toast提示：成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        self.driver.refresh()
        # 断言:判断上下行是否设置正确
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Upload))
        )
        assert self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value") == "1"
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
        )
        assert self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value") == "1"


    #@unittest.skip("跳过")
    def test_C_limitRate_edit_statu_on(self):
        """限速-修改状态：由关变为开"""
        # 状态默认为关闭，如果为关闭状态才进行if的启用操作
        Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
        if Statu_class == "box":
            # 启用
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Statu))
            ).click()
            # 保存
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
            ).click()
            # 断言:toast提示：成功
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言：查看是否启用
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Statu))
        )
        assert self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class') == "box checked"





    #@unittest.skip("跳过")
    def test_D_limitRate_edit_statu_off(self):
        """限速-修改状态：由开变为关"""
        # 状态理应为启用，如果为启用状态才进行if的关闭操作
        Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
        if Statu_class == "box checked":
            # 关闭
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Statu))
            ).click()
            # 保存
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
            ).click()
            # 断言:toast提示：成功
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言：查看是否关闭
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Statu))
        )
        assert self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class') == "box"