#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun

"""端口转发"""


class PortForwardingLocators(object):
    """端口转发 首页 - 列表"""
    Add = "//button[@class='btn btn-small']"
    # 批量删除
    Check_ALL = "//div[@class='table']/div[2]/div[1]/div/div/label/div"
    Deletes = "//button[@class='btn  btn-small']"

    List_Null = "//div[@class='empty']"

    List_Name = "//div[@class='table-body']/div/div[1]/span[2]"
    List_OutNetIp = "//div[@class='table-body']/div[1]/div[2]/p[1]"
    List_OutNetPort = "//div[@class='table-body']/div[1]/div[2]/p[2]"
    List_LocalIp = "//div[@class='table-body']/div[1]/div[3]/p[1]"
    List_LocalPort = "//div[@class='table-body']/div[1]/div[3]/p[2]"
    List_ProtocolType = "//div[@class='table-body']/div[1]/div[4]"
    List_Statu = "//div[@class='table-body']/div[1]/div[5]/div/div"
    # 每一个的 编辑 和 删除 按钮
    Edit = "//div[@class='table-body']/div[1]/div[6]/a[1]"
    Delete = "//div[@class='table-body']/div[1]/div[6]/a[2]"
    Delete_ok = "//div[@class='dialog-buttons']/button[2]"

    """新增端口转发"""
    ProtocolType_TcpUdp = "//div[@class='radio-wrap']/div/div[1]/div[1]"
    ProtocolType_TCP = "//div[@class='radio-wrap']/div/div[2]/div[1]"
    ProtocolType_UDP = "//div[@class='radio-wrap']/div/div[3]/div[1]"
    Name = "//div[@class='form']/div[2]/div/div/div/input"
    OutNetIp = "//div[@class='form']/div[3]/div/div/div/input"
    OutNetPort_start = "//div[@class='form']/div[4]/div/div[1]/div/div/div/input"
    OutNetPort_end = "//div[@class='form']/div[4]/div/div[2]/div/div/div/input"
    LocalIp = "//div[@class='form']/div[5]/div/div/div/input"
    LocalPort_start = "//div[@class='form']/div[6]/div/div[1]/div/div/div/input"
    LocalPort_end = "//div[@class='form']/div[6]/div/div[2]/div/div/div/input"
    Save = "//button[@class='btn']"
