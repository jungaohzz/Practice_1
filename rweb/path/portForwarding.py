#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun

"""端口转发"""
class PortForwardingLocators(object):
    """端口转发 首页 - 列表"""
    Add = "//button[@class='btn btn-small']"
    # 批量删除
    Deletes = "//button[@class='btn m-btn btn-small']"

    List_Name = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[1]/span[2]"
    List_OutNetIp = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[2]/p[1]"
    List_OutNetPort = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[2]/p[2]"
    List_LocalIp = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[3]/p[1]"
    List_LocalPort = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[3]/p[2]"
    List_ProtocolType = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[4]"
    List_Statu = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[5]/div/div"
    # 每一个的 编辑 和 删除 按钮
    Edit = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[6]/a[1]"
    Delete = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[3]/div/div[6]/a[2]"
    Delete_ok = "//div[@class='dialog-buttons']/button[2]"


    """新增端口转发"""
    ProtocolType_TcpUdp = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div[1]/div[1]"
    ProtocolType_TCP = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[1]"
    ProtocolType_UDP = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div[3]/div[1]"
    Name= "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/input"
    OutNetIp = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[3]/div/div/div/input"
    OutNetPort_start = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[4]/div/div[1]/div/div/div/input"
    OutNetPort_end = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[4]/div/div[2]/div/div/div/input"
    LocalIp = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[5]/div/div/div/input"
    LocalPort_start = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[6]/div/div[1]/div/div/div/input"
    LocalPort_end = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[6]/div/div[2]/div/div/div/input"
    Save = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[2]/button"