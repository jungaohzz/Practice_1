#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/const.MEDIUM_WAIT/29 11:54
# @Author:  GaoJun

import unittest
from ..base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from rweb import const
from rweb.path.common import CommonLocators
from rweb.path.guestWifi import GuestWifiLocators
from rweb.path.devices import DevicesLocators
from rweb.path.limitTime import LimitTimeLocators
from selenium.webdriver.common.action_chains import ActionChains
from rweb.path.staticDhcpLease import StaticDHCPLeaseLocators
from rweb.path.dmzHost import DmzHostLocators
from rweb.path.dhcp import DhcpLocators
from rweb.path.wifiSettings import WifiSettingsLocators
from rweb.path.routerManagement import RouterManagementLocators
from .guest_wifi_testcase import Test_guest_wifi
from ..common_dir import common_conf, common_fun

"""WiFi设置"""


class GuestWifiSettings(Base):
    # 定义配置WiFi set相关前置条件的变量
    PRECONDITION = True

    # 定义guest wiFi设置页的url
    url_guestWifiSettingsPage = ""

    def switch_to_guestWifiSetsPage(self, Current_Url):  # 切换到 guest wifi设置页，同时检验WiFi set相关前置条件是否配置成功
        if not GuestWifiSettings.PRECONDITION:
            print("【失败】WiFi set相关前置条件配置失败")
            assert False

        self.driver.refresh()
        time.sleep(2)
        # 判断当前的url是否是目的url
        while GuestWifiSettings.url_guestWifiSettingsPage != Current_Url:
            # 鼠标模拟移动到：设置
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
            )
            mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
            ActionChains(self.driver).move_to_element(mouse).perform()
            # 点击 访客WiFi
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, CommonLocators.Guest_WiFi))
            ).click()
            time.sleep(0.5)
            Current_Url = self.driver.current_url

    # @unittest.skip("跳过")
    def test_A_get_url(self):
        """操作步骤：获取guest wiFi设置页的url"""
        # 鼠标模拟移动到：设置
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 访客WiFi
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Guest_WiFi))
        ).click()
        time.sleep(2)
        GuestWifiSettings.url_guestWifiSettingsPage = self.driver.current_url
        time.sleep(1)

    # @unittest.skip("跳过")
    def test_B_init(self):
        """操作步骤：先执行配置WiFi set相关前置条件"""
        GuestWifiSettings.PRECONDITION = True  # 设置为True的目的是使下面那条代码能正常运行，然后再恢复会False
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        while GuestWifiSettings.PRECONDITION == True:  # 此处一定要将PRECONDITION设置为 False
            GuestWifiSettings.PRECONDITION = False

        flag = False  # 用于标记是否配置成功，False为不成功，True为成功
        i = 1
        while i <= 2 and flag == False:  # 如果第1次失败，则尝试第2次配置
            result = Test_guest_wifi.test_guest_wifi_init()
            if result == 1:
                print("【成功】WiFi set相关前置条件配置成功")
                flag = True
                GuestWifiSettings.PRECONDITION = True
                assert True
            else:
                flag = False

            if i == 2 and flag == False:  # 如果配置2此都没有成功，则报错
                print("【失败】WiFi set相关前置条件配置失败")
                GuestWifiSettings.PRECONDITION = False
                assert False
            i += 1

    # @unittest.skip("跳过")
    def test_C_guestWifi_on(self):
        """操作步骤：将访客WiFi开启（设置为默认值）"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        time.sleep(4)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        # 默认是关闭的
        # 如果是关闭的，才进行下面的if打开操作
        if Statu_class == "switch switch-animation":
            # 点击 启用 按钮
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Satatu))
            ).click()
            # 修改无线名称
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
            ).clear()
            self.driver.find_element_by_xpath(GuestWifiLocators.Name).send_keys(common_conf.guest_ssid_2g)
            # 修改加密方式
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Encryption))
            ).click()
            time.sleep(1)
            WPA_WPA2_PSK = GuestWifiLocators.Encryption_Alls.format(num=2)
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, WPA_WPA2_PSK))
            ).click()
            time.sleep(1)
            # 修改密码
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Password))
            ).clear()
            self.driver.find_element_by_xpath(GuestWifiLocators.Password).send_keys(common_conf.guest_wlan_password)
            # 修改“双频合一”
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
            )
            Smart_Connect_class = self.driver.find_element_by_xpath(GuestWifiLocators.Smart_Connect).get_attribute(
                'class')
            if Smart_Connect_class != "switch switch-animation checked":
                WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                    EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
                ).click()
                time.sleep(2)  # 用于开关切换
            # 保存
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Save))
            ).click()
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Save_Ok))
            ).click()

        # 断言：保存成功后会访客WiFi的首页，则查看是否有“设置”按钮即可
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Settings))
        )

        # 断言：检查状态是否为开启：
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        assert Statu_class == "switch switch-animation checked", Statu_class
        time.sleep(1)

    # @unittest.skip("跳过")
    def test_D_test_guest_wifi_1(self):
        """用例-4371 : 开启访客网络后，访客网络生效，5G和2.4G都能连接到访客网络"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        # 前提条件1：访客WiFi开启
        time.sleep(2)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        if Statu_class == "switch switch-animation":
            print("【备注】该用例无法验证，原因：访客WiFi未开启")
            assert False
        # 前提条件2：值为默认状态
        # 判断SSID、“双频合一”开关、password是否是默认值
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(1)
        self.driver.find_element_by_xpath(GuestWifiLocators.Settings).click()
        # 判断SSID
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Name).get_attribute("value")
        if Wifi_Name_Text != common_conf.guest_ssid_2g:
            print("【备注】该用例无法验证，原因：SSID名不为默认值")
            assert False
        # 判断“双频合一”
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(GuestWifiLocators.Smart_Connect).get_attribute('class')
        if Smart_Connect_class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关不为启用")
            assert False

        # 判断密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Password))
        )
        WiFi_Password_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Password).get_attribute("value")
        if WiFi_Password_Text != common_conf.guest_wlan_password:
            print("【备注】该用例无法验证，原因：密码不为默认值")
            assert False

        # 前提检验完成，开始检验用例
        result = Test_guest_wifi.test_guest_wifi_1()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    # @unittest.skip("跳过")
    def test_E_test_guest_wifi_2(self):
        """用例-5003 : “双频合一”开启状态，扫描到的SSID中，5G和2.4G SSID一样"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        # 前提条件1：访客WiFi开启
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        if Statu_class == "switch switch-animation":
            print("【备注】该用例无法验证，原因：访客WiFi未开启")
            assert False
        # 前提条件2：值为默认状态
        # 判断SSID、“双频合一”开关、password是否是默认值
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(1)
        self.driver.find_element_by_xpath(GuestWifiLocators.Settings).click()
        # 判断SSID
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Name).get_attribute("value")
        if Wifi_Name_Text != common_conf.guest_ssid_2g:
            print("【备注】该用例无法验证，原因：SSID名不为默认值")
            assert False
        # 判断“双频合一”
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(GuestWifiLocators.Smart_Connect).get_attribute('class')
        if Smart_Connect_class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关不为启用")
            assert False
        # 判断密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Password))
        )
        WiFi_Password_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Password).get_attribute("value")
        if WiFi_Password_Text != common_conf.guest_wlan_password:
            print("【备注】该用例无法验证，原因：密码不为默认值")
            assert False

        # 前提检验完成，开始检验用例
        result = Test_guest_wifi.test_guest_wifi_2()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    # @unittest.skip("跳过")
    def test_F_test_guest_wifi_3(self):
        """用例-5004 : “双频合一”开启状态，2T2R设备能成功连接2.4G SSID，协商速率300M"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        # 前提条件1：访客WiFi开启
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        if Statu_class == "switch switch-animation":
            print("【备注】该用例无法验证，原因：访客WiFi未开启")
            assert False
        # 前提条件2：值为默认状态
        # 判断SSID、“双频合一”开关、password是否是默认值
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(1)
        self.driver.find_element_by_xpath(GuestWifiLocators.Settings).click()
        # 判断SSID
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Name).get_attribute("value")
        if Wifi_Name_Text != common_conf.guest_ssid_2g:
            print("【备注】该用例无法验证，原因：SSID名不为默认值")
            assert False
        # 判断“双频合一”
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(GuestWifiLocators.Smart_Connect).get_attribute(
            'class')
        if Smart_Connect_class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关不为启用")
            assert False
        # 判断密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Password))
        )
        WiFi_Password_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Password).get_attribute("value")
        if WiFi_Password_Text != common_conf.guest_wlan_password:
            print("【备注】该用例无法验证，原因：密码不为默认值")
            assert False

        # 前提检验完成，开始检验用例
        result = Test_guest_wifi.test_guest_wifi_3()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    # @unittest.skip("跳过")
    def test_G_test_guest_wifi_4(self):
        """用例-5005 : “双频合一”开启状态，2T2R设备能成功连接5G SSID,协商速率正确867M"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        # 前提条件1：访客WiFi开启
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        if Statu_class == "switch switch-animation":
            print("【备注】该用例无法验证，原因：访客WiFi未开启")
            assert False
        # 前提条件2：值为默认状态
        # 判断SSID、“双频合一”开关、password是否是默认值
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(1)
        self.driver.find_element_by_xpath(GuestWifiLocators.Settings).click()
        # 判断SSID
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Name).get_attribute("value")
        if Wifi_Name_Text != common_conf.guest_ssid_2g:
            print("【备注】该用例无法验证，原因：SSID名不为默认值")
            assert False
        # 判断“双频合一”
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(GuestWifiLocators.Smart_Connect).get_attribute('class')
        if Smart_Connect_class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关不为启用")
            assert False
        # 判断密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Password))
        )
        WiFi_Password_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Password).get_attribute("value")
        if WiFi_Password_Text != common_conf.guest_wlan_password:
            print("【备注】该用例无法验证，原因：密码不为默认值")
            assert False

        # 前提检验完成，开始检验用例
        result = Test_guest_wifi.test_guest_wifi_4()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    # @unittest.skip("跳过")
    def test_H_guestWifiSets_smartConnect_off(self):
        """操作步骤：“双频合一”开关关闭"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Settings))
        ).click()
        # 判断SSID
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Name).get_attribute("value")
        if Wifi_Name_Text != common_conf.guest_ssid_2g:
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
            ).clear()
            self.driver.find_element_by_xpath(GuestWifiLocators.Name).send_keys(common_conf.guest_ssid_2g)
        # 判断密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Password))
        )
        WiFi_Password_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Password).get_attribute("value")
        if WiFi_Password_Text != common_conf.guest_wlan_password:
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Password))
            ).clear()
            self.driver.find_element_by_xpath(GuestWifiLocators.Password).send_keys(common_conf.guest_wlan_password)
        # 判断“双频合一”
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(GuestWifiLocators.Smart_Connect).get_attribute('class')
        if Smart_Connect_class == "switch switch-animation checked":
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
            ).click()
            time.sleep(2)  # 用于开关切换
        # 保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Save))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Save_Ok))
        ).click()

        # 断言：保存成功后会访客WiFi的首页，则查看是否有“设置”按钮即可
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(1)

    # @unittest.skip("跳过")
    def test_I_test_guest_wifi_5(self):
        """用例-5006 : “双频合一”关闭状态，扫描到的SSID中，2.4G SSID为XXXX,5G SSID为XXXX-5G"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        # 前提条件1：访客WiFi开启
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        if Statu_class == "switch switch-animation":
            print("【备注】该用例无法验证，原因：访客WiFi未开启")
            assert False
        # 前提条件2：SSID和password的值为默认状态
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(1)
        self.driver.find_element_by_xpath(GuestWifiLocators.Settings).click()
        # 判断SSID
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Name).get_attribute("value")
        if Wifi_Name_Text != common_conf.guest_ssid_2g:
            print("【备注】该用例无法验证，原因：SSID名不为默认值")
            assert False
        # 判断密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Password))
        )
        WiFi_Password_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Password).get_attribute("value")
        if WiFi_Password_Text != common_conf.guest_wlan_password:
            print("【备注】该用例无法验证，原因：密码不为默认值")
            assert False
        # 前提条件3：“双频合一”为关闭
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(GuestWifiLocators.Smart_Connect).get_attribute('class')
        if Smart_Connect_class == "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关不为关闭")
            assert False

        # 前提检验完成，开始检验用例
        result = Test_guest_wifi.test_guest_wifi_5()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    # @unittest.skip("跳过")
    def test_J_test_guest_wifi_6(self):
        """用例-5007 : “双频合一”关闭状态，2T2R设备能成功连接2.4G，协商速率300M"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        # 前提条件1：访客WiFi开启
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        if Statu_class == "switch switch-animation":
            print("【备注】该用例无法验证，原因：访客WiFi未开启")
            assert False
        # 前提条件2：SSID和password的值为默认状态
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(1)
        self.driver.find_element_by_xpath(GuestWifiLocators.Settings).click()
        # 判断SSID
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Name).get_attribute("value")
        if Wifi_Name_Text != common_conf.guest_ssid_2g:
            print("【备注】该用例无法验证，原因：SSID名不为默认值")
            assert False
        # 判断密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Password))
        )
        WiFi_Password_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Password).get_attribute("value")
        if WiFi_Password_Text != common_conf.guest_wlan_password:
            print("【备注】该用例无法验证，原因：密码不为默认值")
            assert False
        # 前提条件3：“双频合一”为关闭
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(GuestWifiLocators.Smart_Connect).get_attribute('class')
        if Smart_Connect_class == "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关不为关闭")
            assert False

        # 前提检验完成，开始检验用例
        result = Test_guest_wifi.test_guest_wifi_6()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    # @unittest.skip("跳过")
    def test_K_test_guest_wifi_7(self):
        """用例-5008 : “双频合一”关闭状态，2T2R设备能成功连接5G，协商速率867M"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        # 前提条件1：访客WiFi开启
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        if Statu_class == "switch switch-animation":
            print("【备注】该用例无法验证，原因：访客WiFi未开启")
            assert False
        # 前提条件2：SSID和password的值为默认状态
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(1)
        self.driver.find_element_by_xpath(GuestWifiLocators.Settings).click()
        # 判断SSID
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Name).get_attribute("value")
        if Wifi_Name_Text != common_conf.guest_ssid_2g:
            print("【备注】该用例无法验证，原因：SSID名不为默认值")
            assert False
        # 判断密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Password))
        )
        WiFi_Password_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Password).get_attribute("value")
        if WiFi_Password_Text != common_conf.guest_wlan_password:
            print("【备注】该用例无法验证，原因：密码不为默认值")
            assert False
        # 前提条件3：“双频合一”为关闭
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(GuestWifiLocators.Smart_Connect).get_attribute('class')
        if Smart_Connect_class == "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关不为关闭")
            assert False

        # 前提检验完成，开始检验用例
        result = Test_guest_wifi.test_guest_wifi_7()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    # @unittest.skip("跳过")
    def test_L_guestWifiSets_ssid20bit_password24bit(self):
        """操作步骤：设置SSID为20个字节，密码为24个字节，且“双频合一”开关为开"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        ).click()
        # 修改无线名称
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        ).clear()
        self.driver.find_element_by_xpath(GuestWifiLocators.Name).send_keys(common_conf.guest_ssid_2g_20b)
        # 修改密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Password))
        ).clear()
        self.driver.find_element_by_xpath(GuestWifiLocators.Password).send_keys(common_conf.guest_wlan_password_24b)
        # 修改“双频合一”
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(GuestWifiLocators.Smart_Connect).get_attribute('class')
        if Smart_Connect_class != "switch switch-animation checked":
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
            ).click()
            time.sleep(2)  # 用于开关切换
        # 保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Save))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Save_Ok))
        ).click()

        # 断言：保存成功后会访客WiFi的首页，则查看是否有“设置”按钮即可
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(2)

    # @unittest.skip("跳过")
    def test_M_test_guest_wifi_8(self):
        """用例-5011 : SSID为20个字节，密码为24个字节，5G设备能成功连接"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        # 前提条件1：访客WiFi开启
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        if Statu_class == "switch switch-animation":
            print("【备注】该用例无法验证，原因：访客WiFi未开启")
            assert False
        # 前提条件2：SSID和password的值为默认状态
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(1)
        self.driver.find_element_by_xpath(GuestWifiLocators.Settings).click()
        # 判断SSID
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Name).get_attribute("value")
        if Wifi_Name_Text != common_conf.guest_ssid_2g_20b:
            print("【备注】该用例无法验证，原因：SSID名不为20字节")
            assert False
        # 判断密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Password))
        )
        WiFi_Password_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Password).get_attribute("value")
        if WiFi_Password_Text != common_conf.guest_wlan_password_24b:
            print("【备注】该用例无法验证，原因：密码不为24字节")
            assert False
        # 前提条件3：“双频合一”为关闭
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(GuestWifiLocators.Smart_Connect).get_attribute('class')
        if Smart_Connect_class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关不为启用")
            assert False

        # 前提检验完成，开始检验用例
        result = Test_guest_wifi.test_guest_wifi_8()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    # @unittest.skip("跳过")
    def test_N_test_guest_wifi_9(self):
        """用例-5012 : SSID为20个字节，密码为24个字节，2.4G设备能成功连接"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        # 前提条件1：访客WiFi开启
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        if Statu_class == "switch switch-animation":
            print("【备注】该用例无法验证，原因：访客WiFi未开启")
            assert False
        # 前提条件2：SSID和password的值为默认状态
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(1)
        self.driver.find_element_by_xpath(GuestWifiLocators.Settings).click()
        # 判断SSID
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Name).get_attribute("value")
        if Wifi_Name_Text != common_conf.guest_ssid_2g_20b:
            print("【备注】该用例无法验证，原因：SSID名不为20字节")
            assert False
        # 判断密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Password))
        )
        WiFi_Password_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Password).get_attribute("value")
        if WiFi_Password_Text != common_conf.guest_wlan_password_24b:
            print("【备注】该用例无法验证，原因：密码不为24字节")
            assert False
        # 前提条件3：“双频合一”为关闭
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(GuestWifiLocators.Smart_Connect).get_attribute(
            'class')
        if Smart_Connect_class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关不为启用")
            assert False

        # 前提检验完成，开始检验用例
        result = Test_guest_wifi.test_guest_wifi_9()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    # @unittest.skip("跳过")
    def test_O_guestWifiSets_ssid1bit_password8bit(self):
        """操作步骤：设置SSID为1个字节，密码为8个字节，且“双频合一”开关为开"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        ).click()
        # 修改无线名称
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        ).clear()
        self.driver.find_element_by_xpath(GuestWifiLocators.Name).send_keys(common_conf.guest_ssid_2g_1b)
        # 修改密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Password))
        ).clear()
        self.driver.find_element_by_xpath(GuestWifiLocators.Password).send_keys(common_conf.guest_wlan_password_8b)
        # 修改“双频合一”
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(GuestWifiLocators.Smart_Connect).get_attribute('class')
        if Smart_Connect_class != "switch switch-animation checked":
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
            ).click()
            time.sleep(2)  # 用于开关切换
        # 保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Save))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Save_Ok))
        ).click()

        # 断言：保存成功后会访客WiFi的首页，则查看是否有“设置”按钮即可
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(2)

    # @unittest.skip("跳过")
    def test_P_test_guest_wifi_10(self):
        """用例-5013 : SSID为1个字节，密码为8个字节，5G设备能成功连接"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        # 前提条件1：访客WiFi开启
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        if Statu_class == "switch switch-animation":
            print("【备注】该用例无法验证，原因：访客WiFi未开启")
            assert False
        # 前提条件2：SSID和password的值为默认状态
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(1)
        self.driver.find_element_by_xpath(GuestWifiLocators.Settings).click()
        # 判断SSID
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Name).get_attribute("value")
        if Wifi_Name_Text != common_conf.guest_ssid_2g_1b:
            print("【备注】该用例无法验证，原因：SSID名不为1字节")
            assert False
        # 判断密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Password))
        )
        WiFi_Password_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Password).get_attribute("value")
        if WiFi_Password_Text != common_conf.guest_wlan_password_8b:
            print("【备注】该用例无法验证，原因：密码不为8字节")
            assert False
        # 前提条件3：“双频合一”为关闭
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(GuestWifiLocators.Smart_Connect).get_attribute('class')
        if Smart_Connect_class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关不为启用")
            assert False

        # 前提检验完成，开始检验用例
        result = Test_guest_wifi.test_guest_wifi_10()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    # @unittest.skip("跳过")
    def test_Q_test_guest_wifi_11(self):
        """用例-5014 : SSID为1个字节，密码为8个字节，2.4G设备能成功连接"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        # 前提条件1：访客WiFi开启
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        if Statu_class == "switch switch-animation":
            print("【备注】该用例无法验证，原因：访客WiFi未开启")
            assert False
        # 前提条件2：SSID和password的值为默认状态
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(1)
        self.driver.find_element_by_xpath(GuestWifiLocators.Settings).click()
        # 判断SSID
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Name).get_attribute("value")
        if Wifi_Name_Text != common_conf.guest_ssid_2g_1b:
            print("【备注】该用例无法验证，原因：SSID名不为1字节")
            assert False
        # 判断密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Password))
        )
        WiFi_Password_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Password).get_attribute("value")
        if WiFi_Password_Text != common_conf.guest_wlan_password_8b:
            print("【备注】该用例无法验证，原因：密码不为8字节")
            assert False
        # 前提条件3：“双频合一”为关闭
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(GuestWifiLocators.Smart_Connect).get_attribute(
            'class')
        if Smart_Connect_class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关不为启用")
            assert False

        # 前提检验完成，开始检验用例
        result = Test_guest_wifi.test_guest_wifi_11()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    # @unittest.skip("跳过")
    def test_R_guestWifi_default(self):
        """操作步骤：将访客WiFi设置为默认值"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        ).click()
        # 修改无线名称
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        ).clear()
        self.driver.find_element_by_xpath(GuestWifiLocators.Name).send_keys(common_conf.guest_ssid_2g)
        # 修改加密方式
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Encryption))
        ).click()
        time.sleep(1)
        WPA_WPA2_PSK = GuestWifiLocators.Encryption_Alls.format(num=2)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WPA_WPA2_PSK))
        ).click()
        time.sleep(1)
        # 修改密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Password))
        ).clear()
        self.driver.find_element_by_xpath(GuestWifiLocators.Password).send_keys(common_conf.guest_wlan_password)
        # 修改“双频合一”
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(GuestWifiLocators.Smart_Connect).get_attribute('class')
        if Smart_Connect_class != "switch switch-animation checked":
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
            ).click()
            time.sleep(2)  # 用于开关切换
        # 保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Save))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Save_Ok))
        ).click()

        # 断言：保存成功后会访客WiFi的首页，则查看是否有“设置”按钮即可
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(2)

    # @unittest.skip("跳过")
    def test_S_guestWifi_onlyChange_ssid(self):
        """操作步骤：只修改SSID"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        ).click()
        # 修改无线名称
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        ).clear()
        self.driver.find_element_by_xpath(GuestWifiLocators.Name).send_keys(common_conf.guest_ssid_2g_change)
        # 保证“双频合一”为开启
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(GuestWifiLocators.Smart_Connect).get_attribute('class')
        if Smart_Connect_class != "switch switch-animation checked":
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
            ).click()
            time.sleep(2)  # 用于开关切换
        # 保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Save))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Save_Ok))
        ).click()

        # 断言：保存成功后会访客WiFi的首页，则查看是否有“设置”按钮即可
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(2)

    # @unittest.skip("跳过")
    def test_T_test_guest_wifi_12(self):
        """用例-4337 : 修改SSID后，新SSID生效，旧SSID失效"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        # 前提条件1：访客WiFi开启
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        if Statu_class == "switch switch-animation":
            print("【备注】该用例无法验证，原因：访客WiFi未开启")
            assert False
        # 前提条件2：SSID为修改后的值，password的值为默认值
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(1)
        self.driver.find_element_by_xpath(GuestWifiLocators.Settings).click()
        # 判断SSID
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Name).get_attribute("value")
        if Wifi_Name_Text != common_conf.guest_ssid_2g_change:
            print("【备注】该用例无法验证，原因：SSID名不为修改后的值")
            assert False
        # 判断密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Password))
        )
        WiFi_Password_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Password).get_attribute("value")
        if WiFi_Password_Text != common_conf.guest_wlan_password:
            print("【备注】该用例无法验证，原因：密码不为默认值")
            assert False
        # 前提条件3：“双频合一”为关闭
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(GuestWifiLocators.Smart_Connect).get_attribute(
            'class')
        if Smart_Connect_class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关不为启用")
            assert False

        # 前提检验完成，开始检验用例
        result = Test_guest_wifi.test_guest_wifi_12()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    # @unittest.skip("跳过")
    def test_U_guestWifi_default(self):
        """操作步骤：将访客WiFi设置为默认值"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        ).click()
        # 修改无线名称
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        ).clear()
        self.driver.find_element_by_xpath(GuestWifiLocators.Name).send_keys(common_conf.guest_ssid_2g)
        # 修改加密方式
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Encryption))
        ).click()
        time.sleep(1)
        WPA_WPA2_PSK = GuestWifiLocators.Encryption_Alls.format(num=2)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WPA_WPA2_PSK))
        ).click()
        time.sleep(1)
        # 修改密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Password))
        ).clear()
        self.driver.find_element_by_xpath(GuestWifiLocators.Password).send_keys(common_conf.guest_wlan_password)
        # 修改“双频合一”
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(GuestWifiLocators.Smart_Connect).get_attribute('class')
        if Smart_Connect_class != "switch switch-animation checked":
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
            ).click()
            time.sleep(2)  # 用于开关切换
        # 保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Save))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Save_Ok))
        ).click()

        # 断言：保存成功后会访客WiFi的首页，则查看是否有“设置”按钮即可
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(2)

    # @unittest.skip("跳过")
    def test_V_guestWifi_onlyChange_password(self):
        """操作步骤：只修改密码"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        ).click()
        # 修改密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Password))
        ).clear()
        self.driver.find_element_by_xpath(GuestWifiLocators.Password).send_keys(common_conf.guest_wlan_password_change)
        # 保证“双频合一”为开启
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(GuestWifiLocators.Smart_Connect).get_attribute('class')
        if Smart_Connect_class != "switch switch-animation checked":
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
            ).click()
            time.sleep(2)  # 用于开关切换
        # 保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Save))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Save_Ok))
        ).click()

        # 断言：保存成功后会访客WiFi的首页，则查看是否有“设置”按钮即可
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(2)

    # @unittest.skip("跳过")
    def test_W_test_guest_wifi_13(self):
        """用例-4317 : 修改密码后，新密码生效，旧密码失效"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        # 前提条件1：访客WiFi开启
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        if Statu_class == "switch switch-animation":
            print("【备注】该用例无法验证，原因：访客WiFi未开启")
            assert False
        # 前提条件2：SSID为默认值，password的值为修改后的值
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(1)
        self.driver.find_element_by_xpath(GuestWifiLocators.Settings).click()
        # 判断SSID
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Name).get_attribute("value")
        if Wifi_Name_Text != common_conf.guest_ssid_2g:
            print("【备注】该用例无法验证，原因：SSID名不为默认值")
            assert False
        # 判断密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Password))
        )
        WiFi_Password_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Password).get_attribute("value")
        if WiFi_Password_Text != common_conf.guest_wlan_password_change:
            print("【备注】该用例无法验证，原因：密码不为修改后的值")
            assert False
        # 前提条件3：“双频合一”为关闭
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(GuestWifiLocators.Smart_Connect).get_attribute(
            'class')
        if Smart_Connect_class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关不为启用")
            assert False

        # 前提检验完成，开始检验用例
        result = Test_guest_wifi.test_guest_wifi_13()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    # @unittest.skip("跳过")
    def test_X_guestWifi_setEncryption_Open(self):
        """操作步骤：访客WiFi设置为默认值，并设置加密方式为 Open"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        ).click()
        # 修改无线名称
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        ).clear()
        self.driver.find_element_by_xpath(GuestWifiLocators.Name).send_keys(common_conf.guest_ssid_2g)
        # 修改加密方式
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Encryption))
        ).click()
        time.sleep(1)
        Open = GuestWifiLocators.Encryption_Alls.format(num=1)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Open))
        ).click()
        time.sleep(1)
        # 修改“双频合一”
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect_whaleOpen))
        )
        Smart_Connect_whaleOpen_class = self.driver.find_element_by_xpath(
            GuestWifiLocators.Smart_Connect_whaleOpen).get_attribute('class')
        if Smart_Connect_whaleOpen_class != "switch switch-animation checked":
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect_whaleOpen))
            ).click()
            time.sleep(2)  # 用于开关切换
        # 保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Save))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Save_Ok))
        ).click()

        # 断言：保存成功后会访客WiFi的首页，则查看是否有“设置”按钮即可
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(2)

    # @unittest.skip("跳过")
    def test_Y_test_guest_wifi_14(self):
        """用例-5020 : 加密方式为open，5G和2.4G设备可以不需要密码连接到WIFI"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        # 前提条件1：访客WiFi开启
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        if Statu_class == "switch switch-animation":
            print("【备注】该用例无法验证，原因：访客WiFi未开启")
            assert False
        # 前提条件2：SSID为默认值，加密方式为 Open
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(1)
        self.driver.find_element_by_xpath(GuestWifiLocators.Settings).click()
        # 判断SSID
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Name).get_attribute("value")
        if Wifi_Name_Text != common_conf.guest_ssid_2g:
            print("【备注】该用例无法验证，原因：SSID名不为默认值")
            assert False
        # 判断加密方式
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Encryption))
        )
        encryption_value = self.driver.find_element_by_xpath(GuestWifiLocators.Encryption).get_attribute('value')
        if encryption_value != "Open":
            print("【备注】该用例无法验证，原因：加密方式不为 Open")
            assert False
        # 前提条件3：“双频合一”为关闭
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect_whaleOpen))
        )
        Smart_Connect_whaleOpen_class = self.driver.find_element_by_xpath(
            GuestWifiLocators.Smart_Connect_whaleOpen).get_attribute('class')
        if Smart_Connect_whaleOpen_class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关不为启用")
            assert False

        # 前提检验完成，开始检验用例
        result = Test_guest_wifi.test_guest_wifi_14()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    # @unittest.skip("跳过")
    def test_Z_guestWifi_setEncryption_WPA(self):
        """操作步骤：访客WiFi设置为默认值，并设置加密方式为 WPA-PSK"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        ).click()
        # 修改无线名称
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        ).clear()
        self.driver.find_element_by_xpath(GuestWifiLocators.Name).send_keys(common_conf.guest_ssid_2g)
        # 修改加密方式
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Encryption))
        ).click()
        time.sleep(1)
        WPA = GuestWifiLocators.Encryption_Alls.format(num=4)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WPA))
        ).click()
        time.sleep(1)
        # 修改密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Password))
        ).clear()
        self.driver.find_element_by_xpath(GuestWifiLocators.Password).send_keys(common_conf.guest_wlan_password)
        # 修改“双频合一”
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect_whaleOpen))
        )
        Smart_Connect_whaleOpen_class = self.driver.find_element_by_xpath(
            GuestWifiLocators.Smart_Connect_whaleOpen).get_attribute('class')
        if Smart_Connect_whaleOpen_class != "switch switch-animation checked":
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect_whaleOpen))
            ).click()
            time.sleep(2)  # 用于开关切换
        # 保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Save))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Save_Ok))
        ).click()

        # 断言：保存成功后会访客WiFi的首页，则查看是否有“设置”按钮即可
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(2)

    # 未通过测试！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
    # 未通过测试！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
    # 未通过测试！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
    # @unittest.skip("跳过")
    def test_a_test_guest_wifi_15(self):
        """用例-5021 : 加密方式为WPA，5G和2.4G设备可以通过WPA认证方式连接到WIFI"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        # 前提条件1：访客WiFi开启
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        if Statu_class == "switch switch-animation":
            print("【备注】该用例无法验证，原因：访客WiFi未开启")
            assert False
        # 前提条件2：SSID和password都为默认值，加密方式为 WPA
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(1)
        self.driver.find_element_by_xpath(GuestWifiLocators.Settings).click()
        # 判断SSID
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Name).get_attribute("value")
        if Wifi_Name_Text != common_conf.guest_ssid_2g:
            print("【备注】该用例无法验证，原因：SSID名不为默认值")
            assert False
        # 判断加密方式
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Encryption))
        )
        encryption_value = self.driver.find_element_by_xpath(GuestWifiLocators.Encryption).get_attribute('value')
        if encryption_value != "WPA-PSK":
            print("【备注】该用例无法验证，原因：加密方式不为 WPA-PSK")
            assert False
        # 判断密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Password))
        )
        WiFi_Password_Value = self.driver.find_element_by_xpath(GuestWifiLocators.Password).get_attribute("value")
        if WiFi_Password_Value != common_conf.guest_wlan_password:
            print("【备注】该用例无法验证，原因：密码不为初始密码")
            assert False

        # 前提条件3：“双频合一”为关闭
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(GuestWifiLocators.Smart_Connect).get_attribute('class')
        if Smart_Connect_class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关不为启用")
            assert False

        # 前提检验完成，开始检验用例
        result = Test_guest_wifi.test_guest_wifi_15()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    # @unittest.skip("跳过")
    def test_b_test_guest_wifi_16(self):
        """用例-5035 : 加密方式为WPA，5G和2.4G设备不可以通过WPA2认证方式连接到WIFI"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        # 前提条件1：访客WiFi开启
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        if Statu_class == "switch switch-animation":
            print("【备注】该用例无法验证，原因：访客WiFi未开启")
            assert False
        # 前提条件2：SSID和password都为默认值，加密方式为 WPA
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(1)
        self.driver.find_element_by_xpath(GuestWifiLocators.Settings).click()
        # 判断SSID
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Name).get_attribute("value")
        if Wifi_Name_Text != common_conf.guest_ssid_2g:
            print("【备注】该用例无法验证，原因：SSID名不为默认值")
            assert False
        # 判断加密方式
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Encryption))
        )
        encryption_value = self.driver.find_element_by_xpath(GuestWifiLocators.Encryption).get_attribute('value')
        if encryption_value != "WPA-PSK":
            print("【备注】该用例无法验证，原因：加密方式不为 WPA-PSK")
            assert False
        # 判断密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Password))
        )
        WiFi_Password_Value = self.driver.find_element_by_xpath(GuestWifiLocators.Password).get_attribute("value")
        if WiFi_Password_Value != common_conf.guest_wlan_password:
            print("【备注】该用例无法验证，原因：密码不为初始密码")
            assert False

        # 前提条件3：“双频合一”为关闭
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(GuestWifiLocators.Smart_Connect).get_attribute('class')
        if Smart_Connect_class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关不为启用")
            assert False

        # 前提检验完成，开始检验用例
        result = Test_guest_wifi.test_guest_wifi_16()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    # @unittest.skip("跳过")
    def test_c_guestWifi_setEncryption_WPA2(self):
        """操作步骤：访客WiFi设置为默认值，并设置加密方式为 WPA2-PSK"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        ).click()
        # 修改无线名称
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        ).clear()
        self.driver.find_element_by_xpath(GuestWifiLocators.Name).send_keys(common_conf.guest_ssid_2g)
        # 修改加密方式
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Encryption))
        ).click()
        time.sleep(1)
        WPA2 = GuestWifiLocators.Encryption_Alls.format(num=3)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WPA2))
        ).click()
        time.sleep(1)
        # 修改密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Password))
        ).clear()
        self.driver.find_element_by_xpath(GuestWifiLocators.Password).send_keys(common_conf.guest_wlan_password)
        # 修改“双频合一”
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect_whaleOpen))
        )
        Smart_Connect_whaleOpen_class = self.driver.find_element_by_xpath(
            GuestWifiLocators.Smart_Connect_whaleOpen).get_attribute('class')
        if Smart_Connect_whaleOpen_class != "switch switch-animation checked":
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect_whaleOpen))
            ).click()
            time.sleep(2)  # 用于开关切换
        # 保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Save))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Save_Ok))
        ).click()

        # 断言：保存成功后会访客WiFi的首页，则查看是否有“设置”按钮即可
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(2)

    # @unittest.skip("跳过")
    def test_d_test_guest_wifi_17(self):
        """用例-5022 : 加密方式为WPA2，5G和2.4G设备可以通过WPA2认证方式连接到WIFI"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        # 前提条件1：访客WiFi开启
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        if Statu_class == "switch switch-animation":
            print("【备注】该用例无法验证，原因：访客WiFi未开启")
            assert False
        # 前提条件2：SSID和password都为默认值，加密方式为 WPA2
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(1)
        self.driver.find_element_by_xpath(GuestWifiLocators.Settings).click()
        # 判断SSID
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Name).get_attribute("value")
        if Wifi_Name_Text != common_conf.guest_ssid_2g:
            print("【备注】该用例无法验证，原因：SSID名不为默认值")
            assert False
        # 判断加密方式
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Encryption))
        )
        encryption_value = self.driver.find_element_by_xpath(GuestWifiLocators.Encryption).get_attribute('value')
        if encryption_value != "WPA2-PSK":
            print("【备注】该用例无法验证，原因：加密方式不为 WPA2-PSK")
            assert False
        # 判断密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Password))
        )
        WiFi_Password_Value = self.driver.find_element_by_xpath(GuestWifiLocators.Password).get_attribute("value")
        if WiFi_Password_Value != common_conf.guest_wlan_password:
            print("【备注】该用例无法验证，原因：密码不为初始密码")
            assert False

        # 前提条件3：“双频合一”为关闭
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(GuestWifiLocators.Smart_Connect).get_attribute('class')
        if Smart_Connect_class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关不为启用")
            assert False

        # 前提检验完成，开始检验用例
        result = Test_guest_wifi.test_guest_wifi_17()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    # @unittest.skip("跳过")
    def test_e_test_guest_wifi_18(self):
        """用例-4827 : 加密方式为WPA2，5G和2.4G设备不可以通过WPA认证方式连接到WIFI"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        # 前提条件1：访客WiFi开启
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        if Statu_class == "switch switch-animation":
            print("【备注】该用例无法验证，原因：访客WiFi未开启")
            assert False
        # 前提条件2：SSID和password都为默认值，加密方式为 WPA2
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(1)
        self.driver.find_element_by_xpath(GuestWifiLocators.Settings).click()
        # 判断SSID
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Name).get_attribute("value")
        if Wifi_Name_Text != common_conf.guest_ssid_2g:
            print("【备注】该用例无法验证，原因：SSID名不为默认值")
            assert False
        # 判断加密方式
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Encryption))
        )
        encryption_value = self.driver.find_element_by_xpath(GuestWifiLocators.Encryption).get_attribute('value')
        if encryption_value != "WPA2-PSK":
            print("【备注】该用例无法验证，原因：加密方式不为 WPA2-PSK")
            assert False
        # 判断密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Password))
        )
        WiFi_Password_Value = self.driver.find_element_by_xpath(GuestWifiLocators.Password).get_attribute("value")
        if WiFi_Password_Value != common_conf.guest_wlan_password:
            print("【备注】该用例无法验证，原因：密码不为初始密码")
            assert False

        # 前提条件3：“双频合一”为关闭
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(GuestWifiLocators.Smart_Connect).get_attribute('class')
        if Smart_Connect_class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关不为启用")
            assert False

        # 前提检验完成，开始检验用例
        result = Test_guest_wifi.test_guest_wifi_18()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    # @unittest.skip("跳过")
    def test_f_guestWifi_setEncryption_WPA_WPA2(self):
        """操作步骤：访客WiFi设置为默认值，并设置加密方式为 WPA/WPA2-PSK"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        ).click()
        # 修改无线名称
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        ).clear()
        self.driver.find_element_by_xpath(GuestWifiLocators.Name).send_keys(common_conf.guest_ssid_2g)
        # 修改加密方式
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Encryption))
        ).click()
        time.sleep(1)
        WPA_WPA2 = GuestWifiLocators.Encryption_Alls.format(num=2)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WPA_WPA2))
        ).click()
        time.sleep(1)
        # 修改密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Password))
        ).clear()
        self.driver.find_element_by_xpath(GuestWifiLocators.Password).send_keys(common_conf.guest_wlan_password)
        # 修改“双频合一”
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect_whaleOpen))
        )
        Smart_Connect_whaleOpen_class = self.driver.find_element_by_xpath(
            GuestWifiLocators.Smart_Connect_whaleOpen).get_attribute('class')
        if Smart_Connect_whaleOpen_class != "switch switch-animation checked":
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect_whaleOpen))
            ).click()
            time.sleep(2)  # 用于开关切换
        # 保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Save))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Save_Ok))
        ).click()

        # 断言：保存成功后会访客WiFi的首页，则查看是否有“设置”按钮即可
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(2)

    # @unittest.skip("跳过")
    def test_g_test_guest_wifi_19(self):
        """用例-4352 : 加密方式为WPA/WPA2-PSK，5G和2.4G设备可以通过WPA认证方式连接到该WIFI"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        # 前提条件1：访客WiFi开启
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        if Statu_class == "switch switch-animation":
            print("【备注】该用例无法验证，原因：访客WiFi未开启")
            assert False
        # 前提条件2：SSID和password都为默认值，加密方式为 WPA/WPA2-PSK
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(1)
        self.driver.find_element_by_xpath(GuestWifiLocators.Settings).click()
        # 判断SSID
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Name).get_attribute("value")
        if Wifi_Name_Text != common_conf.guest_ssid_2g:
            print("【备注】该用例无法验证，原因：SSID名不为默认值")
            assert False
        # 判断加密方式
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Encryption))
        )
        encryption_value = self.driver.find_element_by_xpath(GuestWifiLocators.Encryption).get_attribute('value')
        if encryption_value != "WPA/WPA2-PSK":
            print("【备注】该用例无法验证，原因：加密方式不为 WPA/WPA2-PSK")
            assert False
        # 判断密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Password))
        )
        WiFi_Password_Value = self.driver.find_element_by_xpath(GuestWifiLocators.Password).get_attribute("value")
        if WiFi_Password_Value != common_conf.guest_wlan_password:
            print("【备注】该用例无法验证，原因：密码不为初始密码")
            assert False

        # 前提条件3：“双频合一”为关闭
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(GuestWifiLocators.Smart_Connect).get_attribute('class')
        if Smart_Connect_class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关不为启用")
            assert False

        # 前提检验完成，开始检验用例
        result = Test_guest_wifi.test_guest_wifi_19()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    # @unittest.skip("跳过")
    def test_h_test_guest_wifi_20(self):
        """用例-4828 : 加密方式为WPA/WPA2-PSK，5G和2.4G设备可以通过WPA2认证方式连接到该WIFI"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        # 前提条件1：访客WiFi开启
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        if Statu_class == "switch switch-animation":
            print("【备注】该用例无法验证，原因：访客WiFi未开启")
            assert False
        # 前提条件2：SSID和password都为默认值，加密方式为 WPA/WPA2-PSK
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
        )
        time.sleep(1)
        self.driver.find_element_by_xpath(GuestWifiLocators.Settings).click()
        # 判断SSID
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Name).get_attribute("value")
        if Wifi_Name_Text != common_conf.guest_ssid_2g:
            print("【备注】该用例无法验证，原因：SSID名不为默认值")
            assert False
        # 判断加密方式
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Encryption))
        )
        encryption_value = self.driver.find_element_by_xpath(GuestWifiLocators.Encryption).get_attribute('value')
        if encryption_value != "WPA/WPA2-PSK":
            print("【备注】该用例无法验证，原因：加密方式不为 WPA/WPA2-PSK")
            assert False
        # 判断密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Password))
        )
        WiFi_Password_Value = self.driver.find_element_by_xpath(GuestWifiLocators.Password).get_attribute("value")
        if WiFi_Password_Value != common_conf.guest_wlan_password:
            print("【备注】该用例无法验证，原因：密码不为初始密码")
            assert False

        # 前提条件3：“双频合一”为关闭
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(GuestWifiLocators.Smart_Connect).get_attribute('class')
        if Smart_Connect_class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：“双频合一”开关不为启用")
            assert False

        # 前提检验完成，开始检验用例
        result = Test_guest_wifi.test_guest_wifi_20()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    # @unittest.skip("跳过")
    def test_i_guestWifi_off(self):
        """操作步骤：将访客WiFi关闭"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        time.sleep(2)  # 用于切换按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        # 理应是打开的
        # 如果是打开的，才进行下面的if关闭操作
        if Statu_class == "switch switch-animation checked":
            # 点击 关闭 按钮
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Satatu))
            ).click()
            # 保存
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Save_Ok))
            ).click()

            # 断言：保存成功后会访客WiFi的首页，则查看是否有“设置”按钮即可
            WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Satatu))
            )
            time.sleep(5)
            print(1111111)

        # 断言：检查状态是否为关闭：
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        assert Statu_class == "switch switch-animation", Statu_class

    # @unittest.skip("跳过")
    def test_j_test_guest_wifi_21(self):
        """用例-4372 : 关闭访客网络后，访客网络生效，5G和2.4G都不能连接到访客网络"""
        self.switch_to_guestWifiSetsPage(self.driver.current_url)
        # 前提条件：访客WiFi关闭
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        if Statu_class != "switch switch-animation":
            print("【备注】该用例无法验证，原因：访客WiFi未关闭")
            assert False

        # 前提检验完成，开始检验用例
        result = Test_guest_wifi.test_guest_wifi_21()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False
