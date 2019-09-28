#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/20 22:42
# @Author:  GaoJun

"""网络诊断"""
class NetworkDiagnosisLocators(object):
    # 诊断工具
    Diagnostics_Tools = "//div[@class='form']/div[1]/div/div/input"
    Ping = "//div[@class='form']/div[1]/div/div/ul/li[1]"
    Traceroute = "//div[@class='form']/div[1]/div/div/ul/li[2]"
    Nslookup = "//div[@class='form']/div[1]/div/div/ul/li[3]"

    IP_or_DomainName = "//div[@class='form']/div[2]/div/div/div/input"

    Start = "//button[@class='btn btn-primary']"