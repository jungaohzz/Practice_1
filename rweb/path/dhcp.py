#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/20 19:12
# @Author:  GaoJun

"""DHCP"""
class DhcpLocators(object):
    Lan_Ip = "//div[@class='form']/div[1]/div/div/div/input"

    # 开始网段 与 结束网段
    IpPool_Start_NetwordSegment = "//div[@class='form']/div[2]/div/div[1]/div/div/div/input[1]"
    IpPool_End_NetwordSegment = "//div[@class='form']/div[2]/div/div[2]/div/div/div/input[1]"

    # 地址池 开始的ip 与 结束的ip
    IpPool_StartIp = "//div[@class='form']/div[2]/div/div[1]/div/div/div/input[2]"
    IpPool_EndIp = "//div[@class='form']/div[2]/div/div[2]/div/div/div/input[2]"

    Lease_Time = "//div[@class='select']/input"
    Lease_Time_1day = "//div[@class='select']/ul/li[5]"
    Save = "//button[@class='btn']"
    Save_Ok = "//div[@class='dialog-buttons']/button[2]"