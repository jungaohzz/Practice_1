#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun

import unittest
import time
from selenium import webdriver
from .. test_base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from rweb import const

from rweb.path.common import CommonLocators
from rweb.path.devices import DevicesLocators
from rweb.path.limitRate import LimitRateLocators

from .rate_limit_testcase import Test_rate_limit




class LimitRate(Base):

    def setUp(self):
        super(LimitRate, self).setUp()
        # 鼠标移动到切换“我的WiFi”按钮上
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_MyWifi))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_MyWifi)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 接入设备
        WebDriverWait(self.driver, const.MEDIUM_WAIT+10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Devices))
        )
        time.sleep(1)
        self.driver.find_element_by_xpath(CommonLocators.Devices).click()

        self.driver.refresh()
        # 点击主网-设置
        Set = DevicesLocators.Set.format(num=1)
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, Set))
        ).click()
        # 切换到限速页
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Page_RateLimit))
        ).click()




    #
    #
    # #@unittest.skip("跳过")
    # def test_A_limitRate_onlyLimitUpload(self):
    #     """操作步骤：只限制上行，并开启开关"""
    #     # 上行：400
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
    #     ).clear()
    #     self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(400)
    #     # 下行：清空
    #     # 模拟鼠标双击
    #     inputBox = self.driver.find_element_by_xpath(LimitRateLocators.Download)
    #     action_chains = ActionChains(self.driver)
    #     action_chains.double_click(inputBox).perform()
    #     # 模拟键盘删除键
    #     self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(Keys.BACK_SPACE)
    #     # 保存
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
    #     ).click()
    #     # 断言:toast提示：成功
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
    #     )
    #     assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
    #
    #     self.driver.refresh()
    #
    #     # 断言:判断上下行是否设置正确
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Upload))
    #     )
    #     Upload_Value = self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value")
    #     assert Upload_Value == "400", Upload_Value
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
    #     )
    #     Download_Value = self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value")
    #     assert Download_Value == "", Download_Value
    #
    #     # 如果状态为关闭时，才进行if的启用操作
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     if Statu_class == "box":
    #         # 启用
    #         WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #             EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Statu))
    #         ).click()
    #         # 保存
    #         WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #             EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
    #         ).click()
    #         # 断言:toast提示：成功
    #         WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #             EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
    #         )
    #         assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
    #
    #
    #
    #
    #
    #
    # #@unittest.skip("跳过")
    # def test_B_limitRate_1(self):
    #     """【检验】用例-1599:限速：只限制了上行流量，下行流量不受限制（TCP连接）"""
    #     # 前提条件：上行：400，下行：空，且开关均为开启
    #     # 断言:判断上下行是否设置正确
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Upload))
    #     )
    #     Upload_Value = self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value")
    #     if Upload_Value != "400":
    #         print("【备注】该用例无法验证，原因：上行设置的值不为400")
    #         assert False
    #
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
    #     )
    #     Download_Value = self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value")
    #     if Download_Value != "":
    #         print("【备注】该用例无法验证，原因：下行设置的值不为空")
    #         assert False
    #
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
    #     )
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     if Statu_class != "box checked":
    #         print("【备注】该用例无法验证，原因：限速开关的状态为关闭")
    #         assert False
    #
    #     # 前提已完成，开始检验用例
    #     Result = Test_rate_limit.test_rate_limit_1()
    #     print("<<<<")
    #     print(Result)
    #     print(">>>>")
    #
    #     """
    #     备注：
    #     1、是否是将上行设置成100兆，需要修改前提判断？
    #     2、在配置中：tcp_wired_servertoclient = "iperf -B 192.168.127.201 -c 10.70.100.182 -R -b 100M -t 3"，即如何将10.70.100.182设置为：iperf -s
    #     3、未断言
    #     """
    #
    #
    #
    #
    #
    # #@unittest.skip("跳过")
    # def test_C_limitRate_onlyLimitDownload(self):
    #     """操作步骤：只限制下行，并开启开关"""
    #     # 上行：清空
    #     # 模拟鼠标双击
    #     inputBox = self.driver.find_element_by_xpath(LimitRateLocators.Upload)
    #     action_chains = ActionChains(self.driver)
    #     action_chains.double_click(inputBox).perform()
    #     # 模拟键盘删除键
    #     self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(Keys.BACK_SPACE)
    #     # 下行：800
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
    #     ).clear()
    #     self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(800)
    #
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
    #     ).click()
    #     # 断言:toast提示：成功
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
    #     )
    #     assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
    #
    #     self.driver.refresh()
    #
    #     # 断言:判断上下行是否设置正确
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Upload))
    #     )
    #     Upload_Value = self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value")
    #     assert Upload_Value == "", Upload_Value
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
    #     )
    #     Download_Value = self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value")
    #     assert Download_Value == "800", Download_Value
    #
    #     # 如果状态为关闭时，才进行if的启用操作
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     if Statu_class == "box":
    #         # 启用
    #         WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #             EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Statu))
    #         ).click()
    #         # 保存
    #         WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #             EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
    #         ).click()
    #         # 断言:toast提示：成功
    #         WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #             EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
    #         )
    #         assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
    #
    #
    #
    #
    #
    #
    #
    # #@unittest.skip("跳过")
    # def test_D_limitRate_2(self):
    #     """【检验】用例-1600:限速：只限制了下行流量，上行流量不受限制（TCP连接）"""
    #
    #     # 前提条件：上行：空，下行：800，且开关均为开启
    #     # 断言:判断上下行是否设置正确
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Upload))
    #     )
    #     Upload_Value = self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value")
    #     if Upload_Value != "":
    #         print("【备注】该用例无法验证，原因：上行设置的值不为空")
    #         assert False
    #
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
    #     )
    #     Download_Value = self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value")
    #     if Download_Value != "800":
    #         print("【备注】该用例无法验证，原因：下行设置的值不为800")
    #         assert False
    #
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
    #     )
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     if Statu_class != "box checked":
    #         print("【备注】该用例无法验证，原因：限速开关的状态为关闭")
    #         assert False
    #
    #     # 前提已完成，开始检验用例
    #     Result = Test_rate_limit.test_rate_limit_2()
    #     print("<<<<")
    #     print(Result)
    #     print(">>>>")
    #     """
    #     备注：
    #     1、是否是将下行设置成100兆，需要修改前提判断？
    #     2、在配置中：tcp_wired_servertoclient = "iperf -B 192.168.127.201 -c 10.70.100.182 -R -b 100M -t 3"，即如何将10.70.100.182设置为：iperf -s
    #     3、未断言
    #     """
    #
    #
    #
    #
    #
    #
    #
    # #@unittest.skip("跳过")
    # def test_E_limitRate_limitAll(self):
    #     """操作步骤：同时限制上下行"""
    #     # 上行：400
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
    #     ).clear()
    #     self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(400)
    #     # 下行：800
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
    #     ).clear()
    #     self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(800)
    #
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
    #     ).click()
    #     # 断言:toast提示：成功
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
    #     )
    #     assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
    #
    #     self.driver.refresh()
    #
    #     # 断言:判断上下行是否设置正确
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Upload))
    #     )
    #     Upload_Value = self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value")
    #     assert Upload_Value == "400", Upload_Value
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
    #     )
    #     Download_Value = self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value")
    #     assert Download_Value == "800", Download_Value
    #
    #     # 如果状态为关闭时，才进行if的启用操作
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     if Statu_class == "box":
    #         # 启用
    #         WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #             EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Statu))
    #         ).click()
    #         # 保存
    #         WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #             EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
    #         ).click()
    #         # 断言:toast提示：成功
    #         WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #             EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
    #         )
    #         assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
    #
    #
    #
    #
    #
    # #@unittest.skip("跳过")
    # def test_F_limitRate_3(self):
    #     """【检验】用例-1601:开启限速功能后，新创建的TCP连接的上行和下行速度被限制"""
    #
    #     # 前提条件：上行：400，下行：800，且开关均为开启
    #     # 断言:判断上下行是否设置正确
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Upload))
    #     )
    #     Upload_Value = self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value")
    #     if Upload_Value != "400":
    #         print("【备注】该用例无法验证，原因：上行设置的值不为400")
    #         assert False
    #
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
    #     )
    #     Download_Value = self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value")
    #     if Download_Value != "800":
    #         print("【备注】该用例无法验证，原因：下行设置的值不为800")
    #         assert False
    #
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
    #     )
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     if Statu_class != "box checked":
    #         print("【备注】该用例无法验证，原因：限速开关的状态为关闭")
    #         assert False
    #
    #     # 前提已完成，开始检验用例
    #     Result = Test_rate_limit.test_rate_limit_3()
    #     print("<<<<")
    #     print(Result)
    #     print(">>>>")
    #     """
    #     备注：
    #     1、是否是将上下行设置成400、800？
    #     2、在配置中：tcp_wired_servertoclient = "iperf -B 192.168.127.201 -c 10.70.100.182 -R -b 100M -t 3"，即如何将10.70.100.182设置为：iperf -s
    #     3、未断言
    #     """
    #
    #
    #
    #
    # #@unittest.skip("跳过")
    # def test_G_limitRate_4(self):
    #     """【检验】用例-1603:开启限速功能后，新创建的UDP连接的上行和下行速度被限制"""
    #
    #     # 前提条件：上行：400，下行：800，且开关均为开启
    #     # 断言:判断上下行是否设置正确
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Upload))
    #     )
    #     Upload_Value = self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value")
    #     if Upload_Value != "400":
    #         print("【备注】该用例无法验证，原因：上行设置的值不为400")
    #         assert False
    #
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
    #     )
    #     Download_Value = self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value")
    #     if Download_Value != "800":
    #         print("【备注】该用例无法验证，原因：下行设置的值不为800")
    #         assert False
    #
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
    #     )
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     if Statu_class != "box checked":
    #         print("【备注】该用例无法验证，原因：限速开关的状态为关闭")
    #         assert False
    #
    #     # 前提已完成，开始检验用例
    #     Result = Test_rate_limit.test_rate_limit_4()
    #     print("<<<<")
    #     print("@@@@@@@@@@@@")
    #     print(Result)
    #     print(">>>>")
    #     """
    #     备注：
    #     1、是否是将上下行设置成400、800？
    #     2、在配置中：tcp_wired_servertoclient = "iperf -B 192.168.127.201 -c 10.70.100.182 -R -b 100M -t 3"，即如何将10.70.100.182设置为：iperf -s
    #     3、为什么一直在执行命令：“iperf -B 192.168.127.201 -c 10.70.100.182 -R -b 100M -t 3”却不主动暂停？所以该用例一直执行却不执行完毕
    #     3、未断言
    #     """
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # #@unittest.skip("跳过")
    # def test_H_limitRate_edit_statu_off(self):
    #     """操作步骤：将限速开关关闭"""
    #     # 状态理应为启用，如果为启用状态才进行if的关闭操作
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
    #     )
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     if Statu_class == "box checked":
    #         # 关闭
    #         self.driver.find_element_by_xpath(LimitRateLocators.Statu).click()
    #         # 保存
    #         WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #             EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
    #         ).click()
    #         # 断言:toast提示：成功
    #         WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #             EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
    #         )
    #         assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
    #
    #
    #
    #
    #
    #
    #
    #
    # #@unittest.skip("跳过")
    # def test_I_limitRate_5(self):
    #     """【检验】用例-979:关闭限速后，上行和下行速度不被限制"""
    #
    #     # 前提条件：上行：400，下行：800，但开关为关闭
    #     # 断言:判断上下行是否设置正确
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Upload))
    #     )
    #     Upload_Value = self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value")
    #     if Upload_Value != "400":
    #         print("【备注】该用例无法验证，原因：上行设置的值不为400")
    #         assert False
    #
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
    #     )
    #     Download_Value = self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value")
    #     if Download_Value != "800":
    #         print("【备注】该用例无法验证，原因：下行设置的值不为800")
    #         assert False
    #
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
    #     )
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     if Statu_class != "box":
    #         print("【备注】该用例无法验证，原因：限速开关的状态为开启")
    #         assert False
    #
    #     # 前提已完成，开始检验用例
    #     Result = Test_rate_limit.test_rate_limit_5()
    #     print("<<<<")
    #     print(Result)
    #     print(">>>>")
    #     """
    #     备注：
    #     1、是否是将上下行设置成400、800？
    #     2、在配置中：tcp_wired_servertoclient = "iperf -B 192.168.127.201 -c 10.70.100.182 -R -b 100M -t 3"，即如何将10.70.100.182设置为：iperf -s
    #     3、为什么一直在执行命令：“iperf -B 192.168.127.201 -c 10.70.100.182 -R -b 100M -t 3”却不主动暂停？所以该用例一直执行却不执行完毕
    #     3、未断言
    #     """
    #
    #
    #
    #
    #
    #
    #
    # #@unittest.skip("跳过")
    # def test_J_limitRate_edit_statu_on(self):
    #     """操作步骤：将设备A的限速开关开启"""
    #     # 状态理应为关闭，如果为关闭状态才进行if的启用操作
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
    #     )
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     if Statu_class == "box":
    #         # 启用
    #         self.driver.find_element_by_xpath(LimitRateLocators.Statu).click()
    #         # 保存
    #         WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #             EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
    #         ).click()
    #         # 断言:toast提示：成功
    #         WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #             EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
    #         )
    #         assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # #@unittest.skip("跳过")
    # def test_K_limitRate_6(self):
    #     """【检验】用例-981：对单个设备限速后，不影响其他设备 (对设备A限速成功后，设备B不会被限速)"""
    #
    #     # 前提条件：上行：400，下行：800，但开关为开启
    #     # 断言:判断上下行是否设置正确
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Upload))
    #     )
    #     Upload_Value = self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value")
    #     if Upload_Value != "400":
    #         print("【备注】该用例无法验证，原因：上行设置的值不为400")
    #         assert False
    #
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
    #     )
    #     Download_Value = self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value")
    #     if Download_Value != "800":
    #         print("【备注】该用例无法验证，原因：下行设置的值不为800")
    #         assert False
    #
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
    #     )
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     if Statu_class != "box checked":
    #         print("【备注】该用例无法验证，原因：限速开关的状态为关闭")
    #         assert False
    #
    #     # 前提已完成，开始检验用例
    #     Result = Test_rate_limit.test_rate_limit_6()
    #     print("<<<<")
    #     print(Result)
    #     print(">>>>")
    #     """
    #     备注：
    #     1、是否是将上下行设置成400、800？
    #     2、在配置中：tcp_wired_servertoclient = "iperf -B 192.168.127.201 -c 10.70.100.182 -R -b 100M -t 3"，即如何将10.70.100.182设置为：iperf -s
    #     3、为什么一直在执行命令：“iperf -B 192.168.127.201 -c 10.70.100.182 -R -b 100M -t 3”却不主动暂停？所以该用例一直执行却不执行完毕
    #     3、未断言
    #     """
    #
    #
    #
    #
    #
    #
    # #@unittest.skip("跳过")
    # def test_L_limitRate_edits(self):
    #     """操作步骤：将设备A限速、设备B均限速"""
    #     # 设备A（有线）
    #     # 上下行的值（400、800）与开关状态（开启）理应都是配置好的，但还是要检验一遍
    #     flag = False    #用于标记是否需要修改，False为不需要修改，True需要修改
    #     # 上行：400
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
    #     )
    #     Upload_Value = self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value")
    #     if Upload_Value != "400":
    #         self.driver.find_element_by_xpath(LimitRateLocators.Upload).clear()
    #         self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(400)
    #         flag = True
    #     # 下行：800
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
    #     )
    #     Download_Value = self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value")
    #     if Download_Value != "800":
    #         self.driver.find_element_by_xpath(LimitRateLocators.Download).clear()
    #         self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(800)
    #         flag = True
    #     # 开关状态
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Statu))
    #     )
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     if Statu_class != "box checked":
    #         self.driver.find_element_by_xpath(LimitRateLocators.Statu).click()
    #         flag = True
    #
    #     if flag == True:    #即需要修改，则需要点击 保存 按钮
    #         WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #             EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
    #         ).click()
    #         # 断言:toast提示：成功
    #         WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #             EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
    #         )
    #         assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
    #
    #     # 设备B（即无线5G）
    #     # 进入到设备B的限速页
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_MyWifi))
    #     )
    #     mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_MyWifi)
    #     ActionChains(self.driver).move_to_element(mouse).perform()
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT + 10).until(
    #         EC.element_to_be_clickable((By.XPATH, CommonLocators.Devices))
    #     )
    #     time.sleep(1)
    #     self.driver.find_element_by_xpath(CommonLocators.Devices).click()
    #     self.driver.refresh()
    #     Set = DevicesLocators.Set.format(num=2)
    #     WebDriverWait(self.driver, 15).until(
    #         EC.element_to_be_clickable((By.XPATH, Set))
    #     ).click()
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Page_RateLimit))
    #     ).click()
    #     # 新增限速
    #     # 上行：400
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
    #     ).clear()
    #     self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(400)
    #     # 下行：800
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
    #     ).clear()
    #     self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(800)
    #     # 状态为关闭时，才进行if的启用操作
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     if Statu_class == "box":
    #         # 启用
    #         WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #             EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Statu))
    #         ).click()
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
    #     ).click()
    #     # 断言:toast提示：成功
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
    #     )
    #     assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # #@unittest.skip("跳过")
    # def test_M_limitRate_7(self):
    #     """【检验】用例-1611：多个设备同时限速可成功（设备A、B都设置了限速，保存成功后A、B都能限速成功）"""
    #
    #     # 前提条件：设备A和设备B的参数值均一致：上行400，下行800，开关开启
    #     # 判断设备A
    #     # 断言:判断上下行是否设置正确
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Upload))
    #     )
    #     Upload_Value = self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value")
    #     if Upload_Value != "400":
    #         print("【备注】该用例无法验证，原因：设备A的上行值不为400")
    #         assert False
    #
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
    #     )
    #     Download_Value = self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value")
    #     if Download_Value != "800":
    #         print("【备注】该用例无法验证，原因：设备A的下行值不为800")
    #         assert False
    #
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
    #     )
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     if Statu_class != "box checked":
    #         print("【备注】该用例无法验证，原因：设备A的限速开关为关闭")
    #         assert False
    #
    #     # 判断设备B
    #     # 进入到设备B的限速页
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_MyWifi))
    #     )
    #     mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_MyWifi)
    #     ActionChains(self.driver).move_to_element(mouse).perform()
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT + 10).until(
    #         EC.element_to_be_clickable((By.XPATH, CommonLocators.Devices))
    #     )
    #     time.sleep(1)
    #     self.driver.find_element_by_xpath(CommonLocators.Devices).click()
    #     self.driver.refresh()
    #     Set = DevicesLocators.Set.format(num=2)
    #     WebDriverWait(self.driver, 15).until(
    #         EC.element_to_be_clickable((By.XPATH, Set))
    #     ).click()
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Page_RateLimit))
    #     ).click()
    #     # 断言:判断上下行是否设置正确
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Upload))
    #     )
    #     Upload_Value = self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value")
    #     if Upload_Value != "400":
    #         print("【备注】该用例无法验证，原因：设备B的上行值不为400")
    #         assert False
    #
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
    #     )
    #     Download_Value = self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value")
    #     if Download_Value != "800":
    #         print("【备注】该用例无法验证，原因：设备B的下行值不为800")
    #         assert False
    #
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
    #     )
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     if Statu_class != "box checked":
    #         print("【备注】该用例无法验证，原因：设备B的限速开关为关闭")
    #         assert False
    #
    #     # 前提已完成，开始检验用例
    #     Result = Test_rate_limit.test_rate_limit_7()
    #     print("<<<<")
    #     print(Result)
    #     print(">>>>")
    #     """
    #     备注：
    #     1、是否是将上下行设置成400、800？
    #     2、在配置中：tcp_wired_servertoclient = "iperf -B 192.168.127.201 -c 10.70.100.182 -R -b 100M -t 3"，即如何将10.70.100.182设置为：iperf -s
    #     3、为什么一直在执行命令：“iperf -B 192.168.127.201 -c 10.70.100.182 -R -b 100M -t 3”却不主动暂停？所以该用例一直执行却不执行完毕
    #     3、未断言
    #     """
    #
    #
    #
    #
    #
    #
    #
    # #@unittest.skip("跳过")
    # def test_N_limitRate_edits_5G(self):
    #     """操作步骤：将设备B限速"""
    #     # 上下行的值（400、800）与开关状态（开启）理应都是配置好的，但还是要检验一遍
    #     # 进入到设备B的限速页
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_MyWifi))
    #     )
    #     mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_MyWifi)
    #     ActionChains(self.driver).move_to_element(mouse).perform()
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT + 10).until(
    #         EC.element_to_be_clickable((By.XPATH, CommonLocators.Devices))
    #     )
    #     time.sleep(1)
    #     self.driver.find_element_by_xpath(CommonLocators.Devices).click()
    #     self.driver.refresh()
    #     Set = DevicesLocators.Set.format(num=2)
    #     WebDriverWait(self.driver, 15).until(
    #         EC.element_to_be_clickable((By.XPATH, Set))
    #     ).click()
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Page_RateLimit))
    #     ).click()
    #     # 检查值是否正确，不正确则修改
    #     flag = False    #用于标记是否需要修改，False为不需要修改，True需要修改
    #     # 上行：400
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
    #     )
    #     Upload_Value = self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value")
    #     if Upload_Value != "400":
    #         self.driver.find_element_by_xpath(LimitRateLocators.Upload).clear()
    #         self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(400)
    #         flag = True
    #     # 下行：800
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
    #     )
    #     Download_Value = self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value")
    #     if Download_Value != "800":
    #         self.driver.find_element_by_xpath(LimitRateLocators.Download).clear()
    #         self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(800)
    #         flag = True
    #     # 开关状态
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Statu))
    #     )
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     if Statu_class != "box checked":
    #         self.driver.find_element_by_xpath(LimitRateLocators.Statu).click()
    #         flag = True
    #
    #     if flag == True:    #即需要修改，则需要点击 保存 按钮
    #         WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #             EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
    #         ).click()
    #         # 断言:toast提示：成功
    #         WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #             EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
    #         )
    #         assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
    #
    #
    #
    #
    #
    #
    #
    # #@unittest.skip("跳过")
    # def test_O_limitRate_8(self):
    #     """【检验】用例-1612:无线接入，限速功能可生效"""
    #
    #     # 前提条件：设备B中：上行400，下行800，开关开启
    #     # 进入到设备B的限速页
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_MyWifi))
    #     )
    #     mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_MyWifi)
    #     ActionChains(self.driver).move_to_element(mouse).perform()
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT + 10).until(
    #         EC.element_to_be_clickable((By.XPATH, CommonLocators.Devices))
    #     )
    #     time.sleep(1)
    #     self.driver.find_element_by_xpath(CommonLocators.Devices).click()
    #     self.driver.refresh()
    #     Set = DevicesLocators.Set.format(num=2)
    #     WebDriverWait(self.driver, 15).until(
    #         EC.element_to_be_clickable((By.XPATH, Set))
    #     ).click()
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Page_RateLimit))
    #     ).click()
    #     # 断言:判断上下行是否设置正确
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Upload))
    #     )
    #     Upload_Value = self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value")
    #     if Upload_Value != "400":
    #         print("【备注】该用例无法验证，原因：设备B的上行值不为400")
    #         assert False
    #
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
    #     )
    #     Download_Value = self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value")
    #     if Download_Value != "800":
    #         print("【备注】该用例无法验证，原因：设备B的下行值不为800")
    #         assert False
    #
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
    #     )
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     if Statu_class != "box checked":
    #         print("【备注】该用例无法验证，原因：设备B的限速开关为关闭")
    #         assert False
    #
    #     # 前提已完成，开始检验用例
    #     Result = Test_rate_limit.test_rate_limit_8()
    #     print("<<<<")
    #     print(Result)
    #     print(">>>>")
    #     """
    #     备注：
    #     1、是否是将上下行设置成400、800？
    #     2、在配置中：tcp_wired_servertoclient = "iperf -B 192.168.127.201 -c 10.70.100.182 -R -b 100M -t 3"，即如何将10.70.100.182设置为：iperf -s
    #     3、为什么一直在执行命令：“iperf -B 192.168.127.201 -c 10.70.100.182 -R -b 100M -t 3”却不主动暂停？所以该用例一直执行却不执行完毕
    #     3、未断言
    #     """
    #
    #
    #
    #
    #
    #
    # #@unittest.skip("跳过")
    # def test_P_limitRate_edits_wired(self):
    #     """操作步骤：将设备A限速"""
    #     # 上下行的值（400、800）与开关状态（开启）理应都是配置好的，但还是要检验一遍
    #     # 检查值是否正确，不正确则修改
    #     flag = False    #用于标记是否需要修改，False为不需要修改，True需要修改
    #     # 上行：400
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
    #     )
    #     Upload_Value = self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value")
    #     if Upload_Value != "400":
    #         self.driver.find_element_by_xpath(LimitRateLocators.Upload).clear()
    #         self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(400)
    #         flag = True
    #     # 下行：800
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
    #     )
    #     Download_Value = self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value")
    #     if Download_Value != "800":
    #         self.driver.find_element_by_xpath(LimitRateLocators.Download).clear()
    #         self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(800)
    #         flag = True
    #     # 开关状态
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Statu))
    #     )
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     if Statu_class != "box checked":
    #         self.driver.find_element_by_xpath(LimitRateLocators.Statu).click()
    #         flag = True
    #
    #     if flag == True:    #即需要修改，则需要点击 保存 按钮
    #         WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #             EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
    #         ).click()
    #         # 断言:toast提示：成功
    #         WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #             EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
    #         )
    #         assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
    #
    #
    #
    #
    #
    #
    #
    # #@unittest.skip("跳过")
    # def test_Q_limitRate_9(self):
    #     """【检验】用例-1613:有线接入，限速功能可生效"""
    #
    #     # 前提条件：设备A中：上行400，下行800，开关开启
    #     # 断言:判断上下行是否设置正确
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Upload))
    #     )
    #     Upload_Value = self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value")
    #     if Upload_Value != "400":
    #         print("【备注】该用例无法验证，原因：设备A的上行值不为400")
    #         assert False
    #
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
    #     )
    #     Download_Value = self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value")
    #     if Download_Value != "800":
    #         print("【备注】该用例无法验证，原因：设备A的下行值不为800")
    #         assert False
    #
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
    #     )
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     if Statu_class != "box checked":
    #         print("【备注】该用例无法验证，原因：设备A的限速开关为关闭")
    #         assert False
    #
    #     # 前提已完成，开始检验用例
    #     Result = Test_rate_limit.test_rate_limit_9()
    #     print("<<<<")
    #     print(Result)
    #     print(">>>>")
    #     """
    #     备注：
    #     1、是否是将上下行设置成400、800？
    #     2、在配置中：tcp_wired_servertoclient = "iperf -B 192.168.127.201 -c 10.70.100.182 -R -b 100M -t 3"，即如何将10.70.100.182设置为：iperf -s
    #     3、为什么一直在执行命令：“iperf -B 192.168.127.201 -c 10.70.100.182 -R -b 100M -t 3”却不主动暂停？所以该用例一直执行却不执行完毕
    #     3、未断言
    #     """






    #@unittest.skip("跳过")
    def test_Q_limitRate_turn_statu_off(self):
        """操作步骤：将设备A、B的开关均关闭，回到初始状态"""
        # 设备A
        # 开关状态理应为启用，如果为启用状态才进行if的关闭操作
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
        )
        Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
        if Statu_class == "box checked":
            # 关闭
            self.driver.find_element_by_xpath(LimitRateLocators.Statu).click()
            # 保存
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
            ).click()
            # 断言:toast提示：成功
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
            )
            Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
            assert Statu_class == "box", Statu_class

        # 设备A
        # 进入到设备B的限速页
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_MyWifi))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_MyWifi)
        ActionChains(self.driver).move_to_element(mouse).perform()
        WebDriverWait(self.driver, const.MEDIUM_WAIT + 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Devices))
        )
        time.sleep(1)
        self.driver.find_element_by_xpath(CommonLocators.Devices).click()
        self.driver.refresh()
        Set = DevicesLocators.Set.format(num=2)
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, Set))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Page_RateLimit))
        ).click()
        # 开关状态理应为启用，如果为启用状态才进行if的关闭操作
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
        )
        Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
        if Statu_class == "box checked":
            # 关闭
            self.driver.find_element_by_xpath(LimitRateLocators.Statu).click()
            # 保存
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
            ).click()
            # 断言:toast提示：成功
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
            )
            Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
            assert Statu_class == "box", Statu_class


