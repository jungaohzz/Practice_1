#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/20 23:59
# @Author:  GaoJun

import unittest
from .. base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from rweb import const
from rweb.path.common import CommonLocators
from rweb.path.devices import DevicesLocators
from rweb.path.limitTime import LimitTimeLocators
from selenium.webdriver.common.action_chains import ActionChains
from rweb.path.staticDhcpLease import StaticDHCPLeaseLocators
from rweb.path.dmzHost import DmzHostLocators
from rweb.path.dhcp import DhcpLocators
from rweb.path.wifiSettings import WifiSettingsLocators
from rweb.path.routerManagement import RouterManagementLocators
from .guestwifi_set_testcase import Test_wifi
from .guestwifi_set_conf import *

"""WiFi设置"""

class GuestWifi(Base):
    # 定义WiFi设置页的url
    url_guestWifiSettingsPage = ""

    def switch_to_guestWifiSetPage(self, Current_Url):  # 切换到 guest Wifi设置页
        self.driver.refresh()
        time.sleep(1)
        # 判断当前的url是否是目的url
        while GuestWifi.url_guestWifiSettingsPage != Current_Url:
            # 鼠标模拟移动到：设置
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
            )
            mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
            ActionChains(self.driver).move_to_element(mouse).perform()
            # 点击 访客WiFi
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, CommonLocators.Guest_WiFi))
            ).click()
            Current_Url = self.driver.current_url
            time.sleep(1)





    @unittest.skip("跳过")
    def test_A_get_url(self):
        """操作步骤：获取访客WiFi的WiFi设置页url"""
        # 鼠标模拟移动到：设置
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 WiFi设置
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.WiFi_Settings))
        ).click()
        time.sleep(2)
        GuestWifi.url_guestWifiSettingsPage = self.driver.current_url
        time.sleep(5)






    @unittest.skip("跳过")
    def test_B_wifiSetting_SmartConnect_on(self):
        """操作步骤：设置SSID名，且将“双频合一”状态开启"""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Wifi_Name))
        ).clear()
        self.driver.find_element_by_xpath(WifiSettingsLocators.Wifi_Name).send_keys(ssid_2g)
        # 密码框
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.WiFi_Password))
        ).clear()
        self.driver.find_element_by_xpath(WifiSettingsLocators.WiFi_Password).send_keys(wlan_password)
        # “双频合一”开关
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute('class')
        # 默认状态：打开，所以如果状态为：关闭，才进行if的打开操作
        if Smart_Connect_class != "switch switch-animation checked":
            # 点击按钮：双频合一，即由关 -> 开
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Smart_Connect))
            ).click()
            time.sleep(2)  # 用于开关切换

        # 保存
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Save))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Save_Ok))
        ).click()
        time.sleep(5)

        # 因为修改密码后没有成功的toast提示，所以不能用成功的toast提示判断是否完成reboot
        # 又因为reboot完成后，页面处于：我的WiFi-管理路由器，故可借判断管理路由器页的“mesh拓扑图”元素是否加载出来，来判断是否完成reboot
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Mesh_Topology))
        )
        time.sleep(10)
        # 断言：判断开关状态是否为：打开
        # 再次进入 WiFi设置 页
        self.switch_to_guestWifiSetPage(self.driver.current_url)

        # 判断无线名称
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Wifi_Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(WifiSettingsLocators.Wifi_Name).get_attribute("value")
        assert Wifi_Name_Text == ssid_2g, Wifi_Name_Text
        # 判断密码
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.WiFi_Password))
        )
        WiFi_Password_Text = self.driver.find_element_by_xpath(WifiSettingsLocators.WiFi_Password).get_attribute("value")
        assert  WiFi_Password_Text== wlan_password
        # 判断双频合一开关
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute('class')
        assert Smart_Connect_class == "switch switch-animation checked", Smart_Connect_class






    @unittest.skip("跳过")
    def test_C_test_wifi_1(self):
        """【检验】用例-3384:“双频合一”开启状态，扫描到的SSID中，5G和2.4G SSID一样"""
        self.switch_to_guestWifiSetPage(self.driver.current_url)
        # 前提条件：“双频合一”开关开启
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute('class')
        if Smart_Connect_class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关未开启")
            assert False

        # 前提检验完成，开始检验用例
        Result = Test_wifi.test_wifi_1()
        if Result == 1:
            print("【成功】“双频合一”开启时扫描到的5G和2.4G的SSID一样")
            assert True
        else:
            print("【失败】“双频合一”开启时扫描到的5G和2.4G的SSID不一样")
            assert False








    @unittest.skip("跳过")
    def test_D_test_wifi_2(self):
        """【检验】用例-3510 :“双频合一”开启状态，2T2R设备能成功连接2.4G SSID，协商速率300M"""
        self.switch_to_guestWifiSetPage(self.driver.current_url)
        # 前提条件：“双频合一”开关开启
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute('class')
        if Smart_Connect_class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关未开启")
            assert False

        # 前提检验完成，开始检验用例
        Result = Test_wifi.test_wifi_2()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False







    @unittest.skip("跳过")
    def test_E_test_wifi_3(self):
        """【检验】用例-3509 :“双频合一”开启状态，2T2R设备能成功连接5G SSID,协商速率正确867M"""
        self.switch_to_guestWifiSetPage(self.driver.current_url)
        # 前提条件：“双频合一”开关开启
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute('class')
        if Smart_Connect_class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关未开启")
            assert False

        # 前提检验完成，开始检验用例
        Result = Test_wifi.test_wifi_3()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False







    @unittest.skip("跳过")
    def test_F_wifiSetting_SmartConnect_off(self):
        """操作步骤：将“双频合一”状态关闭"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute('class')
        # 状态理应是打开的，所以如果状态为：打开，才进行if的关闭操作
        if Smart_Connect_class != "switch switch-animation":
            # 点击按钮：双频合一，即由开 -> 关
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Smart_Connect))
            ).click()
            time.sleep(2)  # 用于开关切换

            # 保存
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Save))
            ).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Save_Ok))
            ).click()
            time.sleep(5)

            # 因为修改密码后没有成功的toast提示，所以不能用成功的toast提示判断是否完成reboot
            # 又因为reboot完成后，页面处于：我的WiFi-管理路由器，故可借判断管理路由器页的“mesh拓扑图”元素是否加载出来，来判断是否完成reboot
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Mesh_Topology))
            )
            time.sleep(10)
            # 断言：判断开关状态是否为：关闭
            # 再次进入 WiFi设置 页
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
            )
            mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
            ActionChains(self.driver).move_to_element(mouse).perform()
            # 点击 WiFi设置
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, CommonLocators.WiFi_Settings))
            ).click()
            time.sleep(2)
        # 判断双频合一开关
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute(
            'class')
        assert Smart_Connect_class == "switch switch-animation", Smart_Connect_class








    @unittest.skip("跳过")
    def test_G_test_wifi_4(self):
        """【检验】用例-2734 :“双频合一”关闭状态，扫描到的SSID中，2.4G SSID为XXXX,5G SSID为XXXX-5G"""
        self.switch_to_guestWifiSetPage(self.driver.current_url)
        # 前提条件：“双频合一”开关为关闭
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute('class')
        if Smart_Connect_class != "switch switch-animation":
            print("【备注】该用例无法验证，原因：“双频合一”开关未关闭")
            assert False

        # 前提检验完成，开始检验用例
        Result = Test_wifi.test_wifi_4()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False







    @unittest.skip("跳过")
    def test_H_test_wifi_5(self):
        """【检验】用例-3075 :“双频合一”关闭状态，2T2R设备能成功连接2.4G，协商速率300M"""
        self.switch_to_guestWifiSetPage(self.driver.current_url)
        # 前提条件：“双频合一”开关为关闭
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute('class')
        if Smart_Connect_class != "switch switch-animation":
            print("【备注】该用例无法验证，原因：“双频合一”开关未关闭")
            assert False

        # 前提检验完成，开始检验用例
        Result = Test_wifi.test_wifi_5()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False







    @unittest.skip("跳过")
    def test_I_test_wifi_6(self):
        """【检验】用例-3076 :“双频合一”关闭状态，2T2R设备能成功连接5G，协商速率867M"""
        self.switch_to_guestWifiSetPage(self.driver.current_url)
        # 前提条件：“双频合一”开关为关闭
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute('class')
        if Smart_Connect_class != "switch switch-animation":
            print("【备注】该用例无法验证，原因：“双频合一”开关未关闭")
            assert False

        # 前提检验完成，开始检验用例
        Result = Test_wifi.test_wifi_6()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False















    @unittest.skip("跳过")
    def test_J_wifiSetting_hideSSID_off(self):
        """操作步骤：修改隐藏SSID开关：由开->关"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute('class')
        # 默认状态：关闭
        # 如果状态为：打开，才进行if的关闭操作
        if Smart_Connect_class == "switch switch-animation checked":
            # 点击按钮：隐藏SSID，即由开 -> 关
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Hide_SSID))
            ).click()
            time.sleep(2)  # 用于开关切换

            # 保存
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Save))
            ).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Save_Ok))
            ).click()
            time.sleep(5)

            # 因为修改密码后没有成功的toast提示，所以不能用成功的toast提示判断是否完成reboot
            # 又因为reboot完成后，页面处于：我的WiFi-管理路由器，故可借判断管理路由器页的“mesh拓扑图”元素是否加载出来，来判断是否完成reboot
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Mesh_Topology))
            )
            time.sleep(5)
            # 断言：判断开关状态是否为：关闭
            # 再次进入 WiFi设置 页
            self.switch_to_guestWifiSetPage(self.driver.current_url)
        # 判断隐藏SSID开关
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute('class')
        assert Smart_Connect_class == "switch switch-animation", Smart_Connect_class








    @unittest.skip("跳过")
    def test_K_test_wifi_7(self):
        """【检验】用例-3378 :隐藏SSID关闭状态，5G设备可以扫描到5G SSID，并可以正常连接"""
        self.switch_to_guestWifiSetPage(self.driver.current_url)
        # 前提条件：“双频合一”开关为关闭
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute('class')
        if Smart_Connect_class != "switch switch-animation":
            print("【备注】该用例无法验证，原因：“隐藏SSID”开关未关闭")
            assert False

        # 前提检验完成，开始检验用例
        Result = Test_wifi.test_wifi_7()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False







    @unittest.skip("跳过")
    def test_L_test_wifi_8(self):
        """【检验】用例-4973 :隐藏SSID关闭状态，2.4G设备可以扫描到2.4G SSID，并可以正常连接"""
        self.switch_to_guestWifiSetPage(self.driver.current_url)
        # 前提条件：“双频合一”开关为关闭
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute('class')
        if Smart_Connect_class != "switch switch-animation":
            print("【备注】该用例无法验证，原因：“隐藏SSID”开关未关闭")
            assert False

        # 前提检验完成，开始检验用例
        Result = Test_wifi.test_wifi_8()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False









    @unittest.skip("跳过")
    def test_M_wifiSetting_hideSSID_on(self):
        """操作步骤：修改隐藏SSID开关：由关->开"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute('class')
        # 默认状态：关闭
        # 如果状态为：关闭，才进行if的打开操作
        if Smart_Connect_class != "switch switch-animation checked":
            # 点击按钮：隐藏SSID，即由关 -> 开
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Hide_SSID))
            ).click()
            time.sleep(2)  # 用于开关切换

            # 保存
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Save))
            ).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Save_Ok))
            ).click()
            time.sleep(5)

            # 因为修改密码后没有成功的toast提示，所以不能用成功的toast提示判断是否完成reboot
            # 又因为reboot完成后，页面处于：我的WiFi-管理路由器，故可借判断管理路由器页的“mesh拓扑图”元素是否加载出来，来判断是否完成reboot
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Mesh_Topology))
            )
            time.sleep(5)
            # 断言：判断开关状态是否为：启用
            # 再次进入 WiFi设置 页
            self.switch_to_guestWifiSetPage(self.driver.current_url)
        # 判断隐藏SSID开关
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute('class')
        assert Smart_Connect_class == "switch switch-animation checked", Smart_Connect_class








    @unittest.skip("跳过")
    def test_N_test_wifi_9(self):
        """【检验】用例-3377 :隐藏SSID开启状态，5G设备无法扫描到5G SSID"""
        self.switch_to_guestWifiSetPage(self.driver.current_url)
        # 前提条件：“双频合一”开关为关闭
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute('class')
        if Smart_Connect_class == "switch switch-animation":
            print("【备注】该用例无法验证，原因：“隐藏SSID”开关未开启")
            assert False

        # 前提检验完成，开始检验用例
        Result = Test_wifi.test_wifi_9()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False







    @unittest.skip("跳过")
    def test_O_test_wifi_10(self):
        """【检验】用例-4971 :隐藏SSID开启状态，2.4G设备无法扫描到2.4G SSID"""
        self.switch_to_guestWifiSetPage(self.driver.current_url)
        # 前提条件：“双频合一”开关为关闭
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute('class')
        if Smart_Connect_class == "switch switch-animation":
            print("【备注】该用例无法验证，原因：“隐藏SSID”开关未开启")
            assert False

        # 前提检验完成，开始检验用例
        Result = Test_wifi.test_wifi_10()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")







    @unittest.skip("跳过")
    def test_P_test_wifi_11(self):
        """【检验】用例-1513 :隐藏SSID开启，5G设备可通过手动添加SSID和密码连接到路由器"""
        self.switch_to_guestWifiSetPage(self.driver.current_url)
        # 前提条件：“双频合一”开关为关闭
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute(
            'class')
        if Smart_Connect_class == "switch switch-animation":
            print("【备注】该用例无法验证，原因：“隐藏SSID”开关未开启")
            assert False

        # 前提检验完成，开始检验用例
        Result = Test_wifi.test_wifi_11()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")








    @unittest.skip("跳过")
    def test_Q_test_wifi_12(self):
        """【检验】用例-4970 :隐藏SSID开启，2.4G设备可通过手动添加SSID和密码连接到路由器"""
        self.switch_to_guestWifiSetPage(self.driver.current_url)
        # 前提条件：“双频合一”开关为关闭
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute(
            'class')
        if Smart_Connect_class == "switch switch-animation":
            print("【备注】该用例无法验证，原因：“隐藏SSID”开关未开启")
            assert False

        # 前提检验完成，开始检验用例
        Result = Test_wifi.test_wifi_12()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")








    @unittest.skip("跳过")
    def test_R_wifiSetting_hideSSID_off(self):
        """操作步骤：修改隐藏SSID开关：由开->关"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute('class')
        # 默认状态：关闭
        # 如果状态为：打开，才进行if的关闭操作
        if Smart_Connect_class == "switch switch-animation checked":
            # 点击按钮：隐藏SSID，即由开 -> 关
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Hide_SSID))
            ).click()
            time.sleep(2)  # 用于开关切换
            # 保存
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Save))
            ).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Save_Ok))
            ).click()
            time.sleep(5)
            # 因为修改密码后没有成功的toast提示，所以不能用成功的toast提示判断是否完成reboot
            # 又因为reboot完成后，页面处于：我的WiFi-管理路由器，故可借判断管理路由器页的“mesh拓扑图”元素是否加载出来，来判断是否完成reboot
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Mesh_Topology))
            )
            time.sleep(5)
            # 断言：判断开关状态是否为：关闭
            # 再次进入 WiFi设置 页
            self.switch_to_guestWifiSetPage(self.driver.current_url)
        # 判断隐藏SSID开关
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute('class')
        assert Smart_Connect_class == "switch switch-animation", Smart_Connect_class








    @unittest.skip("跳过")
    def test_S_test_wifi_13(self):
        """【检验】用例-4973 :隐藏SSID关闭状态，2.4G设备可以扫描到2.4G SSID，并可以正常连接"""
        self.switch_to_guestWifiSetPage(self.driver.current_url)
        # 前提条件：“双频合一”开关为关闭
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute('class')
        if Smart_Connect_class != "switch switch-animation":
            print("【备注】该用例无法验证，原因：“隐藏SSID”开关未关闭")
            assert False

        # 前提检验完成，开始检验用例
        Result = Test_wifi.test_wifi_13()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False








    @unittest.skip("跳过")
    def test_T_test_wifi_14(self):
        """【检验】用例-4975 :隐藏SSID关闭，2.4G设备可通过手动添加SSID和密码连接到路由器"""
        self.switch_to_guestWifiSetPage(self.driver.current_url)
        # 前提条件：“双频合一”开关为关闭
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute('class')
        if Smart_Connect_class != "switch switch-animation":
            print("【备注】该用例无法验证，原因：“隐藏SSID”开关未关闭")
            assert False

        # 前提检验完成，开始检验用例
        Result = Test_wifi.test_wifi_14()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False










    @unittest.skip("跳过")
    def test_U_wifiSetting_ssid20bit_password24bit(self):
        """操作步骤：设置SSID为20个字节，密码为24个字节，且“隐藏SSID”开关为关，“双频合一”开关为开"""
        self.switch_to_guestWifiSetPage(self.driver.current_url)
        # 无线名称框
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Wifi_Name))
        ).clear()
        self.driver.find_element_by_xpath(WifiSettingsLocators.Wifi_Name).send_keys(ssid_2g_20b)
        # 密码框
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.WiFi_Password))
        ).clear()
        self.driver.find_element_by_xpath(WifiSettingsLocators.WiFi_Password).send_keys(wlan_password_24b)
        # “隐藏SSID”开关
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute('class')
        # 默认状态：关闭。如果状态为：开启，才进行if的关闭操作
        if Smart_Connect_class == "switch switch-animation checked":
            # 点击按钮：隐藏SSID，即由开 -> 关
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Hide_SSID))
            ).click()
            time.sleep(2)  # 用于开关切换
        # “双频合一”开关
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute('class')
        # 默认状态：打开，所以如果状态为：关闭，才进行if的打开操作
        if Smart_Connect_class != "switch switch-animation checked":
            # 点击按钮：双频合一，即由关 -> 开
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Smart_Connect))
            ).click()
            time.sleep(2)  # 用于开关切换

        # 保存
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Save))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Save_Ok))
        ).click()
        time.sleep(5)

        # 因为修改密码后没有成功的toast提示，所以不能用成功的toast提示判断是否完成reboot
        # 又因为reboot完成后，页面处于：我的WiFi-管理路由器，故可借判断管理路由器页的“mesh拓扑图”元素是否加载出来，来判断是否完成reboot
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Mesh_Topology))
        )
        time.sleep(10)
        # 断言：判断开关状态是否为：打开
        # 再次进入 WiFi设置 页
        self.switch_to_guestWifiSetPage(self.driver.current_url)

        # 判断无线名称
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Wifi_Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(WifiSettingsLocators.Wifi_Name).get_attribute("value")
        assert Wifi_Name_Text == ssid_2g_20b, Wifi_Name_Text
        # 判断密码
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.WiFi_Password))
        )
        WiFi_Password_Text = self.driver.find_element_by_xpath(WifiSettingsLocators.WiFi_Password).get_attribute("value")
        assert WiFi_Password_Text == wlan_password_24b, WiFi_Password_Text
        # 判断隐藏SSID开关
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Hide_SSID_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute('class')
        assert Hide_SSID_class == "switch switch-animation", Hide_SSID_class
        # 判断双频合一开关
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute(
            'class')
        assert Smart_Connect_class == "switch switch-animation checked", Smart_Connect_class







    @unittest.skip("跳过")
    def test_V_test_wifi_15(self):
        """【检验】用例-4967 :SSID为20个字节，密码为24个字节，5G设备能成功连接"""
        self.switch_to_guestWifiSetPage(self.driver.current_url)
        # 前提条件：SSID为20个字节，密码为24个字节，“隐藏SSID”开关为关，“双频合一”开关为开
        # 判断无线名称
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Wifi_Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(WifiSettingsLocators.Wifi_Name).get_attribute("value")
        if Wifi_Name_Text != ssid_2g_20b:
            print("【备注】该用例无法验证，原因：SSID名不为20字节")
            assert False
        # 判断密码
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.WiFi_Password))
        )
        WiFi_Password_Text = self.driver.find_element_by_xpath(WifiSettingsLocators.WiFi_Password).get_attribute("value")
        if WiFi_Password_Text != wlan_password_24b:
            print("【备注】该用例无法验证，原因：密码不为24字节")
            assert False
        # 判断隐藏SSID开关
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Hide_SSID_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute('class')
        if Hide_SSID_class != "switch switch-animation":
            print("【备注】该用例无法验证，原因：“隐藏SSID”开关不为关")
            assert False
        # 判断双频合一开关
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute('class')
        assert Smart_Connect_class == "switch switch-animation checked", Smart_Connect_class
        if Smart_Connect_class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关不为开")
            assert False

        # 前提检验完成，开始检验用例
        Result = Test_wifi.test_wifi_15()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False








    @unittest.skip("跳过")
    def test_W_test_wifi_16(self):
        """【检验】用例-4969 :SSID为20个字节，密码为24个字节，2.4G设备能成功连接"""
        self.switch_to_guestWifiSetPage(self.driver.current_url)
        # 前提条件：SSID为20个字节，密码为24个字节，“隐藏SSID”开关为关，“双频合一”开关为开
        # 判断无线名称
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Wifi_Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(WifiSettingsLocators.Wifi_Name).get_attribute("value")
        if Wifi_Name_Text != ssid_2g_20b:
            print("【备注】该用例无法验证，原因：SSID名不为20字节")
            assert False
        # 判断密码
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.WiFi_Password))
        )
        WiFi_Password_Text = self.driver.find_element_by_xpath(WifiSettingsLocators.WiFi_Password).get_attribute(
            "value")
        if WiFi_Password_Text != wlan_password_24b:
            print("【备注】该用例无法验证，原因：密码不为24字节")
            assert False
        # 判断隐藏SSID开关
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Hide_SSID_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute('class')
        if Hide_SSID_class != "switch switch-animation":
            print("【备注】该用例无法验证，原因：“隐藏SSID”开关不为关")
            assert False
        # 判断双频合一开关
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute(
            'class')
        assert Smart_Connect_class == "switch switch-animation checked", Smart_Connect_class
        if Smart_Connect_class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关不为开")
            assert False

        # 前提检验完成，开始检验用例
        Result = Test_wifi.test_wifi_16()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False






    @unittest.skip("跳过")
    def test_X_wifiSetting_ssid20bit_password24bit(self):
        """操作步骤：设置SSID为1个字节，密码为8个字节，且“隐藏SSID”开关为关，“双频合一”开关为开"""
        self.switch_to_guestWifiSetPage(self.driver.current_url)
        # 无线名称框
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Wifi_Name))
        ).clear()
        self.driver.find_element_by_xpath(WifiSettingsLocators.Wifi_Name).send_keys(ssid_2g_1b)
        # 密码框
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.WiFi_Password))
        ).clear()
        self.driver.find_element_by_xpath(WifiSettingsLocators.WiFi_Password).send_keys(wlan_password_8b)
        # “隐藏SSID”开关
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute('class')
        # 默认状态：关闭。如果状态为：开启，才进行if的关闭操作
        if Smart_Connect_class == "switch switch-animation checked":
            # 点击按钮：隐藏SSID，即由开 -> 关
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Hide_SSID))
            ).click()
            time.sleep(2)  # 用于开关切换
        # “双频合一”开关
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute('class')
        # 默认状态：打开，所以如果状态为：关闭，才进行if的打开操作
        if Smart_Connect_class != "switch switch-animation checked":
            # 点击按钮：双频合一，即由关 -> 开
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Smart_Connect))
            ).click()
            time.sleep(2)  # 用于开关切换

        # 保存
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Save))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Save_Ok))
        ).click()
        time.sleep(5)

        # 因为修改密码后没有成功的toast提示，所以不能用成功的toast提示判断是否完成reboot
        # 又因为reboot完成后，页面处于：我的WiFi-管理路由器，故可借判断管理路由器页的“mesh拓扑图”元素是否加载出来，来判断是否完成reboot
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Mesh_Topology))
        )
        time.sleep(5)
        # 断言：判断开关状态是否为：打开
        # 再次进入 WiFi设置 页
        self.switch_to_guestWifiSetPage(self.driver.current_url)

        # 判断无线名称
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Wifi_Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(WifiSettingsLocators.Wifi_Name).get_attribute("value")
        assert Wifi_Name_Text == ssid_2g_1b, Wifi_Name_Text
        # 判断密码
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.WiFi_Password))
        )
        WiFi_Password_Text = self.driver.find_element_by_xpath(WifiSettingsLocators.WiFi_Password).get_attribute("value")
        assert WiFi_Password_Text == wlan_password_8b, WiFi_Password_Text
        # 判断隐藏SSID开关
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Hide_SSID_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute('class')
        assert Hide_SSID_class == "switch switch-animation", Hide_SSID_class
        # 判断双频合一开关
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute('class')
        assert Smart_Connect_class == "switch switch-animation checked", Smart_Connect_class







    @unittest.skip("跳过")
    def test_Y_test_wifi_17(self):
        """【检验】用例-4999 :SSID为1个字节，密码为8个字节，5G设备能成功连接"""
        self.switch_to_guestWifiSetPage(self.driver.current_url)
        # 前提条件：SSID为20个字节，密码为24个字节，“隐藏SSID”开关为关，“双频合一”开关为开
        # 判断无线名称
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Wifi_Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(WifiSettingsLocators.Wifi_Name).get_attribute("value")
        if Wifi_Name_Text != ssid_2g_1b:
            print("【备注】该用例无法验证，原因：SSID名不为1字节")
            assert False
        # 判断密码
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.WiFi_Password))
        )
        WiFi_Password_Text = self.driver.find_element_by_xpath(WifiSettingsLocators.WiFi_Password).get_attribute("value")
        if WiFi_Password_Text != wlan_password_8b:
            print("【备注】该用例无法验证，原因：密码不为8字节")
            assert False
        # 判断隐藏SSID开关
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Hide_SSID_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute('class')
        if Hide_SSID_class != "switch switch-animation":
            print("【备注】该用例无法验证，原因：“隐藏SSID”开关不为关")
            assert False
        # 判断双频合一开关
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute('class')
        assert Smart_Connect_class == "switch switch-animation checked", Smart_Connect_class
        if Smart_Connect_class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关不为开")
            assert False

        # 前提检验完成，开始检验用例
        Result = Test_wifi.test_wifi_17()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False







    @unittest.skip("跳过")
    def test_Z_test_wifi_18(self):
        """【检验】用例-5000 :SSID为1个字节，密码为8个字节，2.4G设备能成功连接"""
        self.switch_to_guestWifiSetPage(self.driver.current_url)
        # 前提条件：SSID为20个字节，密码为24个字节，“隐藏SSID”开关为关，“双频合一”开关为开
        # 判断无线名称
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Wifi_Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(WifiSettingsLocators.Wifi_Name).get_attribute("value")
        if Wifi_Name_Text != ssid_2g_1b:
            print("【备注】该用例无法验证，原因：SSID名不为1字节")
            assert False
        # 判断密码
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.WiFi_Password))
        )
        WiFi_Password_Text = self.driver.find_element_by_xpath(WifiSettingsLocators.WiFi_Password).get_attribute(
            "value")
        if WiFi_Password_Text != wlan_password_8b:
            print("【备注】该用例无法验证，原因：密码不为8字节")
            assert False
        # 判断隐藏SSID开关
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Hide_SSID_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute('class')
        if Hide_SSID_class != "switch switch-animation":
            print("【备注】该用例无法验证，原因：“隐藏SSID”开关不为关")
            assert False
        # 判断双频合一开关
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute(
            'class')
        assert Smart_Connect_class == "switch switch-animation checked", Smart_Connect_class
        if Smart_Connect_class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关不为开")
            assert False

        # 前提检验完成，开始检验用例
        Result = Test_wifi.test_wifi_18()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False







    @unittest.skip("跳过")
    def test_a_wifiSetting_onlyChange_ssid(self):
        """操作步骤：只修改SSID"""
        self.switch_to_guestWifiSetPage(self.driver.current_url)

        # 先将SSID和password改回原始的（即SSID=MERCKU-AutoTest，PASSWORD=11111111）
        self.test_B_wifiSetting_SmartConnect_on()

        # 再修改SSID
        # 无线名称框
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Wifi_Name))
        ).clear()
        self.driver.find_element_by_xpath(WifiSettingsLocators.Wifi_Name).send_keys(ssid_2g_change)
        # “隐藏SSID”开关
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute('class')
        # 默认状态：关闭。如果状态为：开启，才进行if的关闭操作
        if Smart_Connect_class == "switch switch-animation checked":
            # 点击按钮：隐藏SSID，即由开 -> 关
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Hide_SSID))
            ).click()
            time.sleep(2)  # 用于开关切换
        # “双频合一”开关
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute('class')
        # 默认状态：打开，所以如果状态为：关闭，才进行if的打开操作
        if Smart_Connect_class != "switch switch-animation checked":
            # 点击按钮：双频合一，即由关 -> 开
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Smart_Connect))
            ).click()
            time.sleep(2)  # 用于开关切换

        # 保存
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Save))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Save_Ok))
        ).click()
        time.sleep(5)

        # 因为修改密码后没有成功的toast提示，所以不能用成功的toast提示判断是否完成reboot
        # 又因为reboot完成后，页面处于：我的WiFi-管理路由器，故可借判断管理路由器页的“mesh拓扑图”元素是否加载出来，来判断是否完成reboot
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Mesh_Topology))
        )
        time.sleep(5)
        # 断言：判断开关状态是否为：打开
        # 再次进入 WiFi设置 页
        self.switch_to_guestWifiSetPage(self.driver.current_url)

        # 判断无线名称
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Wifi_Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(WifiSettingsLocators.Wifi_Name).get_attribute("value")
        assert Wifi_Name_Text == ssid_2g_change, Wifi_Name_Text
        # 判断密码
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.WiFi_Password))
        )
        WiFi_Password_Text = self.driver.find_element_by_xpath(WifiSettingsLocators.WiFi_Password).get_attribute("value")
        assert WiFi_Password_Text == wlan_password, WiFi_Password_Text
        # 判断隐藏SSID开关
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Hide_SSID_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute('class')
        assert Hide_SSID_class == "switch switch-animation", Hide_SSID_class
        # 判断双频合一开关
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute('class')
        assert Smart_Connect_class == "switch switch-animation checked", Smart_Connect_class







    @unittest.skip("跳过")
    def test_b_test_wifi_19(self):
        """【检验】用例-5017 :: 版本: 1 :: 修改SSID后，新SSID生效，旧SSID失效"""
        self.switch_to_guestWifiSetPage(self.driver.current_url)
        # 前提条件：SSID为已修改后的SSID
        # 判断无线名称
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Wifi_Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(WifiSettingsLocators.Wifi_Name).get_attribute("value")
        if Wifi_Name_Text != ssid_2g_change:
            print("【备注】该用例无法验证，原因：SSID名不为修改后的SSID")
            assert False
        # 判断密码
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.WiFi_Password))
        )
        WiFi_Password_Text = self.driver.find_element_by_xpath(WifiSettingsLocators.WiFi_Password).get_attribute("value")
        if WiFi_Password_Text != wlan_password:
            print("【备注】该用例无法验证，原因：密码不为初始密码")
            assert False
        # 判断隐藏SSID开关
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Hide_SSID_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute('class')
        if Hide_SSID_class != "switch switch-animation":
            print("【备注】该用例无法验证，原因：“隐藏SSID”开关不为关")
            assert False
        # 判断双频合一开关
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute('class')
        assert Smart_Connect_class == "switch switch-animation checked", Smart_Connect_class
        if Smart_Connect_class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关不为开")
            assert False

        # 前提检验完成，开始检验用例
        Result = Test_wifi.test_wifi_19()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False





    @unittest.skip("跳过")
    def test_c_wifiSetting_onlyChange_ssid(self):
        """操作步骤：只修改password"""
        self.switch_to_guestWifiSetPage(self.driver.current_url)

        # 先将SSID和password改回原始的（即SSID=MERCKU-AutoTest，PASSWORD=11111111）
        self.test_B_wifiSetting_SmartConnect_on()

        # 再修改password
        # 密码框
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.WiFi_Password))
        ).clear()
        self.driver.find_element_by_xpath(WifiSettingsLocators.WiFi_Password).send_keys(wlan_password_change)
        # “隐藏SSID”开关
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute('class')
        # 默认状态：关闭。如果状态为：开启，才进行if的关闭操作
        if Smart_Connect_class == "switch switch-animation checked":
            # 点击按钮：隐藏SSID，即由开 -> 关
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Hide_SSID))
            ).click()
            time.sleep(2)  # 用于开关切换
        # “双频合一”开关
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute(
            'class')
        # 默认状态：打开，所以如果状态为：关闭，才进行if的打开操作
        if Smart_Connect_class != "switch switch-animation checked":
            # 点击按钮：双频合一，即由关 -> 开
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Smart_Connect))
            ).click()
            time.sleep(2)  # 用于开关切换

        # 保存
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Save))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Save_Ok))
        ).click()
        time.sleep(5)

        # 因为修改密码后没有成功的toast提示，所以不能用成功的toast提示判断是否完成reboot
        # 又因为reboot完成后，页面处于：我的WiFi-管理路由器，故可借判断管理路由器页的“mesh拓扑图”元素是否加载出来，来判断是否完成reboot
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Mesh_Topology))
        )
        time.sleep(5)
        # 断言：判断开关状态是否为：打开
        # 再次进入 WiFi设置 页
        self.switch_to_guestWifiSetPage(self.driver.current_url)

        # 判断无线名称
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Wifi_Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(WifiSettingsLocators.Wifi_Name).get_attribute("value")
        assert Wifi_Name_Text == ssid_2g, Wifi_Name_Text
        # 判断密码
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.WiFi_Password))
        )
        WiFi_Password_Text = self.driver.find_element_by_xpath(WifiSettingsLocators.WiFi_Password).get_attribute("value")
        assert WiFi_Password_Text == wlan_password_change, WiFi_Password_Text
        # 判断隐藏SSID开关
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Hide_SSID_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute('class')
        assert Hide_SSID_class == "switch switch-animation", Hide_SSID_class
        # 判断双频合一开关
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute(
            'class')
        assert Smart_Connect_class == "switch switch-animation checked", Smart_Connect_class








    @unittest.skip("跳过")
    def test_d_test_wifi_20(self):
        """【检验】用例-5018 :: 版本: 1 :: 修改密码后，新密码生效，旧密码失效"""
        self.switch_to_guestWifiSetPage(self.driver.current_url)
        # 前提条件：password为已修改后的password
        # 判断无线名称
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Wifi_Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(WifiSettingsLocators.Wifi_Name).get_attribute("value")
        if Wifi_Name_Text != ssid_2g:
            print("【备注】该用例无法验证，原因：SSID名不为初始SSID")
            assert False
        # 判断密码
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.WiFi_Password))
        )
        WiFi_Password_Text = self.driver.find_element_by_xpath(WifiSettingsLocators.WiFi_Password).get_attribute("value")
        if WiFi_Password_Text != wlan_password_change:
            print("【备注】该用例无法验证，原因：密码不为修改后的密码")
            assert False
        # 判断隐藏SSID开关
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Hide_SSID_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute('class')
        if Hide_SSID_class != "switch switch-animation":
            print("【备注】该用例无法验证，原因：“隐藏SSID”开关不为关")
            assert False
        # 判断双频合一开关
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute(
            'class')
        assert Smart_Connect_class == "switch switch-animation checked", Smart_Connect_class
        if Smart_Connect_class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关不为开")
            assert False

        # 前提检验完成，开始检验用例
        Result = Test_wifi.test_wifi_20()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False