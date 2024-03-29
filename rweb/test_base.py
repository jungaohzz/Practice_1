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
    # def setUp(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get(const.URL)
    #     self.driver.maximize_window()
    #
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, CommonLocators.InputPassword))
    #     ).send_keys(const.PASSWORD)
    #
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, CommonLocators.Login))
    #     ).click()
    #     time.sleep(0.5)
    #
    # def tearDown(self):
    #     self.driver.quit()

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(const.URL)
        cls.driver.maximize_window()

        WebDriverWait(cls.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.InputPassword))
        ).send_keys(const.PASSWORD)

        WebDriverWait(cls.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Login))
        ).click()
        time.sleep(0.5)

        # if True:
        #     try:
        #         WebDriverWait(cls.driver, const.MEDIUM_WAIT).until(
        #             EC.element_to_be_clickable((By.XPATH, CommonLocators.Cancel))
        #         ).click()
        #         time.sleep(0.5)
        #     except:
        #         print("没有升级弹窗")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
