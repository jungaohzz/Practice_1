#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun



"""VPN"""
class VpnLocators(object):
    Add = "//button[@class='btn btn-middle']"
    Statu = "//div[@class='vpn-list']/div[1]/div[1]/div[2]/div"
    Edit = "//div[@class='vpn-list']/div[1]/div[2]/div[1]"
    Delete = "//div[@class='vpn-list']/div[1]/div[2]/div[2]"
    Delete_Ok = "//div[@class='dialog-buttons']/button[2]"

    """新增VPN"""
    # 名称
    Name = "//div[@class='form']/div[1]/div/div/div/input"
    # 协议类型
    Protocol = "//div[@class='form']/div[2]/div/div/input"
    Protocol_PPTP = "//div[@class='form']/div[2]/div/div/ul/li[1]"
    Protocol_L2TP = "//div[@class='form']/div[2]/div/div/ul/li[2]"
    # 服务器
    Server = "//div[@class='form']/div[3]/div/div/div/input"
    # 用户名
    Username = "//div[@class='form']/div[4]/div/div/div/input"
    # 密码
    Password = "//div[@class='form']/div[5]/div/div/div[1]/input"
    # MPPE
    MPPE = "//div[@class='form']/div[6]/div[1]/div/div"
    # MPPC
    MPPC = "//div[@class='form']/div[6]/div[2]/div/div"

    Save = "//button[@class='btn']"
