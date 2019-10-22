#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/20 20:50
# @Author:  GaoJun

"""WiFi设置"""
class WifiSettingsLocators(object):
    # 无线名称
    Wifi_Name = "//div[@class='form']/div[1]/div/div/div/input"
    # 加密方式
    Encryption_Button = "//div[@class='form']/div[2]/div/div/input"
    Encryption_Options = "//div[@class='form']/div[2]/div/div/ul/li[{num}]"
    # 无线密码
    WiFi_Password = "//div[@class='form']/div[3]/div/div/div[1]/input"
    # 隐藏SSID
    Hide_SSID = "//div[@class='form']/div[4]/div/div"
    # 双频合一（加密方式不为空时）
    Smart_Connect = "//div[@class='form']/div[5]/div/div/div"
    #双频合一（加密方式为空时）
    Smart_Connect_whileOpen = "//div[@class='form']/div[4]/div/div/div"
    Save = "//button[@class='btn']"
    Save_Ok = "//div[@class='dialog-buttons']/button[2]"