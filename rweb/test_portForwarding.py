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
from rweb.path.portForwarding import PortForwardingLocators


class PortForwarding(Base):
    def test_portForwarding_add_withoutExternalNetwork(self):
        """端口转发-新增-无外网IP"""
        # 进入端口转发
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, HomePageLocators.LEVEL_1_AdvancedSettings))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, HomePageLocators.PortForwarding))
        ).click()

        time.sleep(8)  #loading页面

        # 点击新增按钮
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.Add))
        ).click()
        # 选择协议类型：TCP
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.ProtocolType_TCP))
        ).click()
        # 输入名称：无外网IP
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.Name))
        ).send_keys("无外网IP")
        # 输入外网端口：1~2
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.OutNetPort_start))
        ).send_keys(1)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.OutNetPort_end))
        ).send_keys(2)
        # 输入本地IP：192.168.127.120
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.LocalIp))
        ).send_keys("192.168.127.120")
        # 输入本地端口：3~4
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.LocalPort_start))
        ).send_keys(3)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.LocalPort_end))
        ).send_keys(4)
        # 新增保存
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.Save))
        ).click()
        time.sleep(2)

        # 断言：名称是否为：无外网IP
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[1]/span[2]"))
        )
        assert self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[1]/span[2]").text == "无外网IP"

        # 断言：外网IP是否为：任意
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[2]/p[1]"))
        )
        assert self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[2]/p[1]").text == "Any"

        # 断言：外网端口是否为：1~2
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[2]/p[2]"))
        )
        assert self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[2]/p[2]").text == "1-2"

        # 断言：本地IP是否为：192.168.127.120
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[3]/p[1]"))
        )
        assert self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[3]/p[1]").text == "192.168.127.120"

        # 断言：本地端口是否为：3~4
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[3]/p[2]"))
        )
        assert self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[3]/p[2]").text == "3-4"

        # 断言：协议类型是否为:TCP
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[4]"))
        )
        assert self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[4]").text == "TCP"

        # 断言：状态是否默认为：打开
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[5]/div/div"))
        )
        assert self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[5]/div/div").get_attribute(
            'class') == "switch switch-animation checked"

        #删除
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[6]/a[2]"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[3]/div/div[2]/button[2]"))
        ).click()
        time.sleep(2)


    # def test_portForwarding_add_ExternalNetwork(self):
    #     """端口转发-新增-有外网IP"""