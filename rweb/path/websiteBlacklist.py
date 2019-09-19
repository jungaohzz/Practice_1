#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/19 22:13
# @Author:  GaoJun

"""网址黑名单"""
class WebsiteBlacklistLocators(object):
    Page_WebsiteBlacklist = "/html/body/div[1]/div/div/div/div[1]/div[1]/div[3]/div/div[3]"

    Add = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div[1]/button"
    Statu = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div/div"
    List_Website = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div[3]/div/div[1]"
    Delete = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/a"

    """新增-网址黑名单"""
    Website = "/html/body/div[3]/div[2]/div/div[1]/div/div/div/div/div/input"
    Save = "/html/body/div[3]/div[2]/div/div[2]/button[2]"