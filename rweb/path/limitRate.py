#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/19 22:13
# @Author:  GaoJun

"""限速"""
class LimitRateLocators(object):
    Page_RateLimit = "/html/body/div[1]/div/div/div/div[1]/div[1]/div[3]/div/div[2]"

    Upload = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[1]/div[1]/div/div/div/input"
    Download = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[1]/div[2]/div/div/div/input"
    Statu = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/label/div[1]"
    Save = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[3]/button"