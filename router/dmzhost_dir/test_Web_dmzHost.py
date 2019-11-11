#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/18 22:43
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
from rweb.path.internetSettings import InternetSettingsLocators
from rweb.path.routerManagement import RouterManagementLocators
from selenium.webdriver.common.action_chains import ActionChains
from rweb.path.staticDhcpLease import StaticDHCPLeaseLocators
from rweb.path.dmzHost import DmzHostLocators

"""DMZ主机"""

class DmzHost(Base):
    # def setUp(self):
    #     super(DmzHost, self).setUp()
    #     # 鼠标模拟移动到：高级设置
    #     WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_AdvancedSettings))
    #     )
    #     mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_AdvancedSettings)
    #     ActionChains(self.driver).move_to_element(mouse).perform()
    #     # 点击 DMZ主机
    #     WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, CommonLocators.DMZ_Host))
    #     ).click()
    #     time.sleep(2)
    #
    #     # WebDriverWait(self.driver,10).until_not(
    #     #     EC.presence_of_element_located((By.XPATH, CommonLocators.Loading))
    #     # )

    # 定义DMZ主机页的url
    url_dmzhostPage = ""

    def switch_to_dmzhostPage(self, Current_Url):  # 切换到 DMZ主机
        self.driver.refresh()
        time.sleep(2)
        # 判断当前的url是否是目的url
        while DmzHost.url_dmzhostPage != Current_Url:
            # 鼠标模拟移动到：高级设置
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_AdvancedSettings))
            )
            mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_AdvancedSettings)
            ActionChains(self.driver).move_to_element(mouse).perform()
            # 点击 DMZ主机
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, CommonLocators.DMZ_Host))
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
        Internet_Way_value = self.driver.find_element_by_xpath(InternetSettingsLocators.Internet_Way).get_attribute(
            'value')

        flag = False  # 标记是否有修改，False为没有修改，True为有修改
        if Way == "DHCP":  # 动态拨号
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

        elif Way == "PPPoE":  # PPPoE
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
        else:  # 静态拨号
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
                self.driver.find_element_by_xpath(InternetSettingsLocators.StaticIP_Netmask).send_keys(
                    "255.255.0.0")
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






    def test_A_get_url(self):
        """操作步骤：获取端口转发页url"""
        # 鼠标模拟移动到：设置
        time.sleep(2)
        # 进入 端口转发
        # 鼠标模拟移动到：高级设置
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_AdvancedSettings))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_AdvancedSettings)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 DMZ主机
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.DMZ_Host))
        ).click()
        time.sleep(2)
        DmzHost.url_dmzhostPage = self.driver.current_url
        time.sleep(1)





    @unittest.skip("跳过")
    def test_B_set_accessWay_PPPoE(self):
        """操作步骤：设置WAN口为PPPoE接入，并配置一条dmz转发规则"""
        # 设置PPPoE
        self.set_access_way("PPPoE")

        # 设置dmz转发规则
        self.switch_to_dmzhostPage(self.driver.current_url)
        # 输入IP地址
        time.sleep(0.5)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.DmzHostIp))
        ).clear()
        time.sleep(0.5)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.DmzHostIp))
        ).send_keys("192.168.127.200")  # ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # 判断：开关如果为关闭，才进行开启操作
        if self.driver.find_element_by_xpath(DmzHostLocators.Statu).get_attribute('class') == "box":
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, DmzHostLocators.Statu))
            ).click()
        # 保存
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.Save))
        ).click()

        # 断言:是否保存成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"






    @unittest.skip("跳过")
    def test_C_2(self):
        """【检验】用例-3993:WAN口接入为PPPOE接入时，配置一条DMZ规则，该规则生效"""

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
        self.switch_to_dmzhostPage(self.driver.current_url)
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, DmzHostLocators.DmzHostIp))
        # )
        # assert self.driver.find_element_by_xpath(DmzHostLocators.DmzHostIp).get_attribute("value") == "192.168.127.200"

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
    def test_D_set_accessWay_StaticIP(self):
        """操作步骤：设置WAN口为静态IP接入，并配置一条dmz转发规则"""
        # 设置StaticIP
        self.set_access_way("StaticIP")

        # 设置dmz转发规则
        self.switch_to_dmzhostPage(self.driver.current_url)
        # 输入IP地址
        time.sleep(0.5)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.DmzHostIp))
        ).clear()
        time.sleep(0.5)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.DmzHostIp))
        ).send_keys("192.168.127.200")  # ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # 判断：开关如果为关闭，才进行开启操作
        if self.driver.find_element_by_xpath(DmzHostLocators.Statu).get_attribute('class') == "box":
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, DmzHostLocators.Statu))
            ).click()
        # 保存
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.Save))
        ).click()

        # 断言:是否保存成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"






    @unittest.skip("跳过")
    def test_E_3(self):
        """【检验】用例-3994 : WAN口接入为静态接入时，配置一条DMZ规则，该规则生效"""

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
        Internet_Way_value = self.driver.find_element_by_xpath(InternetSettingsLocators.Internet_Way).get_attribute(
            'value')
        if Internet_Way_value != "Static IP":
            print("【备注】该用例无法验证，原因：WAN口接入方式不为StaticIP")
            assert False

        # 前提条件2：新增了XXXXXXX转发规则？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        self.switch_to_dmzhostPage(self.driver.current_url)
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, DmzHostLocators.DmzHostIp))
        # )
        # assert self.driver.find_element_by_xpath(DmzHostLocators.DmzHostIp).get_attribute("value") == "192.168.127.200"

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
        """操作步骤：设置WAN口为DHCP接入，并配置一条dmz转发规则"""
        # 设置DHCP
        self.set_access_way("DHCP")

        # 设置dmz转发规则
        self.switch_to_dmzhostPage(self.driver.current_url)
        # 输入IP地址
        time.sleep(0.5)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.DmzHostIp))
        ).clear()
        time.sleep(0.5)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.DmzHostIp))
        ).send_keys("192.168.127.200")      #？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # 判断：开关如果为关闭，才进行开启操作
        if self.driver.find_element_by_xpath(DmzHostLocators.Statu).get_attribute('class') == "box":
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, DmzHostLocators.Statu))
            ).click()
        # 保存
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.Save))
        ).click()

        # 断言:是否保存成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"







    @unittest.skip("跳过")
    def test_G_1(self):
        """【检验】用例-3992 : WAN口接入为DHCP接入时，配置一条DMZ规则，该规则生效"""

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
        Internet_Way_value = self.driver.find_element_by_xpath(InternetSettingsLocators.Internet_Way).get_attribute(
            'value')
        if Internet_Way_value != "DHCP":
            print("【备注】该用例无法验证，原因：WAN口接入方式不为DHCP")
            assert False

        # 前提条件2：新增了XXXXXXX转发规则？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        self.switch_to_dmzhostPage(self.driver.current_url)
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, DmzHostLocators.DmzHostIp))
        # )
        # assert self.driver.find_element_by_xpath(DmzHostLocators.DmzHostIp).get_attribute("value") == "192.168.127.200"

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
    def test_H_edit(self):
        """操作步骤：修改dmz转发规则"""
        self.switch_to_dmzhostPage(self.driver.current_url)

        # 输入IP地址
        time.sleep(0.5)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.DmzHostIp))
        ).clear()
        time.sleep(0.5)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.DmzHostIp))
        ).send_keys("192.168.127.202")  # ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # 判断：开关如果为关闭，才进行开启操作
        if self.driver.find_element_by_xpath(DmzHostLocators.Statu).get_attribute('class') == "box":
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, DmzHostLocators.Statu))
            ).click()
        # 保存
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.Save))
        ).click()

        # 断言:是否保存成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"






    @unittest.skip("跳过")
    def test_I_4(self):
        """【检验】用例-3999 : 修改DMZ规则后，新规则生效，旧规则失效"""
        self.switch_to_dmzhostPage(self.driver.current_url)

        # 前提条件：dmz规则已修改为新的规则
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, DmzHostLocators.DmzHostIp))
        # )
        # assert self.driver.find_element_by_xpath(DmzHostLocators.DmzHostIp).get_attribute("value") == "192.168.127.200"

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
    def test_J_5(self):
        """【检验】用例-2481 : 设置DMZ主机后，外网访问WAN口的TCP报文，未匹配到路由器已建立的连接，会被直接转发给DMZ主机"""
        self.switch_to_dmzhostPage(self.driver.current_url)

        # 前提条件：dmz设置规则且已开启
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, DmzHostLocators.DmzHostIp))
        # )
        # assert self.driver.find_element_by_xpath(DmzHostLocators.DmzHostIp).get_attribute("value") == "192.168.127.200"

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
    def test_K_6(self):
        """【检验】用例-2482 : 设置DMZ主机后，外网访问WAN口的UDP报文，未匹配到路由器已建立的连接，会被直接转发给DMZ主机"""
        self.switch_to_dmzhostPage(self.driver.current_url)

        # 前提条件：dmz设置规则且已开启
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, DmzHostLocators.DmzHostIp))
        # )
        # assert self.driver.find_element_by_xpath(DmzHostLocators.DmzHostIp).get_attribute("value") == "192.168.127.200"

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
    def test_L_7(self):
        """【检验】用例-2478 : 设置DMZ主机后，外网访问WAN口的ICMP报文，未匹配到路由器已建立的连接，会被直接转发给DMZ主机"""
        self.switch_to_dmzhostPage(self.driver.current_url)

        # 前提条件：dmz设置规则且已开启
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, DmzHostLocators.DmzHostIp))
        # )
        # assert self.driver.find_element_by_xpath(DmzHostLocators.DmzHostIp).get_attribute("value") == "192.168.127.200"

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
    def test_M_8(self):
        """【检验】用例-2507 : 设置DMZ主机后，内网访问WAN口的TCP报文，未匹配到路由器已建立的连接，会被直接转发给DMZ主机"""
        self.switch_to_dmzhostPage(self.driver.current_url)

        # 前提条件：dmz设置规则且已开启
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, DmzHostLocators.DmzHostIp))
        # )
        # assert self.driver.find_element_by_xpath(DmzHostLocators.DmzHostIp).get_attribute("value") == "192.168.127.200"

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
    def test_N_9(self):
        """【检验】用例-2509 : 设置DMZ主机后，内网访问WAN口的UDP报文，未匹配到路由器已建立的连接，会被直接转发给DMZ主机"""
        self.switch_to_dmzhostPage(self.driver.current_url)

        # 前提条件：dmz设置规则且已开启
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, DmzHostLocators.DmzHostIp))
        # )
        # assert self.driver.find_element_by_xpath(DmzHostLocators.DmzHostIp).get_attribute("value") == "192.168.127.200"

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
    def test_O_10(self):
        """【检验】用例-2511 : 设置DMZ主机后，内网访问WAN口的ICMP报文，未匹配到路由器已建立的连接，会被直接转发给DMZ主机"""
        self.switch_to_dmzhostPage(self.driver.current_url)

        # 前提条件：dmz设置规则且已开启
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, DmzHostLocators.DmzHostIp))
        # )
        # assert self.driver.find_element_by_xpath(DmzHostLocators.DmzHostIp).get_attribute("value") == "192.168.127.200"

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
    def test_P_11(self):
        """【检验】用例-2538 : 设置DMZ主机后，外网访问WAN口的TCP报文，匹配到路由器已建立的连接，会被直接转给对应主机(该主机不为DMZ主机)"""
        self.switch_to_dmzhostPage(self.driver.current_url)

        # 前提条件：dmz设置规则且已开启
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, DmzHostLocators.DmzHostIp))
        # )
        # assert self.driver.find_element_by_xpath(DmzHostLocators.DmzHostIp).get_attribute("value") == "192.168.127.200"

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
    def test_Q_12(self):
        """【检验】用例-2539 : 设置DMZ主机后，外网访问WAN口的UDP报文，匹配到路由器已建立的连接，会被直接转给对应主机(该主机不为DMZ主机)"""
        self.switch_to_dmzhostPage(self.driver.current_url)

        # 前提条件：dmz设置规则且已开启
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, DmzHostLocators.DmzHostIp))
        # )
        # assert self.driver.find_element_by_xpath(DmzHostLocators.DmzHostIp).get_attribute("value") == "192.168.127.200"

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
    def test_R_13(self):
        """【检验】用例-2580 : 设置DMZ主机后，外网访问WAN口的ICMP报文，匹配到路由器已建立的连接，会被直接转给对应主机(该主机不为DMZ主机)"""
        self.switch_to_dmzhostPage(self.driver.current_url)

        # 前提条件：dmz设置规则且已开启
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, DmzHostLocators.DmzHostIp))
        # )
        # assert self.driver.find_element_by_xpath(DmzHostLocators.DmzHostIp).get_attribute("value") == "192.168.127.200"

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
    def test_S_14(self):
        """【检验】用例-2667 : 设置DMZ主机后，内网访问WAN口的TCP报文，匹配到路由器已建立的连接，会被直接转给对应主机(该主机不为DMZ主机)"""
        self.switch_to_dmzhostPage(self.driver.current_url)

        # 前提条件：dmz设置规则且已开启
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, DmzHostLocators.DmzHostIp))
        # )
        # assert self.driver.find_element_by_xpath(DmzHostLocators.DmzHostIp).get_attribute("value") == "192.168.127.200"

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
    def test_T_15(self):
        """【检验】用例-2668 : 设置DMZ主机后，内网访问WAN口的UDP报文，匹配到路由器已建立的连接，会被直接转给对应主机(该主机不为DMZ主机)"""
        self.switch_to_dmzhostPage(self.driver.current_url)

        # 前提条件：dmz设置规则且已开启
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, DmzHostLocators.DmzHostIp))
        # )
        # assert self.driver.find_element_by_xpath(DmzHostLocators.DmzHostIp).get_attribute("value") == "192.168.127.200"

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
    def test_U_16(self):
        """【检验】用例-2669 : 设置DMZ主机后，内网访问WAN口的ICMP报文，匹配到路由器已建立的连接，会被直接转给对应主机(该主机不为DMZ主机)"""
        self.switch_to_dmzhostPage(self.driver.current_url)

        # 前提条件：dmz设置规则且已开启
        # 编写检验规则的代码？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, DmzHostLocators.DmzHostIp))
        # )
        # assert self.driver.find_element_by_xpath(DmzHostLocators.DmzHostIp).get_attribute("value") == "192.168.127.200"

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
    def test_V_edit_off(self):
        """操作步骤：关闭dmz转发规则"""
        self.switch_to_dmzhostPage(self.driver.current_url)

        # 判断：开关如果为开启，才进行关闭操作
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.Statu))
        )
        if self.driver.find_element_by_xpath(DmzHostLocators.Statu).get_attribute('class') == "box checked":
            self.driver.find_element_by_xpath(DmzHostLocators.Statu).click()
        # 保存
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.Save))
        ).click()

        # 断言:是否保存成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"




    @unittest.skip("跳过")
    def test_W_17(self):
        """【检验】用例-2504 : 关闭DMZ主机后，外网访问WAN口的TCP报文，未匹配到路由器已建立的连接，不会被转发给DMZ主机"""
        self.switch_to_dmzhostPage(self.driver.current_url)

        # 前提条件：dmz开关关闭
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.Statu))
        )
        if self.driver.find_element_by_xpath(DmzHostLocators.Statu).get_attribute('class') != "box":
            print("【备注】该用例无法验证，原因：DMZ状态开关未关闭")
            assert False
        # 还需检验dmz设置为多少吗？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？

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
    def test_X_18(self):
        """【检验】用例-2505 : 关闭DMZ主机后，外网访问WAN口的UDP报文，未匹配到路由器已建立的连接，不会被转发给DMZ主机"""
        self.switch_to_dmzhostPage(self.driver.current_url)

        # 前提条件：dmz开关关闭
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.Statu))
        )
        if self.driver.find_element_by_xpath(DmzHostLocators.Statu).get_attribute('class') != "box":
            print("【备注】该用例无法验证，原因：DMZ状态开关未关闭")
            assert False
        # 还需检验dmz设置为多少吗？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？

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
    def test_Y_19(self):
        """【检验】用例-2506 : 关闭DMZ主机后，外网访问WAN口的ICMP报文，未匹配到路由器已建立的连接，不会被转发给DMZ主机"""
        self.switch_to_dmzhostPage(self.driver.current_url)

        # 前提条件：dmz开关关闭
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.Statu))
        )
        if self.driver.find_element_by_xpath(DmzHostLocators.Statu).get_attribute('class') != "box":
            print("【备注】该用例无法验证，原因：DMZ状态开关未关闭")
            assert False
        # 还需检验dmz设置为多少吗？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？

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
    def test_Z_20(self):
        """【检验】用例-2513 : 关闭DMZ主机后，内网访问WAN口的TCP报文，未匹配到路由器已建立的连接，不会被转发给DMZ主机"""
        self.switch_to_dmzhostPage(self.driver.current_url)

        # 前提条件：dmz开关关闭
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.Statu))
        )
        if self.driver.find_element_by_xpath(DmzHostLocators.Statu).get_attribute('class') != "box":
            print("【备注】该用例无法验证，原因：DMZ状态开关未关闭")
            assert False
        # 还需检验dmz设置为多少吗？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？

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
    def test_a_21(self):
        """【检验】用例-2514 : 关闭DMZ主机后，内网访问WAN口的UDP报文，未匹配到路由器已建立的连接，不会被转发给DMZ主机"""
        self.switch_to_dmzhostPage(self.driver.current_url)

        # 前提条件：dmz开关关闭
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.Statu))
        )
        if self.driver.find_element_by_xpath(DmzHostLocators.Statu).get_attribute('class') != "box":
            print("【备注】该用例无法验证，原因：DMZ状态开关未关闭")
            assert False
        # 还需检验dmz设置为多少吗？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？

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
    def test_b_22(self):
        """【检验】用例-2515 : 关闭DMZ主机后，内网访问WAN口的ICMP报文，未匹配到路由器已建立的连接，不会被转发给DMZ主机"""
        self.switch_to_dmzhostPage(self.driver.current_url)

        # 前提条件：dmz开关关闭
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.Statu))
        )
        if self.driver.find_element_by_xpath(DmzHostLocators.Statu).get_attribute('class') != "box":
            print("【备注】该用例无法验证，原因：DMZ状态开关未关闭")
            assert False
        # 还需检验dmz设置为多少吗？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？

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
    def test_c_23(self):
        """【检验】用例-2656 : 关闭DMZ主机后，外网访问WAN口的TCP报文，匹配到路由器已建立的连接，会被直接转给对应主机(该主机不为DMZ主机)"""
        self.switch_to_dmzhostPage(self.driver.current_url)

        # 前提条件：dmz开关关闭
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.Statu))
        )
        if self.driver.find_element_by_xpath(DmzHostLocators.Statu).get_attribute('class') != "box":
            print("【备注】该用例无法验证，原因：DMZ状态开关未关闭")
            assert False
        # 还需检验dmz设置为多少吗？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？

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
    def test_d_24(self):
        """【检验】用例-2657 : 关闭DMZ主机后，外网访问WAN口的UDP报文，匹配到路由器已建立的连接，会被直接转给对应主机(该主机不为DMZ主机)"""
        self.switch_to_dmzhostPage(self.driver.current_url)

        # 前提条件：dmz开关关闭
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.Statu))
        )
        if self.driver.find_element_by_xpath(DmzHostLocators.Statu).get_attribute('class') != "box":
            print("【备注】该用例无法验证，原因：DMZ状态开关未关闭")
            assert False
        # 还需检验dmz设置为多少吗？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？

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
    def test_e_25(self):
        """【检验】用例-2658 : 关闭DMZ主机后，外网访问WAN口的ICMP报文，匹配到路由器已建立的连接，会被直接转给对应主机(该主机不为DMZ主机)"""
        self.switch_to_dmzhostPage(self.driver.current_url)

        # 前提条件：dmz开关关闭
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.Statu))
        )
        if self.driver.find_element_by_xpath(DmzHostLocators.Statu).get_attribute('class') != "box":
            print("【备注】该用例无法验证，原因：DMZ状态开关未关闭")
            assert False
        # 还需检验dmz设置为多少吗？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？

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
    def test_f_26(self):
        """【检验】用例-2670 : 关闭DMZ主机后，内网访问WAN口的TCP报文，匹配到路由器已建立的连接，会被直接转给对应主机(该主机不为DMZ主机)"""
        self.switch_to_dmzhostPage(self.driver.current_url)

        # 前提条件：dmz开关关闭
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.Statu))
        )
        if self.driver.find_element_by_xpath(DmzHostLocators.Statu).get_attribute('class') != "box":
            print("【备注】该用例无法验证，原因：DMZ状态开关未关闭")
            assert False
        # 还需检验dmz设置为多少吗？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？

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
    def test_g_27(self):
        """【检验】用例-2671 : 关闭DMZ主机后，内网访问WAN口的UDP报文，匹配到路由器已建立的连接，会被直接转给对应主机(该主机不为DMZ主机)"""
        self.switch_to_dmzhostPage(self.driver.current_url)

        # 前提条件：dmz开关关闭
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.Statu))
        )
        if self.driver.find_element_by_xpath(DmzHostLocators.Statu).get_attribute('class') != "box":
            print("【备注】该用例无法验证，原因：DMZ状态开关未关闭")
            assert False
        # 还需检验dmz设置为多少吗？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？

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
    def test_h_28(self):
        """【检验】用例-2672 : 关闭DMZ主机后，内网访问WAN口的ICMP报文，匹配到路由器已建立的连接，会被直接转给对应主机(该主机不为DMZ主机)"""
        self.switch_to_dmzhostPage(self.driver.current_url)

        # 前提条件：dmz开关关闭
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, DmzHostLocators.Statu))
        )
        if self.driver.find_element_by_xpath(DmzHostLocators.Statu).get_attribute('class') != "box":
            print("【备注】该用例无法验证，原因：DMZ状态开关未关闭")
            assert False
        # 还需检验dmz设置为多少吗？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？

        # 前提检验完成，开始检验用例
        time.sleep(5)  # 是否需要等待时间，待配置生效？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        Result = 1  # ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
        if Result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False



