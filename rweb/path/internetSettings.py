#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/21 13:00
# @Author:  GaoJun

"""上网设置"""
class InternetSettingsLocators(object):
    # 上网方式
    Internet_Way = "//div[@class='form']/div[1]/div/div/input"
    # 动态IP
    DHCP = "//div[@class='form']/div[1]/div/div/ul/li[1]"

    # PPPoE
    PPPoE = "//div[@class='form']/div[1]/div/div/ul/li[2]"
    # 宽带账号
    PPPoE_Username = "//div[@class='form']/div[3]/div[1]/div/div/div/input"
    # 宽带密码
    PPPoE_Password = "//div[@class='form']/div[3]/div[2]/div/div/div/input"

    # 静态IP
    StaticIP = "//div[@class='form']/div[1]/div/div/ul/li[3]"
    # IP地址
    StaticIP_IP = "//div[@class='form']/div[4]/div[1]/div/div/div/input"
    # 子网掩码
    StaticIP_Netmask = "//div[@class='form']/div[4]/div[2]/div/div/div/input"
    # 网关
    StaticIP_Gateway = "//div[@class='form']/div[4]/div[3]/div/div/div/input"
    # DNS
    StaticIP_DNS = "//div[@class='form']/div[4]/div[4]/div/div/div/input"



    # 自动获取DNS
    DNS_Auto = "//div[@class='form']/div[2]/div[1]/div/div[1]/div[1]"
    # 手动设置DNS
    DNS_Manual = "//div[@class='form']/div[2]/div[1]/div/div[2]/div[1]"

    Save = "//button[@class='btn']"
    Save_Ok = "//div[@class='dialog-buttons']/button[2]"

    # 主页中，判断网络是否通的那根线
    Line = "//div[@class='dashboard']/div[1]/div/div[4]"