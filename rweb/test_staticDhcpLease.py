#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun


from .test_base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from rweb.path.homePage import HomePageLocators
from rweb.path.devices import DevicesLocators
from rweb.path.limitTime import LimitTimeLocators
from selenium.webdriver.common.action_chains import ActionChains



# Mac与IP绑定

class StaticDHCPLease(Base):
    def test_limit_time(self):
        """新增绑定"""


        # 鼠标移动到切换语言的按钮上
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, HomePageLocators.LEVEL_1_AdvancedSettings))
        )
        mouse = self.driver.find_element_by_xpath(HomePageLocators.LEVEL_1_AdvancedSettings)
        ActionChains(self.driver).move_to_element(mouse).perform()

        # 点击 Mac与IP绑定
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, HomePageLocators.Static_DHCP_Lease))
        ).click()
        time.sleep(1)
        i=1
        while i<=30:

            # 点击 新增
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div[2]/button[1]"))
            ).click()
            # 设置名称
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/input"))
            ).send_keys(i)
            # 设置Mac地址
            mac_end = hex(i+20)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[3]/div/div/div/input"))
            ).send_keys("b4:0b:44:e2:37:"+mac_end[2:])
            # 设置IP地址
            ip_end=110+i
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[4]/div/div/div/input"))
            ).send_keys("192.168.127."+"%d"%ip_end)
            # 点击 保存
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div[2]/button"))
            ).click()
            i+=1
            time.sleep(2)
