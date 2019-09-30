#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun

import unittest
import time
from selenium import webdriver
from .test_base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from . import const

from rweb.path.common import CommonLocators
from rweb.path.devices import DevicesLocators
from rweb.path.limitTime import LimitTimeLocators
from rweb.path.limitRate import LimitRateLocators
from rweb.path.websiteBlacklist import WebsiteBlacklistLocators



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
        ).click()
        self.driver.refresh()
        # 点击主网-设置
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, DevicesLocators.Set))
        ).click()
        # 切换到限速页
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Page_RateLimit))
        ).click()

    @unittest.skip("跳过")
    def test_A_limitRate_elementCheck(self):
        """限速-页面元素检测 及 默认参数"""
        """
        用例-2932 : 页面元素检测
                    是否有配置项：实时上行、实时下行
                    是否显示单位：KB/s
                    查看是否有开关：启用
                    查看是否有按钮：保存  ： 均是
        用例-2964 : web-限速：“上传速度”输入框，没有内容时，显示默认文本
        用例-2968 : web-限速：“下载速度”输入框，没有内容时，显示默认文本
        用例-2933 : 从未配置过，进入页面，显示默认的值
                    全新（恢复出厂设置）路由器，从未配置过，初始化进入页面，查看各项的值:
                    “上传速度”“下载速度”是否默认：空 -> 是
                    “启用”勾选框是否默认：勾选 -> 是
        """
        # 断言：是否有配置项：实时上行、实时下行
        Upload_Name = self.driver.find_element_by_xpath("//div[@class='form']/div/div[1]/div[1]/div/label/span").text[0:6]
        Download_Name = self.driver.find_element_by_xpath("//div[@class='form']/div/div[1]/div[2]/div/label/span").text[0:8]
        assert Upload_Name == "Upload", Upload_Name
        assert Download_Name == "Download", Download_Name

        # 断言：是否显示单位：KB/s
        Upload_Unit = self.driver.find_element_by_xpath("//div[@class='form']/div/div[1]/div[1]/div/label/span").text[8:12]
        Download_Unit = self.driver.find_element_by_xpath("//div[@class='form']/div/div[1]/div[2]/div/label/span").text[10:14]
        assert Upload_Unit == "KB/s", Upload_Unit
        assert Download_Unit == "KB/s", Download_Unit

        # 断言：用例-2964 : web-限速：“上传速度”输入框，没有内容时，显示默认文本
        Upload_DefaultText = self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute('placeholder')
        assert Upload_DefaultText == "1 - 125000", Upload_DefaultText

        # 断言：用例-2968 : web-限速：“下载速度”输入框，没有内容时，显示默认文本
        Download_DefaultText = self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute('placeholder')
        assert Download_DefaultText == "1 - 125000", Download_DefaultText

        # 断言：用例-2933 : 从未配置过，进入页面，显示默认的值
        # “上传速度”“下载速度”是否默认：空
        Upload_DefaultValue = self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value")
        assert Upload_DefaultValue == "", Upload_DefaultValue
        Download_DefaultValue = self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value")
        assert Download_DefaultValue == "", Download_DefaultValue
        # “启用”勾选框是否默认：勾选
        Statu_Default_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
        assert Statu_Default_class == "box", Statu_Default_class




    #@unittest.skip("跳过")
    def test_B_limitRate_error(self):
        """限速-异常情况检查"""
        """
        用例-2979 : web-限速：“上传速度”输入0，光标焦点离开输入框，文字提示
        用例-2980 : web-限速：“下载速度”输入0，光标焦点离开输入框，文字提示
        用例-2982 : web-限速：“上传速度”输入0开头的数字，光标焦点离开输入框，文字提示
        用例-2981 : web-限速：“下载速度”输入0开头的数字，光标焦点离开输入框，文字提示
        用例-2983 : web-限速：“上传速度”输入非数字的其他任意字符，光标焦点离开输入框，文字提示
        用例-2984 : web-限速：“下载速度”输入非数字的其他任意字符，光标焦点离开输入框，文字提示
        用例-2987 : web-限速：“上传速度”输入超过6位数的数字，光标焦点离开输入框，文字提示
        用例-2988 : web-限速：“下载速度”输入超过6位数的数字，光标焦点离开输入框，文字提示
        用例-2943 : Web-限速：“上传速度”支持输入任意字符
        用例-2970 : Web-限速：“下载速度”支持输入任意字符
        """
        # 断言：用例-2979 : web-限速：“上传速度”输入0，光标焦点离开输入框，文字提示
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
        ).send_keys(0)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='form']/div/div[1]"))
        ).click()
        Error_Note = self.driver.find_element_by_xpath("//div[@class='form']/div/div[1]/div[1]/span").text
        assert Error_Note == "Positive integers only.", Error_Note

        # 断言：用例-2980 : web-限速：“下载速度”输入0，光标焦点离开输入框，文字提示
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
        ).send_keys(0)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='form']/div/div[1]"))
        ).click()
        Error_Note = self.driver.find_element_by_xpath("//div[@class='form']/div/div[1]/div[2]/span").text
        assert Error_Note == "Positive integers only.", Error_Note

        self.driver.refresh()

        # 断言：用例-2982 : web-限速：“上传速度”输入0开头的数字，光标焦点离开输入框，文字提示
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
        ).send_keys("012")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='form']/div/div[1]"))
        ).click()
        Error_Note = self.driver.find_element_by_xpath("//div[@class='form']/div/div[1]/div[1]/span").text
        assert Error_Note == "Positive integers only.", Error_Note

        # 断言：用例-2981 : web-限速：“下载速度”输入0开头的数字，光标焦点离开输入框，文字提示
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
        ).send_keys("012")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='form']/div/div[1]"))
        ).click()
        Error_Note = self.driver.find_element_by_xpath("//div[@class='form']/div/div[1]/div[2]/span").text
        assert Error_Note == "Positive integers only.", Error_Note

        self.driver.refresh()

        # 断言：用例-2983: web-限速：“上传速度”输入非数字的其他任意字符，光标焦点离开输入框，文字提示
        # 断言：用例-2943 : Web-限速：“上传速度”支持输入任意字符
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
        ).send_keys("12ab!@ =-<?:'")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='form']/div/div[1]"))
        ).click()
        Upload_Value = self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value")
        assert Upload_Value == "12ab!@ =-<?:'", Upload_Value
        Error_Note = self.driver.find_element_by_xpath("//div[@class='form']/div/div[1]/div[1]/span").text
        assert Error_Note == "Positive integers only.", Error_Note

        # 断言： 用例-2984: web-限速：“下载速度”输入非数字的其他任意字符，光标焦点离开输入框，文字提示
        # 断言：用例-2970 : Web-限速：“下载速度”支持输入任意字符
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
        ).send_keys("12ab!@ =-<?:'")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='form']/div/div[1]"))
        ).click()
        Upload_Value = self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value")
        assert Upload_Value == "12ab!@ =-<?:'", Upload_Value
        Error_Note = self.driver.find_element_by_xpath("//div[@class='form']/div/div[1]/div[2]/span").text
        assert Error_Note == "Positive integers only.", Error_Note





        self.driver.refresh()

        # 断言：用例-2987 : web-限速：“上传速度”输入超过6位数的数字，光标焦点离开输入框，文字提示
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
        ).send_keys("1234567")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='form']/div/div[1]"))
        ).click()
        Error_Note = self.driver.find_element_by_xpath("//div[@class='form']/div/div[1]/div[1]/span").text
        assert Error_Note == "Already reached the limit", Error_Note

        # 断言：用例-2988 : web-限速：“下载速度”输入超过6位数的数字，光标焦点离开输入框，文字提示
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
        ).send_keys("1234567")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='form']/div/div[1]"))
        ).click()
        Error_Note = self.driver.find_element_by_xpath("//div[@class='form']/div/div[1]/div[2]/span").text
        assert Error_Note == "Already reached the limit", Error_Note








    @unittest.skip("跳过")
    def test_A_limitRate_add(self):
        """限速-新增"""
        # 设置上下行:10KB/s
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(10)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(10)
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
        assert self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value") == "10"
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
        )
        assert self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value") == "10"



    @unittest.skip("跳过")
    def test_B_limitRate_edit_value(self):
        """限速-修改参数值"""
        # 修改上下行为：1KB/s
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(1)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(1)
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
        assert self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value") == "1"
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
        )
        assert self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value") == "1"


    @unittest.skip("跳过")
    def test_C_limitRate_edit_statu_on(self):
        """限速-修改状态：由关变为开"""
        # 状态默认为关闭，如果为关闭状态才进行if的启用操作
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

        # 断言：查看是否启用
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Statu))
        )
        assert self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class') == "box checked"





    @unittest.skip("跳过")
    def test_D_limitRate_edit_statu_off(self):
        """限速-修改状态：由开变为关"""
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

        # 断言：查看是否关闭
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Statu))
        )
        assert self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class') == "box"