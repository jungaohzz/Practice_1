#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun

"""限时"""
class LimitTimeLocators(object):
    Add = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div[1]/button"
    Cut_Off_Time = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div[3]/div[1]/div[1]/span[1]"
    Recovery_Time = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div[3]/div[1]/div[2]"
    # 重复
    Repeat = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div[3]/div/div[3]"
    Statu = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div[3]/div[1]/div[4]/div/div/div"
    # 每一个的 编辑 和 删除 按钮
    Edit = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div[3]/div[1]/div[4]/a[1]"
    Delete = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div[3]/div[1]/div[4]/a[2]"




    """新增限时"""
    Mondey = "/html/body/div[3]/div[2]/div/div[1]/div[4]/div/div[1]/div/label/div[1]"
    # 保存按钮
    Save = "/html/body/div[3]/div[2]/div/div[3]/button[2]"