#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/20 20:50
# @Author:  GaoJun

"""WiFi设置"""
class WifiSettingsLocators(object):
    # 无线名称
    Wifi_Name = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/input"
    # 加密方式
    Encryption_Button = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/input"

    # 无线密码
    WiFi_Password = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[3]/div/div/div[1]/input"
    # 隐藏SSID
    Hide_SSID = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[4]/div/div"
    # 双频合一
    Smart_Connect = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[5]/div/div/div"

    Save = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[2]/button"
    Save_Ok = "/html/body/div[3]/div/div[2]/button[2]"