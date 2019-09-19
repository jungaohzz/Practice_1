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
from rweb.path.common import CommonLocators
from rweb.path.portForwarding import PortForwardingLocators


class PortForwarding(Base):

    def setUp(self):
        super(PortForwarding, self).setUp()
        # 进入端口转发
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.LEVEL_1_AdvancedSettings))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.PortForwarding))
        ).click()
        # time.sleep(8)  #loading页面
        time.sleep(2)

    def test_A_portForwarding_add_withoutExternalNetwork(self):
        """端口转发-新增-无外网IP"""
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
        # 断言:toast提示：新增成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言：名称是否为：无外网IP
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Name))
        )
        assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Name).text == "无外网IP"

        # 断言：外网IP是否为：任意
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetIp))
        )
        assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetIp).text == "Any"

        # 断言：外网端口是否为：1~2
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetPort))
        )
        assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetPort).text == "1-2"

        # 断言：本地IP是否为：192.168.127.120
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalIp))
        )
        assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalIp).text == "192.168.127.120"

        # 断言：本地端口是否为：3~4
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalPort))
        )
        assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalPort).text == "3-4"

        # 断言：协议类型是否为:TCP
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_ProtocolType))
        )
        assert self.driver.find_element_by_xpath(PortForwardingLocators.List_ProtocolType).text == "TCP"

        # 断言：状态是否默认为：打开
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        )
        assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute(
            'class') == "switch switch-animation checked"

        #删除
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.Delete))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.Delete_ok))
        ).click()



    def test_B_portForwarding_add_ExternalNetwork(self):
        """端口转发-新增-有外网IP"""
        # 点击新增按钮
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.Add))
        ).click()
        # 选择协议类型：UDP
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.ProtocolType_UDP))
        ).click()
        # 输入名称：有外网IP
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.Name))
        ).send_keys("有外网IP")
        # 输入外网IP：10.70.100.50
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.OutNetIp))
        ).send_keys("10.70.100.50")
        # 输入外网端口：5~10
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.OutNetPort_start))
        ).send_keys(5)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.OutNetPort_end))
        ).send_keys(10)
        # 输入本地IP：192.168.127.125
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.LocalIp))
        ).send_keys("192.168.127.125")
        # 输入本地端口：15~20
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.LocalPort_start))
        ).send_keys(15)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.LocalPort_end))
        ).send_keys(20)
        # 新增保存
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.Save))
        ).click()
        # 断言:toast提示：打开开关成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言：名称是否为：有外网IP
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Name))
        )
        assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Name).text == "有外网IP"

        # 断言：外网IP是否为：10.70.100.50
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetIp))
        )
        assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetIp).text == "10.70.100.50"

        # 断言：外网端口是否为：5~10
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetPort))
        )
        assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetPort).text == "5-10"

        # 断言：本地IP是否为：192.168.127.125
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalIp))
        )
        assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalIp).text == "192.168.127.125"

        # 断言：本地端口是否为：15~20
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalPort))
        )
        assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalPort).text == "15-20"

        # 断言：协议类型是否为:UDP
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_ProtocolType))
        )
        assert self.driver.find_element_by_xpath(PortForwardingLocators.List_ProtocolType).text == "UDP"

        # 断言：状态是否默认为：打开
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        )
        assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute(
            'class') == "switch switch-animation checked"



    def test_C_portForwarding_edit(self):
        """端口转发-编辑"""
        # 将状态变为：关闭
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.List_Statu))
        ).click()
        # 断言:toast提示：关闭开关成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
        # 点击编辑按钮
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.Edit))
        ).click()
        # 选择协议类型：TCP&UDP
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.ProtocolType_TcpUdp))
        ).click()
        # 输入名称：编辑
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.Name))
        ).clear()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.Name))
        ).send_keys("编辑")
        # 输入外网IP：10.70.100.60
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.OutNetIp))
        ).clear()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.OutNetIp))
        ).send_keys("10.70.100.60")
        # 输入外网端口：50~70
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.OutNetPort_start))
        ).clear()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.OutNetPort_start))
        ).send_keys(50)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.OutNetPort_end))
        ).clear()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.OutNetPort_end))
        ).send_keys(70)
        # 输入本地IP：192.168.127.135
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.LocalIp))
        ).clear()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.LocalIp))
        ).send_keys("192.168.127.135")
        # 输入本地端口：80~100
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.LocalPort_start))
        ).clear()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.LocalPort_start))
        ).send_keys(80)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.LocalPort_end))
        ).clear()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.LocalPort_end))
        ).send_keys(100)
        # 保存
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.Save))
        ).click()
        # 断言:toast提示：编辑后保存成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言：名称是否为：编辑
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Name))
        )
        assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Name).text == "编辑"

        # 断言：外网IP是否为：10.70.100.60
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetIp))
        )
        assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetIp).text == "10.70.100.60"

        # 断言：外网端口是否为：50~70
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetPort))
        )
        assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetPort).text == "50-70"

        # 断言：本地IP是否为：192.168.127.135
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalIp))
        )
        assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalIp).text == "192.168.127.135"

        # 断言：本地端口是否为：80~100
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalPort))
        )
        assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalPort).text == "80-100"

        # 断言：协议类型是否为:TCP&UDP
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_ProtocolType))
        )
        assert self.driver.find_element_by_xpath(PortForwardingLocators.List_ProtocolType).text == "TCP&UDP"

        # 断言：状态是否为：关闭
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        )
        assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute(
            'class') == "switch switch-animation"

        # 删除
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.Delete))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.Delete_ok))
        ).click()

