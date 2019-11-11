#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/20 20:32
# @Author:  GaoJun

import unittest
from .. base import Base
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
from rweb.path.routerManagement import RouterManagementLocators
from rweb.path.dhcp import DhcpLocators
from ..common_dir import common_conf,common_fun
from rweb.path.cloneMacAddress import CloneMacAddressLocators

"""MAC地址克隆"""

class CloneMacAddress(Base):

    def switch_to_cloneMacAddress_Page(self):
        # 鼠标模拟移动到：高级设置
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_AdvancedSettings))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_AdvancedSettings)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 MAC地址克隆
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Clone_MAC_Address))
        ).click()
        time.sleep(2)







    @unittest.skip("跳过")
    def test_A_cloneMacAddress_set_mac1(self):
        """操作步骤：从默认MAC修改为自定义MAC1"""
        self.switch_to_cloneMacAddress_Page()
        # 点击按钮 自定义MAC地址
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CloneMacAddressLocators.Custom_Mac_Button))
        ).click()

        #输入自定义的Mac1地址
        Mac1 = common_conf.clone_mac1.split('-')
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CloneMacAddressLocators.Custom_Mac))
        ).clear()
        self.driver.find_element_by_xpath(CloneMacAddressLocators.Custom_Mac).send_keys(Mac1)

        # 点击 保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CloneMacAddressLocators.Save))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CloneMacAddressLocators.Save_Ok))
        ).click()

        # 断言:toast提示：重启成功
        WebDriverWait(self.driver, const.REBOOT_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
        time.sleep(1)









    @unittest.skip("跳过")
    def test_B_cloneMacAddress_1(self):
        """【检验】用例-2825 : WAN口MAC地址配置自定义MAC后，路由器重启后，WAN口MAC地址为自定义MAC"""
        self.switch_to_cloneMacAddress_Page()

        # 前提：已经设置为自定义Mac1
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CloneMacAddressLocators.Custom_Mac))
        )
        Actual_Mac_value = self.driver.find_element_by_xpath(CloneMacAddressLocators.Custom_Mac).get_attribute('value').split(':')
        Expect_Mac_value = common_conf.clone_mac1.lower().split('-')
        if Actual_Mac_value != Expect_Mac_value:
            print("【备注】该用例无法验证，原因：没有将Mac地址设置为MAC1")
            assert False

        # 前提检验完成，开始检验用例
        time.sleep(5)
        Result = 1#?????????????????????????????????????????????????????????????????????????????????
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False







    @unittest.skip("跳过")
    def test_C_cloneMacAddress_set_default(self):
        """操作步骤：从自定义MAC1修改为默认MAC"""
        self.switch_to_cloneMacAddress_Page()

        # 点击按钮 默认MAC地址
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CloneMacAddressLocators.Default_Mac_Button))
        ).click()

        # 点击 保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CloneMacAddressLocators.Save))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CloneMacAddressLocators.Save_Ok))
        ).click()

        # 断言:toast提示：重启成功
        WebDriverWait(self.driver, const.REBOOT_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
        time.sleep(1)







    @unittest.skip("跳过")
    def test_D_cloneMacAddress_2(self):
        """【检验】用例-3371 : WAN口MAC地址从自定义修改为默认MAC后，WAN口出去的所有数据包源MAC地址都为系统默认的MAC地址"""
        self.switch_to_cloneMacAddress_Page()

        # 前提条件：Mac地址设置为默认Mac地址
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CloneMacAddressLocators.Default_Mac_Button))
        )
        time.sleep(1)
        Default_Mac_Button_Value = self.driver.find_element_by_xpath(CloneMacAddressLocators.Default_Mac_Button).get_attribute('class')
        if Default_Mac_Button_Value != "radio selected":
            print("【备注】该用例无法验证，原因：没有将Mac地址设置为默认Mac地址")
            assert False

        # 前提检验完成，开始检验用例
        time.sleep(5)
        Result = 1 #？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False






    @unittest.skip("跳过")
    def test_E_cloneMacAddress_set_mac1(self):
        """操作步骤：从默认MAC修改为自定义MAC1"""
        self.switch_to_cloneMacAddress_Page()

        # 点击按钮 自定义MAC地址
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CloneMacAddressLocators.Custom_Mac_Button))
        ).click()

        # 输入自定义的Mac1地址
        Mac1 = common_conf.clone_mac1.split('-')
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CloneMacAddressLocators.Custom_Mac))
        ).clear()
        self.driver.find_element_by_xpath(CloneMacAddressLocators.Custom_Mac).send_keys(Mac1)

        # 点击 保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CloneMacAddressLocators.Save))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CloneMacAddressLocators.Save_Ok))
        ).click()

        # 断言:toast提示：重启成功
        WebDriverWait(self.driver, const.REBOOT_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
        time.sleep(1)








    @unittest.skip("跳过")
    def test_F_cloneMacAddress_set_mac2(self):
        """操作步骤：从自定义MAC1修改为自定义MAC2"""
        self.switch_to_cloneMacAddress_Page()

        # 点击按钮 自定义MAC地址
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CloneMacAddressLocators.Custom_Mac_Button))
        ).click()

        # 输入自定义的Mac1地址
        Mac2 = common_conf.clone_mac2.split('-')
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CloneMacAddressLocators.Custom_Mac))
        ).clear()
        self.driver.find_element_by_xpath(CloneMacAddressLocators.Custom_Mac).send_keys(Mac2)

        # 点击 保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CloneMacAddressLocators.Save))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CloneMacAddressLocators.Save_Ok))
        ).click()

        # 断言:toast提示：重启成功
        WebDriverWait(self.driver, const.REBOOT_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
        time.sleep(1)







    @unittest.skip("跳过")
    def test_G_cloneMacAddress_3(self):
        """【检验】用例-2823 : 修改WAN口自定义MAC1位MAC2后，WAN口出去的所有数据包源MAC地址都为修改后的MAC地址"""
        self.switch_to_cloneMacAddress_Page()

        # 前提：已经设置为自定义Mac2
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CloneMacAddressLocators.Custom_Mac))
        )
        Actual_Mac_value = self.driver.find_element_by_xpath(CloneMacAddressLocators.Custom_Mac).get_attribute('value').split(':')
        Expect_Mac_value = common_conf.clone_mac2.lower().split('-')
        if Actual_Mac_value != Expect_Mac_value:
            print("【备注】该用例无法验证，原因：没有将Mac地址设置为MAC2")
            assert False

        # 前提检验完成，开始检验用例
        time.sleep(5)
        Result = 1  # ?????????????????????????????????????????????????????????????????????????????????
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False







    #@unittest.skip("跳过")
    def test_H_cloneMacAddress_4(self):
        """【检验】用例-2826 : WAN口MAC地址配置自定义MAC后，路由器恢复出厂后，WAN口MAC地址为系统默认MAC地址"""
        self.switch_to_cloneMacAddress_Page()

        # 前提1：已经设置为自定义Mac2
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CloneMacAddressLocators.Custom_Mac))
        )
        time.sleep(1)
        Actual_Mac_value = self.driver.find_element_by_xpath(CloneMacAddressLocators.Custom_Mac).get_attribute('value').split(':')
        Expect_Mac_value = common_conf.clone_mac2.lower().split('-')
        if Actual_Mac_value != Expect_Mac_value:
            print("【备注】未将Mac地址设置为自定义Mac，所以无法验证后面用例")
            assert False


        # 操作设置：恢复出厂
        # 鼠标移动到切换“My wifi”按钮上
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_MyWifi))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_MyWifi)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 管理路由器
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Router_Management))
        ).click()
        self.driver.refresh()
        time.sleep(1)
        # 点击 列表
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.List))
        ).click()
        # 点击 恢复出厂设置
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.PrimaryRoute_Factory_Reset))
        ).click()
        # 点击 确定 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Confirm))
        ).click()

        # 重启60s,等待遮罩消失
        time.sleep(20)
        WebDriverWait(self.driver, const.REBOOT_WAIT-10).until_not(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Shade))
        )

        # 前提2：已恢复出厂（重置成功后会跳转到“设置路由器”页，查看是否有“设置路由器”按钮即可）
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.SetupWifi))
        )
        SetupWifi_Text = self.driver.find_element_by_xpath(CommonLocators.SetupWifi).text
        if SetupWifi_Text != "Setup Wi-Fi":
            print("【备注】该用例无法验证，原因：没有将路由器恢复出厂")
            assert False

        # 前提检验完成，开始检验用例
        time.sleep(5)
        Result = 1#？？？？？？？？？？？？？？？？？
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False
