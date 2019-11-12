#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/21 12:54
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
from rweb.path.internetSettings import InternetSettingsLocators
from rweb.path.routerManagement import RouterManagementLocators

"""上网设置"""


class InternetSettings(Base):
    def setUp(self):
        super(InternetSettings, self).setUp()
        # 鼠标模拟移动到：设置
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 上网设置
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Internet_Settings))
        ).click()
        time.sleep(2)

    # @unittest.skip("跳过")
    def test_A_PPPoE(self):
        """上网设置-设置为PPPoE"""
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, InternetSettingsLocators.Internet_Way))
        # )
        # Internet_Way_value = self.driver.find_element_by_xpath(InternetSettingsLocators.Internet_Way).get_attribute('value')
        # # 如果上网方式不为PPPoE，才进行下面的if操作，切换为PPPoE
        # if Internet_Way_value != "PPPoE":
        #     # 点击上网方式
        #     WebDriverWait(self.driver, 10).until(
        #         EC.element_to_be_clickable((By.XPATH, InternetSettingsLocators.Internet_Way))
        #     ).click()
        #     # 选择 PPPoE
        #     WebDriverWait(self.driver, 10).until(
        #         EC.element_to_be_clickable((By.XPATH, InternetSettingsLocators.PPPoE))
        #     ).click()
        #     # 输入 宽带账号
        #     WebDriverWait(self.driver, 10).until(
        #         EC.element_to_be_clickable((By.XPATH, InternetSettingsLocators.PPPoE_Username))
        #     ).clear()
        #     self.driver.find_element_by_xpath(InternetSettingsLocators.PPPoE_Username).send_keys("gaojun")
        #     # 输入 宽带密码
        #     WebDriverWait(self.driver, 10).until(
        #         EC.element_to_be_clickable((By.XPATH, InternetSettingsLocators.PPPoE_Password))
        #     ).clear()
        #     self.driver.find_element_by_xpath(InternetSettingsLocators.PPPoE_Password).send_keys("gaojun@2019")
        #     # 保存
        #     WebDriverWait(self.driver, 10).until(
        #         EC.element_to_be_clickable((By.XPATH, InternetSettingsLocators.Save))
        #     ).click()
        #     WebDriverWait(self.driver, 10).until(
        #         EC.element_to_be_clickable((By.XPATH, InternetSettingsLocators.Save_Ok))
        #     ).click()
        #
        #     # 因为修改成功后没有toast提示，所以不能用成功的toast提示判断是否完成reboot
        #     # 又因为reboot完成后，页面处于：我的WiFi-管理路由器，故可借判断管理路由器页的“mesh拓扑图”元素是否加载出来，来判断是否完成reboot
        #     WebDriverWait(self.driver, 60).until(
        #         EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Mesh_Topology))
        #     )
        #
        #     # 断言：判断主页那根线是否是通的
        #     time.sleep(5)
        #     self.driver.refresh()
        #     time.sleep(5)
        #     assert self.driver.find_element_by_xpath(InternetSettingsLocators.Line).get_attribute('class') == "line"
        #
        #     # 断言：判断是否修改为：PPPoE
        #     # 再次进入 上网设置 页
        #     WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
        #     )
        #     mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
        #     ActionChains(self.driver).move_to_element(mouse).perform()
        #     # 点击 上网设置
        #     WebDriverWait(self.driver, 10).until(
        #         EC.element_to_be_clickable((By.XPATH, CommonLocators.Internet_Settings))
        #     ).click()
        #     time.sleep(2)
        # # 断言：是否为：PPPoE：
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, InternetSettingsLocators.Internet_Way))
        # )
        # Internet_Way_value = self.driver.find_element_by_xpath(InternetSettingsLocators.Internet_Way).get_attribute('value')
        # assert Internet_Way_value == "PPPoE", Internet_Way_value

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, InternetSettingsLocators.Internet_Way))
        )
        Internet_Way_value = self.driver.find_element_by_xpath(InternetSettingsLocators.Internet_Way).get_attribute(
            'value')
        # 如果上网方式不为PPPoE，才进行下面的if操作，切换为PPPoE
        if Internet_Way_value != "PPPoE":
            # 点击上网方式
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, InternetSettingsLocators.Internet_Way))
            ).click()
            # 选择 PPPoE
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, InternetSettingsLocators.PPPoE))
            ).click()
            # 输入 宽带账号
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, InternetSettingsLocators.PPPoE_Username))
            ).clear()
            self.driver.find_element_by_xpath(InternetSettingsLocators.PPPoE_Username).send_keys("gaojun")
            # 输入 宽带密码
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, InternetSettingsLocators.PPPoE_Password))
            ).clear()
            self.driver.find_element_by_xpath(InternetSettingsLocators.PPPoE_Password).send_keys("gaojun@2019")
            # 保存
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, InternetSettingsLocators.Save))
            ).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, InternetSettingsLocators.Save_Ok))
            ).click()

            # 因为修改成功后没有toast提示，所以不能用成功的toast提示判断是否完成reboot
            # 又因为reboot完成后，页面处于：我的WiFi-管理路由器，故可借判断管理路由器页的“mesh拓扑图”元素是否加载出来，来判断是否完成reboot
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Mesh_Topology))
            )

            time.sleep(5)
            WebDriverWait(self.driver, 60).until_not(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Shadow))
            )

        # 断言：是否为：PPPoE：
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, InternetSettingsLocators.Internet_Way))
        )
        Internet_Way_value = self.driver.find_element_by_xpath(InternetSettingsLocators.Internet_Way).get_attribute(
            "value")
        assert Internet_Way_value == "PPPoE", Internet_Way_value

        # # 进入 管理设备 页，目的：断言那根线是否是通的
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_MyWifi))
        # )
        # mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_MyWifi)
        # ActionChains(self.driver).move_to_element(mouse).perform()
        # # 点击 管理设备
        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, CommonLocators.Router_Management))
        # ).click()
        # time.sleep(2)

        # # 断言：判断主页那根线是否是通的
        # time.sleep(5)
        # self.driver.refresh()
        # time.sleep(5)
        # assert self.driver.find_element_by_xpath(InternetSettingsLocators.Line).get_attribute('class') == "line"

    @unittest.skip("跳过")
    def test_B_StaticIP(self):
        """上网设置-设置为静态IP"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, InternetSettingsLocators.Internet_Way))
        )
        Internet_Way_value = self.driver.find_element_by_xpath(InternetSettingsLocators.Internet_Way).get_attribute(
            'value')
        # 如果上网方式不为静态IP，才进行下面的if操作，切换为静态IP
        if Internet_Way_value != "Static IP":
            # 点击上网方式
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, InternetSettingsLocators.Internet_Way))
            ).click()
            # 选择 静态IP
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, InternetSettingsLocators.StaticIP))
            ).click()
            # 输入 IP地址
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, InternetSettingsLocators.StaticIP_IP))
            ).clear()
            self.driver.find_element_by_xpath(InternetSettingsLocators.StaticIP_IP).send_keys("10.70.100.46")
            # 输入 子网掩码
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, InternetSettingsLocators.StaticIP_Netmask))
            ).clear()
            self.driver.find_element_by_xpath(InternetSettingsLocators.StaticIP_Netmask).send_keys("255.255.0.0")
            # 输入 网关
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, InternetSettingsLocators.StaticIP_Gateway))
            ).clear()
            self.driver.find_element_by_xpath(InternetSettingsLocators.StaticIP_Gateway).send_keys("10.70.0.1")
            # 输入 DNS
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, InternetSettingsLocators.StaticIP_DNS))
            ).clear()
            self.driver.find_element_by_xpath(InternetSettingsLocators.StaticIP_DNS).send_keys("10.70.0.1")
            # 保存
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, InternetSettingsLocators.Save))
            ).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, InternetSettingsLocators.Save_Ok))
            ).click()

            # 因为修改成功后没有toast提示，所以不能用成功的toast提示判断是否完成reboot
            # 又因为reboot完成后，页面处于：我的WiFi-管理路由器，故可借判断管理路由器页的“mesh拓扑图”元素是否加载出来，来判断是否完成reboot
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Mesh_Topology))
            )

            # 断言：判断主页那根线是否是通的
            time.sleep(7)
            self.driver.refresh()
            time.sleep(3)
            assert self.driver.find_element_by_xpath(InternetSettingsLocators.Line).get_attribute('class') == "line"

            # 断言：判断是否修改为：静态IP
            # 再次进入 上网设置 页
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
            )
            mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
            ActionChains(self.driver).move_to_element(mouse).perform()
            # 点击 上网设置
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, CommonLocators.Internet_Settings))
            ).click()
            time.sleep(2)
        # 断言：是否为：静态IP：
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, InternetSettingsLocators.Internet_Way))
        )
        Internet_Way_value = self.driver.find_element_by_xpath(InternetSettingsLocators.Internet_Way).get_attribute(
            'value')
        assert Internet_Way_value == "Static IP", Internet_Way_value

    @unittest.skip("跳过")
    def test_C_DHCP(self):
        """上网设置-设置为动态IP"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, InternetSettingsLocators.Internet_Way))
        )
        Internet_Way_value = self.driver.find_element_by_xpath(InternetSettingsLocators.Internet_Way).get_attribute(
            'value')
        # 如果上网方式不为动态IP，才进行下面的if操作，切换为动态IP
        if Internet_Way_value != "DHCP":
            # 点击上网方式
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, InternetSettingsLocators.Internet_Way))
            ).click()
            # 选择 动态IP
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, InternetSettingsLocators.DHCP))
            ).click()
            # 保存
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, InternetSettingsLocators.Save))
            ).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, InternetSettingsLocators.Save_Ok))
            ).click()

            # 因为修改成功后没有toast提示，所以不能用成功的toast提示判断是否完成reboot
            # 又因为reboot完成后，页面处于：我的WiFi-管理路由器，故可借判断管理路由器页的“mesh拓扑图”元素是否加载出来，来判断是否完成reboot
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Mesh_Topology))
            )

            # 断言：判断主页那根线是否是通的
            time.sleep(7)
            self.driver.refresh()
            time.sleep(3)
            assert self.driver.find_element_by_xpath(InternetSettingsLocators.Line).get_attribute('class') == "line"

            # 断言：判断是否修改为：动态IP
            # 再次进入 上网设置 页
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
            )
            mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
            ActionChains(self.driver).move_to_element(mouse).perform()
            # 点击 上网设置
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, CommonLocators.Internet_Settings))
            ).click()
            time.sleep(2)
        # 断言：是否为：动态IP：
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, InternetSettingsLocators.Internet_Way))
        )
        Internet_Way_value = self.driver.find_element_by_xpath(InternetSettingsLocators.Internet_Way).get_attribute(
            'value')
        assert Internet_Way_value == "DHCP", Internet_Way_value
