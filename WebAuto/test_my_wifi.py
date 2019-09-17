#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun
import unittest
from .login import Login
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains  # 鼠标事件


class MyWifi(Login):
    def test_access_devices_limit_time(self):
        '''接入设备-限时'''


        # 进入接入设备页
        # self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[1]/div/div[1]/div/img").click()
        # time.sleep(1)
        my_wifi = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/header/div[2]/ul/li[1]/div/div")
        ActionChains(self.driver).move_to_element(my_wifi).perform()
        time.sleep(1)
        decices = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/header/div[2]/ul/li[1]/ul/li[2]")
        ActionChains(self.driver).click(decices).perform()
        time.sleep(1)

        # 进入设置页
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div/ul/li[7]/span[1]").click()
        time.sleep(1)
        # 时间限制-新增
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div[1]/button").click()
        time.sleep(1)
        # 选择每周一

        checkboxs = self.driver.find_elements_by_xpath("//div[@class='date-wrap']/div")
        for i in checkboxs:
            i.click()
        # self.driver.find_element_by_xpath("//div[text()='每周一']").click()
        time.sleep(5)
        # 确定新增
        self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[3]/button[2]").click()
        time.sleep(5)

        # #开关-关闭
        # self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div[3]/div[1]/div[4]/div/div/div").click()
        # time.sleep(5)

    def test_access_devices_limit_speed(self):
        '''接入设备-限速'''

        # # 进入接入设备页
        # self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[1]/div/div[1]/div/img").click()
        # time.sleep(1)
        #
        # # 进入设置页
        # self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div/ul/li[7]/span[1]").click()
        # time.sleep(1)

        # 进入网速限制
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div[3]/div/div[2]").click()
        time.sleep(1)

        # 开关-启用
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/label/div[1]").click()
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/button").click()
        time.sleep(1)

        class_name = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/label/div[1]").get_attribute("class")
        assert class_name == "box checked", "expect：box checked，actual：" + class_name
        time.sleep(4)

        # 开关-关闭

    # def test_access_devices_url_blacklist(self):
    #     '''接入设备-网址黑名单'''
    #     pass
