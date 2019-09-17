#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun


import unittest
from selenium import webdriver
import time

class Login(unittest.TestCase):
    # 初始化，打开浏览器并登陆
    @classmethod
    def setUpClass(cls) :
        #打开浏览器
        p = "F:\chromedriver.exe"
        driver = webdriver.Chrome(p)
        driver.get('http://mywifi.mercku.tech/#/login')
        time.sleep(2)
        driver.maximize_window()
        time.sleep(1)
        #登陆系统
        driver.find_element_by_xpath("//input").send_keys("11111111")
        driver.find_element_by_xpath("//button[@class='btn']").click()
        time.sleep(5)


