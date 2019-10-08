#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun


from .test_base import Base
import unittest
from . import const
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time
from rweb.path.common import CommonLocators
from rweb.path.timeZone import TimeZoneLocators

class TimeZone(Base):

    def setUp(self):
        super(TimeZone, self).setUp()
        # 鼠标移动到切换“设置”按钮上
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_Set))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_Set)
        ActionChains(self.driver).move_to_element(mouse).perform()
        # 点击 时区
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Timezone))
        ).click()
        self.driver.refresh()




    #@unittest.skip("跳过")
    def test_A_timeZone_elementCheck(self):
        """时区-元素检查"""
        """
        用例-1635 : 页面元素检测
                    查看页面元素，是否包括 ：label: 当前时区
                                            当前显示的具体时区
                                            label：修改时区
                                            时区选择下拉框
                                            确定按钮
        """
        # 断言：是否包括：当前显示的具体时区（默认值显示为美国）
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))
        )
        Timezone_Value = self.driver.find_element_by_tag_name("input").get_attribute('value')
        assert Timezone_Value == "(GMT-05:00)Eastern Time (US & Canada)", Timezone_Value

        # 断言：是否包括：label: 当前时区
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, TimeZoneLocators.TimeZone))
        ).click()
        TimeZone = TimeZoneLocators.TimeZone_All.format(num=12)
        time.sleep(1)
        Timezone_Class = self.driver.find_element_by_xpath(TimeZone).get_attribute("class")
        assert Timezone_Class == "selected", Timezone_Value

        # 断言：是否包括：时区选择下拉框（判断检验到所有下拉列表元素即可）
        i = 1
        while i <= 65:
            TimeZone_All = TimeZoneLocators.TimeZone_All.format(num=i)
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, TimeZone_All))
            )
            Each_Select = self.driver.find_element_by_xpath(TimeZone_All)
            assert Each_Select.is_displayed()
            i += 1

        # 断言：是否包括：label：修改时区(选择1个即作为判断)
        TimeZone = TimeZoneLocators.TimeZone_All.format(num=1)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, TimeZone))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))
        )
        timezone_value = self.driver.find_element_by_tag_name("input").get_attribute('value')
        assert timezone_value == "(GMT-12:00)Eniwetok, Kwajalein", timezone_value

        # 断言：是否包括：确定按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, TimeZoneLocators.Save))
        )
        Save_Button = self.driver.find_element_by_xpath(TimeZoneLocators.Save)
        assert Save_Button.is_displayed()





    #@unittest.skip("跳过")
    def test_B_timeZone_canSelect(self):
        """时区-正常下拉并选中"""
        """
        用例-1636 : 时区下拉框，能正常下拉并选中
                    点击下拉框 ： 显示下拉列表
                    点击选择某一个时区 ： 能选择成功，并显示出来
        """


        # 断言：用例-1636 : 时区下拉框，能正常下拉并选中
        # 点击3个时区进行检查
        # 第1个
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, TimeZoneLocators.TimeZone))
        ).click()
        TimeZone = TimeZoneLocators.TimeZone_All.format(num=1)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, TimeZone))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))
        )
        timezone_value = self.driver.find_element_by_tag_name("input").get_attribute('value')
        assert timezone_value == "(GMT-12:00)Eniwetok, Kwajalein", timezone_value

        # 第2个
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, TimeZoneLocators.TimeZone))
        ).click()
        TimeZone = TimeZoneLocators.TimeZone_All.format(num=35)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, TimeZone))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))
        )
        timezone_value = self.driver.find_element_by_tag_name("input").get_attribute('value')
        assert timezone_value == "(GMT+02:00)Jerusalem", timezone_value

        # 第3个
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, TimeZoneLocators.TimeZone))
        ).click()
        TimeZone = TimeZoneLocators.TimeZone_All.format(num=65)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, TimeZone))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))
        )
        timezone_value = self.driver.find_element_by_tag_name("input").get_attribute('value')
        assert timezone_value == "(GMT+12:00)Fiji, Kamchatka, Marshall Is.", timezone_value





    #@unittest.skip("跳过")
    def test_C_timeZone_selectFull(self):
        """时区-下拉框显示完整检查"""
        TimeZone_AllSelect = [
            "Eniwetok, Kwajalein", "Midway Island, Samoa", "Hawaii", "Alaska", "Pacific Time (US & Canada); Tijuana",
            "Arizona", "Mountain Time (US & Canada)", "Central Time (US & Canada)", "Mexico City, Tegucigalpa", "Saskatchewan",
            "Bogota, Lima, Quito", "Eastern Time (US & Canada)", "Indiana (East)", "Atlantic Time (Canada)", "Caracas, La Paz",
            "Santiago", "Newfoundland", "Brasilia", "Buenos Aires, Georgetown", "Mid-Atlantic",
            "Azores, Cape Verde Is.", "Casablanca, Monrovia", "Greenwich Mean Time: Dublin, Edinburgh, Lisbon, London", "Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna", "Belgrade, Bratislava, Budapest, Ljubljana, Prague",
            "Barcelona, Madrid", "Brussels, Copenhagen, Madrid, Paris, Vilnius", "Paris", "Sarajevo, Skopje, Sofija, Warsaw, Zagreb", "Athens, Istanbul, Minsk",
            "Bucharest", "Cairo", "Harare, Pretoria", "Helsinki, Riga, Tallinn", "Jerusalem",
            "Baghdad, Kuwait, Riyadh", "Moscow, St. Petersburg, Volgograd", "Mairobi", "Tehran", "Abu Dhabi, Muscat",
            "Baku, Tbilisi", "Kabul", "Ekaterinburg", "Islamabad, Karachi, Tashkent", "Mumbai, Calcutta, Madras, New Delhi",
            "Astana, Almaty, Dhaka", "Colombo", "Bangkok, Hanoi, Jakarta", "Beijing, Chongqing, Hong Kong, Urumqi", "Perth",
            "Singapore", "Taipei", "Osaka, Sapporo, Tokyo", "Seoul", "Yakutsk",
            "Adelaide", "Darwin", "Brisbane", "Canberra, Melbourne, Sydney", "Guam, Port Moresby",
            "Hobart", "Vladivostok", "Magadan, Solomon Is., New Caledonia", "Auckland, Wllington", "Fiji, Kamchatka, Marshall Is."
        ]
        # 点击 时区框
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, TimeZoneLocators.TimeZone))
        ).click()

        # 断言：时区所有选项完整
        i = 1
        while i <= 65:
            TimeZone_All = TimeZoneLocators.TimeZone_All.format(num=i)
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, TimeZone_All))
            )
            Select = self.driver.find_element_by_xpath(TimeZone_All).text[11:]
            assert Select == TimeZone_AllSelect[i-1], Select
            i += 1




    #@unittest.skip("跳过")
    def test_D_timeZone_save_ok_notEdit(self):
        """时区-未修改时区可成功保存"""
        # 直接点击 保存 按钮
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, TimeZoneLocators.Save))
        ).click()
        # 断言:toast提示：保存成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 判断是否还是默认是 美国 时区
        self.driver.refresh()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))
        )
        Timezone_Value = self.driver.find_element_by_tag_name("input").get_attribute('value')
        assert Timezone_Value == "(GMT-05:00)Eastern Time (US & Canada)", Timezone_Value





    #@unittest.skip("跳过")
    def test_E_timeZone_save_ok_edit(self):
        """时区-已修改时区可成功保存"""
        # 点击 时区框
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, TimeZoneLocators.TimeZone))
        ).click()
        # 选择 中国时区
        TimeZone_Chinese = TimeZoneLocators.TimeZone_All.format(num=49)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, TimeZone_Chinese))
        ).click()
        # 点击 保存
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, TimeZoneLocators.Save))
        ).click()
        # 断言:toast提示：保存成功
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 判断是否选中 中国 时区
        self.driver.refresh()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))
        )
        timezone_value = self.driver.find_element_by_tag_name("input").get_attribute('value')
        assert timezone_value == "(GMT+08:00)Beijing, Chongqing, Hong Kong, Urumqi", timezone_value

