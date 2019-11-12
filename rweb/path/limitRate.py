#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/19 22:13
# @Author:  GaoJun

"""限速"""


class LimitRateLocators(object):
    Page_RateLimit = "//div[@class='tabs tabs']/div[2]"

    Upload = "//div[@class='form']/div/div[1]/div[1]/div/div/div/input"
    Download = "//div[@class='form']/div/div[1]/div[2]/div/div/div/input"
    Statu = "//div[@class='checkbox-container']/label/div[1]"
    Save = "//div[@class='form']/div/div[3]/button"
