#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/18 22:43
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
from rweb.path.dmzHost import DmzHostLocators

"""DMZ主机"""


class DmzHost(Base):
    def setUp(self):
        super(DmzHost, self).setUp()
        # 鼠标模拟移动到：高级设置
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_AdvancedSettings))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_AdvancedSettings)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 DMZ主机
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.DMZ_Host))
        ).click()
        time.sleep(2)

        # WebDriverWait(self.driver,10).until_not(
        #     EC.presence_of_element_located((By.XPATH, CommonLocators.Loading))
        # )

    # @unittest.skip("跳过")
    def test_A_dmz_save(self):
        """DMZ-保存"""
        # 输入IP地址：192.168.127.200
        print(11111111)
        time.sleep(0.5)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.DmzHostIp))
        ).clear()
        time.sleep(0.5)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.DmzHostIp))
        ).send_keys("192.168.127.200")

        # 保存
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.Save))
        ).click()

        # 断言:是否保存成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        self.driver.refresh()
        # 断言：DMZ host的IP地址是否为：192.168.127.200
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, DmzHostLocators.DmzHostIp))
        )
        assert self.driver.find_element_by_xpath(DmzHostLocators.DmzHostIp).get_attribute("value") == "192.168.127.200"

    # @unittest.skip("跳过")
    def test_B_dmz_on(self):
        """DMZ-开启"""
        # 判断：如果已关闭，才进行开启操作
        if self.driver.find_element_by_xpath(DmzHostLocators.Statu).get_attribute('class') == "box":
            # 开启 DMZ
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, DmzHostLocators.Statu))
            ).click()
            # 保存
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, DmzHostLocators.Save))
            ).click()
            # 断言:是否保存成功
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
            self.driver.refresh()

        # 断言：DMZ状态是否为：开启
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, DmzHostLocators.Statu))
        )
        assert self.driver.find_element_by_xpath(DmzHostLocators.Statu).get_attribute('class') == "box checked"

    # @unittest.skip("跳过")
    def test_C_dmz_off(self):
        """DMZ-关闭"""
        # 判断：如果已开启，才进行关闭操作
        if self.driver.find_element_by_xpath(DmzHostLocators.Statu).get_attribute('class') == "box checked":
            # 关闭 DMZ
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, DmzHostLocators.Statu))
            ).click()
            # 保存
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, DmzHostLocators.Save))
            ).click()
            # 断言:toast提示：成功
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
            self.driver.refresh()

        # 断言：DMZ状态是否为：关闭
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, DmzHostLocators.Statu))
        )
        assert self.driver.find_element_by_xpath(DmzHostLocators.Statu).get_attribute('class') == "box"
