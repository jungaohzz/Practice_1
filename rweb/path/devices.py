#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun

"""接入设备"""

class DevicesLocators(object):

    """主网列表"""
    MyWifi = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div[1]"
    # 操作-设置按钮
    Set = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div/ul[1]/li[7]/span[1]"


    """访客列表"""
    Guest = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div[2]"



    """离线列表"""
    Offline = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div[3]"
    Offline_Deletes = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div/div[2]/button"
    Offline_Choose_All = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div[1]/ul/li[1]/div/div/label/div"
    # 离线列表第一个设备
    Offline_DeviceName_First = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div[2]/div/ul[1]/li[1]/div/div[2]/a/span"
    Offline_AddToBlacklist = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div[2]/div/ul[1]/li[4]/span[1]"
    Offline_AddToBlacklist_Ok = "/html/body/div[5]/div/div[2]/button[2]"
