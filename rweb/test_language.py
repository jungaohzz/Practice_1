#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun


from selenium import webdriver
from .test_base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from rweb.path.common import CommonLocators
from rweb.path.routerManagement import RouterManagementLocators

class Language(Base):

    def test_A_set_English(self):
        """语言-成功切换为英文"""
        # time.sleep(1)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_MyWifi))
        )
        # 检验3个地方
        assert self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_MyWifi).text == "My WiFi", CommonLocators.LEVEL_1_MyWifi
        assert self.driver.find_element_by_xpath(RouterManagementLocators.Mesh_Topology).text == "Mesh Topology", RouterManagementLocators.Mesh_Topology
        assert self.driver.find_element_by_xpath(CommonLocators.Logout).text == "Logout", CommonLocators.Logout

    def test_B_set_Chinese(self):
        """语言-成功切换为为中文"""
        # 鼠标移动到切换语言的按钮上
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Language))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.Language)
        ActionChains(self.driver).move_to_element(mouse).perform()

        # 切换为中文
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Language_Chinese))
        ).click()

        # 检验3个地方
        assert self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_MyWifi).text == "我的WiFi", CommonLocators.LEVEL_1_MyWifi
        assert self.driver.find_element_by_xpath(RouterManagementLocators.Mesh_Topology).text == "Mesh拓扑图", RouterManagementLocators.Mesh_Topology
        assert self.driver.find_element_by_xpath(CommonLocators.Logout).text == "退出登录", CommonLocators.Logout

    def test_C_set_Deutsch(self):
        """语言-成功切换为德文"""
        # 鼠标移动到切换语言的按钮上
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Language))
        )
        mouse = self.driver.find_element_by_xpath(CommonLocators.Language)
        ActionChains(self.driver).move_to_element(mouse).perform()

        # 切换为德文
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Language_Deutsch))
        ).click()

        # 检验3个地方
        assert self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_MyWifi).text == "Mein WLAN", CommonLocators.LEVEL_1_MyWifi
        assert self.driver.find_element_by_xpath(RouterManagementLocators.Mesh_Topology).text == "Netzwerk Topologie", RouterManagementLocators.Mesh_Topology
        assert self.driver.find_element_by_xpath(CommonLocators.Logout).text == "Ausloggen", CommonLocators.Logout

