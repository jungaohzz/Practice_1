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
from selenium.webdriver.common.keys import Keys

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




    #@unittest.skip("跳过")
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
        用例-2989 : web-限速：“上传速度”“下载速度”都为空，点击“保存”，toast提示
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

        self.driver.refresh()

        # 断言：用例-2989 : web-限速：“上传速度”“下载速度”都为空，点击“保存”，toast提示
        # 未填写上、下行，直接点 保存 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
        ).clear()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
        ).clear()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Error_Toast))
        )
        Error_Note = self.driver.find_element_by_xpath(CommonLocators.Error_Toast).text
        assert Error_Note == "Please enter at least one item", Error_Note





    #@unittest.skip("跳过")
    def test_C_limitRate_errorNotSave(self):
        """限速-输入框有错误时点击“保存”无效"""
        """
        用例-2986 : 输入框后方有错误提示时，点击“保存”无效，保持显示错误提示
        """
        # 下面模拟多种情况：
        # 情况一：上行输入0，下行输入正常数值（如：100）
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(0)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(100)
        # 第一次点击 保存 按钮，检验异常提示是否还在
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
        ).click()
        Error_Note = self.driver.find_element_by_xpath("//div[@class='form']/div/div[1]/div[1]/span").text
        assert Error_Note == "Positive integers only.", Error_Note
        # 第二次点击 保存 按钮，检验异常提示是否还在
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
        ).click()
        Error_Note = self.driver.find_element_by_xpath("//div[@class='form']/div/div[1]/div[1]/span").text
        assert Error_Note == "Positive integers only.", Error_Note

        self.driver.refresh()

        # 情况二：上行输入正常数值（如：100），下行输入非数字的任意字符（如：asd123!~@）
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(100)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys("asd123!~@")
        # 第一次点击 保存 按钮，检验异常提示是否还在
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
        ).click()
        Error_Note = self.driver.find_element_by_xpath("//div[@class='form']/div/div[1]/div[2]/span").text
        assert Error_Note == "Positive integers only.", Error_Note
        # 第二次点击 保存 按钮，检验异常提示是否还在
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
        ).click()
        Error_Note = self.driver.find_element_by_xpath("//div[@class='form']/div/div[1]/div[2]/span").text
        assert Error_Note == "Positive integers only.", Error_Note

        self.driver.refresh()

        # 情况三：上行输入以0开头的数字（如：012），下行输入正常数值（如：100）
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys("012")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(100)
        # 第一次点击 保存 按钮，检验异常提示是否还在
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
        ).click()
        Error_Note = self.driver.find_element_by_xpath("//div[@class='form']/div/div[1]/div[1]/span").text
        assert Error_Note == "Positive integers only.", Error_Note
        # 第二次点击 保存 按钮，检验异常提示是否还在
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
        ).click()
        Error_Note = self.driver.find_element_by_xpath("//div[@class='form']/div/div[1]/div[1]/span").text
        assert Error_Note == "Positive integers only.", Error_Note

        self.driver.refresh()

        # 情况四：上行输入正常数值（如：100），下行输入超过6位数的数字（如99999999）
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(100)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys("99999999")
        # 第一次点击 保存 按钮，检验异常提示是否还在
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
        ).click()
        Error_Note = self.driver.find_element_by_xpath("//div[@class='form']/div/div[1]/div[2]/span").text
        assert Error_Note == "Already reached the limit", Error_Note
        # 第二次点击 保存 按钮，检验异常提示是否还在
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Save))
        ).click()
        Error_Note = self.driver.find_element_by_xpath("//div[@class='form']/div/div[1]/div[2]/span").text
        assert Error_Note == "Already reached the limit", Error_Note






    #@unittest.skip("跳过")
    def test_D_limitRate_add(self):
        """限速-新增成功"""
        """
        用例-2956 : 上下行都限制，路由器配置项保存正确
			        上下行都输入值，保存成功后，查看路由器（上行限速值，下行限速值）配置项是否保存成功：是
        用例-2951 : web-限速：填写表单正确，点击“保存”，保存成功
			        一切正常，点击“保存”，查看响应：1. toast提示：操作成功
			                                       2. 页面重新拉取后显示的值为保存的值
		用例-2995 : ”启用“不勾选，路由器配置项保存正确
			        “启用”不勾选，保存成功，查看路由器（是否启用）配置项是否保存成功：是
        """
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






    #@unittest.skip("跳过")
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






    #@unittest.skip("跳过")
    def test_F_limitRate_edit_statu_off(self):
        """限速-配置成功后再次查看是否一致"""
        """
        用例-2934 : 配置成功过，进入页面，显示当前配置的值
			        配置成功后，再次进入，查看“上传速度”“下载速度”“启用”是否显示上次配置的值 ： 是
        """
        Upload_Value = self.driver.find_element_by_xpath(LimitRateLocators.Upload).get_attribute("value")
        assert Upload_Value == "12500", Upload_Value
        Download_Value = self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value")
        assert Download_Value == "12500", Download_Value
        Statu_class = self.driver.find_element_by_xpath(LimitRateLocators.Statu).get_attribute('class')
        assert Statu_class == "box checked", Statu_class





    #@unittest.skip("跳过")
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






    #@unittest.skip("跳过")
    def test_H_limitRate_edit_value(self):
        """限速-超过125000但为6位数，自动截取为125000"""
        """
        用例-2953 :上行下行输入框输入6位数以内，超过125000的数字，可保存成功，路由器自动截取成125000
                    上行下行输入框，输入小于6位数，大于125000的数字（例：125001），查看是否保存成功 ： 是
                    再次进入查看，上行下行的值是否自动截取成了125000 ： 是
        用例-2994 : “启用”勾选上，路由器配置项保存正确
			        “启用”勾选上，保存成功，查看路由器（是否启用）配置项是否保存成功：是
        """
        # 检验三次
        # 第1次：上行125001，下行20000
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(125001)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(20000)
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
        assert Download_Value == "20000", Download_Value


        # 第2次：上行20000，下行125001
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(20000)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(125001)
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
        assert Upload_Value == "20000", Upload_Value
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, LimitRateLocators.Download))
        )
        Download_Value = self.driver.find_element_by_xpath(LimitRateLocators.Download).get_attribute("value")
        assert Download_Value == "125000", Download_Value


        # 第3次：上行125099，下行125099
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(125099)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Download))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(125099)
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
        assert Download_Value == "125000", Download_Value






    #@unittest.skip("跳过")
    def test_I_limitRate_onlyLimitUpload(self):
        """限速-只限制上行，可成功保存"""
        """
        用例-2954 : 只限制上行值，路由器配置项保存正确
			        只配置上行的流量，下行流量为空，保存成功后，查看路由器（上行限速值，下行限速值）配置项是否保存成功：是
        """
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitRateLocators.Upload))
        ).clear()
        self.driver.find_element_by_xpath(LimitRateLocators.Upload).send_keys(125000)

        # 模拟鼠标双击
        inputBox = self.driver.find_element_by_xpath(LimitRateLocators.Download)
        action_chains = ActionChains(self.driver)
        action_chains.double_click(inputBox).perform()
        # 模拟键盘删除键
        self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(Keys.BACK_SPACE)

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






    #@unittest.skip("跳过")
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