#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun

"""接入设备"""


class DevicesLocators(object):
    """主网列表"""
    MyWifi = "//div[@class='tabs']/div[1]"
    # 列表头
    MyWifi_Table_Head = "//div[@class='table-head']/ul/li[{num}]"
    MyWifi_List_Name = "//div[@class='table-inner']/div[2]/div/ul/li[1]/div/div[1]/a/span"
    MyWifi_List_Name_Edit = "//div[@class='table-inner']/div[2]/div/ul/li[1]/div/div[1]/a/img[2]"
    MyWifi_List_Ip = "//div[@class='table-inner']/div[2]/div/ul/li[4]/span[2]"
    MyWifi_List_Mac = "//div[@class='table-inner']/div[2]/div/ul/li[4]/span[2]/span"
    MyWifi_List_Speed_Uplink = "//div[@class='table-inner']/div[2]/div/ul/li[2]/div[1]/div[1]"
    MyWifi_List_Speed_Downlink = "//div[@class='table-inner']/div[2]/div/ul/li[2]/div/div[2]"
    MyWifi_List_DeviceThroughput = "//div[@class='table-inner']/div[2]/div/ul/li[3]/span[2]/span[1]"
    Limit_Time_Icon = "//div[@class='table-inner']/div[2]/div/ul/li[6]/div/div[1]/span[1]"
    Limit_Rate_Icon = "//div[@class='table-inner']/div[2]/div/ul/li[6]/div/div[2]/span[1]"
    Limit_WebsiteBlacklist_Icon = "//div[@class='table-inner']/div[2]/div/ul/li[6]/div/div[3]/span[1]"
    # 接入图标
    MyWifi_Access_Icon = "//div[@class='table-inner']/div[2]/div/ul/li[1]/div/div[2]/span/span[2]"

    # 操作-设置按钮
    Set = "//div[@class='table-inner']/div[2]/div/ul[{num}]/li[@class='column-black-list']/span[1]"
    AddtoBlacklist = "//div[@class='table-inner']/div[2]/div/ul[1]/li[@class='column-black-list']/span[2]"

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
