#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun

import unittest
import time
from . import const
from selenium import webdriver
from .test_base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from rweb.path.common import CommonLocators
from rweb.path.devices import DevicesLocators
from rweb.path.limitTime import LimitTimeLocators
from rweb.path.limitRate import LimitRateLocators
from rweb.path.websiteBlacklist import WebsiteBlacklistLocators



class LimitWebsiteBlacklist(Base):

    def setUp(self):
        super(LimitWebsiteBlacklist, self).setUp()
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
        # 切换到网址黑名单页
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Page_WebsiteBlacklist))
        ).click()





    #@unittest.skip("跳过")
    def test_A_limitWebsiteBlacklist_listDefault(self):
        """网址黑名单-列表默认情况检查"""
        """
        用例-1962 : 默认开关为关闭状态
        用例-1963 : 网址列表-默认为空
        """
        # 断言：用例-1962 : 默认开关为关闭状态
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Statu))
        )
        Statu_class = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Statu).get_attribute("class")
        assert Statu_class == "switch switch-animation", Statu_class

        # 断言：用例-1963 : 网址列表-默认为空
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Empty_List))
        )
        Empty_Text = self.driver.find_element_by_xpath(CommonLocators.Empty_List).text
        assert Empty_Text == "Empty", Empty_Text




    #@unittest.skip("跳过")
    def test_B_limitWebsiteBlacklist_insertElementCheck(self):
        """网址黑名单-新增框元素检查"""
        """
        用例-1975 : 新增网址框-元素检测
	                查看页面包含元素：标题：网址黑名单
						              文本：请输入(输入框无数据时显示)
						              按钮：取消、确定
        """
        # 点击 新增 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Add))
        ).click()
        # 断言：标题：网址黑名单
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='form']/div/div/label/span"))
        ).click()
        Title_Text = self.driver.find_element_by_xpath("//div[@class='form']/div/div/label/span").text
        assert Title_Text == "Website Blacklist", Title_Text

        # 断言：文本：请输入(输入框无数据时显示)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, WebsiteBlacklistLocators.Website))
        )
        Input_Note = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Website).get_attribute("placeholder")
        assert Input_Note == "Please enter", Input_Note

        # 断言：按钮：取消、确定
        assert self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Cancel).is_displayed()
        assert self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Save).is_displayed()




    #@unittest.skip("跳过")
    def test_C_limitWebsiteBlacklist_required(self):
        """网址黑名单-新增网址框-必填项和超过范围检查"""
        """
        用例-1979 : 新增网址框-输入框为空，点击“保存”，输入框后方提示错误信息
		            网址输入框为空，点击“保存”，看是否输入框后方文字提示“必填” ： 是
		用例-1977 : 新增网址框-输入框输入31个字节的网址，有错误提示
			        输入网址为31个字节（例：wwwwwwe1234567890abcd-123es2sec），看输入框后方是否显示错误提示“域名只能为1-30个字符‘《trans00226》”：是
        """
        # 点击 新增 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Add))
        ).click()

        # 断言：用例-1979 : 新增网址框-输入框为空，点击“保存”，输入框后方提示错误信息
        # 直接点击 保存 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Save))
        ).click()
        Error_Message_Text = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Error_Message).text
        assert Error_Message_Text == "Required", Error_Message_Text

        # 断言：用例-1977: 新增网址框-输入框输入31个字节的网址，有错误提示
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).send_keys("wwwwwwe1234567890abcd-123es2sec")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Save))
        ).click()
        Error_Message = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Error_Message).text
        assert Error_Message == "Domain name should be within 30 characters", Error_Message




    #@unittest.skip("跳过")
    def test_D_limitWebsiteBlacklist_anyCharacter(self):
        """网址黑名单-新增网址框-支持输入任意字符"""
        """
        用例-1976 : 新增网址框-输入框支持输入任意字符
                    输入框输入任意字符（数字，字母，字符，汉字）等，看是否支持 ： 是
        """
        # 点击 新增 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Add))
        ).click()
        # 断言：单输入数字，如：123
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).send_keys("123")
        Website_Value = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Website).get_attribute("value")
        assert Website_Value == "123", Website_Value

        # 断言：单输入字母，如：abcd
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).clear()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).send_keys("abcd")
        Website_Value = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Website).get_attribute("value")
        assert Website_Value == "abcd", Website_Value

        # 断言：单输入字符，如：%^&*
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).clear()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).send_keys("%^&*")
        Website_Value = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Website).get_attribute("value")
        assert Website_Value == "%^&*", Website_Value

        # 断言：单输入汉字，如：测试
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).clear()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).send_keys("测试")
        Website_Value = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Website).get_attribute("value")
        assert Website_Value == "测试", Website_Value

        # 断言：组合输入，如：123abc%^&测试
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).clear()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).send_keys("123abc%^&测试")
        Website_Value = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Website).get_attribute("value")
        assert Website_Value == "123abc%^&测试", Website_Value



    #@unittest.skip("跳过")
    def test_E_limitWebsiteBlacklist_notStandard(self):
        """网址黑名单-新增网址框-不符合规则输入有错误提示"""
        """
        用例-1978 : 新增网址框-输入框输入不符合规则的字符，有错误提示
                    依次输入以下网址，查看输入框后方是否提示“无效域名《trans00227》” ：是
                    输入一个有空格的网址 
                    输入一个“-”开头的网址
                    输入一个“-”结尾的网址
                    输入一个“_”开头的网址
                    输入一个“_”结尾的网址
                    输入一个“.”开头的网址
                    输入一个“.”结尾的网址
                    输入一个“...”开头的网址
                    输入一个“........”结尾的网址
                    输入非（字母，数字，"-"，"."，"_"）字符
                    输入带协议头（http，https等）的网址
        """
        # 点击 新增 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Add))
        ).click()

        # 断言：输入一个有空格的网址，如：www.bai du.com
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).send_keys("www.bai du.com")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Save))
        ).click()
        Error_Message = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Error_Message).text
        assert Error_Message == "Invalid domain name", Error_Message

        # 断言：输入一个“-”开头的网址，如：-baidu
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).clear()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).send_keys("-baidu")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Save))
        ).click()
        Error_Message = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Error_Message).text
        assert Error_Message == "Invalid domain name", Error_Message

        # 断言：输入一个“-”结尾的网址，如：baidu-
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).clear()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).send_keys("baidu-")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Save))
        ).click()
        Error_Message = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Error_Message).text
        assert Error_Message == "Invalid domain name", Error_Message

        # 断言：输入一个“_”开头的网址，如：_baidu
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).clear()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).send_keys("_baidu")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Save))
        ).click()
        Error_Message = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Error_Message).text
        assert Error_Message == "Invalid domain name", Error_Message

        # 断言：输入一个“_”结尾的网址，如：baidu_
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).clear()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).send_keys("baidu_")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Save))
        ).click()
        Error_Message = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Error_Message).text
        assert Error_Message == "Invalid domain name", Error_Message

        # 断言：输入一个“.”开头的网址，如：.baidu
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).clear()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).send_keys(".baidu")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Save))
        ).click()
        Error_Message = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Error_Message).text
        assert Error_Message == "Invalid domain name", Error_Message

        # 断言：输入一个“.”结尾的网址，如：baidu.
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).clear()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).send_keys("baidu.")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Save))
        ).click()
        Error_Message = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Error_Message).text
        assert Error_Message == "Invalid domain name", Error_Message

        # 断言：输入一个“...”开头的网址，如：...baidu
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).clear()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).send_keys("...baidu")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Save))
        ).click()
        Error_Message = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Error_Message).text
        assert Error_Message == "Invalid domain name", Error_Message

        # 断言：输入一个“........”结尾的网址，如：baidu.......
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).clear()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).send_keys("baidu.......")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Save))
        ).click()
        Error_Message = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Error_Message).text
        assert Error_Message == "Invalid domain name", Error_Message

        # 断言：输入非（字母，数字，"-"，"."，"_"）字符，如：%^&()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).clear()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).send_keys("%^&()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Save))
        ).click()
        Error_Message = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Error_Message).text
        assert Error_Message == "Invalid domain name", Error_Message

        # 断言：输入带协议头（http，https等）的网址，如：https://www.baidu.com、http://www.baidu.com/
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).clear()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).send_keys("https://www.baidu.com")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Save))
        ).click()
        Error_Message = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Error_Message).text
        assert Error_Message == "Invalid domain name", Error_Message

        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).clear()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).send_keys("http://www.baidu.com/")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Save))
        ).click()
        Error_Message = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Error_Message).text
        assert Error_Message == "Invalid domain name", Error_Message



    #@unittest.skip("跳过")
    def test_F_limitWebsiteBlacklist_errorNotSave(self):
        """网址黑名单-新增网址框-有错误提示不能保存"""
        """
        用例-1982 : 新增网址框-输入框后方有错误提示时，点击“保存”，弹框不关闭，保持显示错误提示
        """
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Add))
        ).click()
        # 以下分析三种情况：
        # 第一种：错误提示：必填
        # 第一次点击 保存 按钮，检验异常提示是否还在
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Save))
        ).click()
        Error_Message = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Error_Message).text
        assert Error_Message == "Required", Error_Message
        # 第二次点击 保存 按钮，检验异常提示是否还在
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Save))
        ).click()
        Error_Note = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Error_Message).text
        assert Error_Note == "Required", Error_Note

        # 第二种：错误提示：域名只能为1-30个字符
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).clear()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).send_keys("1234567890abcdefghijklmnopqrstu")
        # 第一次点击 保存 按钮，检验异常提示是否还在
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Save))
        ).click()
        Error_Message = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Error_Message).text
        assert Error_Message == "Domain name should be within 30 characters", Error_Message
        # 第二次点击 保存 按钮，检验异常提示是否还在
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Save))
        ).click()
        Error_Note = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Error_Message).text
        assert Error_Note == "Domain name should be within 30 characters", Error_Note

        # 第三种：错误提示：无效域名
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).clear()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).send_keys("www.bai du.com")
        # 第一次点击 保存 按钮，检验异常提示是否还在
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Save))
        ).click()
        Error_Message = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Error_Message).text
        assert Error_Message == "Invalid domain name", Error_Message
        # 第二次点击 保存 按钮，检验异常提示是否还在
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Save))
        ).click()
        Error_Note = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Error_Message).text
        assert Error_Note == "Invalid domain name", Error_Note




    #@unittest.skip("跳过")
    def test_G_limitWebsiteBlacklist_add_Cancel(self):
        """网址黑名单-新增-取消不新增"""
        """
        用例-1981 : 新增网址框-输入正确网址，点击“取消”，关闭弹框，不保存对应配置
	                输入一个网址，点击“取消”按钮，看是否关闭弹框，不保存：是
        """
        # 点击黑名单 新增 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Add))
        ).click()
        # 输入：www.baidu.com
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).send_keys("www.baidu.com")
        # 点击 取消 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Cancel))
        ).click()

        # 断言:用例-1981 : 新增网址框-输入正确网址，点击“取消”，关闭弹框，不保存对应配置
        self.driver.refresh()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.List_Null))
        )
        assert self.driver.find_element_by_xpath(WebsiteBlacklistLocators.List_Null).is_displayed()






    #@unittest.skip("跳过")
    def test_H_limitWebsiteBlacklist_add_ok(self):
        """网址黑名单-新增成功"""
        """
        用例-1980 : 新增网址框-输入正确网址，点击“保存”，关闭弹框，新增成功，显示在列表
	                输入正确网址，点击保存，看是否关闭弹框，列表显示新增的网址 ： 是
	    用例-1969 : 网址列表-网址为大写字母，保存成功后，配置都存为小写字母
                    创建网址网址1：WWW.BAIDU.COM
                    保存成功后，显示为：www.baidu.com ： 是
        """
        # 点击黑名单 新增 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Add))
        ).click()
        # 输入：WWW.BAIDU.COM
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).send_keys("WWW.BAIDU.COM")
        # 完成添加
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Save))
        ).click()
        # 断言:toast提示：添加成功
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言：用例-1980 : 新增网址框-输入正确网址，点击“保存”，关闭弹框，新增成功，显示在列表
        # 断言：用例-1969 : 网址列表-网址为大写字母，保存成功后，配置都存为小写字母
        self.driver.refresh()
        List_Website = WebsiteBlacklistLocators.List_Website.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, List_Website))
        )
        assert self.driver.find_element_by_xpath(List_Website).text == "www.baidu.com"

    #@unittest.skip("跳过")
    def test_I_limitWebsiteBlacklist_add_exist_error(self):
        """网址黑名单-新增已存在的网址报错"""
        """
        用例-7081 : 新增网址框-新增一个已存在的网址，保存时提示错误信息
	                查看是否提示错误信息：“不能保存重复的信息/trans0659”：是
        """
        # 点击黑名单 新增 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Add))
        ).click()
        # 输入：www.baidu.com
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
        ).send_keys("www.baidu.com")
        # 点击 新增 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Save))
        ).click()

        # 断言：用例-7081 : 新增网址框-新增一个已存在的网址，保存时提示错误信息
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Error_Toast))
        )
        Error_Note = self.driver.find_element_by_xpath(CommonLocators.Error_Toast).text
        assert Error_Note == "Data is existing already", Error_Note




    #@unittest.skip("跳过")
    def test_J_limitWebsiteBlacklist_elementCheck(self):
        """网址黑名单-页面元素检查"""
        """
        用例-1961 : 页面元素检测
                    查看页面包含元素：	开关
                                        文本：黑名单网址、加入黑名单的网址会被自动拦截、操作
                                        按钮：删除、新增

        """
        # 断言：页面元素包含：开关
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, WebsiteBlacklistLocators.Statu))
        )
        assert self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Statu).is_displayed()

        # 断言：页面元素包含文本：黑名单网址
        Text_1 = self.driver.find_element_by_xpath("//div[@class='table']/div[2]/div[1]").text[0:17]
        assert Text_1 == "Website Blacklist", Text_1

        # 断言：页面元素包含文本：加入黑名单的网址会被自动拦截
        Text_2 = self.driver.find_element_by_xpath("//div[@class='table']/div[2]/div[1]/span").text
        assert Text_2 == "Blacklisted websites will automatically be blocked.", Text_2

        # 断言：页面元素包含文本：操作
        Text_3 = self.driver.find_element_by_xpath("//div[@class='table']/div[2]/div[2]").text
        assert Text_3 == "Actions", Text_3

        # 断言：页面元素包含按钮：删除
        Delete = WebsiteBlacklistLocators.Delete.format(num="last()")
        assert self.driver.find_element_by_xpath(Delete).is_displayed()

        # 断言：页面元素包含按钮：新增
        assert self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Add).is_displayed()





    #@unittest.skip("跳过")
    def test_K_limitWebsiteBlacklist_delete(self):
        """网址黑名单-删除"""
        """
        用例-1987 : 删除一个网址，删除成功，从列表消失
                    点击设备列表中的“删除”按钮，查看是否从列表消失：是
        """
        flag = False
        while flag == False:
            try:
                assert self.driver.find_element_by_xpath(WebsiteBlacklistLocators.List_Null).is_displayed()
                flag = True
            except:
                Delete = WebsiteBlacklistLocators.Delete.format(num="last()")
                WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                    EC.element_to_be_clickable((By.XPATH, Delete))
                ).click()
                # 断言:toast提示：成功
                WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                    EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
                )
                time.sleep(2)

        # 断言：用例-1987 : 删除一个网址，删除成功，从列表消失
        self.driver.refresh()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.List_Null))
        )
        assert self.driver.find_element_by_xpath(WebsiteBlacklistLocators.List_Null).is_displayed()



    #@unittest.skip("跳过")
    def test_L_limitWebsiteBlacklist_add_number(self):
        """网址黑名单-新增-网址为数字，检查排列顺序"""
        """
        用例-1968 : 网址列表-网址为数字，按照0-9排列
                    创建多个网址：网址1：01、网址2：03、网址3：02
                    查看排序是否为：网址1、网址3、网址2
        用例-1964 : 网址列表-网址显示正确
                    添加几个不同的网址成功后，查看列表是否正常显示添加的网址：是
        """
        Insert_List=["01", "03", "02"]

        i = 0
        while i <= 2:
            # 点击黑名单 新增 按钮
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Add))
            ).click()
            # 输入：网址
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
            ).send_keys(Insert_List[i])
            # 完成添加
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Save))
            ).click()
            # 断言:toast提示：添加成功
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
            i += 1
            time.sleep(2)

        # 断言：用例-1968 : 网址列表-网址为数字，按照0-9排列
        # 断言：用例-1964 : 网址列表-网址显示正确
        List_Website_1 = WebsiteBlacklistLocators.List_Website.format(num="1")
        List_Website_1_name = self.driver.find_element_by_xpath(List_Website_1).text
        assert List_Website_1_name == "01", List_Website_1_name

        List_Website_2 = WebsiteBlacklistLocators.List_Website.format(num="2")
        List_Website_2_name = self.driver.find_element_by_xpath(List_Website_2).text
        assert List_Website_2_name == "02", List_Website_2_name

        List_Website_3 = WebsiteBlacklistLocators.List_Website.format(num="3")
        List_Website_3_name = self.driver.find_element_by_xpath(List_Website_3).text
        assert List_Website_3_name == "03", List_Website_3_name

        # 调用删除函数，使其删除干净，以便后面用例执行
        self.test_K_limitWebsiteBlacklist_delete()





    #@unittest.skip("跳过")
    def test_M_limitWebsiteBlacklist_add_letter(self):
        """网址黑名单-新增-网址为字母，检查排列顺序"""
        """
        用例-1970 : 网址列表-网址为小写字母，按照a-z排列
                    创建多个网址：网址1：c、网址2：a、网址3：b
                    查看排序是否为：网址2、网址3、网址1
        用例-1967 : 网址列表-开关开启关闭，列表状态不受影响
                    列表添加几个黑名单网址
                    开关开启和关闭，查看列表状态，保持不变，不受影响，按钮都可正常点击 ： 是
        """
        Insert_List = ["c", "a", "b"]

        i = 0
        while i <= 2:
            # 点击黑名单 新增 按钮
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Add))
            ).click()
            # 输入：网址
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
            ).send_keys(Insert_List[i])
            # 完成添加
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Save))
            ).click()
            # 断言:toast提示：添加成功
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
            i += 1
            time.sleep(2)

        # 断言：用例-1968 : 网址列表-网址为数字，按照0-9排列
        List_Website_1 = WebsiteBlacklistLocators.List_Website.format(num="1")
        List_Website_1_name = self.driver.find_element_by_xpath(List_Website_1).text
        assert List_Website_1_name == "a", List_Website_1_name

        List_Website_2 = WebsiteBlacklistLocators.List_Website.format(num="2")
        List_Website_2_name = self.driver.find_element_by_xpath(List_Website_2).text
        assert List_Website_2_name == "b", List_Website_2_name

        List_Website_3 = WebsiteBlacklistLocators.List_Website.format(num="3")
        List_Website_3_name = self.driver.find_element_by_xpath(List_Website_3).text
        assert List_Website_3_name == "c", List_Website_3_name

        # 断言：用例-1967 : 网址列表-开关开启关闭，列表状态不受影响
        i = 1
        while i <= 2:
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Statu))
            ).click()
            # 断言:toast提示：操作成功
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

            List_Website_1 = WebsiteBlacklistLocators.List_Website.format(num="1")
            List_Website_1_name = self.driver.find_element_by_xpath(List_Website_1).text
            assert List_Website_1_name == "a", List_Website_1_name

            List_Website_2 = WebsiteBlacklistLocators.List_Website.format(num="2")
            List_Website_2_name = self.driver.find_element_by_xpath(List_Website_2).text
            assert List_Website_2_name == "b", List_Website_2_name

            List_Website_3 = WebsiteBlacklistLocators.List_Website.format(num="3")
            List_Website_3_name = self.driver.find_element_by_xpath(List_Website_3).text
            assert List_Website_3_name == "c", List_Website_3_name
            i += 1
            time.sleep(2)

        # 调用删除函数，使其删除干净，以便后面用例执行
        self.test_K_limitWebsiteBlacklist_delete()




    #@unittest.skip("跳过")
    def test_N_limitWebsiteBlacklist_order_number_letter(self):
        """网址黑名单-网址列表-网址字符优先级按（数字>大写字母>小写字母>其他）排序检测"""
        """
        用例-1971 : 网址列表-网址字符优先级按（数字>大写字母>小写字母>其他）排序检测
                    建多个网址：网址1：01、网址2：A（会转换成小写字母a）、网址3：b
                    查看设备的排序是否为：网址1、网址2、网址3
        """
        Insert_List = ["01", "A", "b"]

        i = 0
        while i <= 2:
            # 点击黑名单 新增 按钮
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Add))
            ).click()
            # 输入：网址
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
            ).send_keys(Insert_List[i])
            # 完成添加
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Save))
            ).click()
            # 断言:toast提示：添加成功
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
            i += 1
            time.sleep(2)

        # 断言：用例-1971 : 网址列表-网址字符优先级按（数字>大写字母>小写字母>其他）排序检测
        self.driver.refresh()
        List_Website_1 = WebsiteBlacklistLocators.List_Website.format(num="1")
        List_Website_1_name = self.driver.find_element_by_xpath(List_Website_1).text
        assert List_Website_1_name == "01", List_Website_1_name

        List_Website_2 = WebsiteBlacklistLocators.List_Website.format(num="2")
        List_Website_2_name = self.driver.find_element_by_xpath(List_Website_2).text
        assert List_Website_2_name == "a", List_Website_2_name

        List_Website_3 = WebsiteBlacklistLocators.List_Website.format(num="3")
        List_Website_3_name = self.driver.find_element_by_xpath(List_Website_3).text
        assert List_Website_3_name == "b", List_Website_3_name

        # 调用删除函数，使其删除干净，以便后面用例执行
        self.test_K_limitWebsiteBlacklist_delete()




    #@unittest.skip("跳过")
    def test_O_limitWebsiteBlacklist_add_15(self):
        """网址黑名单-添加15条记录"""
        """
        用例-1983 : 新增1个字节的网址，保存成功
                    输入网址为：1			
                    保存配置
                    是否能保存成功 ： 是
        用例-1984 : 新增30个字节的网址，保存成功
                    输入网址为30个字节：www.1234567890ab-123.s2s.3.com
                    保存配置
                    是否能保存成功 ： 是
        用例-1998 : 新增没有符号的网址，保存成功
        用例-1985 : 新增网址包含（.-_），保存成功
	                输入一个网址包含（.）（-）（_）的网址，看是否可保存成功 ： 是
	    用例-1972 : 网址列表-列表数量达到最大15条时可正常显示
	                创建最大的条数15条，查看列表是否可正常显示完整：是
	    用例-1973 : 网址列表-单个设备网址数量未超过15条，点击“新增”，弹出新增框
	                当前接入设备的黑名单网址，总共未达到15个，点击“新增”，看是否弹出新增框 ： 是
        """

        Insert_List = [
            "1", "2", "3", "4", "5",
            "abc.1234567890abcd-1.s.3.com-6", "bcd-7", "ccc.com-8", "def-9", "efghi.123.com-10",
            "fsdfsd-11", "g1234-12", "h.hsj-13", "www.abc-14", "www.sogou.com-15",
        ]

        i = 0
        while i <= 14:
            # 点击黑名单 新增 按钮
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Add))
            ).click()
            # 输入：网址
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Website))
            ).send_keys(Insert_List[i])
            # 完成添加
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Save))
            ).click()
            # 断言:toast提示：添加成功
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            Successful_Toast = self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text
            assert Successful_Toast == "Successful operation", Successful_Toast
            i += 1
            time.sleep(2)

        # 断言：用例-1983 : 新增1个字节的网址，保存成功
        # 断言：用例-1998 : 新增没有符号的网址，保存成功
        # 断言：用例-1985 : 新增网址包含（.-_），保存成功
        # 断言：输入一个网址包含（.）（-）（_）的网址，看是否可保存成功 ： 是（注：没有找到带有“_”的合法网址，故没有该测试点）
        # 断言：用例-1972 : 网址列表-列表数量达到最大15条时可正常显示
        # 断言：用例-1973 : 网址列表-单个设备网址数量未超过15条，点击“新增”，弹出新增框
        j = 1
        while j <= 15:
            List_Website = WebsiteBlacklistLocators.List_Website.format(num=j)
            List_Website_name = self.driver.find_element_by_xpath(List_Website).text
            assert List_Website_name == Insert_List[j-1], List_Website_name
            j += 1




    #@unittest.skip("跳过")
    def test_P_limitWebsiteBlacklist_add_morethan15(self):
        """网址黑名单-超过15条记录再添加检验"""
        """
        用例-1974 : 网址列表-单个设备添加的总网址数量超过15条，点击“新增”，有文字提示
                    给连接的任意一个设备，增加15条网址黑名单
                    这个设备，再次点击“新增”，看是否提示“已经达到上限。trans0060” ： 是
                    其他设备，点击“新增”，看是否不提示，而是弹出新增框 ： 是
                    （注：上面最后一点暂没有检验）
        """
        # 点击黑名单 新增 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Add))
        ).click()

        # 断言：用例-1974 : 网址列表-单个设备添加的总网址数量超过15条，点击“新增”，有文字提示
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Error_Toast))
        )
        Error_Note = self.driver.find_element_by_xpath(CommonLocators.Error_Toast).text
        assert Error_Note == "Already reached the limit", Error_Note




    #@unittest.skip("跳过")
    def test_Q_limitWebsiteBlacklist_statu_on(self):
        """网址黑名单-修改状态：由关变为开"""
        # 状态理应为关闭，如果为关闭状态才进行if的启用操作
        Statu_class = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Statu).get_attribute('class')
        if Statu_class == "switch switch-animation":
            # 打开网址黑名单开关
            time.sleep(1)
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Statu))
            ).click()
            # 断言:toast提示：打开开关成功
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        self.driver.refresh()
        time.sleep(2)   #用于状态按钮切换
        # 断言：判断开关是否开启
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Statu))
        )
        Statu_class = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Statu).get_attribute('class')
        assert Statu_class == "switch switch-animation checked", Statu_class










    #@unittest.skip("跳过")
    def test_R_limitWebsiteBlacklist_statu_off(self):
        """网址黑名单-修改状态：由开变为关"""
        # 状态理应为开启，如果为开启状态才进行if的关闭操作
        Statu_class = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Statu).get_attribute('class')
        if Statu_class == "switch switch-animation checked":
            # 关闭网址黑名单开关
            time.sleep(1)
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Statu))
            ).click()
            # 断言:toast提示：关闭开关成功
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        self.driver.refresh()
        # 断言：判断开关是否关闭
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, WebsiteBlacklistLocators.Statu))
        )
        Statu_class = self.driver.find_element_by_xpath(WebsiteBlacklistLocators.Statu).get_attribute('class')
        assert Statu_class == "switch switch-animation", Statu_class




