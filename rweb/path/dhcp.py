#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/20 19:12
# @Author:  GaoJun

"""DHCP"""
class DhcpLocators(object):
    Lan_Ip = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/input"

    # 开始网段 与 结束网段
    IpPool_Start_NetwordSegment = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div[1]/div/div/div/input[1]"
    IpPool_End_NetwordSegment = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div/div/input[1]"

    # 地址池 开始的ip 与 结束的ip
    IpPool_StartIp = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div[1]/div/div/div/input[2]"
    IpPool_EndIp = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div/div/input[2]"

    Lease_Time = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[3]/div/div/input"
    Lease_Time_1day = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[3]/div/div/ul/li[5]"
    Save = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[2]/button"
    Save_Ok = "/html/body/div[3]/div/div[2]/button[2]"