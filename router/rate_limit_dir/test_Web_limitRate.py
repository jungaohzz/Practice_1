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
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
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












    @unittest.skip("跳过")
    def test_A_limitRate_onlyLimitUpload(self):
        """操作步骤：只限制上行，并开启开关"""
        # 上行：102400
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(102400)
        # 下行：清空
        # 模拟鼠标双击
        inputBox = self.driver.find_element_by_xpath(LimitRateLocators.Download)
        action_chains = ActionChains(self.driver)
        action_chains.double_click(inputBox).perform()
        # 模拟键盘删除键
        self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(Keys.BACK_SPACE)
        # 保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
        ).click()
        # 断言:toast提示：成功
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        self.driver.refresh()

        # 断言:判断上下行是否设置正确
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Upload))
        )
        Upload_Value = self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value")
        assert Upload_Value == "125000", Upload_Value
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
        )
        Download_Value = self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value")
        assert Download_Value == "", Download_Value

        # 如果状态为关闭时，才进行if的启用操作
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







    #@unittest.skip("跳过")
    def test_B_limitRate_add(self):
        """【检验】用例-1599:限速：只限制了上行流量，下行流量不受限制（TCP连接）"""
        Result = Test_rate_limit.test_rate_limit_1()
        print("<<<<")
        print(Result)
        print(">>>>")






    @unittest.skip("跳过")
    def test_J_limitRate_onlyLimitDownload(self):
        """限速-只限制下行，可成功保存"""
        """
        用例-2955 : 只限制下行值，路由器配置项保存正确
                    只配置下行的流量，上行流量为空，保存成功后，查看路由器（上行限速值，下行限速值）配置项是否保存成功：是
        """
        # 模拟鼠标双击
        inputBox = self.driver.find_element_by_xpath(LimitRateLocators.Upload)
        action_chains = ActionChains(self.driver)
        action_chains.double_click(inputBox).perform()
        # 模拟键盘删除键
        self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(Keys.BACK_SPACE)

        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(125000)

        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
        ).click()
        # 断言:toast提示：成功
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        self.driver.refresh()

        # 断言:判断上下行是否设置正确
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Upload))
        )
        Upload_Value = self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value")
        assert Upload_Value == "", Upload_Value
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
        )
        Download_Value = self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value")
        assert Download_Value == "125000", Download_Value






    @unittest.skip("跳过")
    def test_D_limitRate_add(self):
        """操作步骤：只限制了上行流量"""

        # 设置上下行:10000KB/s和20000KB/s
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(10000)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(20000)
        # 保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
        ).click()

        # 断言:toast提示：操作成功
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        self.driver.refresh()
        # 断言:页面重新拉取后显示的值为保存的值
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Upload))
        )
        assert self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value") == "10000"
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
        )
        assert self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value") == "20000"
        # 断言：查看状态是否为：关闭
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Statu))
        )
        assert self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class') == "box"






    @unittest.skip("跳过")
    def test_E_limitRate_edit_statu_on(self):
        """限速-修改状态：由关变为开"""
        """
        用例-2971 : “启用”勾选框可正常勾选/取消勾选
        用例-2994 : “启用”勾选上，路由器配置项保存正确
			        “启用”勾选上，保存成功，查看路由器（是否启用）配置项是否保存成功：是
        """
        # 状态默认为关闭，如果为关闭状态才进行if的启用操作
        Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
        if Statu_class == "box":
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
            ).clear()
            self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(12500)
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
            ).clear()
            self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(12500)

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
            self.driver.refresh()

        # 断言：查看是否启用
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Statu))
        )
        assert self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class') == "box checked"













    @unittest.skip("跳过")
    def test_G_limitRate_edit_statu_off(self):
        """限速-修改状态：由开变为关"""
        """用例-2971 : “启用”勾选框可正常勾选/取消勾选"""
        # 状态理应为启用，如果为启用状态才进行if的关闭操作
        Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
        if Statu_class == "box checked":
            # 关闭
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
            self.driver.refresh()

        # 断言：查看是否关闭
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Statu))
        )
        assert self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class') == "box"









