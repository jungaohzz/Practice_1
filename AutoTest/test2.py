#!/usr/bin/python
# -*- coding: utf-8 -*-

# Time  :  2019/7/24 13:43
# Author:  GaoJun


import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 键盘操作
from selenium.webdriver.common.action_chains import ActionChains  # 鼠标事件


# 这是测试百度登录


class Baidulogin(unittest.TestCase):
    def setUp(self):
        p = "F:\chromedriver.exe"
        self.driver = webdriver.Chrome(p)
        self.driver.get("https://www.baidu.com/")
        time.sleep(3)
        self.driver.get_screenshot_as_file("D:\\1.png")
        self.driver.refresh()

        self.driver.maximize_window()
        time.sleep(2)

    # def test_login(self):
    #     # 点击首页登录按钮
    #     element1 = self.driver.find_element_by_xpath("//div[@id='u1']/a[@name='tj_login']")
    #     element1.click()
    #     time.sleep(5)
    #
    #     # 点击用户名登录
    #     element2 = self.driver.find_element_by_xpath("//p[@data-type='normal']")
    #     element2.click()
    #     time.sleep(5)
    #
    #     # 不输入账号和密码点击登录按钮
    #     element3 = self.driver.find_element_by_xpath("//input[@id='TANGRAM__PSP_10__submit']")
    #     element3.click()
    #     time.sleep(5)

    def test_set(self):
        set_menu = self.driver.find_element_by_link_text("设置")
        ActionChains(self.driver).move_to_element(set_menu).perform()
        search_set = self.driver.find_element_by_xpath("//*[@id='wrapper']/div[6]/a[1]")
        ActionChains(self.driver).click(search_set).perform()
        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
