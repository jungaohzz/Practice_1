#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/20 20:57
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
from rweb.path.dhcp import DhcpLocators
from rweb.path.cloneMacAddress import CloneMacAddressLocators
from rweb.path.ddns import DDNSLocators
from rweb import const

"""DDNS"""


class DDNS(Base):
    def setUp(self):
        super(DDNS, self).setUp()
        # 鼠标模拟移动到：高级设置
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_AdvancedSettings))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_AdvancedSettings)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 DDNS
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.DDNS))
        ).click()
        time.sleep(2)

    # @unittest.skip("跳过")
    def test_A_set_DynDNS(self):
        """DDNS-设置DynDNS"""
        # 选择服务提供商：DynDNS
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, DDNSLocators.Service_Provider_DynDNS))
        ).click()
        # 输入 域名
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, DDNSLocators.Domain_Name))
        ).clear()
        self.driver.find_element_by_xpath(DDNSLocators.Domain_Name).send_keys("mercku.homelinux.org")
        # 输入 用户名
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, DDNSLocators.Username))
        ).clear()
        self.driver.find_element_by_xpath(DDNSLocators.Username).send_keys("hyku")
        # 输入 密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, DDNSLocators.Password))
        ).clear()
        self.driver.find_element_by_xpath(DDNSLocators.Password).send_keys("hrmes2018")
        # 启用（没启用才进行if操作）
        if self.driver.find_element_by_xpath(DDNSLocators.Statu).get_attribute('class') == "box":
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, DDNSLocators.Statu))
            ).click()
        # 保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, DDNSLocators.Save))
        ).click()

        # 断言:toast提示：保存成功
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        self.driver.refresh()
        # 断言：域名是否正确
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, DDNSLocators.Domain_Name))
        )
        Domain_Name_value = self.driver.find_element_by_xpath(DDNSLocators.Domain_Name).get_attribute('value')
        assert Domain_Name_value == "mercku.homelinux.org", Domain_Name_value

        # 断言：用户名是否正确
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, DDNSLocators.Username))
        )
        Username_value = self.driver.find_element_by_xpath(DDNSLocators.Username).get_attribute('value')
        assert Username_value == "hyku", Username_value

        # 断言：密码是否正确
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, DDNSLocators.Password))
        )
        Password_value = self.driver.find_element_by_xpath(DDNSLocators.Password).get_attribute('value')
        assert Password_value == "hrmes2018", Password_value

        # 断言：是否启用
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, DDNSLocators.Statu))
        )
        assert self.driver.find_element_by_xpath(DDNSLocators.Statu).get_attribute('class') == "box checked"

    # @unittest.skip("跳过")
    def test_B_set_Oray(self):
        """DDNS-设置花生壳"""
        # 选择服务提供商：Oray
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, DDNSLocators.Service_Provider_Oray))
        ).click()
        # 输入 域名
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, DDNSLocators.Domain_Name))
        ).clear()
        self.driver.find_element_by_xpath(DDNSLocators.Domain_Name).send_keys("22632jr080.iok.la")
        # 输入 用户名
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, DDNSLocators.Username))
        ).clear()
        self.driver.find_element_by_xpath(DDNSLocators.Username).send_keys("mercku2018")
        # 输入 密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, DDNSLocators.Password))
        ).clear()
        self.driver.find_element_by_xpath(DDNSLocators.Password).send_keys("mercku2018-2019")
        # 启用（没启用才进行if操作）
        if self.driver.find_element_by_xpath(DDNSLocators.Statu).get_attribute('class') == "box":
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, DDNSLocators.Statu))
            ).click()
        # 保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, DDNSLocators.Save))
        ).click()

        # 断言:toast提示：保存成功
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        self.driver.refresh()
        # 断言：域名是否正确
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, DDNSLocators.Domain_Name))
        )
        Domain_Name_value = self.driver.find_element_by_xpath(DDNSLocators.Domain_Name).get_attribute('value')
        assert Domain_Name_value == "22632jr080.iok.la", Domain_Name_value

        # 断言：用户名是否正确
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, DDNSLocators.Username))
        )
        Username_value = self.driver.find_element_by_xpath(DDNSLocators.Username).get_attribute('value')
        assert Username_value == "mercku2018", Username_value

        # 断言：密码是否正确
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, DDNSLocators.Password))
        )
        Password_value = self.driver.find_element_by_xpath(DDNSLocators.Password).get_attribute('value')
        assert Password_value == "mercku2018-2019", Password_value

        # 断言：是否启用
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, DDNSLocators.Statu))
        )
        assert self.driver.find_element_by_xpath(DDNSLocators.Statu).get_attribute('class') == "box checked"
