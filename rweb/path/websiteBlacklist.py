#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/19 22:13
# @Author:  GaoJun

"""网址黑名单"""
class WebsiteBlacklistLocators(object):
    Page_WebsiteBlacklist = "//div[@class='tabs tabs']/div[3]"

    Add = "//button[@class='btn btn-small']"
    Statu = "//div[@class='switch-container']/div"
    List_Null = "//p[@class='empty-text']"
    List_Website = "//div[@class='table']/div[3]/div[{num}]/div[1]"
    Delete = "//div[@class='table']/div[3]/div[{num}]/div[2]/a"

    """新增-网址黑名单"""
    Website = "//div[@class='inputarea']/div/input"
    Error_Message = "//span[@class='error-message']"
    Cancel = "//div[@class='btn-info']/button[1]"
    Save = "//div[@class='btn-info']/button[2]"