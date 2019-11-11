#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/20 20:50
# @Author:  GaoJun

"""MAC地址克隆"""
class CloneMacAddressLocators(object):
    Default_Mac_Button = "//div[@class='form']/div[1]/div"
    Custom_Mac_Button = "//div[@class='form']/div[2]/div[1]"
    Custom_Mac = "//div[@class='input-wrapper']/input"
    Save = "//button[@class='btn primary']"
    Save_Ok = "//button[@class='btn']"