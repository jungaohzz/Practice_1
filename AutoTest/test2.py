#!/usr/bin/python
# -*- coding: utf-8 -*-

# Time  :  2019/7/24 13:43
# Author:  GaoJun


import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 键盘操作
from selenium.webdriver.common.action_chains import ActionChains  # 鼠标事件
import pygame
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# 这是测试百度登录


class Baidulogin(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        # time.sleep(3)
        #
        # self.driver.refresh()

        self.driver.maximize_window()

    def test_login(self):
        # 点击首页登录按钮
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='u1']/a[@name='tj_login']"))
        )
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='u1']/a[@name='tj_login']"))
        ).click()

        time.sleep(5)

        # 点击用户名登录
        element2 = self.driver.find_element_by_xpath("//p[@data-type='normal']")
        element2.click()
        time.sleep(5)

        # 不输入账号和密码点击登录按钮
        element3 = self.driver.find_element_by_xpath("//input[@id='TANGRAM__PSP_10__submit']")
        element3.click()
        time.sleep(5)



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
