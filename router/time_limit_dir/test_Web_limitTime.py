#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun

import unittest
import time
from selenium import webdriver
from BeautifulReport import BeautifulReport
import os
from unittest import TestLoader

from rweb.test_base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from rweb import const

from rweb.path.common import CommonLocators
from rweb.path.devices import DevicesLocators
from rweb.path.limitTime import LimitTimeLocators
from rweb.path.limitRate import LimitRateLocators
from rweb.path.websiteBlacklist import WebsiteBlacklistLocators





class LimitTime(Base):

    def setUp(self):
        super(LimitTime, self).setUp()
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
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, DevicesLocators.Set))
        ).click()






    #@unittest.skip("跳过")
    def test_C_limitTime_add(self):
        """限时-新增"""
        """
        用例-2028 : 新增框-配置正常，点击“保存”，创建成功，显示在列表中
                    正常输入时间，选择重复项，点击“新增”，看是否关闭弹框，创建成功，显示在列表中 ： 是
        用例-2032 : 限时开关开启，可创建成功
                    限时开关开启，看是否能新增成功 ： 是
        """
        # 点击 新增 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Add))
        ).click()

        # 选择断网时间：14:51
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Insert_CutOffTime_Form))
        ).click()
        Hour_14 = LimitTimeLocators.Hour.format(num=14)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Hour_14))
        ).click()
        Minute_51 = LimitTimeLocators.Minute.format(num=51)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Minute_51))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Form_Confirm))
        ).click()

        # 选择星期一
        Mondey = LimitTimeLocators.Weeks.format(num=1)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Mondey))
        ).click()

        # 点击 新增 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Insert_Add))
        ).click()

        # 断言:是否操作成功：保存
        # 用例-2028 : 新增框-配置正常，点击“保存”，创建成功，显示在列表中
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言:限时列表中重复时间显示每周一
        self.driver.refresh()
        Repeat = LimitTimeLocators.Repeat.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Repeat))
        )
        assert self.driver.find_element_by_xpath(Repeat).text == "Monday"

        # 断言：判断开关是否默认开启。
        # 用例-2032 : 限时开关开启，可创建成功
        Statu = LimitTimeLocators.Statu.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Statu))
        )
        assert self.driver.find_element_by_xpath(Statu).get_attribute('class') == "switch switch-animation checked"


        # a=test_time_limit_add_1.test_ping()
        # print(1111111111111111111111)
        # print(a)
        # assert a == 1





    #@unittest.skip("跳过")
    def test_F_limitTime_edit_elementCheck(self):
        """限时-编辑-元素检查及默认值"""
        """
        用例-2034 : 编辑框-元素检测
                    查看元素 ： 开始时间、结束时间、限时开关
                               重复：每周一；每周二；每周三；每周四；每周五；每周六；每周日
                               按钮：取消、删除
        用例-2035 : 编辑框-默认显示创建时的值
                    分别查看以下项的值是否默认显示创建时配置的值：开始时间、结束时间、限时开关、重复项
        用例-2036 : 编辑框-点击”取消“，编辑框关闭，不保存修改
                    进入限时列表
                    点击“编辑”按钮进入编辑页面
                    把旧的限时时间A改为限时时间B
                    点击“取消”按钮，不保存配置 ：返回限时列表
                                               编辑的限时条目不发生变化仍旧为时间A
        """
        # 点击 编辑 按钮
        Edit = LimitTimeLocators.Edit.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Edit))
        ).click()
        time.sleep(1)
        # 断言：限时开关-元素检查及默认值（开）
        assert self.driver.find_element_by_xpath("//div[@class='modal-form']/div[1]/label").text == "Time Limit"
        Insert_Statu_class = self.driver.find_element_by_xpath(LimitTimeLocators.Insert_Statu).get_attribute('class')
        assert Insert_Statu_class == "switch switch-animation checked", Insert_Statu_class

        # 断言：断网时间-元素检查及默认值（14:51）
        assert self.driver.find_element_by_xpath("//div[@class='modal-form']/div[2]/label").text == "Cut off time"
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Insert_CutOffTime_Form))
        ).click()
        Hour_class = self.driver.find_element_by_xpath("//div[@class='combobox']/div/div[1]/ul/li[15]").get_attribute('class')
        Minute_class = self.driver.find_element_by_xpath("//div[@class='combobox']/div/div[2]/ul/li[52]").get_attribute('class')
        assert Hour_class == "selected", Hour_class
        assert Minute_class == "selected", Minute_class
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Form_Confirm))
        ).click()

        # 断言：恢复时间-元素检查及默认值（23:59）
        assert self.driver.find_element_by_xpath("//div[@class='modal-form']/div[3]/label").text == "Recovery time"
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Insert_RecoveryTime_Form))
        ).click()
        Hour_class = self.driver.find_element_by_xpath("//div[@class='combobox']/div/div[1]/ul/li[24]").get_attribute('class')
        Minute_class = self.driver.find_element_by_xpath("//div[@class='combobox']/div/div[2]/ul/li[60]").get_attribute('class')
        assert Hour_class == "selected", Hour_class
        assert Minute_class == "selected", Minute_class
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Form_Confirm))
        ).click()

        # 断言：重复项-元素检查及默认值（默认只选择星期一）
        assert self.driver.find_element_by_xpath("//div[@class='modal-form']/div[4]/label").text == "Repeat"

        Mondey_class = self.driver.find_element_by_xpath(LimitTimeLocators.Weeks.format(num=1)).get_attribute('class')
        assert Mondey_class == "box checked"
        i = 2
        while i <= 7:
            Data_class = self.driver.find_element_by_xpath(LimitTimeLocators.Weeks.format(num=i)).get_attribute('class')
            assert Data_class == "box"
            i += 1

        # 修改恢复时间：由23:59改为23:00
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Insert_RecoveryTime_Form))
        ).click()
        Hour_23 = LimitTimeLocators.Hour.format(num=23)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Hour_23))
        ).click()
        Minute_0 = LimitTimeLocators.Minute.format(num=0)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Minute_0))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Form_Confirm))
        ).click()

        # 断言：用例-2036 : 编辑框-点击”取消“，编辑框关闭，不保存修改
        # 点击 取消 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Insert_Cancel))
        ).click()
        self.driver.refresh()
        # 检验恢复时间是否还是：23：59
        Recovery_Time = LimitTimeLocators.Recovery_Time.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, Recovery_Time))
        )
        Recovery_Time_text = self.driver.find_element_by_xpath(Recovery_Time).text
        assert Recovery_Time_text == "23:59", Recovery_Time_text
        time.sleep(2)





    #@unittest.skip("跳过")
    def test_G_limitTime_editValue(self):
        """限时-编辑-修改参数值"""
        """
        用例-2013 : 点击“编辑”按钮弹出编辑框
        用例-2038 : 编辑框-修改内容，点击“保存”，编辑框关闭，列表显示修改后的值
                    编辑框修改（时间，开关，重复项）等，点击“确定”后查看是否如下 
                    编辑框关闭、列表更新成新修改的值: 是
        """
        # 点击 编辑 按钮
        Edit = LimitTimeLocators.Edit.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Edit))
        ).click()
        # 取消 星期一，选择 星期二
        Mondey = LimitTimeLocators.Weeks.format(num=1)
        Tuesday = LimitTimeLocators.Weeks.format(num=2)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Mondey))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Tuesday))
        ).click()
        # 点击 新增 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Insert_Add))
        ).click()

        # 断言:是否操作成功：保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言:判断是否只选中的星期二
        self.driver.refresh()
        Repeat = LimitTimeLocators.Repeat.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Repeat))
        )
        assert self.driver.find_element_by_xpath(Repeat).text == "Tuesday"

        # 断言：判断开关是否默认开启
        Statu = LimitTimeLocators.Statu.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Statu))
        )
        assert self.driver.find_element_by_xpath(Statu).get_attribute('class') == "switch switch-animation checked"






    #@unittest.skip("跳过")
    def test_I_limitTime_editStatu(self):
        """限时-列表中修改状态：由开变为关"""
        """
        用例-2012 : 限时列表开关按钮可正常开启关闭
                    限时列表，点击开启按钮，看是否可正常开启，关闭 ： 是
        """
        # 点击 开关 按钮，由开变为关
        Statu = LimitTimeLocators.Statu.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Statu))
        ).click()
        # 断言:toast提示：关闭成功
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言：开关状态是否为：关闭
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, Statu))
        )
        assert self.driver.find_element_by_xpath(Statu).get_attribute('class') == "switch switch-animation"








    #@unittest.skip("跳过")
    def test_O_limitTime_delete(self):
        """限时-删除限时记录"""
        flag = False
        while flag == False:
            try:
                assert self.driver.find_element_by_xpath(LimitTimeLocators.List_Null).is_displayed()
                flag = True
            except:
                Delete = LimitTimeLocators.Delete.format(num="last()")
                WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                    EC.element_to_be_clickable((By.XPATH, Delete))
                ).click()
                # 断言:toast提示：成功
                WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                    EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
                )
                time.sleep(2)




def core():
    s = []
    class_tests = [
        # 建议执行顺序（倒序排如下）：
        # 管理路由器、管理密码、工作方式、限时（？如果被限制住未删掉情况怎么处理）
        LimitTime
    ]

    for t in class_tests:
        suite = TestLoader().loadTestsFromTestCase(t)
        s.append(suite)
    t_s = unittest.TestSuite(s)
    return t_s



if __name__ == "__main__":
    t_suites = core()
    result = BeautifulReport(t_suites)
    log_path = 'report/router'
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    result.report(filename="路由器功能自动化测试",
                  description="路由器功能自动化测试报告",
                  log_path=log_path)