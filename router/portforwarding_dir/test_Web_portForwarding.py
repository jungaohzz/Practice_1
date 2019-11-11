#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun


import unittest
from selenium import webdriver
from .. base import Base
from rweb import const
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from rweb.path.common import CommonLocators
from rweb.path.portForwarding import PortForwardingLocators
from rweb.path.internetSettings import InternetSettingsLocators
from rweb.path.routerManagement import RouterManagementLocators
from selenium.webdriver.common.action_chains import ActionChains


class PortForwarding(Base):

    # 定义端口转发页的url
    url_portForwardingPage = ""

    def switch_to_portForwardingPage(self, Current_Url):  # 切换到 端口转发
        self.driver.refresh()
        time.sleep(2)
        # 判断当前的url是否是目的url
        while PortForwarding.url_portForwardingPage != Current_Url:
            # 进入 端口转发
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, CommonLocators.LEVEL_1_AdvancedSettings))
            ).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, CommonLocators.PortForwarding))
            ).click()
            time.sleep(2)
            Current_Url = self.driver.current_url






    def set_access_way(self, Way):
        """设置接入方式：DHCP、静态IP、PPPoE"""
        # 先进入 上网设置 页
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
        ActionChains(self.driver).move_to_element(mouse).perform()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Internet_Settings))
        ).click()
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, InternetSettingsLocators.Internet_Way))
        )
        Internet_Way_value = self.driver.find_element_by_xpath(InternetSettingsLocators.Internet_Way).get_attribute('value')

        flag = False    #标记是否有修改，False为没有修改，True为有修改
        if Way == "DHCP":       # 动态拨号
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
                flag = True

        elif Way == "PPPoE":    # PPPoE
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
                flag = True
        else:                   # 静态拨号
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
                flag = True

        # 保存
        if flag == True:
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
            time.sleep(5)
            self.driver.refresh()
            time.sleep(5)
            assert self.driver.find_element_by_xpath(InternetSettingsLocators.Line).get_attribute('class') == "line"

            # # 断言：判断是否修改为：动态IP
            # # 再次进入 上网设置 页
            # WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
            # )
            # mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
            # ActionChains(self.driver).move_to_element(mouse).perform()
            # # 点击 上网设置
            # WebDriverWait(self.driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, CommonLocators.Internet_Settings))
            # ).click()
            # time.sleep(2)
            # # 断言：是否为：动态IP：
            # WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, InternetSettingsLocators.Internet_Way))
            # )
            # Internet_Way_value = self.driver.find_element_by_xpath(InternetSettingsLocators.Internet_Way).get_attribute('value')
            # assert Internet_Way_value == "DHCP", Internet_Way_value






    def deleteAll(self):
        """删除所有转发规则"""
        flag = False
        while flag == False:
            try:
                assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Null).is_displayed()
                flag = True
            except:
                # 批量删除
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.Check_ALL))
                ).click()
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.Deletes))
                ).click()
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.Delete_ok))
                ).click()
                # 断言:toast提示：成功
                WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                    EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
                )
                time.sleep(1)





    def add(self, ProtocolType, Name, OutNetIp, OutNetPort_start, OutNetPort_end, LocalIp, LocalPort_start, LocalPort_end):
        """配置端口转发规则"""
        # 点击 新增 按钮
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.Add))
        ).click()
        time.sleep(0.5)
        # 选择协议类型
        if ProtocolType == "TCP":
            Type = PortForwardingLocators.ProtocolType_TCP
        elif ProtocolType == "UDP":
            Type = PortForwardingLocators.ProtocolType_UDP
        else:
            Type = PortForwardingLocators.ProtocolType_TcpUdp
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Type))
        ).click()
        # 输入名称
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.Name))
        ).send_keys(Name)
        # 输入外网IP
        if OutNetIp != None:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.OutNetIp))
            ).send_keys(OutNetIp)
        # 输入外网端口
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.OutNetPort_start))
        ).send_keys(OutNetPort_start)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.OutNetPort_end))
        ).send_keys(OutNetPort_end)
        # 输入本地IP
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.LocalIp))
        ).send_keys(LocalIp)
        # 输入本地端口
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.LocalPort_start))
        ).send_keys(LocalPort_start)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.LocalPort_end))
        ).send_keys(LocalPort_end)
        # 新增保存
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.Save))
        ).click()
        # 断言:toast提示：打开开关成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"







    def test_A_get_url(self):
        """操作步骤：获取端口转发页url"""
        # 鼠标模拟移动到：设置
        time.sleep(2)
        # 进入 端口转发
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.LEVEL_1_AdvancedSettings))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.PortForwarding))
        ).click()
        time.sleep(2)
        PortForwarding.url_portForwardingPage = self.driver.current_url
        time.sleep(1)





    @unittest.skip("跳过")
    def test_B_set_accessWay_StaticIP(self):
        """操作步骤：设置WAN口为静态IP接入，并配置一条端口转发规则"""
        # 设置StaticIP
        self.set_access_way("StaticIP")
        # 清空转发规则
        self.switch_to_portForwardingPage(self.driver.current_url)
        self.deleteAll()
        # 新增转发规则
        self.add("TCP", "无外网IP", None, 1, 2, "192.168.127.100", 1, 2)   #？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？





    @unittest.skip("跳过")
    def test_C_2(self):
        """【检验】用例-3997:WAN口接入为静态IP接入时，配置一条端口转发规则，该规则生效"""

        # 前提条件1：WAN口接入方式为静态IP
        # 先进入 上网设置 页
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
        ActionChains(self.driver).move_to_element(mouse).perform()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Internet_Settings))
        ).click()
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, InternetSettingsLocators.Internet_Way))
        )
        Internet_Way_value = self.driver.find_element_by_xpath(InternetSettingsLocators.Internet_Way).get_attribute('value')
        if Internet_Way_value != "Static IP":
            print("【备注】该用例无法验证，原因：WAN口接入方式不为静态IP")
            assert False

        # 前提条件2：新增了XXXXXXX转发规则？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        self.switch_to_portForwardingPage(self.driver.current_url)
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # # 断言：名称是否为：有外网IP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Name))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Name).text == "有外网IP"
        #
        # # 断言：外网IP是否为：10.70.100.50
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetIp).text == "10.70.100.50"
        #
        # # 断言：外网端口是否为：5~10
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetPort).text == "5-10"
        #
        # # 断言：本地IP是否为：192.168.127.125
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalIp).text == "192.168.127.125"
        #
        # # 断言：本地端口是否为：15~20
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalPort).text == "15-20"
        #
        # # 断言：协议类型是否为:UDP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_ProtocolType))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_ProtocolType).text == "UDP"
        #
        # # 断言：状态是否默认为：打开
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute(
        #     'class') == "switch switch-animation checked"

        # 前提检验完成，开始检验用例
        time.sleep(5)  # 是否需要等待时间，待配置生效？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        Result = 1  # ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False




    @unittest.skip("跳过")
    def test_D_set_accessWay_PPPoE(self):
        """操作步骤：设置WAN口为PPPoE接入，并配置一条端口转发规则"""
        # 设置PPPoE
        self.set_access_way("PPPoE")
        # 清空转发规则
        self.switch_to_portForwardingPage(self.driver.current_url)
        self.deleteAll()
        # 新增转发规则
        self.add("TCP", "无外网IP", None, 1, 2, "192.168.127.100", 1, 2)   #？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？




    @unittest.skip("跳过")
    def test_E_3(self):
        """【检验】用例-3996 : WAN口接入为PPPOE接入时，配置一条端口转发规则，该规则生效"""

        # 前提条件1：WAN口接入方式为PPPoE
        # 先进入 上网设置 页
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
        ActionChains(self.driver).move_to_element(mouse).perform()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Internet_Settings))
        ).click()
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, InternetSettingsLocators.Internet_Way))
        )
        Internet_Way_value = self.driver.find_element_by_xpath(InternetSettingsLocators.Internet_Way).get_attribute(
            'value')
        if Internet_Way_value != "PPPoE":
            print("【备注】该用例无法验证，原因：WAN口接入方式不为PPPoE")
            assert False

        # 前提条件2：新增了XXXXXXX转发规则？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        self.switch_to_portForwardingPage(self.driver.current_url)
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # # 断言：名称是否为：有外网IP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Name))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Name).text == "有外网IP"
        #
        # # 断言：外网IP是否为：10.70.100.50
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetIp).text == "10.70.100.50"
        #
        # # 断言：外网端口是否为：5~10
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetPort).text == "5-10"
        #
        # # 断言：本地IP是否为：192.168.127.125
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalIp).text == "192.168.127.125"
        #
        # # 断言：本地端口是否为：15~20
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalPort).text == "15-20"
        #
        # # 断言：协议类型是否为:UDP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_ProtocolType))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_ProtocolType).text == "UDP"
        #
        # # 断言：状态是否默认为：打开
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute(
        #     'class') == "switch switch-animation checked"

        # 前提检验完成，开始检验用例
        time.sleep(5)  # 是否需要等待时间，待配置生效？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        Result = 1  # ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False




    @unittest.skip("跳过")
    def test_F_set_accessWay_DHCP(self):
        """操作步骤：设置WAN口为DHCP接入，并配置一条端口转发规则"""
        # 设置DHCP
        self.set_access_way("DHCP")
        # 清空转发规则
        self.switch_to_portForwardingPage(self.driver.current_url)
        self.deleteAll()
        # 新增转发规则
        self.add("TCP", "无外网IP", None, 1, 2, "192.168.127.100", 1, 2)   #？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？




    @unittest.skip("跳过")
    def test_G_1(self):
        """【检验】用例-3995:WAN口接入为DHCP接入时，配置一条端口转发规则，该规则生效"""

        # 前提条件1：WAN口接入方式为DHCP
        # 先进入 上网设置 页
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
        ActionChains(self.driver).move_to_element(mouse).perform()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Internet_Settings))
        ).click()
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, InternetSettingsLocators.Internet_Way))
        )
        Internet_Way_value = self.driver.find_element_by_xpath(InternetSettingsLocators.Internet_Way).get_attribute('value')
        if Internet_Way_value != "DHCP":
            print("【备注】该用例无法验证，原因：WAN口接入方式不为DHCP")
            assert False

        # 前提条件2：新增了XXXXXXX转发规则？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        self.switch_to_portForwardingPage(self.driver.current_url)
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # # 断言：名称是否为：有外网IP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Name))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Name).text == "有外网IP"
        #
        # # 断言：外网IP是否为：10.70.100.50
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetIp).text == "10.70.100.50"
        #
        # # 断言：外网端口是否为：5~10
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetPort).text == "5-10"
        #
        # # 断言：本地IP是否为：192.168.127.125
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalIp).text == "192.168.127.125"
        #
        # # 断言：本地端口是否为：15~20
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalPort).text == "15-20"
        #
        # # 断言：协议类型是否为:UDP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_ProtocolType))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_ProtocolType).text == "UDP"
        #
        # # 断言：状态是否默认为：打开
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute(
        #     'class') == "switch switch-animation checked"

        # 前提检验完成，开始检验用例
        time.sleep(5)   #是否需要等待时间，待配置生效？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        Result = 1  #？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False




    @unittest.skip("跳过")
    def test_H_add(self):
        """操作步骤：设置一条单对单TCP&UDP协议端口转发规则"""
        self.switch_to_portForwardingPage(self.driver.current_url)

        # 清空转发规则
        self.deleteAll()
        # 新增转发规则
        self.add("TCP&UDP", "无外网IP", None, 1, 1, "192.168.127.100", 1, 1)  # ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？




    @unittest.skip("跳过")
    def test_I_4(self):
        """【检验】用例-2774 : 设置一条单对单TCP&UDP协议端口转发规则，外网访问WAN口的TCP连接匹配到该规则，该数据包只被转发到规则中的主机"""
        self.switch_to_portForwardingPage(self.driver.current_url)

        # 前提条件：存在一条单对单TCP&UDP协议端口转发规则
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # # 断言：名称是否为：有外网IP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Name))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Name).text == "有外网IP"
        #
        # # 断言：外网IP是否为：10.70.100.50
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetIp).text == "10.70.100.50"
        #
        # # 断言：外网端口是否为：5~10
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetPort).text == "5-10"
        #
        # # 断言：本地IP是否为：192.168.127.125
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalIp).text == "192.168.127.125"
        #
        # # 断言：本地端口是否为：15~20
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalPort).text == "15-20"
        #
        # # 断言：协议类型是否为:UDP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_ProtocolType))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_ProtocolType).text == "UDP"
        #
        # # 断言：状态是否默认为：打开
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute(
        #     'class') == "switch switch-animation checked"

        # 前提检验完成，开始检验用例
        # time.sleep(5)  # 是否需要等待时间，待配置生效？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        Result = 1  # ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False




    @unittest.skip("跳过")
    def test_J_5(self):
        """【检验】用例-2312 : 设置一条单对单TCP&UDP协议端口转发规则，外网访问WAN口的UDP连接匹配到该规则，该数据包只被转发到规则中的主机"""
        self.switch_to_portForwardingPage(self.driver.current_url)

        # 前提条件：存在一条单对单TCP&UDP协议端口转发规则
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # # 断言：名称是否为：有外网IP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Name))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Name).text == "有外网IP"
        #
        # # 断言：外网IP是否为：10.70.100.50
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetIp).text == "10.70.100.50"
        #
        # # 断言：外网端口是否为：5~10
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetPort).text == "5-10"
        #
        # # 断言：本地IP是否为：192.168.127.125
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalIp).text == "192.168.127.125"
        #
        # # 断言：本地端口是否为：15~20
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalPort).text == "15-20"
        #
        # # 断言：协议类型是否为:UDP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_ProtocolType))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_ProtocolType).text == "UDP"
        #
        # # 断言：状态是否默认为：打开
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute(
        #     'class') == "switch switch-animation checked"

        # 前提检验完成，开始检验用例
        # time.sleep(5)  # 是否需要等待时间，待配置生效？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        Result = 1  # ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False




    @unittest.skip("跳过")
    def test_K_off(self):
        """操作步骤：将单对单TCP&UDP协议端口转发规则的状态关闭"""
        self.switch_to_portForwardingPage(self.driver.current_url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        )
        Statu_Class = self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute('class')

        # 状态为开时，才进行下面的关闭操作
        if Statu_Class == "switch switch-animation checked":
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.List_Statu))
            ).click()
            # 断言:toast提示：关闭成功
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"






    @unittest.skip("跳过")
    def test_L_16(self):
        """【检验】用例-4003 : 关闭一条单端口对单端口的TCP&UDP转发规则，外网访问WAN口的TCP连接匹配到该规则，该数据包不被转发到规则中的主机"""
        self.switch_to_portForwardingPage(self.driver.current_url)

        # 前提条件1：存在一条单对单TCP&UDP协议端口转发规则
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # # 断言：名称是否为：有外网IP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Name))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Name).text == "有外网IP"
        #
        # # 断言：外网IP是否为：10.70.100.50
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetIp).text == "10.70.100.50"
        #
        # # 断言：外网端口是否为：5~10
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetPort).text == "5-10"
        #
        # # 断言：本地IP是否为：192.168.127.125
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalIp).text == "192.168.127.125"
        #
        # # 断言：本地端口是否为：15~20
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalPort).text == "15-20"
        #
        # # 断言：协议类型是否为:UDP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_ProtocolType))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_ProtocolType).text == "UDP"
        #
        # # 断言：状态是否默认为：打开
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute(
        #     'class') == "switch switch-animation checked"

        # 前提条件2：开关状态为关闭
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        )
        Statu_Class = self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute('class')
        if Statu_Class != "switch switch-animation":
            print("【备注】该用例无法验证，原因：端口转发状态不为关闭")
            assert False

        # 前提检验完成，开始检验用例
        # time.sleep(5)  # 是否需要等待时间，待配置生效？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        Result = 1  # ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False






    @unittest.skip("跳过")
    def test_M_17(self):
        """【检验】用例-4004 : 关闭一条单端口对单端口的TCP&UDP转发规则，外网访问WAN口的UDP连接匹配到该规则，该数据包不被转发到规则中的主机"""
        self.switch_to_portForwardingPage(self.driver.current_url)

        # 前提条件1：存在一条单对单TCP&UDP协议端口转发规则
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # # 断言：名称是否为：有外网IP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Name))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Name).text == "有外网IP"
        #
        # # 断言：外网IP是否为：10.70.100.50
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetIp).text == "10.70.100.50"
        #
        # # 断言：外网端口是否为：5~10
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetPort).text == "5-10"
        #
        # # 断言：本地IP是否为：192.168.127.125
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalIp).text == "192.168.127.125"
        #
        # # 断言：本地端口是否为：15~20
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalPort).text == "15-20"
        #
        # # 断言：协议类型是否为:UDP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_ProtocolType))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_ProtocolType).text == "UDP"
        #
        # # 断言：状态是否默认为：打开
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute(
        #     'class') == "switch switch-animation checked"

        # 前提条件2：开关状态为关闭
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        )
        Statu_Class = self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute('class')
        if Statu_Class != "switch switch-animation":
            print("【备注】该用例无法验证，原因：端口转发状态不为关闭")
            assert False

        # 前提检验完成，开始检验用例
        # time.sleep(5)  # 是否需要等待时间，待配置生效？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        Result = 1  # ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False






    @unittest.skip("跳过")
    def test_N_add(self):
        """操作步骤：设置一条多个端口对多个端口的TCP&UDP端口转发规则"""
        self.switch_to_portForwardingPage(self.driver.current_url)

        # 清空转发规则
        self.deleteAll()
        # 新增转发规则
        self.add("TCP&UDP", "无外网IP", None, 5000, 6000, "192.168.127.100", 5000, 6000)  # ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？




    @unittest.skip("跳过")
    def test_O_6(self):
        """【检验】用例-3405 : 设置一条多个端口对多个端口的TCP&UDP端口转发规则，外网访问WAN口的连接匹配到该规则，该数据包只被转发到规则中的主机"""
        self.switch_to_portForwardingPage(self.driver.current_url)

        # 前提条件：存在一条多个端口对多个端口的TCP&UDP端口转发规则
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # # 断言：名称是否为：有外网IP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Name))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Name).text == "有外网IP"
        #
        # # 断言：外网IP是否为：10.70.100.50
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetIp).text == "10.70.100.50"
        #
        # # 断言：外网端口是否为：5~10
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetPort).text == "5-10"
        #
        # # 断言：本地IP是否为：192.168.127.125
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalIp).text == "192.168.127.125"
        #
        # # 断言：本地端口是否为：15~20
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalPort).text == "15-20"
        #
        # # 断言：协议类型是否为:UDP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_ProtocolType))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_ProtocolType).text == "UDP"
        #
        # # 断言：状态是否默认为：打开
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute(
        #     'class') == "switch switch-animation checked"

        # 前提检验完成，开始检验用例
        # time.sleep(5)  # 是否需要等待时间，待配置生效？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        Result = 1  # ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False




    @unittest.skip("跳过")
    def test_P_off(self):
        """操作步骤：将多个端口对多个端口的TCP&UDP端口转发规则的状态关闭"""
        self.switch_to_portForwardingPage(self.driver.current_url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        )
        Statu_Class = self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute('class')

        # 状态为开时，才进行下面的关闭操作
        if Statu_Class == "switch switch-animation checked":
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.List_Statu))
            ).click()
            # 断言:toast提示：关闭成功
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"





    @unittest.skip("跳过")
    def test_Q_15(self):
        """【检验】用例-3410 : 关闭一条多个端口对多个端口的TCP&UDP端口转发规则，外网访问WAN口的连接匹配到该规则，该数据包只被转发到规则中的主机"""
        self.switch_to_portForwardingPage(self.driver.current_url)

        # 前提条件1：存在多个端口对多个端口的TCP&UDP端口转发规则
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # # 断言：名称是否为：有外网IP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Name))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Name).text == "有外网IP"
        #
        # # 断言：外网IP是否为：10.70.100.50
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetIp).text == "10.70.100.50"
        #
        # # 断言：外网端口是否为：5~10
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetPort).text == "5-10"
        #
        # # 断言：本地IP是否为：192.168.127.125
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalIp).text == "192.168.127.125"
        #
        # # 断言：本地端口是否为：15~20
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalPort).text == "15-20"
        #
        # # 断言：协议类型是否为:UDP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_ProtocolType))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_ProtocolType).text == "UDP"
        #
        # # 断言：状态是否默认为：打开
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute(
        #     'class') == "switch switch-animation checked"

        # 前提条件2：开关状态为关闭
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        )
        Statu_Class = self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute('class')
        if Statu_Class != "switch switch-animation":
            print("【备注】该用例无法验证，原因：端口转发状态不为关闭")
            assert False

        # 前提检验完成，开始检验用例
        # time.sleep(5)  # 是否需要等待时间，待配置生效？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        Result = 1  # ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False





    @unittest.skip("跳过")
    def test_R_add(self):
        """操作步骤：设置一条单对单TCP协议端口转发规则"""
        self.switch_to_portForwardingPage(self.driver.current_url)

        # 清空转发规则
        self.deleteAll()
        # 新增转发规则
        self.add("TCP", "无外网IP", None, 1, 1, "192.168.127.100", 1, 1)  # ？？？？？？？？？？？？？？？？？？？？？？？？？





    @unittest.skip("跳过")
    def test_S_7(self):
        """【检验】用例-2310 : 设置一条单对单TCP协议端口转发规则，外网访问WAN口的连接匹配到该规则，该数据包只被转发到规则中的主机"""
        self.switch_to_portForwardingPage(self.driver.current_url)

        # 前提条件：存在一条单对单TCP协议端口转发规则
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # # 断言：名称是否为：有外网IP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Name))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Name).text == "有外网IP"
        #
        # # 断言：外网IP是否为：10.70.100.50
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetIp).text == "10.70.100.50"
        #
        # # 断言：外网端口是否为：5~10
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetPort).text == "5-10"
        #
        # # 断言：本地IP是否为：192.168.127.125
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalIp).text == "192.168.127.125"
        #
        # # 断言：本地端口是否为：15~20
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalPort).text == "15-20"
        #
        # # 断言：协议类型是否为:UDP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_ProtocolType))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_ProtocolType).text == "UDP"
        #
        # # 断言：状态是否默认为：打开
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute(
        #     'class') == "switch switch-animation checked"

        # 前提检验完成，开始检验用例
        # time.sleep(5)  # 是否需要等待时间，待配置生效？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        Result = 1  # ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False





    @unittest.skip("跳过")
    def test_T_9(self):
        """【检验】用例-2678 : 设置一条单对单TCP协议端口转发规则，外网访问WAN口的连接没有完全匹配到规则，该数据包不被转发到规则中的主机"""
        self.switch_to_portForwardingPage(self.driver.current_url)

        # 前提条件：存在一条单对单TCP协议端口转发规则
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # # 断言：名称是否为：有外网IP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Name))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Name).text == "有外网IP"
        #
        # # 断言：外网IP是否为：10.70.100.50
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetIp).text == "10.70.100.50"
        #
        # # 断言：外网端口是否为：5~10
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetPort).text == "5-10"
        #
        # # 断言：本地IP是否为：192.168.127.125
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalIp).text == "192.168.127.125"
        #
        # # 断言：本地端口是否为：15~20
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalPort).text == "15-20"
        #
        # # 断言：协议类型是否为:UDP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_ProtocolType))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_ProtocolType).text == "UDP"
        #
        # # 断言：状态是否默认为：打开
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute(
        #     'class') == "switch switch-animation checked"

        # 前提检验完成，开始检验用例
        # time.sleep(5)  # 是否需要等待时间，待配置生效？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        Result = 1  # ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False




    @unittest.skip("跳过")
    def test_U_11(self):
        """【检验】用例-3383 : 设置一条单对单TCP协议端口转发规则，内网访问WAN口的连接匹配到该规则，该数据包只被转发到规则中的主机"""
        self.switch_to_portForwardingPage(self.driver.current_url)

        # 前提条件：存在一条单对单TCP协议端口转发规则
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # # 断言：名称是否为：有外网IP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Name))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Name).text == "有外网IP"
        #
        # # 断言：外网IP是否为：10.70.100.50
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetIp).text == "10.70.100.50"
        #
        # # 断言：外网端口是否为：5~10
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetPort).text == "5-10"
        #
        # # 断言：本地IP是否为：192.168.127.125
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalIp).text == "192.168.127.125"
        #
        # # 断言：本地端口是否为：15~20
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalPort).text == "15-20"
        #
        # # 断言：协议类型是否为:UDP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_ProtocolType))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_ProtocolType).text == "UDP"
        #
        # # 断言：状态是否默认为：打开
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute(
        #     'class') == "switch switch-animation checked"

        # 前提检验完成，开始检验用例
        # time.sleep(5)  # 是否需要等待时间，待配置生效？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        Result = 1  # ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False




    @unittest.skip("跳过")
    def test_V_13(self):
        """【检验】用例-3391 : 设置一条单对单TCP协议端口转发规则，内网访问WAN口的连接没有完全匹配到该规则，该数据包不被转发到规则中的主机"""
        self.switch_to_portForwardingPage(self.driver.current_url)

        # 前提条件：存在一条单对单TCP协议端口转发规则
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # # 断言：名称是否为：有外网IP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Name))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Name).text == "有外网IP"
        #
        # # 断言：外网IP是否为：10.70.100.50
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetIp).text == "10.70.100.50"
        #
        # # 断言：外网端口是否为：5~10
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetPort).text == "5-10"
        #
        # # 断言：本地IP是否为：192.168.127.125
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalIp).text == "192.168.127.125"
        #
        # # 断言：本地端口是否为：15~20
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalPort).text == "15-20"
        #
        # # 断言：协议类型是否为:UDP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_ProtocolType))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_ProtocolType).text == "UDP"
        #
        # # 断言：状态是否默认为：打开
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute(
        #     'class') == "switch switch-animation checked"

        # 前提检验完成，开始检验用例
        # time.sleep(5)  # 是否需要等待时间，待配置生效？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        Result = 1  # ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False




    @unittest.skip("跳过")
    def test_W_off(self):
        """操作步骤：将单对单TCP协议端口转发规则的状态关闭"""
        self.switch_to_portForwardingPage(self.driver.current_url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        )
        Statu_Class = self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute('class')

        # 状态为开时，才进行下面的关闭操作
        if Statu_Class == "switch switch-animation checked":
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.List_Statu))
            ).click()
            # 断言:toast提示：关闭成功
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"





    @unittest.skip("跳过")
    def test_X_18(self):
        """【检验】用例-3395 : 关闭一条单端口对单端口的TCP协议端口转发规则，外网访问WAN口的连接匹配到该规则，该数据包不被转发到规则中的主机"""
        self.switch_to_portForwardingPage(self.driver.current_url)

        # 前提条件1：存在一条单对单TCP协议端口转发规则
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # # 断言：名称是否为：有外网IP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Name))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Name).text == "有外网IP"
        #
        # # 断言：外网IP是否为：10.70.100.50
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetIp).text == "10.70.100.50"
        #
        # # 断言：外网端口是否为：5~10
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetPort).text == "5-10"
        #
        # # 断言：本地IP是否为：192.168.127.125
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalIp).text == "192.168.127.125"
        #
        # # 断言：本地端口是否为：15~20
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalPort).text == "15-20"
        #
        # # 断言：协议类型是否为:UDP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_ProtocolType))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_ProtocolType).text == "UDP"
        #
        # # 断言：状态是否默认为：打开
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute(
        #     'class') == "switch switch-animation checked"

        # 前提条件2：开关状态为关闭
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        )
        Statu_Class =  self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute('class')
        if Statu_Class != "switch switch-animation":
            print("【备注】该用例无法验证，原因：端口转发状态不为关闭")
            assert False

        # 前提检验完成，开始检验用例
        # time.sleep(5)  # 是否需要等待时间，待配置生效？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        Result = 1  # ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False





    @unittest.skip("跳过")
    def test_Y_add(self):
        """操作步骤：设置一条单对单UDP协议端口转发规则"""
        self.switch_to_portForwardingPage(self.driver.current_url)

        # 清空转发规则
        self.deleteAll()
        # 新增转发规则
        self.add("UDP", "无外网IP", None, 1, 1, "192.168.127.100", 1, 1)  # ？？？？？？？？？？？？？？？？？？？？？？？？？





    @unittest.skip("跳过")
    def test_Z_8(self):
        """【检验】用例-2311 : 设置一条单对单UDP协议端口转发规则，外网访问WAN口的连接匹配到该规则，该数据包只被转发到规则中的主机"""
        self.switch_to_portForwardingPage(self.driver.current_url)

        # 前提条件：存在一条单对单UDP协议端口转发规则
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # # 断言：名称是否为：有外网IP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Name))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Name).text == "有外网IP"
        #
        # # 断言：外网IP是否为：10.70.100.50
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetIp).text == "10.70.100.50"
        #
        # # 断言：外网端口是否为：5~10
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetPort).text == "5-10"
        #
        # # 断言：本地IP是否为：192.168.127.125
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalIp).text == "192.168.127.125"
        #
        # # 断言：本地端口是否为：15~20
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalPort).text == "15-20"
        #
        # # 断言：协议类型是否为:UDP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_ProtocolType))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_ProtocolType).text == "UDP"
        #
        # # 断言：状态是否默认为：打开
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute(
        #     'class') == "switch switch-animation checked"

        # 前提检验完成，开始检验用例
        # time.sleep(5)  # 是否需要等待时间，待配置生效？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        Result = 1  # ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False




    @unittest.skip("跳过")
    def test_a_10(self):
        """【检验】用例-3372 : 设置一条单对单UDP协议端口转发规则，外网访问WAN口的连接没有完全匹配到规则，该数据包不被转发到规则中的主机"""
        self.switch_to_portForwardingPage(self.driver.current_url)

        # 前提条件：存在一条单对单UDP协议端口转发规则
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # # 断言：名称是否为：有外网IP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Name))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Name).text == "有外网IP"
        #
        # # 断言：外网IP是否为：10.70.100.50
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetIp).text == "10.70.100.50"
        #
        # # 断言：外网端口是否为：5~10
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetPort).text == "5-10"
        #
        # # 断言：本地IP是否为：192.168.127.125
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalIp).text == "192.168.127.125"
        #
        # # 断言：本地端口是否为：15~20
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalPort).text == "15-20"
        #
        # # 断言：协议类型是否为:UDP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_ProtocolType))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_ProtocolType).text == "UDP"
        #
        # # 断言：状态是否默认为：打开
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute(
        #     'class') == "switch switch-animation checked"

        # 前提检验完成，开始检验用例
        # time.sleep(5)  # 是否需要等待时间，待配置生效？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        Result = 1  # ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False




    @unittest.skip("跳过")
    def test_b_12(self):
        """【检验】用例-3389 : 设置一条单对单UDP协议端口转发规则，内网访问WAN口的连接匹配到该规则，该数据包只被转发到规则中的主机"""
        self.switch_to_portForwardingPage(self.driver.current_url)

        # 前提条件：存在一条单对单UDP协议端口转发规则
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # # 断言：名称是否为：有外网IP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Name))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Name).text == "有外网IP"
        #
        # # 断言：外网IP是否为：10.70.100.50
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetIp).text == "10.70.100.50"
        #
        # # 断言：外网端口是否为：5~10
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetPort).text == "5-10"
        #
        # # 断言：本地IP是否为：192.168.127.125
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalIp).text == "192.168.127.125"
        #
        # # 断言：本地端口是否为：15~20
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalPort).text == "15-20"
        #
        # # 断言：协议类型是否为:UDP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_ProtocolType))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_ProtocolType).text == "UDP"
        #
        # # 断言：状态是否默认为：打开
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute(
        #     'class') == "switch switch-animation checked"

        # 前提检验完成，开始检验用例
        # time.sleep(5)  # 是否需要等待时间，待配置生效？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        Result = 1  # ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False




    @unittest.skip("跳过")
    def test_c_14(self):
        """【检验】用例-3390 : 设置一条单对单UDP协议端口转发规则，内网访问WAN口的连接没有完全匹配到该规则，该数据包不被转发到规则中的主机"""
        self.switch_to_portForwardingPage(self.driver.current_url)

        # 前提条件：存在一条单对单UDP协议端口转发规则
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # # 断言：名称是否为：有外网IP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Name))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Name).text == "有外网IP"
        #
        # # 断言：外网IP是否为：10.70.100.50
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetIp).text == "10.70.100.50"
        #
        # # 断言：外网端口是否为：5~10
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetPort).text == "5-10"
        #
        # # 断言：本地IP是否为：192.168.127.125
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalIp).text == "192.168.127.125"
        #
        # # 断言：本地端口是否为：15~20
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalPort).text == "15-20"
        #
        # # 断言：协议类型是否为:UDP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_ProtocolType))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_ProtocolType).text == "UDP"
        #
        # # 断言：状态是否默认为：打开
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute(
        #     'class') == "switch switch-animation checked"

        # 前提检验完成，开始检验用例
        # time.sleep(5)  # 是否需要等待时间，待配置生效？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        Result = 1  # ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False





    @unittest.skip("跳过")
    def test_d_off(self):
        """操作步骤：将单对单UDP协议端口转发规则的状态关闭"""
        self.switch_to_portForwardingPage(self.driver.current_url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        )
        Statu_Class = self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute('class')

        # 状态为开时，才进行下面的关闭操作
        if Statu_Class == "switch switch-animation checked":
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, PortForwardingLocators.List_Statu))
            ).click()
            # 断言:toast提示：关闭成功
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"





    @unittest.skip("跳过")
    def test_e_19(self):
        """【检验】用例-3397 : 关闭一条单端口对单端口UDP协议端口转发规则，外网访问WAN口的连接匹配到该规则，该数据包不被转发到规则中的主机"""
        self.switch_to_portForwardingPage(self.driver.current_url)

        # 前提条件1：存在一条单对单UDP协议端口转发规则
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # # 断言：名称是否为：有外网IP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Name))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Name).text == "有外网IP"
        #
        # # 断言：外网IP是否为：10.70.100.50
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetIp).text == "10.70.100.50"
        #
        # # 断言：外网端口是否为：5~10
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_OutNetPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_OutNetPort).text == "5-10"
        #
        # # 断言：本地IP是否为：192.168.127.125
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalIp))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalIp).text == "192.168.127.125"
        #
        # # 断言：本地端口是否为：15~20
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_LocalPort))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_LocalPort).text == "15-20"
        #
        # # 断言：协议类型是否为:UDP
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_ProtocolType))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_ProtocolType).text == "UDP"
        #
        # # 断言：状态是否默认为：打开
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        # )
        # assert self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute(
        #     'class') == "switch switch-animation checked"

        # 前提条件2：开关状态为关闭
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PortForwardingLocators.List_Statu))
        )
        Statu_Class = self.driver.find_element_by_xpath(PortForwardingLocators.List_Statu).get_attribute('class')
        if Statu_Class != "switch switch-animation":
            print("【备注】该用例无法验证，原因：端口转发状态不为关闭")
            assert False

        # 前提检验完成，开始检验用例
        # time.sleep(5)  # 是否需要等待时间，待配置生效？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        Result = 1  # ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False



