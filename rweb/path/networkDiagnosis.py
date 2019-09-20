#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/20 22:42
# @Author:  GaoJun

"""网络诊断"""
class NetworkDiagnosisLocators(object):
    # 诊断工具
    Diagnostics_Tools = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/input"
    Ping = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/ul/li[1]"
    Traceroute = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/ul/li[2]"
    Nslookup = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/ul/li[3]"

    IP_or_DomainName = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/input"

    Start = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[2]/button"