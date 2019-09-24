#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/21 13:00
# @Author:  GaoJun

"""上网设置"""
class InternetSettingsLocators(object):
    # 上网方式
    Internet_Way = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/div/input"
    # 动态IP
    DHCP = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/div/ul/li[1]"

    # PPPoE
    PPPoE = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/div/ul/li[2]"
    # 宽带账号
    PPPoE_Username = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[2]/div[3]/div[1]/div/div/div/input"
    # 宽带密码
    PPPoE_Password = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/input"

    # 静态IP
    StaticIP = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/div/ul/li[3]"
    # IP地址
    StaticIP_IP = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[2]/div[4]/div[1]/div/div/div/input"
    # 子网掩码
    StaticIP_Netmask = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[2]/div[4]/div[2]/div/div/div/input"
    # 网关
    StaticIP_Gateway = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[2]/div[4]/div[3]/div/div/div/input"
    # DNS
    StaticIP_DNS = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[2]/div[4]/div[4]/div/div/div/input"



    # 自动获取DNS
    DNS_Auto = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[1]"
    # 手动设置DNS
    DNS_Manual = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[1]"

    Save = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[2]/div[5]/button"
    Save_Ok = "/html/body/div[3]/div/div[2]/button[2]"

    # 主页中，判断网络是否通的那根线
    Line = "/html/body/div[1]/div/div/div/div[1]/div[1]/div/div[4]"