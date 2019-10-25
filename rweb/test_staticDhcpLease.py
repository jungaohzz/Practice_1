#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun

import unittest
from .test_base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from rweb.path.common import CommonLocators
from rweb.path.devices import DevicesLocators
from rweb.path.limitTime import LimitTimeLocators
from selenium.webdriver.common.action_chains import ActionChains
from rweb.path.staticDhcpLease import StaticDHCPLeaseLocators

"""Mac与IP绑定"""


class StaticDHCPLease(Base):

    def setUp(self):
        super(StaticDHCPLease, self).setUp()
        # 鼠标模拟移动到：高级设置
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_AdvancedSettings))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_AdvancedSettings)
        ActionChains(self.driver).move_to_element(mouse).perform()

        # 点击 Mac与IP绑定
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Static_DHCP_Lease))
        ).click()
        time.sleep(2)







    def test_A_staticDHCPLease_add(self):
        """Mac与IP绑定-新增绑定"""
        # 点击 新增
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, StaticDHCPLeaseLocators.Add))
        ).click()
        # 设置名称
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, StaticDHCPLeaseLocators.Name))
        ).send_keys(1)
        # 设置Mac地址
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, StaticDHCPLeaseLocators.MacAddr))
        ).send_keys("68:f7:28:b6:dc:f8")
        # 设置IP地址
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, StaticDHCPLeaseLocators.IpAddr))
        ).send_keys("192.168.127.120")
        # 点击 保存
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, StaticDHCPLeaseLocators.Save))
        ).click()
        # 断言:toast提示：保存成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言：名称是否为：1
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, StaticDHCPLeaseLocators.List_Name))
        )
        assert self.driver.find_element_by_xpath(StaticDHCPLeaseLocators.List_Name).text == "1"
        # 断言：Mac地址是否为：68:f7:28:b6:dc:f8
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, StaticDHCPLeaseLocators.List_MacAddr))
        )
        assert self.driver.find_element_by_xpath(StaticDHCPLeaseLocators.List_MacAddr).text == "68:f7:28:b6:dc:f8"
        # 断言：IP地址是否为：192.168.127.120
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, StaticDHCPLeaseLocators.List_IpAddr))
        )
        assert self.driver.find_element_by_xpath(StaticDHCPLeaseLocators.List_IpAddr).text == "192.168.127.120"









    #@unittest.skip("跳过")
    def test_B_staticDHCPLease_adds(self):
        """Mac与IP绑定-再新增19条绑定记录"""
        i = 2
        while i <= 20:

            # 点击 新增
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div[2]/button[1]"))
            ).click()
            # 设置名称
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/input"))
            ).send_keys(i)
            # 设置Mac地址
            mac_end = hex(i+20)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[3]/div/div/div/input"))
            ).send_keys("b4:0b:44:e2:37:"+mac_end[2:])
            # 设置IP地址
            ip_end=110+i
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[4]/div/div/div/input"))
            ).send_keys("192.168.127."+"%d"%ip_end)
            # 点击 保存
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div[2]/button"))
            ).click()
            # 断言:toast提示：保存成功
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
            i += 1
            time.sleep(1)






    @unittest.skip("跳过")
    def test_C_deletes(self):
        """Mac与IP绑定-批量删除"""
        # 需要再新增1条记录检验
        # 新增
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, StaticDHCPLeaseLocators.Add))
        ).click()
        # 设置名称
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, StaticDHCPLeaseLocators.Name))
        ).send_keys(1)
        # 设置Mac地址
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, StaticDHCPLeaseLocators.MacAddr))
        ).send_keys("68:f7:28:b6:dc:a1")
        # 设置IP地址
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, StaticDHCPLeaseLocators.IpAddr))
        ).send_keys("192.168.127.131")
        # 点击 保存
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, StaticDHCPLeaseLocators.Save))
        ).click()
        # 断言:toast提示：保存成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"


        # 批量删除
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, StaticDHCPLeaseLocators.All_check))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, StaticDHCPLeaseLocators.Deletes))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, StaticDHCPLeaseLocators.Delete_ok))
        ).click()

        # 断言：
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, StaticDHCPLeaseLocators.List_Null))
        )
        assert self.driver.find_element_by_xpath(StaticDHCPLeaseLocators.List_Null).text == "Empty"

