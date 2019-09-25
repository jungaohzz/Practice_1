#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun


from .test_base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from rweb.path.common import CommonLocators
from rweb.path.timeZone import TimeZoneLocators

class TimeZone(Base):

    def test_A_timeZone_set_Chinese(self):
        """时区-设置中国时区"""
        # 点击 设置
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.LEVEL_1_Set))
        ).click()
        # 点击 时区
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.LEVEL_1_Set_Timezone))
        ).click()
        # 点击 时区框
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, TimeZoneLocators.TimeZone))
        ).click()
        # 选择 中国时区
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, TimeZoneLocators.TimeZone_Chinese))
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





