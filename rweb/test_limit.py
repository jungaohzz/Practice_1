#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun

import unittest
from selenium import webdriver
from .test_base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from rweb.path.homePage import HomePageLocators
from rweb.path.devices import DevicesLocators
from rweb.path.limitTime import LimitTimeLocators
from selenium.webdriver.common.action_chains import ActionChains


class Limit(Base):

    def test_A_limit_time(self):
        """设置限时"""
        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, HomePageLocators.LEVEL_1_MyWifi))
        # ).click()
        # 鼠标移动到切换“我的WiFi”按钮上
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, HomePageLocators.LEVEL_1_MyWifi))
        )
        mouse = self.driver.find_element_by_xpath(HomePageLocators.LEVEL_1_MyWifi)
        ActionChains(self.driver).move_to_element(mouse).perform()


        # 点击 接入设备
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, HomePageLocators.Devices))
        ).click()
        # 点击主网-设置
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DevicesLocators.Set))
        ).click()
        # 点击限时的新增按钮
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Add))
        ).click()
        # 选择星期一
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div[1]/div[4]/div/div[1]/div/label/div[1]"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div[3]/button[2]"))
        ).click()

        # 断言:判断是否选中的星期一
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div[3]/div/div[3]"))
        )
        assert self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div[3]/div/div[3]").text == "Monday"

        # 断言：判断开关是否开启
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div[3]/div/div[4]/div/div/div"))
        )
        assert self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div[3]/div/div[4]/div/div/div").get_attribute('class') == "switch switch-animation checked"
        # 断言：关闭开关，再判断开关是否关闭
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div[3]/div/div[4]/div/div/div"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div[3]/div/div[4]/div/div/div"))
        )
        assert self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div[3]/div/div[4]/div/div/div").get_attribute('class') == "switch switch-animation"

        # 最后删除限时

        time.sleep(1)   #这里为什么必须需要sleep？？？？？？？？？？？？？？？？？？？？？？？？？？

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Delete"))
        ).click()



    def test_B_limit_rate(self):
        """设置限速"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, HomePageLocators.LEVEL_1_MyWifi))
        ).click()
        # 点击 设备
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, HomePageLocators.Devices))
        ).click()
        # 点击主网-设置
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DevicesLocators.Set))
        ).click()
        # 切换到限速页
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[1]/div[3]/div/div[2]"))
        ).click()
        # 设置上下行
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[1]/div[1]/div/div/div/input"))
        ).clear()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[1]/div[1]/div/div/div/input").send_keys(12000)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div/input"))
        ).clear()
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div/input").send_keys(12000)
        # 启用
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/label/div[2]"))
        ).click()
        # 保存
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[3]/button"))
        ).click()

        # 断言:判断上下行是否设置为了12000
        upRate = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[1]/div[1]/div/div/div/input")
        downRate = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div/input")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[1]/div[1]/div/div/div/input"))
        )
        assert upRate.get_attribute("value") == "12000"
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div/input"))
        )
        assert downRate.get_attribute("value") == "12000"
        # 断言：查看是否启用
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/label/div[1]"))
        )
        assert self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/label/div[1]").get_attribute('class') == "box checked"

        time.sleep(2)   #为什么必须要sleep？？？？？？？？？？？？？？？？？？？？？

        # 断言：关闭开关，再判断开关是否关闭
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/label/div[2]"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[3]/button"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/label/div[1]"))
        )
        assert self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/label/div[1]").get_attribute('class') == "box"



    def test_C_limit_WebsiteBlacklist(self):
        """设置网址黑名单"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, HomePageLocators.LEVEL_1_MyWifi))
        ).click()
        # 点击 设备
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, HomePageLocators.Devices))
        ).click()
        # 点击主网-设置
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DevicesLocators.Set))
        ).click()
        # 切换到网址黑名单页
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[1]/div[3]/div/div[3]"))
        ).click()
        # 点击黑名单的新增按钮
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div[1]/button"))
        ).click()
        # 输入：www.baidu.com
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[3]/div[2]/div/div[1]/div/div/div/div/div/input"))
        ).send_keys("www.baidu.com")
        # 完成添加
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/button[2]"))
        ).click()
        # 打开网址黑名单开关
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div/div"))
        ).click()
        time.sleep(1)
        # 断言:判断添加的网址是否是：www.baidu.com
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div[3]/div/div[1]"))
        )
        assert self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div[3]/div/div[1]").text == "www.baidu.com"

        # 断言：判断开关是否开启
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div/div"))
        )
        assert self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div/div").get_attribute(
            'class') == "switch switch-animation checked"

        # 断言：关闭开关，再判断开关是否关闭
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[2]/div/div[1]/div/div"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div/div"))
        )
        assert self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div/div").get_attribute(
            'class') == "switch switch-animation"

        # 最后删除网址黑名单

        time.sleep(1)  # 这里为什么必须需要sleep？？？？？？？？？？？？？？？？？？？？？？？？？？

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Delete"))
        ).click()