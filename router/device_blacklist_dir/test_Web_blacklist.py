#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/21 15:42
# @Author:  GaoJun

import unittest
from .. base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from rweb import const
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
from rweb.path.devices import DevicesLocators
from rweb.path.blacklist import BlacklistLocators
from selenium.common.exceptions import NoSuchElementException
from rweb.path.wifiSettings import WifiSettingsLocators
from rweb.path.guestWifi import GuestWifiLocators
from ..common_dir import common_conf,common_fun
from .device_black_testcase import Test_wifi_device_black, Test_guestwifi_device_black


"""黑名单"""

class DeviceBlacklist(Base):
    # 定义配置设备黑名单相关前置条件的变量
    Precondition = True

    # 定义设备黑名单页的url
    url_deviceBlacklistPage = ""

    def switch_to_deviceBlacklistPage(self, Current_Url):  # 切换到 设备黑名单 页
        if DeviceBlacklist.Precondition == False:
            print("【失败】设备黑名单测试的相关前置条件配置失败")
            assert False

        self.driver.refresh()
        time.sleep(2)
        # 判断当前的url是否是目的url
        while DeviceBlacklist.url_deviceBlacklistPage != Current_Url:
            # 鼠标模拟移动到：设置
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
            )
            mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
            ActionChains(self.driver).move_to_element(mouse).perform()
            # 点击 黑名单
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, CommonLocators.Blacklist))
            ).click()
            time.sleep(1)
            Current_Url = self.driver.current_url






    # 拉黑设备操作
    def add_to_blacklist(self, Device_Mac):
        # 点击 新增 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, BlacklistLocators.Add))
        ).click()
        time.sleep(1)
        i = 1
        while i <= 2:
            Form_Devices_Mac = BlacklistLocators.Form_Devices_Mac.format(num=i)
            Form_Devices_Mac = self.driver.find_element_by_xpath(Form_Devices_Mac).text[4:]
            if Form_Devices_Mac == Device_Mac:
                Form_Devices_Check = BlacklistLocators.Form_Devices_Check.format(num=i)
                WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                    EC.element_to_be_clickable((By.XPATH, Form_Devices_Check))
                ).click()
                break
            i += 1
        time.sleep(1)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, BlacklistLocators.Add_to_Blacklist))
        ).click()
        # 断言:toast提示：保存成功
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
        time.sleep(1)







    # 删除列表中所有设备操作
    def delete_allDevices(self):
        try:
            # 查看是否有 空列表 存在，如果不存在则表示列表不为空
            time.sleep(2)
            Empty_List_Text = self.driver.find_element_by_xpath(BlacklistLocators.Empty_List).text
            assert Empty_List_Text == "Empty", Empty_List_Text
        except:
            # 点击 全选 按钮
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, BlacklistLocators.Check_All))
            ).click()
            time.sleep(1)
            # 点击 批量删除 按钮
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, BlacklistLocators.Delete_Alls))
            ).click()
            # 断言:toast提示：保存成功
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
            time.sleep(1)







    @unittest.skip("跳过")
    def test_A_wifiSettings_default(self):
        """操作步骤：将主WiFi配置为默认值"""

        # 【进入主WiFi配置页】
        # 鼠标模拟移动到：设置
        time.sleep(2)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 WiFi设置
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.WiFi_Settings))
        ).click()
        time.sleep(2)

        # 【设置默认参数】
        flag = False  # 标记是否需要保存重启，False为不需要，True为需要
        # 获取SSID
        WebDriverWait(self.driver, const.REBOOT_WAIT).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Wifi_Name))
        )
        Wifi_Name_Text = self.driver.find_element_by_xpath(WifiSettingsLocators.Wifi_Name).get_attribute("value")
        if Wifi_Name_Text != common_conf.ssid_2g:
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Wifi_Name))
            ).clear()
            self.driver.find_element_by_xpath(WifiSettingsLocators.Wifi_Name).send_keys(common_conf.ssid_2g)
            flag = True
        # 获取加密方式
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Encryption_Button))
        )
        Encryption_Value = self.driver.find_element_by_xpath(WifiSettingsLocators.Encryption_Button).get_attribute('value')
        if Encryption_Value != "WPA/WPA2-PSK":
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Encryption_Button))
            ).click()
            time.sleep(1)
            WPA2 = WifiSettingsLocators.Encryption_Options.format(num=2)
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, WPA2))
            ).click()
            time.sleep(1)
            flag = True
        # 获取密码
        time.sleep(1)
        WebDriverWait(self.driver, const.REBOOT_WAIT).until(
            EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.WiFi_Password))
        )
        WiFi_Password_Text = self.driver.find_element_by_xpath(WifiSettingsLocators.WiFi_Password).get_attribute("value")
        if WiFi_Password_Text != common_conf.wlan_password:
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.WiFi_Password))
            ).clear()
            self.driver.find_element_by_xpath(WifiSettingsLocators.WiFi_Password).send_keys(common_conf.wlan_password)
            flag = True
        # 获取“隐藏SSID”开关状态
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Hide_SSID))
        )
        Hide_SSID_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute('class')
        if Hide_SSID_class != "switch switch-animation":
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Hide_SSID))
            ).click()
            time.sleep(2)  # 用于开关切换
            flag = True
        # 获取双频合一开关状态
        time.sleep(1)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute('class')
        if Smart_Connect_class != "switch switch-animation checked":
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Smart_Connect))
            ).click()
            time.sleep(2)  # 用于开关切换
            flag = True

        # 判断是否需要保存
        time.sleep(1)
        if flag == True:
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Save))
            ).click()
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Save_Ok))
            ).click()
            time.sleep(5)
            # 因为修改密码后没有成功的toast提示，所以不能用成功的toast提示判断是否完成reboot
            # 又因为reboot完成后，页面处于：我的WiFi-管理路由器，故可借判断管理路由器页的“mesh拓扑图”元素是否加载出来，来判断是否完成reboot
            WebDriverWait(self.driver, const.REBOOT_WAIT).until(
                EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Mesh_Topology))
            )
            time.sleep(5)



            # 断言：检查是否所有项均设置为默认状态

            # 【进入主WiFi配置页】
            # 鼠标模拟移动到：设置
            time.sleep(2)
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
            )
            mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
            ActionChains(self.driver).move_to_element(mouse).perform()
            # 点击 WiFi设置
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, CommonLocators.WiFi_Settings))
            ).click()
            time.sleep(2)

            # 【设置默认参数】
            # 获取SSID
            WebDriverWait(self.driver, const.REBOOT_WAIT).until(
                EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Wifi_Name))
            )
            Wifi_Name_Text = self.driver.find_element_by_xpath(WifiSettingsLocators.Wifi_Name).get_attribute("value")
            # 获取加密方式
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.Encryption_Button))
            )
            Encryption_Value = self.driver.find_element_by_xpath(WifiSettingsLocators.Encryption_Button).get_attribute('value')
            # 获取密码
            time.sleep(1)
            WebDriverWait(self.driver, const.REBOOT_WAIT).until(
                EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.WiFi_Password))
            )
            WiFi_Password_Text = self.driver.find_element_by_xpath(WifiSettingsLocators.WiFi_Password).get_attribute("value")
            # 获取“隐藏SSID”开关状态
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Hide_SSID))
            )
            Hide_SSID_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Hide_SSID).get_attribute('class')
            # 获取双频合一开关状态
            time.sleep(1)
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, WifiSettingsLocators.Smart_Connect))
            )
            Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute('class')


            # 判断是否设置成功
            if Wifi_Name_Text != common_conf.ssid_2g and Encryption_Value != "WPA/WPA2-PSK" and WiFi_Password_Text != common_conf.wlan_password and \
                    Hide_SSID_class != "switch switch-animation" and Smart_Connect_class != "switch switch-animation checked":
                print("【失败】主WiFi设置为默认值操作失败")
                DeviceBlacklist.Precondition = False
                assert False
            else:
                print("【成功】主WiFi设置为默认值操作成功")
                DeviceBlacklist.Precondition = True
                assert True






    @unittest.skip("跳过")
    def test_B_guestWifiSettings_defaule(self):
        """操作步骤：将访客WiFi配置为默认值"""
        # 先判断主WiFi是否设置成功，如果不成功则不进行后面操作
        if DeviceBlacklist.Precondition == False:
            print("【失败】主WiFi设置为默认值操作失败")
            assert False

        # 【进入访客WiFi配置页】
        # 鼠标模拟移动到：设置
        time.sleep(2)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 WiFi设置
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Guest_WiFi))
        ).click()
        time.sleep(2)


        # 【设置默认参数】
        time.sleep(2)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        # 如果是关闭的，才进行下面的if打开操作
        if Statu_class == "switch switch-animation":
            # 点击 启用 按钮
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Satatu))
            ).click()
            time.sleep(2)
        else:
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Settings))
            ).click()
            time.sleep(1)
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
        WebDriverWait(self.driver, const.REBOOT_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Settings))
        )

        # 断言：检查状态是否为开启：
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
        assert Statu_class == "switch switch-animation checked", Statu_class
        time.sleep(1)


        # 断言：判断是否设置为了默认值

        # 前提条件1：访客WiFi开启
        time.sleep(2)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Satatu))
        )
        Statu_class = self.driver.find_element_by_xpath(GuestWifiLocators.Satatu).get_attribute('class')
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
        # 判断“双频合一”
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, GuestWifiLocators.Smart_Connect))
        )
        Smart_Connect_class = self.driver.find_element_by_xpath(GuestWifiLocators.Smart_Connect).get_attribute('class')
        # 判断密码
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, GuestWifiLocators.Password))
        )
        WiFi_Password_Text = self.driver.find_element_by_xpath(GuestWifiLocators.Password).get_attribute("value")


        if Statu_class == "switch switch-animation" and Wifi_Name_Text != common_conf.guest_ssid_2g and \
            Smart_Connect_class != "switch switch-animation checked" and WiFi_Password_Text != common_conf.guest_wlan_password:
            print("【失败】访客WiFi设置为默认值操作失败")
            DeviceBlacklist.Precondition = False
            assert False
        else:
            print("【成功】访客WiFi设置为默认值操作成功")
            DeviceBlacklist.Precondition = True
            assert True






    #@unittest.skip("跳过")
    def test_C_get_url(self):
        """操作步骤：获取设备黑名单页的url"""
        # 鼠标模拟移动到：设置
        time.sleep(2)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 黑名单
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Blacklist))
        ).click()
        time.sleep(2)
        DeviceBlacklist.url_deviceBlacklistPage = self.driver.current_url
        time.sleep(1)







    #@unittest.skip("跳过")
    def test_D_init(self):
        """操作步骤：主WiFi-先执行配置WiFi set相关前置条件"""
        if DeviceBlacklist.Precondition == False:
            print("【失败】主WiFi或访客WiFi设置为默认值操作失败")
            assert False

        DeviceBlacklist.Precondition = True     #设置为True的目的是使下面那条代码能正常运行，然后再恢复会False
        self.switch_to_deviceBlacklistPage(self.driver.current_url)
        DeviceBlacklist.Precondition = False    #此处一定要将Precondition设置为 False


        flag = False    #用于标记是否配置成功，False为不成功，True为成功
        i = 1
        while i <= 2 and flag == False:     # 如果第1次失败，则尝试第2次配置
            print("这是第%s次init"%i)
            Result = Test_wifi_device_black.test_wifi_device_black_init()
            if Result == 1:
                print("【成功】主WiFi-设备黑名单测试的相关前置条件配置成功")
                flag = True
                DeviceBlacklist.Precondition = True
                assert True
                break
            else:
                flag = False

            if i == 2 and flag == False:    # 如果配置2此都没有成功，则报错
                print("【失败】主WiFi-设备黑名单测试的相关前置条件配置失败")
                DeviceBlacklist.Precondition = False
                assert False
            i += 1








    #@unittest.skip("跳过")
    def test_E_deviceBlacklist_5G(self):
        """操作步骤：拉黑一个主WiFi下的5G设备"""
        self.switch_to_deviceBlacklistPage(self.driver.current_url)
        # 拉黑5G设备
        self.add_to_blacklist(common_conf.wlan5g_mac)
        self.driver.refresh()
        # 判断是否进入设备黑名单列表
        Device_Mac = BlacklistLocators.Device_Mac.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, Device_Mac))
        )
        Device_Mac_Value = self.driver.find_element_by_xpath(Device_Mac).text
        assert Device_Mac_Value == common_conf.wlan5g_mac, Device_Mac_Value







    #@unittest.skip("跳过")
    def test_F_test_deviceBlacklist_1(self):
        """【检验】用例-7724 : 拉黑一个主WiFi下的5G设备，该设备会被立即踢下线，其他2G设备不会被提下线"""
        self.switch_to_deviceBlacklistPage(self.driver.current_url)
        # 前提条件：5G设备已被拉黑，即存在于设备黑名单列表中
        Device_Mac = BlacklistLocators.Device_Mac.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, Device_Mac))
        )
        Device_Mac_Value = self.driver.find_element_by_xpath(Device_Mac).text
        if Device_Mac_Value != common_conf.wlan5g_mac:
            print("【备注】该用例无法验证，原因：5G设备没有被拉黑，即没有显示在列表中")
            assert False

        # 前提检验完成，开始检验用例
        time.sleep(20)
        Result = Test_wifi_device_black.test_device_black_1()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False








    # @unittest.skip("跳过")
    def test_G_test_deviceBlacklist_5(self):
        """【检验】用例-7732 : 黑名单中的设备无法连接主WIFI 5G ssid"""
        self.switch_to_deviceBlacklistPage(self.driver.current_url)
        # 前提条件：5G设备已被拉黑，即存在于设备黑名单列表中
        Device_Mac = BlacklistLocators.Device_Mac.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, Device_Mac))
        )
        Device_Mac_Value = self.driver.find_element_by_xpath(Device_Mac).text
        if Device_Mac_Value != common_conf.wlan5g_mac:
            print("【备注】该用例无法验证，原因：5G设备没有被拉黑，即没有显示在列表中")
            assert False

        # 前提检验完成，开始检验用例
        Result = Test_wifi_device_black.test_device_black_5()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False







    # @unittest.skip("跳过")
    def test_H_test_deviceBlacklist_7(self):
        """【检验】用例-7734 : 黑名单中的设备无法连接主guest WIFI 5G ssid"""
        self.switch_to_deviceBlacklistPage(self.driver.current_url)
        # 前提条件：5G设备已被拉黑，即存在于设备黑名单列表中
        Device_Mac = BlacklistLocators.Device_Mac.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, Device_Mac))
        )
        Device_Mac_Value = self.driver.find_element_by_xpath(Device_Mac).text
        if Device_Mac_Value != common_conf.wlan5g_mac:
            print("【备注】该用例无法验证，原因：5G设备没有被拉黑，即没有显示在列表中")
            assert False

        # 前提检验完成，开始检验用例
        Result = Test_wifi_device_black.test_device_black_7()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False






    #@unittest.skip("跳过")
    def test_I_deviceBlacklist_deleteAlls(self):
        """操作步骤：删除设备黑名单中所有设备"""
        self.switch_to_deviceBlacklistPage(self.driver.current_url)
        # 删除所有设备
        self.delete_allDevices()






    # @unittest.skip("跳过")
    def test_J_test_deviceBlacklist_10(self):
        """【检验】用例-7738 : 删除黑名单中设备后，该设备可以连接主WIFI 5G ssid"""
        self.switch_to_deviceBlacklistPage(self.driver.current_url)
        # 前提条件：设备黑名单列表为空
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, BlacklistLocators.Empty_List))
        )
        Empty_List_Text = self.driver.find_element_by_xpath(BlacklistLocators.Empty_List).text
        if Empty_List_Text != "Empty":
            print("【备注】该用例无法验证，原因：设备黑名单列表没有清空")
            assert False

        # 前提检验完成，开始检验用例
        time.sleep(20)
        Result = Test_wifi_device_black.test_device_black_10()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False







    # @unittest.skip("跳过")
    def test_K_test_deviceBlacklist_12(self):
        """【检验】用例-7740 : 删除黑名单中设备后，该设备可以连接访客WIFI 5G ssid"""
        self.switch_to_deviceBlacklistPage(self.driver.current_url)
        # 前提条件：设备黑名单列表为空
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, BlacklistLocators.Empty_List))
        )
        Empty_List_Text = self.driver.find_element_by_xpath(BlacklistLocators.Empty_List).text
        if Empty_List_Text != "Empty":
            print("【备注】该用例无法验证，原因：设备黑名单列表没有清空")
            assert False

        # 前提检验完成，开始检验用例
        time.sleep(20)
        Result = Test_wifi_device_black.test_device_black_12()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False








    # @unittest.skip("跳过")
    def test_L_deviceBlacklist_settings(self):
        """操作步骤：恢复默认状态，并拉黑2G设备"""
        self.switch_to_deviceBlacklistPage(self.driver.current_url)

        # 删除所有设备
        self.delete_allDevices()

        # 执行init
        self.test_D_init()

        # 拉黑一个主WiFi下的2G设备
        self.switch_to_deviceBlacklistPage(self.driver.current_url)
        # 拉黑2G设备
        self.add_to_blacklist(common_conf.wlan2g_mac)
        self.driver.refresh()
        # 判断是否进入设备黑名单列表
        Device_Mac = BlacklistLocators.Device_Mac.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, Device_Mac))
        )
        Device_Mac_Value = self.driver.find_element_by_xpath(Device_Mac).text
        assert Device_Mac_Value == common_conf.wlan2g_mac, Device_Mac_Value









    # @unittest.skip("跳过")
    def test_M_test_deviceBlacklist_3(self):
        """【检验】用例-7726 : 拉黑一个主WiFi下的2G设备，该设备会被立即踢下线，其他5G设备不会被提下线"""
        self.switch_to_deviceBlacklistPage(self.driver.current_url)
        # 前提条件：5G设备已被拉黑，即存在于设备黑名单列表中
        Device_Mac = BlacklistLocators.Device_Mac.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, Device_Mac))
        )
        Device_Mac_Value = self.driver.find_element_by_xpath(Device_Mac).text
        if Device_Mac_Value != common_conf.wlan2g_mac:
            print("【备注】该用例无法验证，原因：2G设备没有被拉黑，即没有显示在列表中")
            assert False

        # 前提检验完成，开始检验用例
        time.sleep(20)
        Result = Test_wifi_device_black.test_device_black_3()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False







    # @unittest.skip("跳过")
    def test_N_test_deviceBlacklist_6(self):
        """【检验】用例-7733 : 黑名单中的设备无法连接主WIFI 2G ssid"""
        self.switch_to_deviceBlacklistPage(self.driver.current_url)
        # 前提条件：5G设备已被拉黑，即存在于设备黑名单列表中
        Device_Mac = BlacklistLocators.Device_Mac.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, Device_Mac))
        )
        Device_Mac_Value = self.driver.find_element_by_xpath(Device_Mac).text
        if Device_Mac_Value != common_conf.wlan2g_mac:
            print("【备注】该用例无法验证，原因：2G设备没有被拉黑，即没有显示在列表中")
            assert False

        # 前提检验完成，开始检验用例
        Result = Test_wifi_device_black.test_device_black_6()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False






    # @unittest.skip("跳过")
    def test_O_test_deviceBlacklist_8(self):
        """【检验】用例-7735 : 黑名单中的设备无法连接主guest WIFI 2G ssid"""
        self.switch_to_deviceBlacklistPage(self.driver.current_url)
        # 前提条件：5G设备已被拉黑，即存在于设备黑名单列表中
        Device_Mac = BlacklistLocators.Device_Mac.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, Device_Mac))
        )
        Device_Mac_Value = self.driver.find_element_by_xpath(Device_Mac).text
        if Device_Mac_Value != common_conf.wlan2g_mac:
            print("【备注】该用例无法验证，原因：2G设备没有被拉黑，即没有显示在列表中")
            assert False

        # 前提检验完成，开始检验用例
        Result = Test_wifi_device_black.test_device_black_8()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False








    # @unittest.skip("跳过")
    def test_P_deviceBlacklist_default(self):
        """操作步骤：恢复默认状态：列表为空"""
        self.switch_to_deviceBlacklistPage(self.driver.current_url)

        # 删除所有设备
        self.delete_allDevices()







    # @unittest.skip("跳过")
    def test_Q_test_deviceBlacklist_11(self):
        """【检验】用例-7739 : 删除黑名单中设备后，该设备可以连接主WIFI 2G ssid"""
        self.switch_to_deviceBlacklistPage(self.driver.current_url)
        # 前提条件：设备黑名单列表为空
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, BlacklistLocators.Empty_List))
        )
        Empty_List_Text = self.driver.find_element_by_xpath(BlacklistLocators.Empty_List).text
        if Empty_List_Text != "Empty":
            print("【备注】该用例无法验证，原因：设备黑名单列表没有清空")
            assert False

        # 前提检验完成，开始检验用例
        time.sleep(20)
        Result = Test_wifi_device_black.test_device_black_11()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False








    # @unittest.skip("跳过")
    def test_R_test_deviceBlacklist_13(self):
        """【检验】用例-7741 : 删除黑名单中设备后，该设备可以连接访客WiFi 2G ssid"""
        self.switch_to_deviceBlacklistPage(self.driver.current_url)
        # 前提条件：设备黑名单列表为空
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, BlacklistLocators.Empty_List))
        )
        Empty_List_Text = self.driver.find_element_by_xpath(BlacklistLocators.Empty_List).text
        if Empty_List_Text != "Empty":
            print("【备注】该用例无法验证，原因：设备黑名单列表没有清空")
            assert False

        # 前提检验完成，开始检验用例
        time.sleep(20)
        Result = Test_wifi_device_black.test_device_black_13()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False






    # 为实现！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
    # 为实现！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
    # 为实现！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
    # 为实现！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
    # 为实现！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
    @unittest.skip("跳过")
    def test_S_deviceBlacklist_settings(self):
        """操作步骤：恢复默认状态，并拉黑有线设备"""
        self.switch_to_deviceBlacklistPage(self.driver.current_url)

        # 删除所有设备
        self.delete_allDevices()

        # 执行init
        self.test_D_init()

        # 拉黑一个主WiFi下的2G设备
        self.switch_to_deviceBlacklistPage(self.driver.current_url)
        # 拉黑 有线 设备
        self.add_to_blacklist(common_conf.wired2_mac)
        self.driver.refresh()
        # 判断是否进入设备黑名单列表
        Device_Mac = BlacklistLocators.Device_Mac.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, Device_Mac))
        )
        Device_Mac_Value = self.driver.find_element_by_xpath(Device_Mac).text
        assert Device_Mac_Value == common_conf.wired2_mac, Device_Mac_Value













    #@unittest.skip("跳过")
    def test_T_init(self):
        """操作步骤：访客WiFi-先执行配置WiFi set相关前置条件"""
        if DeviceBlacklist.Precondition == False:
            print("【失败】主WiFi或访客WiFi设置为默认值操作失败")
            assert False

        DeviceBlacklist.Precondition = True  # 设置为True的目的是使下面那条代码能正常运行，然后再恢复会False
        self.switch_to_deviceBlacklistPage(self.driver.current_url)
        DeviceBlacklist.Precondition = False  # 此处一定要将Precondition设置为 False

        flag = False  # 用于标记是否配置成功，False为不成功，True为成功
        i = 1
        while i <= 2 and flag == False:  # 如果第1次失败，则尝试第2次配置
            print("这是第%s次init" % i)
            Result = Test_guestwifi_device_black.test_guestwifi_device_black_init()
            if Result == 1:
                print("【成功】访客WiFi-设备黑名单测试的相关前置条件配置成功")
                flag = True
                DeviceBlacklist.Precondition = True
                assert True
                break
            else:
                flag = False

            if i == 2 and flag == False:  # 如果配置2此都没有成功，则报错
                print("【失败】访客WiFi-设备黑名单测试的相关前置条件配置失败")
                DeviceBlacklist.Precondition = False
                assert False
            i += 1







    #@unittest.skip("跳过")
    def test_U_deviceBlacklist_5G(self):
        """操作步骤：拉黑一个主WiFi下的5G设备"""
        self.switch_to_deviceBlacklistPage(self.driver.current_url)
        # 拉黑5G设备
        self.add_to_blacklist(common_conf.wlan5g_mac)
        self.driver.refresh()
        # 判断是否进入设备黑名单列表
        Device_Mac = BlacklistLocators.Device_Mac.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, Device_Mac))
        )
        Device_Mac_Value = self.driver.find_element_by_xpath(Device_Mac).text
        assert Device_Mac_Value == common_conf.wlan5g_mac, Device_Mac_Value







    #@unittest.skip("跳过")
    def test_V_test_deviceBlacklist_15(self):
        """【检验】用例-7728 : 拉黑一个访客WiFi下的5G设备，该设备会被立即踢下线，其他2G设备不会被提下线"""
        self.switch_to_deviceBlacklistPage(self.driver.current_url)
        # 前提条件：5G设备已被拉黑，即存在于设备黑名单列表中
        Device_Mac = BlacklistLocators.Device_Mac.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, Device_Mac))
        )
        Device_Mac_Value = self.driver.find_element_by_xpath(Device_Mac).text
        if Device_Mac_Value != common_conf.wlan5g_mac:
            print("【备注】该用例无法验证，原因：访客WiFi-5G设备没有被拉黑，即没有显示在列表中")
            assert False

        # 前提检验完成，开始检验用例
        time.sleep(20)
        Result = Test_guestwifi_device_black.test_device_black_15()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False







    #@unittest.skip("跳过")
    def test_W_deviceBlacklist_default(self):
        """操作步骤：删除设备黑名单中所有设备"""
        self.switch_to_deviceBlacklistPage(self.driver.current_url)

        # 删除所有设备
        self.delete_allDevices()







    #@unittest.skip("跳过")
    def test_X_deviceBlacklist_settings(self):
        """操作步骤：访客WiFi-恢复默认状态，并拉黑2G设备"""
        self.switch_to_deviceBlacklistPage(self.driver.current_url)

        # 删除所有设备
        self.delete_allDevices()

        # 执行init
        self.test_T_init()

        # 拉黑一个主WiFi下的2G设备
        self.switch_to_deviceBlacklistPage(self.driver.current_url)
        # 拉黑2G设备
        self.add_to_blacklist(common_conf.wlan2g_mac)
        self.driver.refresh()
        # 判断是否进入设备黑名单列表
        Device_Mac = BlacklistLocators.Device_Mac.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, Device_Mac))
        )
        Device_Mac_Value = self.driver.find_element_by_xpath(Device_Mac).text
        assert Device_Mac_Value == common_conf.wlan2g_mac, Device_Mac_Value









    # @unittest.skip("跳过")
    def test_Y_test_deviceBlacklist_17(self):
        """【检验】用例-7730 : 拉黑一个访客WiFi下的2G设备，该设备会被立即踢下线，其他5G设备不会被提下线"""
        self.switch_to_deviceBlacklistPage(self.driver.current_url)
        # 前提条件：2G设备已被拉黑，即存在于设备黑名单列表中
        Device_Mac = BlacklistLocators.Device_Mac.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, Device_Mac))
        )
        Device_Mac_Value = self.driver.find_element_by_xpath(Device_Mac).text
        if Device_Mac_Value != common_conf.wlan2g_mac:
            print("【备注】该用例无法验证，原因：访客WiFi-2G设备没有被拉黑，即没有显示在列表中")
            assert False

        # 前提检验完成，开始检验用例
        time.sleep(20)
        Result = Test_guestwifi_device_black.test_device_black_17()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False







    #@unittest.skip("跳过")
    def test_Z_deviceBlacklist_default(self):
        """操作步骤：删除设备黑名单中所有设备"""
        self.switch_to_deviceBlacklistPage(self.driver.current_url)

        # 删除所有设备
        self.delete_allDevices()