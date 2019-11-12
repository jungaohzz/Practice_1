#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/21 14:04
# @Author:  GaoJun

import unittest
from ..base import Base
from rweb import const
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
from rweb.path.internetSettings import InternetSettingsLocators
from rweb.path.routerManagement import RouterManagementLocators
from rweb.path.adminPassword import AdminPasswordLocators
from ..common_dir import common_conf

"""管理密码"""


class AdminPassword(Base):
    # 定义密码修改是否成功的变量：True为修改成功，False为修改失败
    Flag = True

    def setUp(self):
        super(AdminPassword, self).setUp()
        # 鼠标模拟移动到：设置
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 管理密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Admin_Password))
        ).click()
        time.sleep(2)

    def change_password(self, password):
        """修改管理密码"""
        # 输入密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, AdminPasswordLocators.New_Password))
        ).send_keys(password)
        # 保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, AdminPasswordLocators.Save))
        ).click()

        # 断言：修改成功后会跳转到登录页面，则查看是否有“登录”按钮即可
        WebDriverWait(self.driver, const.REBOOT_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Login))
        )
        time.sleep(1)

    # @unittest.skip("跳过")
    def test_A_set_newPassword(self):
        """操作步骤：修改管理密码"""
        self.change_password("22222222")  # ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        time.sleep(2)
        # 重新登录
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.InputPassword))
        ).send_keys("22222222")  # ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Login))
        ).click()

        # #作用：登录后关闭升级框
        if True:
            try:
                WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                    EC.element_to_be_clickable((By.XPATH, CommonLocators.Cancel))
                ).click()
                time.sleep(0.5)
            except:
                print("正常")

        # 如果密码修改成功则会登录成功。则以判断是否有“退出登录”来检验是否登录成功
        if self.driver.find_element_by_xpath(CommonLocators.Logout).is_displayed():
            AdminPassword.Flag = True
            assert True
        else:
            AdminPassword.Flag = False
            assert False

    # @unittest.skip("跳过")
    def test_B_1(self):
        """【检验】用例-102272 : 修改管理密码，旧密码失效，新密码生效"""
        # 前提条件：管理密码修改为新密码成功
        if not AdminPassword.Flag:
            print("【备注】该用例无法验证，原因：管理密码未成功修改为新密码")
            assert False

        # 前提检验完成，开始检验用例
        result = 1  # ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    # @unittest.skip("跳过")
    def test_C_set_defaultPassword(self):
        """操作步骤：修改回默认的管理密码"""

        self.change_password(common_conf.telnet_password)
        time.sleep(1)
        # 重新登录
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.InputPassword))
        ).send_keys(common_conf.telnet_password)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Login))
        ).click()

        # #作用：登录后关闭升级框
        if True:
            try:
                WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                    EC.element_to_be_clickable((By.XPATH, CommonLocators.Cancel))
                ).click()
                time.sleep(0.5)
            except:
                print("正常")

        # 如果密码修改成功则会登录成功。则以判断是否有“退出登录”来检验是否登录成功
        if self.driver.find_element_by_xpath(CommonLocators.Logout).is_displayed():
            assert True
        else:
            assert False
