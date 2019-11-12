#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/18 21:25
# @Author:  GaoJun

"""Mac与IP绑定"""


class StaticDHCPLeaseLocators(object):
    """Mac与IP绑定 首页 - 列表"""
    # 重启生效
    Restart = "//div[@class='page']/div[2]/p/span"
    Add = "//button[@class='btn btn-small'][1]"
    # 批量删除
    Deletes = "//button[@class='btn btn-small'][2]"
    # 全选框（批量删除）
    All_check = "//div[@class='table-head']/div[1]/div/div/label/div"
    List_Name = "//div[@class='table-body']/div[1]/div[1]"
    List_MacAddr = "//div[@class='table-body']/div/div[2]"
    List_IpAddr = "//div[@class='table-body']/div/div[3]"
    # 空列表
    List_Null = "//div[@class='empty']/p"
    # 每一个的 编辑 和 删除 按钮
    Edit = "//div[@class='table-body']/div/div[4]/a[1]"
    Delete = "//div[@class='table-body']/div/div[4]/a[2]"
    Delete_ok = "//div[@class='dialog-buttons']/button[2]"

    """新增Mac与IP绑定"""
    Name = "//div[@class='form']/div[2]/div/div/div/input"
    MacAddr = "//div[@class='form']/div[3]/div/div/div/input"
    IpAddr = "//div[@class='form']/div[4]/div/div/div/input"
    Save = "//button[@class='btn']"
