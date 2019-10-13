#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun

from BeautifulReport import BeautifulReport
import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tkinter import messagebox
import pygame   # 播放器



class Base(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://yz.chsi.com.cn/apply/bmxx/sep7.do")
        self.driver.maximize_window()

    def test_baoming(self):
        # # 输入账号并登陆（杨蕾的）
        # WebDriverWait(self.driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//div[@class='yz-main']/div/form/div[2]/input"))
        # ).send_keys("51138119970211857X")
        # WebDriverWait(self.driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//input[@id='password']"))
        # ).send_keys("23611130622")
        # WebDriverWait(self.driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//div[@class='yz-main']/div/form/div[4]/input"))
        # ).click()

        # 输入账号并登陆（我的）
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='yz-main']/div/form/div[2]/input"))
        ).send_keys("15775969376")
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='password']"))
        ).send_keys("15775969376")
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='yz-main']/div/form/div[4]/input"))
        ).click()


        time.sleep(2)

        # 点击 首页
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='home mark']"))
        ).click()
        time.sleep(2)
        # 点击“填写报考信息”
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='app']/div[2]/div[2]/div/a/div/div[2]"))
        ).click()
        time.sleep(2)
        # 点击“阅读完毕”
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='yzwb-box']//button[@type='button']"))
        ).click()
        time.sleep(2)
        # 点击“同意”
        time.sleep(11)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='yzwb-box']//button[@type='button'][1]"))
        ).click()
        time.sleep(2)

        # 点击“确定”
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='t-center']/button[1]"))
        ).click()
        time.sleep(2)

        # 选择“招生单位”：四川、电子科大
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='ivu-row']/div[1]/div/div/select"))
        ).click()
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='ivu-row']/div[1]/div/div/select/option[24]"))
        ).click()
        time.sleep(5)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='ivu-row']/div[3]/div/div/select"))
        ).click()
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='ivu-row']/div[3]/div/div/select/option[10]"))
        ).click()
        time.sleep(1)

        # 选择“考试方式”
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='app']/div[3]/form/div[2]/div/select"))
        ).click()
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='app']/div[3]/form/div[2]/div/select/option[2]"))
        ).click()
        time.sleep(1)

        # 选择“专项计划”
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='app']/div[3]/form/div[3]/div/select"))
        ).click()
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='app']/div[3]/form/div[3]/div/select/option[2]"))
        ).click()
        time.sleep(1)

        # 选择“报考类别”
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='app']/div[3]/form/div[4]/div/select"))
        ).click()
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='app']/div[3]/form/div[4]/div/select/option[2]"))
        ).click()
        time.sleep(1)

        # 点击“下一步”
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='app']/div[3]/form/div[5]/div/button[2]"))
        ).click()
        time.sleep(1)

        # 点击“下一步”
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='app']/div[3]/form/div[3]/div/button[2]"))
        ).click()
        time.sleep(1)

        # 选择“报考院系所名称”
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='app']/div[1]/form[2]/div[2]/div[1]/div/select"))
        ).click()
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='app']/div[1]/form[2]/div[2]/div[1]/div/select/option[9]"))
        ).click()
        time.sleep(1)

        # 选择“报考专业”
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='app']/div[1]/form[2]/div[2]/div[2]/div/select"))
        ).click()
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='app']/div[1]/form[2]/div[2]/div[2]/div/select/option[2]"))
        ).click()
        time.sleep(1)

        # 选择“研究方向”
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='app']/div[1]/form[2]/div[2]/div[3]/div/select"))
        ).click()
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='app']/div[1]/form[2]/div[2]/div[3]/div/select/option[3]"))
        ).click()
        time.sleep(1)

        # 选择“学习方式”
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='app']/div[1]/form[2]/div[2]/div[4]/div/select"))
        ).click()
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='app']/div[1]/form[2]/div[2]/div[4]/div/select/option[2]"))
        ).click()
        time.sleep(1)

        # 选择“考试科目”
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='app']/div[1]/form[2]/div[2]/div[5]/div/select"))
        ).click()
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='app']/div[1]/form[2]/div[2]/div[5]/div/select/option[2]"))
        ).click()
        time.sleep(1)

        # 点击“下一步”
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='app']/div[1]/form[2]/div[4]/div/button[2]"))
        ).click()
        time.sleep(1)



        # 定时（20秒）刷新，检验是否还有位置
        i = 1
        while i <= 900:         # 1h执行180次，设置5h的量共900次

            WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='ivu-row']/div[1]/div/div/select"))
            )
            time.sleep(1)
            self.driver.find_element_by_xpath("//div[@class='ivu-row']/div[1]/div/div/select").click()

            WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='ivu-row']/div[1]/div/div/select/option[24]"))
            )
            time.sleep(1)
            self.driver.find_element_by_xpath("//div[@class='ivu-row']/div[1]/div/div/select/option[24]").click()

            time.sleep(2)

            WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='ivu-row']/div[3]/div/div/select"))
            )
            time.sleep(1)
            self.driver.find_element_by_xpath("//div[@class='ivu-row']/div[3]/div/div/select").click()
            time.sleep(1)
            zigong_text = self.driver.find_element_by_xpath("//div[@class='ivu-row']/div[3]/div/div/select/option[7]").text
            yibin_text = self.driver.find_element_by_xpath("//div[@class='ivu-row']/div[3]/div/div/select/option[18]").text
            if yibin_text != "5132(宜宾学院（本考点报名人数已满，请选择其他考点）)":

                # 播放音乐
                filepath = r"G:\DJ.mp3"
                pygame.mixer.init()
                # 加载音乐
                pygame.mixer.music.load(filepath)
                pygame.mixer.music.play(start=0.0)
                pygame.mixer.music.set_volume(1.0)
                # 播放时长，没有此设置，音乐不会播放，会一次性加载完


                self.driver.get_screenshot_as_file("G:\宜宾学院.png")
                time.sleep(0.5)
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[@class='ivu-row']/div[3]/div/div/select/option[18]"))
                )
                time.sleep(0.5)
                self.driver.find_element_by_xpath("//div[@class='ivu-row']/div[3]/div/div/select/option[18]").click()

                # # 点击 下一步
                # time.sleep(0.5)
                # WebDriverWait(self.driver, 10).until(
                #     EC.element_to_be_clickable((By.XPATH, "//div[@class='main-wrapper']/div[3]/form/div[2]/div/button[2]"))
                # )
                # time.sleep(0.5)
                # self.driver.find_element_by_xpath("//div[@class='main-wrapper']/div[3]/form/div[2]/div/button[2]").click()
                #
                # # 点击 “同意信息属实”
                # WebDriverWait(self.driver, 10).until(
                #     EC.element_to_be_clickable(
                #         (By.XPATH, "//input[@type='checkbox']"))
                # )
                # time.sleep(0.5)
                # self.driver.find_element_by_xpath("//input[@type='checkbox']").click()


                messagebox.showinfo("提示", "宜宾学院")
                time.sleep(20)
                pygame.mixer.music.stop()
                time.sleep(600)



            # elif zigong_text != "5114(四川轻化工大学(自贡校区) （本考点报名人数已满，请选择其他考点）)":
            #
            #     # 播放音乐
            #     filepath = r"G:\DJ.mp3"
            #     pygame.mixer.init()
            #     # 加载音乐
            #     pygame.mixer.music.load(filepath)
            #     pygame.mixer.music.play(start=0.0)
            #     pygame.mixer.music.set_volume(1.0)
            #     # 播放时长，没有此设置，音乐不会播放，会一次性加载完
            #
            #
            #     self.driver.get_screenshot_as_file("G:\轻化工大学.png")
            #     time.sleep(0.5)
            #     WebDriverWait(self.driver, 10).until(
            #         EC.element_to_be_clickable((By.XPATH, "//div[@class='ivu-row']/div[3]/div/div/select/option[7]"))
            #     )
            #     time.sleep(0.5)
            #     self.driver.find_element_by_xpath("//div[@class='ivu-row']/div[3]/div/div/select/option[7]").click()
            #
            #     # # 点击 下一步
            #     # time.sleep(0.5)
            #     # WebDriverWait(self.driver, 10).until(
            #     #     EC.element_to_be_clickable((By.XPATH, "//div[@class='main-wrapper']/div[3]/form/div[2]/div/button[2]"))
            #     # )
            #     # time.sleep(0.5)
            #     # self.driver.find_element_by_xpath("//div[@class='main-wrapper']/div[3]/form/div[2]/div/button[2]").click()
            #     #
            #     # # 点击 “同意信息属实”
            #     # WebDriverWait(self.driver, 10).until(
            #     #     EC.element_to_be_clickable(
            #     #         (By.XPATH, "//input[@type='checkbox']"))
            #     # )
            #     # time.sleep(0.5)
            #     # self.driver.find_element_by_xpath("//input[@type='checkbox']").click()
            #
            #     messagebox.showinfo("提示", "轻化工大学")
            #     pygame.mixer.music.stop()
            #     time.sleep(20)
            #     time.sleep(600)



            i += 1

            time.sleep(14)
            self.driver.refresh()










if __name__ == "__main__":

    # 先构造测试集，即实例化测试套件
    suite = unittest.TestSuite()

    #将用例加载到测试套件中
    suite.addTest(Base('test_baoming'))

    result = BeautifulReport(suite)
    result.report(filename='报名', description='报名', log_path='report')
