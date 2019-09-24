#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun

"""访客WiFi"""


class GuestWifiLocators(object):
    Satatu = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div/div"
    Settings = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div[4]/button"


    # 有效时长
    Active_Time = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div/div/input"
    Active_Time_1day = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div/div/ul/li[2]"
    # 无线名称
    Name = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div/input"
    # 加密方式
    Encryption = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div[3]/div/div/input"
    Encryption_WPA_WPA2_PSK = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div[3]/div/div/ul/li[2]"
    # 无线密码
    Password = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div[4]/div/div/div[1]/input"
    # 双频合一
    Smart_Connect = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div[5]/div/div"

    Save = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div[7]/button"
    Save_Ok = "/html/body/div[3]/div/div[2]/button[2]"