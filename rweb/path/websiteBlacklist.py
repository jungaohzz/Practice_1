#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/19 22:13
# @Author:  GaoJun

"""网址黑名单"""
class WebsiteBlacklistLocators(object):
    Page_WebsiteBlacklist = "//div[@class='tabs tabs']/div[3]"

    Add = "//button[@class='btn btn-small']"
    Statu = "//div[@class='switch-container']/div"
    List_Website = "//div[@class='table']/div[3]/div/div[1]"
    Delete = "//div[@class='table']/div[3]/div/div[2]/a"

    """新增-网址黑名单"""
    Website = "//div[@class='inputarea']/div/input"
    Save = "//div[@class='btn-info']/button[2]"