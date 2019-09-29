#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun

"""接入设备"""

class DevicesLocators(object):

    """主网列表"""
    MyWifi = "//div[@class='tabs']/div[1]"
    # 操作-设置按钮
    Set = "//span[@class='black-btn btn-text setting']"


    """访客列表"""
    Guest = "//div[@class='tabs']/div[2]"



    """离线列表"""
    Offline = "//div[@class='tabs']/div[3]"
    Offline_Deletes = "//button[@class='btn btn-small']"
    Offline_Choose_All = "//div[@class='table-head']/ul/li[1]/div/div/label/div"
    # 离线列表第一个设备
    Offline_DeviceName_First = "//div[@class='name-inner off-name']/a/span"
    Offline_AddToBlacklist = "//div[@class='table-inner']/div[2]/div/ul/li[4]/span[1]"
    Offline_Delete = "//div[@class='table-inner']/div[2]/div/ul/li[4]/span[2]"
    Offline_AddToBlacklist_Ok = "//div[@class='dialog-buttons']/button[2]"
