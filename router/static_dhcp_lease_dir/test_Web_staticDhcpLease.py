#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun

import unittest
from .. base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from rweb.path.common import CommonLocators
from rweb.path.devices import DevicesLocators
from rweb.path.limitTime import LimitTimeLocators
from rweb.path.routerManagement import RouterManagementLocators
from selenium.webdriver.common.action_chains import ActionChains
from rweb.path.staticDhcpLease import StaticDHCPLeaseLocators
from rweb.path.wifiSettings import WifiSettingsLocators
from rweb.path.guestWifi import GuestWifiLocators
from rweb import const
from ..common_dir import common_conf,common_fun
from .static_dhcp_lease_testcase import Test_static_dhcp_lease

"""Mac与IP绑定"""


class StaticDHCPLease(Base):

    # 定义 Mac与IP绑定 相关前置条件的变量
    Precondition = True
    # 定义有线网卡配置的Mac和IP是否生效的变量
    Wired1_Effect = True

    # 定义设备黑名单页的url
    url_staticDHCPLeasePage = ""

    def switch_to_staticDHCPLeasePage(self, Current_Url):  # 切换到 Mac与IP绑定 页
        if StaticDHCPLease.Precondition == False:
            print("【失败】Mac与IP绑定测试的相关前置条件配置失败")
            assert False

        self.driver.refresh()
        time.sleep(2)
        # 判断当前的url是否是目的url
        while StaticDHCPLease.url_staticDHCPLeasePage != Current_Url:
            # 鼠标模拟移动到：高级设置
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_AdvancedSettings))
            )
            mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_AdvancedSettings)
            ActionChains(self.driver).move_to_element(mouse).perform()
            # 点击 Mac与IP绑定
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, CommonLocators.Static_DHCP_Lease))
            ).click()
            time.sleep(1)
            Current_Url = self.driver.current_url








    def add(self, Type, Mac, IP):
        """操作步骤：新增记录"""
        if StaticDHCPLease.Precondition == False:
            print("【失败】主WiFi默认设置或Mac与IP绑定相关前置条件配置失败")
            assert False

        self.switch_to_staticDHCPLeasePage(self.driver.current_url)

        # 清空列表
        self.deleteAlls()

        # 点击 新增
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, StaticDHCPLeaseLocators.Add))
        ).click()
        # 设置名称
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, StaticDHCPLeaseLocators.Name))
        ).send_keys(Type)
        # 设置Mac地址
        Except_Mac = Mac.split('-')
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, StaticDHCPLeaseLocators.MacAddr))
        ).send_keys(Except_Mac)
        # 设置IP地址
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, StaticDHCPLeaseLocators.IpAddr))
        ).send_keys(IP)
        # 点击 保存
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, StaticDHCPLeaseLocators.Save))
        ).click()
        # 断言:toast提示：保存成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
        time.sleep(1)
        # 重启生效
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, StaticDHCPLeaseLocators.Restart))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Confirm))
        ).click()
        time.sleep(10)
        # 重启成功判断：遮罩消失即可
        WebDriverWait(self.driver, const.REBOOT_WAIT).until_not(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Shade))
        )
        time.sleep(1)




    # @unittest.skip("跳过")
    def deleteAlls(self):
        """操作步骤：删除列表所有记录"""
        flag = False
        while flag == False:
            try:
                assert self.driver.find_element_by_xpath(StaticDHCPLeaseLocators.List_Null).is_displayed()
                flag = True
            except:
                # 批量删除
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, StaticDHCPLeaseLocators.All_check))
                ).click()
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, StaticDHCPLeaseLocators.Deletes))
                ).click()
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, StaticDHCPLeaseLocators.Delete_ok))
                ).click()
                # 断言:toast提示：成功
                WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                    EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
                )




    @unittest.skip("跳过")
    def test_A_staticDHCPLease_default(self):
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
        Encryption_Value = self.driver.find_element_by_xpath(WifiSettingsLocators.Encryption_Button).get_attribute(
            'value')
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
        WiFi_Password_Text = self.driver.find_element_by_xpath(WifiSettingsLocators.WiFi_Password).get_attribute(
            "value")
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
        Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute(
            'class')
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
            Encryption_Value = self.driver.find_element_by_xpath(WifiSettingsLocators.Encryption_Button).get_attribute(
                'value')
            # 获取密码
            time.sleep(1)
            WebDriverWait(self.driver, const.REBOOT_WAIT).until(
                EC.presence_of_element_located((By.XPATH, WifiSettingsLocators.WiFi_Password))
            )
            WiFi_Password_Text = self.driver.find_element_by_xpath(WifiSettingsLocators.WiFi_Password).get_attribute(
                "value")
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
            Smart_Connect_class = self.driver.find_element_by_xpath(WifiSettingsLocators.Smart_Connect).get_attribute(
                'class')

            # 判断是否设置成功
            if Wifi_Name_Text != common_conf.ssid_2g and Encryption_Value != "WPA/WPA2-PSK" and WiFi_Password_Text != common_conf.wlan_password and \
                    Hide_SSID_class != "switch switch-animation" and Smart_Connect_class != "switch switch-animation checked":
                print("【失败】主WiFi设置为默认值操作失败")
                StaticDHCPLease.Precondition = False
                assert False
            else:
                print("【成功】主WiFi设置为默认值操作成功")
                StaticDHCPLease.Precondition = True
                assert True







    # @unittest.skip("跳过")
    def test_B_get_url(self):
        """操作步骤：获取设备黑名单页的url"""
        # 鼠标模拟移动到：高级设置
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_AdvancedSettings))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_AdvancedSettings)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 Mac与IP绑定
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Static_DHCP_Lease))
        ).click()
        time.sleep(2)
        StaticDHCPLease.url_staticDHCPLeasePage = self.driver.current_url
        time.sleep(1)







    #未通过测试！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
    # 未通过测试！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
    # 未通过测试！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
    # 未通过测试！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
    # 未通过测试！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
    @unittest.skip("跳过")
    def test_C_init(self):
        """操作步骤：先执行Mac与IP绑定相关前置条件"""
        if StaticDHCPLease.Precondition == False:
            print("【失败】主WiFi设置为默认值操作失败")
            assert False

        StaticDHCPLease.Precondition = True  # 设置为True的目的是使下面那条代码能正常运行，然后再恢复会False
        self.switch_to_staticDHCPLeasePage(self.driver.current_url)
        StaticDHCPLease.Precondition = False  # 此处一定要将Precondition设置为 False

        flag = False  # 用于标记是否配置成功，False为不成功，True为成功
        i = 1
        while i <= 2 and flag == False:  # 如果第1次失败，则尝试第2次配置
            print("这是第%s次init" % i)
            Result = Test_static_dhcp_lease.test_static_dhcp_lease_init()
            if Result == 1:
                print("【成功】Mac与IP绑定测试的相关前置条件配置成功")
                flag = True
                StaticDHCPLease.Precondition = True
                assert True
                break
            else:
                flag = False

            if i == 2 and flag == False:  # 如果配置2此都没有成功，则报错
                print("【失败】Mac与IP绑定测试的相关前置条件配置失败")
                StaticDHCPLease.Precondition = False
                assert False
            i += 1









    @unittest.skip("跳过")
    def test_D_staticDHCPLease_add_wired1(self):
        """操作步骤：配置有线网卡WIRED1的一条MAC/IP绑定规则"""
        if StaticDHCPLease.Precondition == False:
            print("【失败】主WiFi默认设置或Mac与IP绑定相关前置条件配置失败")
            assert False

        self.add("Wired1", common_conf.wired1_mac, common_conf.static_ip1)








    @unittest.skip("跳过")
    def test_E_staticDhcpLease_1(self):
        """
        【检验】用例-2830 : 配置一条MAC/IP绑定规则（IP未分配），该MAC对应主机发送一个DISCOVER报文，其中可选字段请求IP地址为空，该主机只能获取到绑定的IP地址
        【检验】用例-3985 : 配置一条MAC/IP绑定规则，主路由器下的有线设备会重新获取到绑定的IP地址
        """
        self.switch_to_staticDHCPLeasePage(self.driver.current_url)
        # 前提条件：在列表中有记录，有线网卡wired1对应IP为static_ip1
        # 获取Mac地址，是否为wired1
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, StaticDHCPLeaseLocators.List_MacAddr))
        )
        # 期望设置成的Mac地址
        Expect_Mac = common_conf.wired1_mac.lower().split('-')
        # 实际列表中设置的Mac地址
        Actual_Mac = self.driver.find_element_by_xpath(StaticDHCPLeaseLocators.List_MacAddr).text.split(':')

        # 获取IP地址,是否为static_ip1
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, StaticDHCPLeaseLocators.List_IpAddr))
        )
        Actual_IP = self.driver.find_element_by_xpath(StaticDHCPLeaseLocators.List_IpAddr).text
        # 断言：wired1跟static_ip1是否为期望的值
        if Expect_Mac != Actual_Mac or Actual_IP != common_conf.static_ip1:
            print("【备注】该用例无法验证，原因：有线网卡WIRED1前端配置的Mac和IP与期望不匹配")
            assert False

        # 前提检验完成，开始检验用例
        time.sleep(5)
        Result = Test_static_dhcp_lease.test_static_dhcp_lease_1()
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False









    @unittest.skip("跳过")
    def test_F_staticDHCPLease_add_wired1(self):
        """操作步骤：配置有线网卡WIRED1的一条MAC/IP绑定规则"""
        if StaticDHCPLease.Precondition == False:
            print("【失败】主WiFi默认设置或Mac与IP绑定相关前置条件配置失败")
            assert False

        self.add("Wired1", common_conf.wired1_mac, common_conf.static_ip1)








    @unittest.skip("跳过")
    def test_G_staticDhcpLease_2_1(self):
        """【检验】有线网卡WIRED1的静态IP和static_ip1成功生效"""
        self.switch_to_staticDHCPLeasePage(self.driver.current_url)
        # 前提条件：在列表中有记录，有线网卡wired1对应IP为static_ip1
        # 获取Mac地址，是否为wired1
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, StaticDHCPLeaseLocators.List_MacAddr))
        )
        # 期望设置成的Mac地址
        Expect_Mac = common_conf.wired1_mac.lower().split('-')
        # 实际列表中设置的Mac地址
        Actual_Mac = self.driver.find_element_by_xpath(StaticDHCPLeaseLocators.List_MacAddr).text.split(':')

        # 获取IP地址,是否为static_ip1
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, StaticDHCPLeaseLocators.List_IpAddr))
        )
        Actual_IP = self.driver.find_element_by_xpath(StaticDHCPLeaseLocators.List_IpAddr).text
        # 断言：wired1跟static_ip1是否为期望的值
        if Expect_Mac != Actual_Mac or Actual_IP != common_conf.static_ip1:
            print("【备注】该用例无法验证，原因：有线网卡WIRED1前端配置的Mac和IP与期望不匹配")
            assert False

        # 前提检验完成，开始检验用例
        time.sleep(5)
        Result = Test_static_dhcp_lease.test_static_dhcp_lease_2_1()
        if Result == 1:
            print("【成功】")
            StaticDHCPLease.Wired1_Effect = True
            assert True
        else:
            print("【失败】")
            StaticDHCPLease.Wired1_Effect = False
            assert False






    @unittest.skip("跳过")
    def test_H_staticDhcpLease_2_2(self):
        """【检验】有线网卡WIRED1的静态IP和static_ip1成功生效"""
        # if StaticDHCPLease.Wired1_Effect == False:

        # self.switch_to_staticDHCPLeasePage(self.driver.current_url)
        # # 前提条件：在列表中有记录，有线网卡wired1对应IP为static_ip1
        # # 获取Mac地址，是否为wired1
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, StaticDHCPLeaseLocators.List_MacAddr))
        # )
        # # 期望设置成的Mac地址
        # Expect_Mac = common_conf.wired1_mac.lower().split('-')
        # # 实际列表中设置的Mac地址
        # Actual_Mac = self.driver.find_element_by_xpath(StaticDHCPLeaseLocators.List_MacAddr).text.split(':')
        #
        # # 获取IP地址,是否为static_ip1
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, StaticDHCPLeaseLocators.List_IpAddr))
        # )
        # Actual_IP = self.driver.find_element_by_xpath(StaticDHCPLeaseLocators.List_IpAddr).text
        # # 断言：wired1跟static_ip1是否为期望的值
        # if Expect_Mac != Actual_Mac or Actual_IP != common_conf.static_ip1:
        #     print("【备注】该用例无法验证，原因：有线网卡WIRED1前端配置的Mac和IP与期望不匹配")
        #     assert False
        #
        # # 前提检验完成，开始检验用例
        # time.sleep(5)
        # Result = Test_static_dhcp_lease.test_static_dhcp_lease_2_2()
        # if Result == 1:
        #     print("【成功】")
        #     assert True
        # else:
        #     print("【失败】")
        #     assert False