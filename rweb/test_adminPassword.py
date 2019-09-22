#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/21 14:04
# @Author:  GaoJun

import unittest
from .test_base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from . import const
import time
from rweb.path.common import CommonLocators
from rweb.path.devices import DevicesLocators
from rweb.path.limitTime import LimitTimeLocators
from selenium.webdriver.common.action_chains import ActionChains
from rweb.path.staticDhcpLease import StaticDHCPLeaseLocators
from rweb.path.dmzHost import DmzHostLocators
from rweb.path.internetSettings import InternetSettingsLocators
from rweb.path.routerManagement import RouterManagementLocators
from rweb.path.adminPassword import AdminPasswordLocators


"""管理密码"""

class AdminPassword(Base):
    def setUp(self):
        super(AdminPassword, self).setUp()
        # 鼠标模拟移动到：设置
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 管理密码
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Admin_Password))
        ).click()
        time.sleep(2)

    #@unittest.skip("跳过")
    def test_set_admin_password(self):
        """管理密码-设置管理密码：各种字符组合"""
        # 输入 新密码，各种组合
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, AdminPasswordLocators.New_Password))
        ).send_keys(const.PASSWORD_MIX)
        # 保存
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, AdminPasswordLocators.Save))
        ).click()

        #断言：修改成功后悔跳转到登录页面，则查看是否有登录按钮即可
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Login))
        )

        #重新登录
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.InputPassword))
        ).send_keys(const.PASSWORD_MIX)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Login))
        ).click()
        time.sleep(0.5)

        # 如果密码修改成功则会登录成功。则以判断是否有“退出登录”来检验是否登录成功
        assert self.driver.find_element_by_xpath(CommonLocators.Logout).is_displayed()

        # 重新将复杂的密码改回简单的密码
        #  进入 管理密码页
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
        ActionChains(self.driver).move_to_element(mouse).perform()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Admin_Password))
        ).click()
        time.sleep(2)
        # 改回普通密码
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, AdminPasswordLocators.New_Password))
        ).send_keys(const.PASSWORD)
        # 保存
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, AdminPasswordLocators.Save))
        ).click()

        # 断言：修改成功后悔跳转到登录页面，则查看是否有登录按钮即可
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Login))
        )


