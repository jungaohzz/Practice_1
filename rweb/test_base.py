#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun


import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from . import const
from rweb.path.common import CommonLocators


class Base(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(const.URL)
        self.driver.maximize_window()

        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.InputPassword))
        ).send_keys(const.PASSWORD)

        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Login))
        ).click()
        time.sleep(0.5)


    def tearDown(self):
        self.driver.quit()
