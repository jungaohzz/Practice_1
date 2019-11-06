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
from . import const
from rweb.path.staticDhcpLease import StaticDHCPLeaseLocators
from rweb.path.dmzHost import DmzHostLocators
from rweb.path.dhcp import DhcpLocators
from rweb.path.cloneMacAddress import CloneMacAddressLocators
from rweb.path.ddns import DDNSLocators
from rweb.path.networkMode import NetworkModeLocators
from rweb.path.networkDiagnosis import NetworkDiagnosisLocators
from rweb.path.systemLog import SystemLogLocators
from rweb.path.vpn import VpnLocators


"""VPN"""

class VPN(Base):
    def setUp(self):
        super(VPN, self).setUp()
        # 鼠标模拟移动到：高级设置
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_AdvancedSettings))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_AdvancedSettings)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 VPN
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.VPN))
        ).click()
        time.sleep(2)


    #@unittest.skip("跳过")
    def test_A_vpn_pptp(self):
        """VPN-新增PPTP"""
        # 点击 新增 按钮
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VpnLocators.Add))
        ).click()
        # 输入 名称
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VpnLocators.Name))
        ).send_keys("PPTP")
        # 选择协议：PPTP
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VpnLocators.Protocol))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VpnLocators.Protocol_PPTP))
        ).click()
        # 输入 服务器
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VpnLocators.Server))
        ).send_keys("vpn.hyku.org")
        # 输入 用户名
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VpnLocators.Username))
        ).send_keys("gaojun")
        # 输入 密码
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VpnLocators.Password))
        ).send_keys("gaojun@2019")
        # 保存
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VpnLocators.Save))
        ).click()
        # 断言:toast提示：新增成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言：查看是否与新增时填写的一致
        # 点击 编辑 按钮
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VpnLocators.Edit))
        ).click()
        # 断言：名称
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, VpnLocators.Name))
        )
        assert self.driver.find_element_by_xpath(VpnLocators.Name).get_attribute("value") == "PPTP"
        # 断言：协议
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, VpnLocators.Protocol))
        )
        Protocol_value = self.driver.find_element_by_xpath(VpnLocators.Protocol).get_attribute('value')
        assert Protocol_value == "PPTP", Protocol_value
        # 断言：服务器
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, VpnLocators.Server))
        )
        assert self.driver.find_element_by_xpath(VpnLocators.Server).get_attribute("value") == "vpn.hyku.org"
        # 断言：用户名
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, VpnLocators.Username))
        )
        assert self.driver.find_element_by_xpath(VpnLocators.Username).get_attribute("value") == "gaojun"
        # 断言：密码
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, VpnLocators.Password))
        )
        assert self.driver.find_element_by_xpath(VpnLocators.Password).get_attribute("value") == "gaojun@2019"

        # 删除该VPN
        self.driver.back()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VpnLocators.Delete))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VpnLocators.Delete_Ok))
        ).click()


    #@unittest.skip("跳过")
    def test_B_vpn_l2tp(self):
        """VPN-新增L2TP"""
        # 点击 新增 按钮
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VpnLocators.Add))
        ).click()
        # 输入 名称
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VpnLocators.Name))
        ).send_keys("L2TP")
        # 选择协议：L2TP
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VpnLocators.Protocol))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VpnLocators.Protocol_L2TP))
        ).click()
        # 输入 服务器
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VpnLocators.Server))
        ).send_keys("vpn.hyku.org")
        # 输入 用户名
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VpnLocators.Username))
        ).send_keys("gaojun")
        # 输入 密码
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VpnLocators.Password))
        ).send_keys("gaojun@2019")
        # 保存
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VpnLocators.Save))
        ).click()
        # 断言:toast提示：新增成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言：查看是否与新增时填写的一致
        # 点击 编辑 按钮
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VpnLocators.Edit))
        ).click()
        # 断言：名称
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, VpnLocators.Name))
        )
        assert self.driver.find_element_by_xpath(VpnLocators.Name).get_attribute("value") == "L2TP"
        # 断言：协议
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, VpnLocators.Protocol))
        )
        Protocol_value = self.driver.find_element_by_xpath(VpnLocators.Protocol).get_attribute('value')
        assert Protocol_value == "L2TP", Protocol_value
        # 断言：服务器
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, VpnLocators.Server))
        )
        assert self.driver.find_element_by_xpath(VpnLocators.Server).get_attribute("value") == "vpn.hyku.org"
        # 断言：用户名
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, VpnLocators.Username))
        )
        assert self.driver.find_element_by_xpath(VpnLocators.Username).get_attribute("value") == "gaojun"
        # 断言：密码
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, VpnLocators.Password))
        )
        assert self.driver.find_element_by_xpath(VpnLocators.Password).get_attribute("value") == "gaojun@2019"


    #@unittest.skip("跳过")
    def test_C_vpn_on(self):
        """VPN-打开VPN"""
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VpnLocators.Statu))
        )
        Statu_class = self.driver.find_element_by_xpath(VpnLocators.Statu).get_attribute('class')
        # 理应是关闭的，如果是关闭状态，才进行if操作打开VPN
        if Statu_class == "switch switch-animation":
            # 点击 打开 按钮
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, VpnLocators.Statu))
            ).click()

            # 断言:toast提示：打开成功
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言：检验开关状态是否为：打开
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VpnLocators.Statu))
        )
        Statu_class = self.driver.find_element_by_xpath(VpnLocators.Statu).get_attribute('class')
        assert Statu_class == "switch switch-animation checked", Statu_class





    #@unittest.skip("跳过")
    def test_D_vpn_off(self):
        """VPN-关闭VPN"""
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VpnLocators.Statu))
        )
        Statu_class = self.driver.find_element_by_xpath(VpnLocators.Statu).get_attribute('class')
        # 理应是打开的，如果是打开状态，才进行if操作关闭VPN

        if Statu_class == "switch switch-animation checked":
            # 点击 关闭 按钮
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, VpnLocators.Statu))
            ).click()

            # 断言:toast提示：关闭成功
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言：检验开关状态是否为：关闭
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, VpnLocators.Statu))
        )
        Statu_class = self.driver.find_element_by_xpath(VpnLocators.Statu).get_attribute('class')
        assert Statu_class == "switch switch-animation", Statu_class


    #@unittest.skip("跳过")
    def test_E_vpn_deleteAll(self):
        """VPN-删除所有VPN"""
        time.sleep(2)

        flag = False
        while flag == False:
            try:
                assert self.driver.find_element_by_xpath("//p[@class='empty-text']").is_displayed()
                flag = True
            except:
                Delete = VpnLocators.Delete.format(num="last()")
                WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                    EC.element_to_be_clickable((By.XPATH, Delete))
                ).click()
                WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                    EC.element_to_be_clickable((By.XPATH, VpnLocators.Delete_Ok))
                ).click()
                # 断言:toast提示：成功
                WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                    EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
                )
                time.sleep(2)