#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/18 21:25
# @Author:  GaoJun

"""Mac与IP绑定"""
class StaticDHCPLeaseLocators(object):
    """Mac与IP绑定 首页 - 列表"""
    Add = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div[2]/button[1]"
    # 批量删除
    Deletes = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div[2]/button[3]"
    # 全选框（批量删除）
    All_check = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div/div/label/div"
    List_Name = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[1]"
    List_MacAddr = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[2]"
    List_IpAddr = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[3]"
    # 空列表
    List_Null = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/p"
    # 每一个的 编辑 和 删除 按钮
    Edit = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[4]/a[1]"
    Delete = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[4]/a[2]"
    Delete_ok = "/html/body/div[3]/div/div[2]/button[2]"



    """新增端口转发"""
    Name = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/input"
    MacAddr = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[3]/div/div/div/input"
    IpAddr = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[4]/div/div/div/input"
    Save = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[2]/button"