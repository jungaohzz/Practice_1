#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun

"""限时"""
class LimitTimeLocators(object):
    Add = "//button[@class='btn btn-small']"



    """列表"""
    # 列表头
    Table_Heads = "//div[@class='table-head']/div[{num}]"
    List_Null = "//p[@class='empty-text']"
    Cut_Off_Time = "//div[@class='table-body']/div[{num}]/div/span[1]"
    Recovery_Time = "//div[@class='table-body']/div[{num}]/div/span[3]"

    # 重复
    Repeat = "//div[@class='table-body']/div[{num}]/div[3]"
    Statu = "//div[@class='table-body']/div[{num}]/div/div/div/div"
    # 每一个的 编辑 和 删除 按钮
    Edit = "//div[@class='table-body']/div[{num}]/div[4]/a[1]"
    Delete = "//div[@class='table-body']/div[{num}]/div[4]/a[2]"





    """新增限时"""
    Insert_Statu = "//div[@class='item']/div/div"
    Weeks = "/html/body/div[3]/div[2]/div/div[1]/div[4]/div/div[{num}]/div/label/div[1]"
    Insert_CutOffTime_Form = "//div[@class='modal-form']/div[2]/div"
    Hour_14 = "//div[@class='combobox']/div[1]/div/ul/li[15]"
    Minute_59 = "//div[@class='combobox']/div[1]/div[2]/ul/li[60]"
    Insert_CutOffTime_Ok = "//div[@class='combobox']/div[@class='button-wrap']/button[2]"


    Insert_RecoveryTime = "/html/body/div[2]/div[2]/div/div[1]/div[3]/div/div/input"
    Cancel = "/html/body/div[2]/div[2]/div/div[3]/button[1]"
    Save = "/html/body/div[3]/div[2]/div/div[3]/button[2]"