#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/20 21:02
# @Author:  GaoJun

"""DDNS"""
class DDNSLocators(object):
    # 服务提供商
    Service_Provider_DynDNS = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div[1]/div[1]"
    Service_Provider_Oray = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[1]"
    # 域名
    Domain_Name = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/input"
    # 用户名
    Username = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[3]/div/div/div/input"
    # 密码
    Password = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[4]/div/div/div[1]/input"
    # 启用
    Statu = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[5]/div/label/div[1]"
    # 保存
    Save = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[2]/button"
