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



class Limit(Base):

    def setUp(self):
        super(Limit, self).setUp()
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
        # 点击主网-设置
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DevicesLocators.Set))
        ).click()

    @unittest.skip("跳过")
    def test_A_limit_time(self):
        """设置限时"""
        # 点击限时的新增按钮
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Add))
        ).click()
        # 选择星期一
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Mondey))
        ).click()
        # 点击 新增 按钮
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Save))
        ).click()

        # 断言:是否操作成功：保存
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        self.driver.refresh()
        # 断言:判断是否选中的星期一
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Repeat))
        )
        assert self.driver.find_element_by_xpath(LimitTimeLocators.Repeat).text == "Monday"

        # 断言：判断开关是否开启
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Statu))
        )
        assert self.driver.find_element_by_xpath(LimitTimeLocators.Statu).get_attribute('class') == "switch switch-animation checked"

        # 断言：关闭开关，再判断开关是否关闭
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Statu))
        ).click()
        # 断言:是否操作成功：关闭
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, LimitTimeLocators.Statu))
        )
        assert self.driver.find_element_by_xpath(LimitTimeLocators.Statu).get_attribute('class') == "switch switch-animation"

        time.sleep(1)

        # 最后删除限时
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Delete))
        ).click()
        # 断言:toast提示：成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

    @unittest.skip("跳过")
    def test_B_limit_rate(self):
        """设置限速"""
        # 切换到限速页
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Page_RateLimit))
        ).click()
        # 设置上下行
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(120000)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(125000)
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

        self.driver.refresh()
        # 断言:判断上下行是否设置正确
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Upload))
        )
        assert self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value") == "120000"
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
        )
        assert self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value") == "125000"

        # 断言：查看是否启用
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Statu))
        )
        assert self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class') == "box checked"


        # 断言：关闭开关，再判断开关是否关闭
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Statu))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, LimitRateLocators.Save))
        ).click()
        self.driver.refresh()


        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Statu))
        )
        assert self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class') == "box"

    #@unittest.skip("跳过")
    def test_C_limit_WebsiteBlacklist(self):
        """设置网址黑名单"""
        # 切换到网址黑名单页
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Page_WebsiteBlacklist))
        ).click()
        # 点击黑名单的新增按钮
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
        # 断言:判断添加的网址是否是：www.baidu.com
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.List_Website))
        )
        assert self.driver.find_element_by_xpath(WebsiteBlacklistLocators.List_Website).text == "www.baidu.com"

        # 断言：判断开关是否开启
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Statu))
        )
        assert self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Statu).get_attribute('class') == "switch switch-animation checked"

        # 断言：关闭开关，再判断开关是否关闭
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Statu))
        ).click()
        # 断言:toast提示：关闭开关成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Statu))
        )
        assert self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Statu).get_attribute('class') == "switch switch-animation"

        # 最后删除网址黑名单
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Delete))
        ).click()