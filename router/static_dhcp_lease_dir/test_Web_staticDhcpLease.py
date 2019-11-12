#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun

import unittest
from ..base import Base
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
from ..common_dir import common_conf, common_fun
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
        if not StaticDHCPLease.Precondition:
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
        if not StaticDHCPLease.Precondition:
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
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
        time.sleep(1)
        # 重启生效
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, StaticDHCPLeaseLocators.Restart))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Save))
        ).click()
        time.sleep(10)
        # 重启成功判断：遮罩消失即可
        WebDriverWait(self.driver, const.REBOOT_WAIT).until_not(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Shade))
        )
        time.sleep(1)

    def deleteAlls(self):
        """操作步骤：删除列表所有记录"""
        flag = False
        while not flag:
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
        encryption_value = self.driver.find_element_by_xpath(WifiSettingsLocators.Encryption_Button).get_attribute(
            'value')
        if encryption_value != "WPA/WPA2-PSK":
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
            encryption_value = self.driver.find_element_by_xpath(WifiSettingsLocators.Encryption_Button).get_attribute(
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
            if Wifi_Name_Text != common_conf.ssid_2g and encryption_value != "WPA/WPA2-PSK" and WiFi_Password_Text != common_conf.wlan_password and \
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

    # 未通过测试！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
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
            result = Test_static_dhcp_lease.test_static_dhcp_lease_init()
            if result == 1:
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

    """
        验证：用例1-X系列
        配置有线网卡WIRED1的静态IP为static_ip1，能成功获取到对应ip地址
    """

    @unittest.skip("跳过")
    def test_D_staticDHCPLease_add_wired1(self):
        """操作步骤：配置WIRED1-static_ip1"""
        if StaticDHCPLease.Precondition == False:
            print("【失败】主WiFi默认设置或Mac与IP绑定相关前置条件配置失败")
            assert False

        self.add("WIRED1", common_conf.wired1_mac, common_conf.static_ip1)

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
        result = Test_static_dhcp_lease.test_static_dhcp_lease_1()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    """
        验证：用例2-X系列
        先配置有线网卡WIRED1的静态IP为static_ip1
        执行test_static_dhcp_lease_2_1
        test_static_dhcp_lease_2_1测试结果为1时，再将static_ip1绑定到WLAN5G1
        生效后执行test_static_dhcp_lease_2_2，然后使得WLAN5G1连接到WiFi并且拿到的ip为static_ip1，并且WIRED1拿到的ip不为static_ip1
    """

    @unittest.skip("跳过")
    def test_F_staticDHCPLease_add_wired1(self):
        """操作步骤：配置WIRED1-static_ip1"""
        if StaticDHCPLease.Precondition == False:
            print("【失败】主WiFi默认设置或Mac与IP绑定相关前置条件配置失败")
            assert False

        self.deleteAlls()
        self.add("WIRED1", common_conf.wired1_mac, common_conf.static_ip1)

    @unittest.skip("跳过")
    def test_G_staticDhcpLease_2_1(self):
        """【检验】用例-2836: 配置一条MAC / IP绑定规则，其他主机发送一个Request报文，其中可选字段请求IP地址为绑定的IP地址，该主机获取到路由器分配的其他IP"""
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
        result = Test_static_dhcp_lease.test_static_dhcp_lease_2_1()
        if result == 1:
            print("【成功】")
            StaticDHCPLease.Wired1_Effect = True
            assert True
        else:
            print("【失败】")
            StaticDHCPLease.Wired1_Effect = False
            assert False

    @unittest.skip("跳过")
    def test_H_staticDHCPLease_add_wlan5G1(self):
        """操作步骤：配置WLAN5G1-static_ip1"""
        if StaticDHCPLease.Precondition == False:
            print("【失败】主WiFi默认设置或Mac与IP绑定相关前置条件配置失败")
            assert False

        # 清空绑定列表
        self.deleteAlls()
        # 新增记录：将static_ip1绑定到WLAN5G1
        self.add("WLAN5G1", common_conf.wlan5g_mac, common_conf.static_ip1)

    # 未通过测试！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
    # 未通过测试！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
    # 原因：if static_ip1 == wlan5g1_ip and static_ip1 != wired1_ip的判断错误，实际是成功了的。
    # static_ip1，wlan5g1_ip，wired1_ip的值分别是：192.168.127.160，192.168.127.100192.168.127.160，192.168.127.100192.168.127.160，为什么输出2个IP？？？
    @unittest.skip("跳过")
    def test_I_staticDhcpLease_2_2(self):
        """
        【检验】用例-7372 : 配置一条MAC/IP绑定规则（IP已分配），原分配到该IP的主机发送一个request报文，原主机不能再分配到该IP
        【检验】用例-3987 : 配置一条MAC/IP绑定规则，主路由器下的5G设备会重新获取到绑定的IP地址
        """
        self.switch_to_staticDHCPLeasePage(self.driver.current_url)

        # 前提条件：有线网卡Wired1配置的静态IP成功生效
        if StaticDHCPLease.Wired1_Effect == False:
            print("Wired1配置static_ip1未生效")
            assert False

        # 前提检验完成，开始检验用例
        time.sleep(5)
        result = Test_static_dhcp_lease.test_static_dhcp_lease_2_2()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    """
        验证：用例3-X系列
        先配置有线网卡WIRED1的静态IP为static_ip1
        保存生效，执行test_static_dhcp_lease_3_1
        test_static_dhcp_lease_3_1测试结果为1时，修改WIRED1的静态IP为static_ip2
        保存生效后再执行test_static_dhcp_lease_3_2
    """

    @unittest.skip("跳过")
    def test_J_staticDHCPLease_add_wired1(self):
        """操作步骤：配置WIRED1-static_ip1"""
        if StaticDHCPLease.Precondition == False:
            print("【失败】主WiFi默认设置或Mac与IP绑定相关前置条件配置失败")
            assert False
        self.deleteAlls()
        self.add("WIRED1", common_conf.wired1_mac, common_conf.static_ip1)

    @unittest.skip("跳过")
    def test_K_staticDhcpLease_3_1(self):
        """【检验】用例-2833 : 配置一条MAC/IP绑定规则，该MAC对应主机发送一个Request报文，其中可选字段请求IP地址不为绑定的IP地址，该主机只能获取到绑定的IP地址"""
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
        result = Test_static_dhcp_lease.test_static_dhcp_lease_3_1()
        if result == 1:
            print("【成功】")
            StaticDHCPLease.Wired1_Effect = True
            assert True
        else:
            print("【失败】")
            StaticDHCPLease.Wired1_Effect = False
            assert False

    @unittest.skip("跳过")
    def test_L_staticDHCPLease_add_wired1(self):
        """操作步骤：配置WIRED1-static_ip2"""
        if StaticDHCPLease.Precondition == False:
            print("【失败】主WiFi默认设置或Mac与IP绑定相关前置条件配置失败")
            assert False

        # 清空绑定列表
        self.deleteAlls()
        # 新增记录：将static_ip1绑定到WLAN5G1
        self.add("WIRED1", common_conf.wired1_mac, common_conf.static_ip2)

    @unittest.skip("跳过")
    def test_M_staticDhcpLease_3_2(self):
        """【检验】用例-4009 : 修改一条MAC/IP绑定规则，新规则生效，老规则失效"""
        self.switch_to_staticDHCPLeasePage(self.driver.current_url)

        # 前提条件：有线网卡Wired1配置的静态IP成功生效
        if StaticDHCPLease.Wired1_Effect == False:
            print("Wired1配置static_ip1未生效")
            assert False

        # 前提检验完成，开始检验用例
        time.sleep(5)
        result = Test_static_dhcp_lease.test_static_dhcp_lease_3_2()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    """
        验证：用例4-X系列   
        配置有线网卡WIRED1的静态IP为static_ip1
        保存生效后，执行test_static_dhcp_lease_4
        test_static_dhcp_lease_4测试结果为1时，然后不做任何修改
        保存生效后，再执行test_static_dhcp_lease_4，测试结果为1表示通过
    """

    @unittest.skip("跳过")
    def test_N_staticDHCPLease_add_wired1(self):
        """操作步骤：配置WIRED1-static_ip1"""
        if StaticDHCPLease.Precondition == False:
            print("【失败】主WiFi默认设置或Mac与IP绑定相关前置条件配置失败")
            assert False
        self.deleteAlls()
        self.add("WIRED1", common_conf.wired1_mac, common_conf.static_ip1)

    @unittest.skip("跳过")
    def test_O_staticDhcpLease_4(self):
        """【检验】用例-2834 : 配置一条MAC/IP绑定规则，该MAC对应主机发送一个Request报文，其中可选字段请求IP地址绑定的IP地址，该主机只能获取到绑定的IP地址"""
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
        result = Test_static_dhcp_lease.test_static_dhcp_lease_4()
        if result == 1:
            print("【成功】")
            StaticDHCPLease.Wired1_Effect = True
            assert True
        else:
            print("【失败】")
            StaticDHCPLease.Wired1_Effect = False
            assert False

    @unittest.skip("跳过")
    def test_P_staticDhcpLease_4(self):
        """【检验】用例-2834 : 配置一条MAC/IP绑定规则，该MAC对应主机发送一个Request报文，其中可选字段请求IP地址绑定的IP地址，该主机只能获取到绑定的IP地址"""
        self.switch_to_staticDHCPLeasePage(self.driver.current_url)

        # 前提条件：有线网卡Wired1配置的静态IP成功生效
        if StaticDHCPLease.Wired1_Effect == False:
            print("Wired1配置static_ip1未生效")
            assert False

        # 前提检验完成，开始检验用例
        time.sleep(5)
        result = Test_static_dhcp_lease.test_static_dhcp_lease_4()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    # """
    #     验证：用例5-X系列
    #     先配置无线网卡WLAN5G1的静态IP为static_ip1
    #     保存生效后，执行test_static_dhcp_lease_5_1
    #     test_static_dhcp_lease_5_1测试结果为1时，删除所绑定的MAC/IP绑定规则
    #     保存生效后再执行test_static_dhcp_lease_5_2
    #     注：这部分用例在路由器端未实现，没有找到验证该功能的方式！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
    #     注：这部分用例在路由器端未实现，没有找到验证该功能的方式！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
    #     注：这部分用例在路由器端未实现，没有找到验证该功能的方式！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
    # """
    # #@unittest.skip("跳过")
    # def test_Q_staticDHCPLease_add_wlan5G1(self):
    #     """操作步骤：配置WLAN5G1-static_ip1"""
    #     if StaticDHCPLease.Precondition == False:
    #         print("【失败】主WiFi默认设置或Mac与IP绑定相关前置条件配置失败")
    #         assert False
    #     self.deleteAlls()
    #     self.add("WLAN5G1", common_conf.wlan5g_mac, common_conf.static_ip1)
    #
    #
    # #@unittest.skip("跳过")
    # def test_R_staticDhcpLease_5_1(self):
    #     """检验配置的WLAN5G1-static_ip1是否生效"""
    #     self.switch_to_staticDHCPLeasePage(self.driver.current_url)
    #     # 前提条件：在列表中有记录，有线网卡WLAN5G1对应IP为static_ip1
    #     # 获取Mac地址，是否为WLAN5G1
    #     WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, StaticDHCPLeaseLocators.List_MacAddr))
    #     )
    #     # 期望设置成的Mac地址
    #     Expect_Mac = common_conf.wlan5g_mac.lower().split('-')
    #     # 实际列表中设置的Mac地址
    #     Actual_Mac = self.driver.find_element_by_xpath(StaticDHCPLeaseLocators.List_MacAddr).text.split(':')
    #
    #     # 获取IP地址,是否为static_ip1
    #     WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, StaticDHCPLeaseLocators.List_IpAddr))
    #     )
    #     Actual_IP = self.driver.find_element_by_xpath(StaticDHCPLeaseLocators.List_IpAddr).text
    #     # 断言：WLAN5G1跟static_ip1是否为期望的值
    #     print("%s,%s,%s,%s"%(Expect_Mac,Actual_Mac,Actual_IP,common_conf.static_ip1))
    #     if Expect_Mac != Actual_Mac or Actual_IP != common_conf.static_ip1:
    #         print("【备注】该用例无法验证，原因：无线网卡WLAN5G1前端配置的Mac和IP与期望不匹配")
    #         assert False
    #
    #     # 前提检验完成，开始检验用例
    #     time.sleep(5)
    #     result = Test_static_dhcp_lease.test_static_dhcp_lease_5_1()
    #     if result == 1:
    #         print("【成功】")
    #         StaticDHCPLease.Wired1_Effect = True
    #         assert True
    #     else:
    #         print("【失败】")
    #         StaticDHCPLease.Wired1_Effect = False
    #         assert False
    #
    #
    # #@unittest.skip("跳过")
    # def test_S_staticDHCPLease_deleteAll(self):
    #     """操作步骤：删除所有绑定记录"""
    #     if StaticDHCPLease.Precondition == False:
    #         print("【失败】主WiFi默认设置或Mac与IP绑定相关前置条件配置失败")
    #         assert False
    #
    #     # 清空绑定列表
    #     self.deleteAlls()
    #
    #     # 重启生效
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, StaticDHCPLeaseLocators.Restart))
    #     ).click()
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, CommonLocators.Save))
    #     ).click()
    #     time.sleep(10)
    #     # 重启成功判断：遮罩消失即可
    #     WebDriverWait(self.driver, const.REBOOT_WAIT).until_not(
    #         EC.element_to_be_clickable((By.XPATH, CommonLocators.Shade))
    #     )
    #     time.sleep(1)
    #
    #
    # #@unittest.skip("跳过")
    # def test_T_staticDhcpLease_5_2(self):
    #     """【检验】用例-2838 : 删除一条MAC/IP绑定规则，该规则失效"""
    #     self.switch_to_staticDHCPLeasePage(self.driver.current_url)
    #
    #     # 前提条件：有线网卡Wired1配置的静态IP成功生效
    #     if StaticDHCPLease.Wired1_Effect == False:
    #         print("Wired1配置static_ip1未生效")
    #         assert False
    #
    #     # 前提检验完成，开始检验用例
    #     time.sleep(5)
    #     result = Test_static_dhcp_lease.test_static_dhcp_lease_5_2()
    #     if result == 1:
    #         print("【成功】")
    #         assert True
    #     else:
    #         print("【失败】")
    #         assert False
