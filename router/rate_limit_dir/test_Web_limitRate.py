#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun

import unittest
import time
from selenium import webdriver
from ..base import Base
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
from .rate_limit_conf import *


class LimitRate(Base):
    # 以下定义2个变量：有线和5G的限速页url变量。目的：用于判断当前页是在有线的限速页，还是5G的限速页
    url_wired_limitRatePage = ""
    url_5g_limitRatePage = ""
    url_24g_limitRatePage = ""

    def switch_to_limitTimePage_wired_5g_24g(self, Type, Current_Url):  # 切换到 有线/5G/2.4G 的限速页
        self.driver.refresh()
        time.sleep(1)
        # 根据不同类型（有线/5G），定义变量：目的url
        if Type == "Wired":
            Purpose_Url = LimitRate.url_wired_limitRatePage
        elif Type == "5G":
            Purpose_Url = LimitRate.url_5g_limitRatePage
        else:
            Purpose_Url = LimitRate.url_24g_limitRatePage
        # 判断当前的url是否是目的url
        while Purpose_Url != Current_Url:
            # 鼠标移动到切换“我的WiFi”按钮上
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_MyWifi))
            )
            mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_MyWifi)
            ActionChains(self.driver).move_to_element(mouse).perform()
            # 点击 接入设备
            WebDriverWait(self.driver, const.MEDIUM_WAIT + 10).until(
                EC.element_to_be_clickable((By.XPATH, CommonLocators.Devices))
            )
            time.sleep(1)
            self.driver.find_element_by_xpath(CommonLocators.Devices).click()
            self.driver.refresh()
            # 点击主网-设置
            if Type == "Wired":
                Set = DevicesLocators.Set.format(num=1)
            elif Type == "5G":
                Set = DevicesLocators.Set.format(num=2)
            elif Type == "2.4G":
                Set = DevicesLocators.Set.format(num=3)
            WebDriverWait(self.driver, const.MEDIUM_WAIT + 5).until(
                EC.element_to_be_clickable((By.XPATH, Set))
            ).click()
            # 切换到限速页
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Page_RateLimit))
            ).click()
            Current_Url = self.driver.current_url

    # @unittest.skip("跳过")
    def test_A_get_url(self):
        """操作步骤：获取有线的限速url、5G的限速url"""
        i = 1
        while i <= 2:
            # 鼠标移动到切换“我的WiFi”按钮上
            time.sleep(2)
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_MyWifi))
            )
            mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_MyWifi)
            ActionChains(self.driver).move_to_element(mouse).perform()
            # 点击 接入设备
            WebDriverWait(self.driver, const.MEDIUM_WAIT + 10).until(
                EC.element_to_be_clickable((By.XPATH, CommonLocators.Devices))
            )
            time.sleep(1)
            self.driver.find_element_by_xpath(CommonLocators.Devices).click()
            self.driver.refresh()
            # 点击主网-设置
            Set = DevicesLocators.Set.format(num=i)
            WebDriverWait(self.driver, const.MEDIUM_WAIT + 5).until(
                EC.element_to_be_clickable((By.XPATH, Set))
            ).click()
            # 切换到限速页
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Page_RateLimit))
            ).click()
            if i == 1:
                LimitRate.url_wired_limitRatePage = self.driver.current_url  # 获取有线的限速url
            else:
                LimitRate.url_5g_limitRatePage = self.driver.current_url  # 获取5G的限速url
            i += 1

    # #@unittest.skip("跳过")
    # def test_B_limitRate_onlyLimitUpload(self):
    #     """操作步骤：只限制上行，并开启开关"""
    #     self.switch_to_limitTimePage_wired_5g_24g("Wired", self.driver.current_url)
    #     # 上行：500
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
    #     ).clear()
    #     self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(rata_upload_1)
    #     # 下行：清空
    #     # 模拟鼠标双击
    #     inputBox = self.driver.find_element_by_xpath(LimitRateLocators.Download)
    #     action_chains = ActionChains(self.driver)
    #     action_chains.double_click(inputBox).perform()
    #     # 模拟键盘删除键
    #     self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(Keys.BACK_SPACE)
    #     # 默认状态为关闭，为关闭时才进行if的启用操作
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     if Statu_class == "box":
    #         # 启用
    #         WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #             EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Statu))
    #         ).click()
    #     # 保存
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
    #     ).click()
    #     # 断言:toast提示：成功
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
    #     )
    #     assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
    #     self.driver.refresh()
    #
    #     # 断言:判断上下行是否设置正确
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Upload))
    #     )
    #     Upload_Value = int(self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value"))
    #     assert Upload_Value == rata_upload_1, Upload_Value
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
    #     )
    #     Download_Value = self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value")
    #     assert Download_Value == "", Download_Value
    #     # 断言：开关是否开启
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
    #     )
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     assert Statu_class == "box checked", Statu_class
    #
    #
    #
    #
    #
    #
    #
    #
    # #@unittest.skip("跳过")
    # def test_C_limitRate_1(self):
    #     """【检验】用例-1599:限速：只限制了上行流量，下行流量不受限制（TCP连接）"""
    #     self.switch_to_limitTimePage_wired_5g_24g("Wired", self.driver.current_url)
    #     # 前提条件：上行：500，下行：空，且开关均为开启
    #     # 断言:判断上下行是否设置正确
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Upload))
    #     )
    #     Upload_Value = int(self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value"))
    #     if Upload_Value != rata_upload_1:
    #         print("【备注】该用例无法验证，原因：上行设置的值不为500")
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
    #     result = Test_rate_limit.test_rate_limit_1()
    #     if result == 1:
    #         print("【成功】")
    #         assert True
    #     else:
    #         print("【失败】")
    #         assert False
    #
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
    # def test_D_limitRate_onlyLimitDownload(self):
    #     """操作步骤：只限制下行，并开启开关"""
    #     self.switch_to_limitTimePage_wired_5g_24g("Wired", self.driver.current_url)
    #     # 上行：清空
    #     # 模拟鼠标双击
    #     inputBox = self.driver.find_element_by_xpath(LimitRateLocators.Upload)
    #     action_chains = ActionChains(self.driver)
    #     action_chains.double_click(inputBox).perform()
    #     # 模拟键盘删除键
    #     self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(Keys.BACK_SPACE)
    #     # 下行：500
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
    #     ).clear()
    #     self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(rata_download_1)
    #     # 状态理应为开启，但此处还是判断一下，如果为关闭才进行if的启用操作
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     if Statu_class == "box":
    #         # 启用
    #         WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #             EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Statu))
    #         ).click()
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
    #     assert Upload_Value == "", Upload_Value
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
    #     )
    #     Download_Value = int(self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value"))
    #     assert Download_Value == rata_download_1, Download_Value
    #     # 断言：开关是否开启
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
    #     )
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     assert Statu_class == "box checked", Statu_class
    #
    #
    #
    #
    #
    #
    # #@unittest.skip("跳过")
    # def test_E_limitRate_2(self):
    #     """【检验】用例-1600:限速：只限制了下行流量，上行流量不受限制（TCP连接）"""
    #     self.switch_to_limitTimePage_wired_5g_24g("Wired", self.driver.current_url)
    #     # 前提条件：上行空，下行500，且开关均为开启
    #     # 断言：判断上下行是否设置正确
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
    #     Download_Value = int(self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value"))
    #     if Download_Value != rata_download_1:
    #         print("【备注】该用例无法验证，原因：下行设置的值不为500")
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
    #     result = Test_rate_limit.test_rate_limit_2()
    #     if result == 1:
    #         print("【成功】")
    #         assert True
    #     else:
    #         print("【失败】")
    #         assert False
    #
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
    # def test_F_limitRate_limitAll(self):
    #     """操作步骤：同时限制上下行（上行1000，下行500）"""
    #     self.switch_to_limitTimePage_wired_5g_24g("Wired", self.driver.current_url)
    #     # 上行：1000
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
    #     ).clear()
    #     self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(rata_upload_2)
    #     # 下行：200
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
    #     ).clear()
    #     self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(rata_download_1)
    #     # 状态理应是开启的，但此处还是判断一下，如果为关闭状态才进行if的启用操作
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     if Statu_class == "box":
    #         # 启用
    #         WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #             EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Statu))
    #         ).click()
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
    #     Upload_Value = int(self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value"))
    #     assert Upload_Value == rata_upload_2, Upload_Value
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
    #     )
    #     Download_Value = int(self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value"))
    #     assert Download_Value == rata_download_1, Download_Value
    #     # 断言：开关是否开启
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
    #     )
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     assert Statu_class == "box checked", Statu_class
    #
    #
    #
    #
    #
    #
    #
    #
    # #@unittest.skip("跳过")
    # def test_G_limitRate_3(self):
    #     """【检验】用例-1601:开启限速功能后，新创建的TCP连接的上行和下行速度被限制"""
    #     self.switch_to_limitTimePage_wired_5g_24g("Wired", self.driver.current_url)
    #     # 前提条件：上行：1000，下行：500，且开关均为开启
    #     # 断言:判断上下行是否设置正确
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Upload))
    #     )
    #     Upload_Value = int(self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value"))
    #     if Upload_Value != rata_upload_2:
    #         print("【备注】该用例无法验证，原因：上行设置的值不为1000")
    #         assert False
    #
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
    #     )
    #     Download_Value = int(self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value"))
    #     if Download_Value != rata_download_1:
    #         print("【备注】该用例无法验证，原因：下行设置的值不为500")
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
    #     result = Test_rate_limit.test_rate_limit_3()
    #     if result == 1:
    #         print("【成功】")
    #         assert True
    #     else:
    #         print("【失败】")
    #         assert False
    #
    #
    #
    #
    #
    #
    #
    #
    # # @unittest.skip("跳过")
    # def test_H_limitRate_limitAll(self):
    #     """操作步骤：同时限制上下行（上行500，下行1000）"""
    #     self.switch_to_limitTimePage_wired_5g_24g("Wired", self.driver.current_url)
    #     # 上行：500
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
    #     ).clear()
    #     self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(rata_upload_1)
    #     # 下行：1000
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
    #     ).clear()
    #     self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(rata_download_2)
    #     # 状态理应是开启的，但此处还是判断一下，如果为关闭状态才进行if的启用操作
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     if Statu_class == "box":
    #         # 启用
    #         WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #             EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Statu))
    #         ).click()
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
    #     Upload_Value = int(self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value"))
    #     assert Upload_Value == rata_upload_1, Upload_Value
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
    #     )
    #     Download_Value = int(self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value"))
    #     assert Download_Value == rata_download_2, Download_Value
    #     # 断言：开关是否开启
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
    #     )
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     assert Statu_class == "box checked", Statu_class
    #
    #
    #
    #
    #
    #
    #
    #
    # #@unittest.skip("跳过")
    # def test_I_limitRate_4(self):
    #     """【检验】用例-1603:开启限速功能后，新创建的UDP连接的上行和下行速度被限制"""
    #     self.switch_to_limitTimePage_wired_5g_24g("Wired", self.driver.current_url)
    #     # 前提条件：上行：500，下行：1000，且开关均为开启
    #     # 断言:判断上下行是否设置正确
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Upload))
    #     )
    #     Upload_Value = int(self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value"))
    #     if Upload_Value != rata_upload_1:
    #         print("【备注】该用例无法验证，原因：上行设置的值不为400")
    #         assert False
    #
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
    #     )
    #     Download_Value = int(self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value"))
    #     if Download_Value != rata_download_2:
    #         print("【备注】该用例无法验证，原因：下行设置的值不为1000")
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
    #     result = Test_rate_limit.test_rate_limit_4()
    #     if result == 1:
    #         print("【成功】")
    #         assert True
    #     else:
    #         print("【失败】")
    #         assert False
    #
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
    # def test_J_limitRate_edit_statu_off(self):
    #     """操作步骤：将限速开关关闭"""
    #     self.switch_to_limitTimePage_wired_5g_24g("Wired", self.driver.current_url)
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
    #         self.driver.refresh()
    #         # 断言：开关是否开启
    #         WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #             EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
    #         )
    #         Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #         assert Statu_class == "box", Statu_class
    #
    #
    #
    #

    @unittest.skip("跳过")
    def test_K_limitRate_5(self):
        """【检验】用例-979:关闭限速后，上行和下行速度不被限制"""
        self.switch_to_limitTimePage_wired_5g_24g("Wired", self.driver.current_url)
        # 前提条件：开关为关闭
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
        )
        Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
        if Statu_class != "box":
            print("【备注】该用例无法验证，原因：限速开关的状态为开启")
            assert False

        # 前提已完成，开始检验用例
        result = Test_rate_limit.test_rate_limit_5()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    @unittest.skip("跳过")
    def test_L_limitRate_edit_statu_on(self):
        """操作步骤：将设备A的限速开关开启"""
        self.switch_to_limitTimePage_wired_5g_24g("Wired", self.driver.current_url)
        # 状态理应为关闭，如果为关闭状态才进行if的启用操作
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
        )
        Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
        if Statu_class == "box":
            # 启用
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
            # 断言：开关是否开启
            self.driver.refresh()
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
            )
            Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
            assert Statu_class == "box checked", Statu_class

    # @unittest.skip("跳过")
    def test_M_limitRate_6(self):
        """【检验】用例-981：对单个设备限速后，不影响其他设备 (对设备A限速成功后，设备B不会被限速)"""
        self.switch_to_limitTimePage_wired_5g_24g("Wired", self.driver.current_url)
        # 前提条件：开关为开启
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
        )
        Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
        if Statu_class != "box checked":
            print("【备注】该用例无法验证，原因：设备A限速开关的状态为关闭")
            assert False

        # 前提已完成，开始检验用例
        result = Test_rate_limit.test_rate_limit_6()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    @unittest.skip("跳过")
    def test_N_limitRate_edits(self):
        """操作步骤：将设备A限速、设备B均限速"""
        # 设备A（有线）
        self.switch_to_limitTimePage_wired_5g_24g("Wired", self.driver.current_url)
        # 上下行的值（500、1000）与开关状态（开启）理应都是配置好的，但还是要检验一遍
        flag = False  # 用于标记是否需要修改，False为不需要修改，True为需要修改
        # 上行：500
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
        )
        Upload_Value = int(self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value"))
        if Upload_Value != rata_upload_1:
            self.driver.find_element_by_xpath(LimitRateLocators.Upload).clear()
            self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(rata_upload_1)
            flag = True
        # 下行：1000
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
        )
        Download_Value = int(self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value"))
        if Download_Value != rata_download_2:
            self.driver.find_element_by_xpath(LimitRateLocators.Download).clear()
            self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(rata_download_2)
            flag = True
        # 开关状态
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Statu))
        )
        Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
        if Statu_class != "box checked":
            self.driver.find_element_by_xpath(LimitRateLocators.Statu).click()
            flag = True

        if flag == True:  # 即需要修改，则需要点击 保存 按钮
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
            ).click()
            # 断言:toast提示：成功
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 设备B（即无线5G）
        self.switch_to_limitTimePage_wired_5g_24g("5G", self.driver.current_url)
        # 新增限速
        # 上行：1500
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(rata_upload_3)
        # 下行：2000
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(rata_download_4)
        # 状态理应为关闭，还是做一下判断，当为关闭时才进行if的启用操作
        Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
        if Statu_class == "box":
            # 启用
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Statu))
            ).click()
        # 保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
        ).click()
        # 断言:toast提示：成功
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

    @unittest.skip("跳过")
    def test_O_limitRate_7(self):
        """【检验】用例-1611：多个设备同时限速可成功（设备A、B都设置了限速，保存成功后A、B都能限速成功）"""

        # 前提条件：设备A：上下500、下行1000。 设备B：上下1500、下行2000。 开关均为开启
        # 判断设备B
        self.switch_to_limitTimePage_wired_5g_24g("5G", self.driver.current_url)
        # 断言:判断上下行及开关状态是否设置正确
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Upload))
        )
        Upload_Value = int(self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value"))
        if Upload_Value != rata_upload_3:
            print("【备注】该用例无法验证，原因：设备B的上行值不为1500")
            assert False

        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
        )
        Download_Value = int(self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value"))
        if Download_Value != rata_download_4:
            print("【备注】该用例无法验证，原因：设备B的下行值不为2000")
            assert False

        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
        )
        Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
        if Statu_class != "box checked":
            print("【备注】该用例无法验证，原因：设备B的限速开关为关闭")
            assert False

        # 判断设备A
        self.switch_to_limitTimePage_wired_5g_24g("Wired", self.driver.current_url)
        # 断言:判断上下行及开关状态是否设置正确
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Upload))
        )
        Upload_Value = int(self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value"))
        if Upload_Value != rata_upload_1:
            print("【备注】该用例无法验证，原因：设备A的上行值不为500")
            assert False

        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
        )
        Download_Value = int(self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value"))
        if Download_Value != rata_download_2:
            print("【备注】该用例无法验证，原因：设备A的下行值不为1000")
            assert False

        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
        )
        Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
        if Statu_class != "box checked":
            print("【备注】该用例无法验证，原因：设备A的限速开关为关闭")
            assert False

        # 前提已完成，开始检验用例
        result = Test_rate_limit.test_rate_limit_7()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    @unittest.skip("跳过")
    def test_P_limitRate_edits_5G(self):
        """操作步骤：将设备B限速"""
        # 上行1000、下行500，开关状态开启
        # 进入到设备B的限速页
        self.switch_to_limitTimePage_wired_5g_24g("5G", self.driver.current_url)
        # 上行：1000
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(rata_upload_2)

        # 下行：500
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(rata_download_1)

        # 开关状态
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Statu))
        )
        Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
        if Statu_class != "box checked":
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

    @unittest.skip("跳过")
    def test_Q_limitRate_8(self):
        """【检验】用例-1612:无线接入，限速功能可生效"""
        self.switch_to_limitTimePage_wired_5g_24g("5G", self.driver.current_url)
        # 前提条件：设备B中：上行1000，下行500，开关开启
        # 断言:判断上下行是否设置正确
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Upload))
        )
        Upload_Value = int(self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value"))
        if Upload_Value != rata_upload_2:
            print("【备注】该用例无法验证，原因：设备B的上行值不为1000")
            assert False

        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
        )
        Download_Value = int(self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value"))
        if Download_Value != rata_download_1:
            print("【备注】该用例无法验证，原因：设备B的下行值不为500")
            assert False

        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
        )
        Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
        if Statu_class != "box checked":
            print("【备注】该用例无法验证，原因：设备B的限速开关为关闭")
            assert False

        # 前提已完成，开始检验用例
        result = Test_rate_limit.test_rate_limit_8()
        if result == 1:
            print("【成功】")
            assert True
        else:
            print("【失败】")
            assert False

    #
    #
    # #@unittest.skip("跳过")
    # def test_R_limitRate_edits_wired(self):
    #     """操作步骤：将设备A限速"""
    #     # 上行1000、下行500，开关状态开启
    #     # 进入到设备B的限速页
    #     self.switch_to_limitTimePage_wired_5g_24g("Wired", self.driver.current_url)
    #     # 上行：1000
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
    #     ).clear()
    #     self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(rata_upload_2)
    #
    #     # 下行：500
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
    #     ).clear()
    #     self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(rata_download_1)
    #
    #     # 开关状态
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Statu))
    #     )
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     if Statu_class != "box checked":
    #         self.driver.find_element_by_xpath(LimitRateLocators.Statu).click()
    #
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
    #
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
    # def test_S_limitRate_9(self):
    #     """【检验】用例-1613:有线接入，限速功能可生效"""
    #     self.switch_to_limitTimePage_wired_5g_24g("Wired", self.driver.current_url)
    #     # 前提条件：设备B中：上行1000，下行500，开关开启
    #     # 断言:判断上下行是否设置正确
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Upload))
    #     )
    #     Upload_Value = int(self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value"))
    #     if Upload_Value != rata_upload_2:
    #         print("【备注】该用例无法验证，原因：设备A的上行值不为1000")
    #         assert False
    #
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
    #     )
    #     Download_Value = int(self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value"))
    #     if Download_Value != rata_download_1:
    #         print("【备注】该用例无法验证，原因：设备A的下行值不为500")
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
    #     result = Test_rate_limit.test_rate_limit_9()
    #     if result == 1:
    #         print("【成功】")
    #         assert True
    #     else:
    #         print("【失败】")
    #         assert False
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
    # def test_T_limitRate_turn_statu_off(self):
    #     """操作步骤：将设备A、B的开关均关闭，回到初始状态"""
    #     # 设备A
    #     self.switch_to_limitTimePage_wired_5g_24g("Wired", self.driver.current_url)
    #     # 开关状态理应为启用，如果为启用状态才进行if的关闭操作
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
    #     )
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     if Statu_class == "box checked":
    #         # 关闭
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
    #         self.driver.refresh()
    #         WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #             EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
    #         )
    #         Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #         assert Statu_class == "box", Statu_class
    #
    #     # 设备B
    #     self.switch_to_limitTimePage_wired_5g_24g("5G", self.driver.current_url)
    #     # 开关状态理应为启用，如果为启用状态才进行if的关闭操作
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
    #     )
    #     Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #     if Statu_class == "box checked":
    #         # 关闭
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
    #         self.driver.refresh()
    #         WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #             EC.presence_of_element_located((By.XPATH, LimitRateLocators.Statu))
    #         )
    #         Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
    #         assert Statu_class == "box", Statu_class
    #
    #
