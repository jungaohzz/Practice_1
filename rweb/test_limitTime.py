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

from router.time_limit import test_time_limit_add_1



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
    def test_A_limitTime_null(self):
        """限时-列表为空检验"""
        """
        用例-2000 : 没有限时条目，显示列表为空
        """
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, LimitTimeLocators.List_Null))
        )
        List_Null_text = self.driver.find_element_by_xpath(LimitTimeLocators.List_Null).text
        assert List_Null_text == "Empty", List_Null_text



    #@unittest.skip("跳过")
    def test_B_limitTime_insert_check(self):
        """限时-新增框元素检查、默认值检查、重复时间为空保存有提示、取消则未新增成功"""
        """
        用例-2017 : 新增框-元素检测
                    查看页面元素包含哪些 : 限时开关
                                         断网时间、恢复时间
                                         重复：每周一、每周二、每周三、每周四、每周五、每周六、每周日
                                         按钮 : 取消、保存
        用例-2018 : 新增框-断网时间默认00:00
        用例-2019 : 新增框-恢复时间默认23:59
        用例-2020 : 新增框-限时开关默认为开启
        用例-2021 : 新增框-重复项默认都不勾选
        用例-2012 : 限时列表开关按钮可正常开启关闭
        用例-2027 : 新增框-重复时间为空，点击“保存”，有错误提示
                    输入框内容如下：开始时间为：22:00（这个时间可以随机）
                                  截止时间为：23:00（这个时间可以随机）
                                  重复时间为：未选择任何一项
                    保存是否成功：否，提示“请选择重复时间《trans0388》”
        用例-2026 : 新增框-点击取消按钮，关闭弹框，不添加成功
        """
        # 点击 新增 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Add))
        ).click()

        time.sleep(1)
        #断言：限时开关-元素检查及默认值（开）
        assert self.driver.find_element_by_xpath("//div[@class='modal-form']/div[1]/label").text == "Time Limit"
        Insert_Statu_class = self.driver.find_element_by_xpath(LimitTimeLocators.Insert_Statu).get_attribute('class')
        assert Insert_Statu_class == "switch switch-animation checked", Insert_Statu_class

        # 断言：用例-2012 : 限时列表开关按钮可正常开启、关闭
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Insert_Statu))
        ).click()
        Insert_Statu_class = self.driver.find_element_by_xpath(LimitTimeLocators.Insert_Statu).get_attribute('class')
        assert Insert_Statu_class == "switch switch-animation", Insert_Statu_class      #验证可关闭
        time.sleep(2)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Insert_Statu))
        ).click()
        Insert_Statu_class = self.driver.find_element_by_xpath(LimitTimeLocators.Insert_Statu).get_attribute('class')
        assert Insert_Statu_class == "switch switch-animation checked", Insert_Statu_class      #验证可开启

        # 断言：断网时间-元素检查及默认值（00:00）
        assert self.driver.find_element_by_xpath("//div[@class='modal-form']/div[2]/label").text == "Cut off time"
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Insert_CutOffTime_Form))
        ).click()
        Hour_class = self.driver.find_element_by_xpath("//div[@class='combobox']/div/div[1]/ul/li[1]").get_attribute('class')
        Minute_class = self.driver.find_element_by_xpath("//div[@class='combobox']/div/div[2]/ul/li[1]").get_attribute('class')
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

        # 断言：重复项-元素检查及默认值（默认都不勾选）
        assert self.driver.find_element_by_xpath("//div[@class='modal-form']/div[4]/label").text == "Repeat"
        i = 1
        while i <= 7:
            Data_class = self.driver.find_element_by_xpath(LimitTimeLocators.Weeks.format(num=i)).get_attribute('class')
            assert Data_class == "box"
            i += 1

        # 断言：用例-2027 : 新增框-重复时间为空，点击“保存”，有错误提示
        # 未选择重复时间，直接点击按钮 新增
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Insert_Add))
        ).click()
        Warning = self.driver.find_element_by_xpath("//div[@class='message']/span").text
        assert Warning == "Please select the repeated times", Warning

        # 断言：用例-2026 : 新增框-点击取消按钮，关闭弹框，不添加成功
        # 选择星期一
        Mondey = LimitTimeLocators.Weeks.format(num=1)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Mondey))
        ).click()
        # 点击 取消 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Insert_Cancel))
        ).click()
        self.driver.refresh()
        # 检验页面列表是否还是为空
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, LimitTimeLocators.List_Null))
        )
        List_Null_text = self.driver.find_element_by_xpath(LimitTimeLocators.List_Null).text
        assert List_Null_text == "Empty", List_Null_text





    #@unittest.skip("跳过")
    def test_C_limitTime_add(self):
        """限时-新增"""
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
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言:判断是否选中的星期一
        self.driver.refresh()
        Repeat = LimitTimeLocators.Repeat.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Repeat))
        )
        assert self.driver.find_element_by_xpath(Repeat).text == "Monday"

        # 断言：判断开关是否默认开启
        Statu = LimitTimeLocators.Statu.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Statu))
        )
        assert self.driver.find_element_by_xpath(Statu).get_attribute('class') == "switch switch-animation checked"


        # a=test_time_limit_add_1.test_ping()
        # print(1111111111111111111111)
        # print(a)
        # assert a == 1

   # @unittest.skip("跳过")
    def test_D_limitTime_time_style(self):
        """限时-时间显示格式为24小时制"""
        """
        用例-2001 : 截止时间，恢复时间列表显示格式为24小时制
                    配置截止时间和恢复时间为14:59，看列表中截止时间和恢复时间是否显示14:59
        """
        # 断网时间点
        Cut_off_time = LimitTimeLocators.Cut_Off_Time.format(num="last()")
        Cut_off_time_value = self.driver.find_element_by_xpath(Cut_off_time).text
        assert Cut_off_time_value == "14:51", Cut_off_time_value

        # 恢复时间点
        Recovery_time = LimitTimeLocators.Recovery_Time.format(num="last()")
        Recovery_time_value = self.driver.find_element_by_xpath(Recovery_time).text
        print(111111)
        print(Recovery_time_value)
        assert Recovery_time_value == "23:59", Recovery_time_value





    #@unittest.skip("跳过")
    def test_E_limitTime_elementAssert(self):
        """限时-页面元素检测"""
        """
        用例-1999：列表页面元素检测
                  列表标题：断网时间，恢复时间，重复，操作
                  列表内容：断网时间点，恢复时间点，重复天，开启关闭按钮，编辑按钮，删除按钮
                  新增按钮
        """

        # 断网时间
        Head_Cut_off_time = LimitTimeLocators.Table_Heads.format(num=1)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, Head_Cut_off_time))
        )
        Head_Cut_off_time_text = self.driver.find_element_by_xpath(Head_Cut_off_time).text
        assert Head_Cut_off_time_text == "Cut off time", Head_Cut_off_time_text

        # 恢复时间
        Head_Recovery_time = LimitTimeLocators.Table_Heads.format(num=2)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, Head_Recovery_time))
        )
        Head_Recovery_time_text = self.driver.find_element_by_xpath(Head_Recovery_time).text
        assert Head_Recovery_time_text == "Recovery time", Head_Recovery_time_text

        # 重复
        Head_Repeat = LimitTimeLocators.Table_Heads.format(num=3)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, Head_Repeat))
        )
        Head_Repeat_text = self.driver.find_element_by_xpath(Head_Repeat).text
        assert Head_Repeat_text == "Repeat", Head_Repeat_text

        # 操作
        Head_Actions = LimitTimeLocators.Table_Heads.format(num=4)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, Head_Actions))
        )
        Head_Actions_text = self.driver.find_element_by_xpath(Head_Actions).text
        assert Head_Actions_text == "Actions", Head_Actions_text

        time.sleep(2)

        # 断网时间点
        Cut_off_time = LimitTimeLocators.Cut_Off_Time.format(num="last()")
        assert self.driver.find_element_by_xpath(Cut_off_time).is_displayed()

        # 恢复时间点
        Recovery_time = LimitTimeLocators.Cut_Off_Time.format(num="last()")
        assert self.driver.find_element_by_xpath(Recovery_time).is_displayed()

        # 重复天
        Repeat = LimitTimeLocators.Repeat.format(num="last()")
        assert self.driver.find_element_by_xpath(Repeat).is_displayed()
        # 开启关闭按钮
        Statu = LimitTimeLocators.Statu.format(num="last()")
        assert self.driver.find_element_by_xpath(Statu).is_displayed()

        # 编辑按钮
        Edit = LimitTimeLocators.Edit.format(num="last()")
        assert self.driver.find_element_by_xpath(Edit).is_displayed()

        # 删除按钮
        Delete = LimitTimeLocators.Edit.format(num="last()")
        assert self.driver.find_element_by_xpath(Delete).is_displayed()

        # 新增按钮
        Insert = LimitTimeLocators.Edit.format(num="last()")
        assert self.driver.find_element_by_xpath(Insert).is_displayed()




    #@unittest.skip("跳过")
    def test_F_limitTime_edit_value(self):
        """限时-编辑-修改参数值"""
        """
        用例-2013 : 点击“编辑”按钮弹出编辑框
        
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
    def test_G_limitTime_add_Weekdays(self):
        """限时-新增-重复时间为周一 ~ 周五，显示为：Weekdays"""
        """
        用例-2009 : 添加一条重复时间为每周一，每周二，每周三，每周四，每周五条目，限时列表中重复时间显示Weekdays
                    添加一条重复时间为每周一，每周二，每周三，每周四，每周五的条目并保存成功
                    时间列表中显示重复时间是否为Weekdays：是
        """
        # 点击 新增 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Add))
        ).click()

        # 选择断网时间：14:52
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Insert_CutOffTime_Form))
        ).click()
        Hour_14 = LimitTimeLocators.Hour.format(num=14)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Hour_14))
        ).click()
        Minute_52 = LimitTimeLocators.Minute.format(num=52)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Minute_52))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Form_Confirm))
        ).click()

        # 重复时间选择：周一到周五
        i = 1
        while i <= 5:
            Date = LimitTimeLocators.Weeks.format(num=i)
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, Date))
            ).click()
            i += 1
        # 点击 新增 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Insert_Add))
        ).click()
        # 断言:是否操作成功：保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言:判断重复处是否显示：Weekdays
        self.driver.refresh()
        Repeat = LimitTimeLocators.Repeat.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Repeat))
        )
        Repeat_value = self.driver.find_element_by_xpath(Repeat).text
        assert Repeat_value == "Weekdays", Repeat_value

    #@unittest.skip("跳过")
    def test_H_limitTime_add_Everyday(self):
        """限时-新增-重复时间每天，显示为：Everyday"""
        """
        用例-2011 : 添加一条重复时间为每天条目，限时列表中重复时间显示每天
                    添加一条重复时间为每天的条目并保存成功
                    时间列表中显示重复时间是否为每天：是
        """
        # 点击 新增 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Add))
        ).click()
        # 选择断网时间：14:53
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Insert_CutOffTime_Form))
        ).click()
        Hour_14 = LimitTimeLocators.Hour.format(num=14)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Hour_14))
        ).click()
        Minute_53 = LimitTimeLocators.Minute.format(num=53)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Minute_53))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Form_Confirm))
        ).click()
        # 重复时间选择：每天
        i = 1
        while i <= 7:
            Date = LimitTimeLocators.Weeks.format(num=i)
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, Date))
            ).click()
            i += 1
        # 点击 新增 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Insert_Add))
        ).click()
        # 断言:是否操作成功：保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言:判断重复处是否显示：Weekdays
        self.driver.refresh()
        Repeat = LimitTimeLocators.Repeat.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Repeat))
        )
        Repeat_value = self.driver.find_element_by_xpath(Repeat).text
        assert Repeat_value == "Everyday", Repeat_value




    #@unittest.skip("跳过")
    def test_I_limitTime_add_Everyday(self):
        """限时-新增-重复时间为任意6天，显示具体的星期"""
        """
        用例-2010 : 添加一条重复时间为任意6天，限时列表中重复时间显示为勾选的6天
                    添加一条重复时间为任意6天（例：每周一，每周二，每周三，每周四，每周五，每周六）的条目并保存成功
                    时间列表中显示重复时间是否显示的勾选的6天（例：每周一，每周二，每周三，每周四，每周五，每周六）：是
        """
        # 点击 新增 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Add))
        ).click()
        # 选择断网时间：14:54
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Insert_CutOffTime_Form))
        ).click()
        Hour_14 = LimitTimeLocators.Hour.format(num=14)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Hour_14))
        ).click()
        Minute_54 = LimitTimeLocators.Minute.format(num=54)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Minute_54))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Form_Confirm))
        ).click()
        # 重复时间选择：周一 到 周六
        i = 1
        while i <= 6:
            Date = LimitTimeLocators.Weeks.format(num=i)
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, Date))
            ).click()
            i += 1
        # 点击 新增 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Insert_Add))
        ).click()
        # 断言:是否操作成功：保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言:判断重复处是否显示：Weekdays
        self.driver.refresh()
        Repeat = LimitTimeLocators.Repeat.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Repeat))
        )
        Repeat_value = self.driver.find_element_by_xpath(Repeat).text
        assert Repeat_value == "Monday / Tuesday / Wednesday / Thursday / Friday / Saturday", Repeat_value

    #@unittest.skip("跳过")
    def test_J_limitTime_add_OtherMondey(self):
        """限时-新增-再添加一个星期一，显示2个星期一"""
        # 点击 新增 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Add))
        ).click()
        # 选择断网时间：14:55
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Insert_CutOffTime_Form))
        ).click()
        Hour_14 = LimitTimeLocators.Hour.format(num=14)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Hour_14))
        ).click()
        Minute_55 = LimitTimeLocators.Minute.format(num=55)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Minute_55))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Form_Confirm))
        ).click()
        Mondey = LimitTimeLocators.Weeks.format(num=1)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Mondey))
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

    #@unittest.skip("跳过")
    def test_K_limitTime_edit_statu(self):
        """限时-编辑-修改状态：由开变为关"""
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
    def test_L_limitTime_delete(self):
        """限时-删除"""
        i = 1
        while i <= 5:
            Delete = LimitTimeLocators.Delete.format(num="last()")
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, Delete))
            ).click()
            # 断言:toast提示：成功
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
            time.sleep(2)
            i += 1



