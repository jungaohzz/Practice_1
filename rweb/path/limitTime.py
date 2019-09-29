#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun

"""限时"""
class LimitTimeLocators(object):
    Page_TimeLimit = "//div[@class='tabs tabs']/div[2]"


    Add = "//button[@class='btn btn-small']"



    """列表"""
    # 列表头
    Table_Heads = "//div[@class='table-head']/div[{num}]"
    List_Null = "//p[@class='empty-text']"
    Cut_Off_Time = "//div[@class='table-body']/div[{num}]/div[1]/span[1]"
    Recovery_Time = "//div[@class='table-body']/div[{num}]/div[2]"

    # 重复
    Repeat = "//div[@class='table-body']/div[{num}]/div[3]"
    Statu = "//div[@class='table-body']/div[{num}]/div/div/div/div"
    # 每一个的 编辑 和 删除 按钮
    Edit = "//div[@class='table-body']/div[{num}]/div[4]/a[1]"
    Delete = "//div[@class='table-body']/div[{num}]/div[4]/a[2]"





    """新增限时"""
    Insert_Statu = "//div[@class='item']/div/div"
    Insert_CutOffTime_Form = "//div[@class='modal-form']/div[2]/div"
    Insert_RecoveryTime_Form = "//div[@class='modal-form']/div[3]/div"
    Form_Confirm = "//div[@class='combobox']/div[@class='button-wrap']/button[2]"
    Hour = "//div[@class='combobox']/div[1]/div/ul/li[{num}+1]"
    Minute = "//div[@class='combobox']/div[1]/div[2]/ul/li[{num}+1]"


    Insert_RecoveryTime = "//div[@class='modal-form']/div[3]/div"

    Weeks = "//div[@class='date-wrap']/div[{num}]/div/label/div[1]"

    Insert_Cancel = "//button[@class='btn btn-default']"
    Insert_Add = "//button[@class='btn']"