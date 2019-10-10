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


# 这是测试百度登录


class Baidulogin(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        # time.sleep(3)
        #
        # self.driver.refresh()

        self.driver.maximize_window()

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
        filepath = r"G:\DJ.mp3"
        pygame.mixer.init()
        # 加载音乐
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play(start=0.0)
        pygame.mixer.music.set_volume(1.0)
        # 播放时长，没有此设置，音乐不会播放，会一次性加载完
        time.sleep(300)
        pygame.mixer.music.stop()




if __name__ == '__main__':
    unittest.main()
