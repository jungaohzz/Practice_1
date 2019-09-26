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

from router.time_limit import test_time_limit_add_1



class LimitTime(Base):

    def setUp(self):
        super(LimitTime, self).setUp()
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
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, DevicesLocators.Set))
        ).click()

    @unittest.skip("跳过")
    def test_A_limitTime_null(self):
        """限时-列表为空检验"""
        """
        用例-2000 : 没有限时条目，显示列表为空
        """
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, LimitTimeLocators.List_Null))
        ).click()
        List_Null_text = self.driver.find_element_by_xpath(LimitTimeLocators.List_Null).text
        assert List_Null_text == "Empty", List_Null_text

    @unittest.skip("跳过")
    def test_A_limitTime_add(self):
        """限时-新增"""
        # 点击 新增 按钮
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Add))
        ).click()
        # 选择星期一
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Mondey))
        ).click()
        # 点击 保存 按钮
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Save))
        ).click()

        # 断言:是否操作成功：保存
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言:判断是否选中的星期一
        self.driver.refresh()
        Repeat = LimitTimeLocators.Repeat.format(num="last()")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Repeat))
        )
        assert self.driver.find_element_by_xpath(Repeat).text == "Monday"

        # 断言：判断开关是否默认开启
        Statu = LimitTimeLocators.Statu.format(num="last()")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Statu))
        )
        assert self.driver.find_element_by_xpath(Statu).get_attribute('class') == "switch switch-animation checked"


        # a=test_time_limit_add_1.test_ping()
        # print(1111111111111111111111)
        # print(a)
        # assert a == 1


    #@unittest.skip("跳过")
    def test_B_limitTime_elementAssert(self):
        """限时-页面元素检测"""
        """
        用例-1999：列表页面元素检测
                  列表标题：断网时间，恢复时间，重复，操作
                  列表内容：开始时间点，结束时间点，重复天，开启关闭按钮，编辑按钮，删除按钮
                  新增按钮
        """

        # 断网时间
        Table_Heads = LimitTimeLocators.Table_Heads.format(num=1)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Table_Heads))
        )
        Table_Heads_text = self.driver.find_element_by_xpath(Table_Heads).text
        assert Table_Heads_text == "Cut off time", Table_Heads_text
        # 恢复时间
        # 重复
        # 操作
        # 开始时间点
        # 结束时间点
        # 重复天
        # 开启关闭按钮
        # 编辑按钮
        # 删除按钮
        # 新增按钮




    @unittest.skip("跳过")
    def test_B_limitTime_edit_value(self):
        """限时-编辑-修改参数值"""
        # 点击 编辑 按钮
        Edit = LimitTimeLocators.Edit.format(num="last()")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Edit))
        ).click()
        # 取消 星期一，选择 星期二
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Mondey))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Tuesday))
        ).click()
        # 点击 保存 按钮
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Save))
        ).click()

        # 断言:是否操作成功：保存
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言:判断是否只选中的星期二
        self.driver.refresh()
        Repeat = LimitTimeLocators.Repeat.format(num="last()")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Repeat))
        )
        assert self.driver.find_element_by_xpath(Repeat).text == "Tuesday"

        # 断言：判断开关是否默认开启
        Statu = LimitTimeLocators.Statu.format(num="last()")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Statu))
        )
        assert self.driver.find_element_by_xpath(Statu).get_attribute('class') == "switch switch-animation checked"






    @unittest.skip("跳过")
    def test_C_limitTime_edit_statu(self):
        """限时-编辑-修改状态：由开变为关"""
        # 点击 开关 按钮，由开变为关
        Statu = LimitTimeLocators.Statu.format(num="last()")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Statu))
        ).click()
        # 断言:toast提示：关闭成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言：开关状态是否为：关闭
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Statu))
        )
        assert self.driver.find_element_by_xpath(Statu).get_attribute('class') == "switch switch-animation"




    @unittest.skip("跳过")
    def test_D_limitTime_delete(self):
        """限时-删除"""
        Delete = LimitTimeLocators.Delete.format(num="last()")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Delete))
        ).click()
        # 断言:toast提示：成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"






