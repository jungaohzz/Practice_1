#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/20 21:02
# @Author:  GaoJun

"""DDNS"""
class DDNSLocators(object):
    # 服务提供商
    "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div[1]"
    Service_Provider_DynDNS = "//div[@class='form']/div[1]/div/div[1]"
    Service_Provider_Oray = "//div[@class='form']/div[1]/div/div[2]"
    # 域名
    Domain_Name = "//div[@class='form']/div[2]/div/div/div/input"
    # 用户名
    Username = "//div[@class='form']/div[3]/div/div/div/input"
    # 密码
    Password = "//div[@class='form']/div[4]/div/div/div/input"
    # 启用
    Statu = "//label/div[1]"
    # 保存
    Save = "//button[@class='btn']"
