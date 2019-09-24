#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun



"""VPN"""
class VpnLocators(object):
    Add = "btn"
    Statu = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div/div[1]/div[2]/div"
    # 连接/关闭 的文字提示
    Statu_Text = "/html/body/div[1]/div[1]/div/div/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/div/span"
    Edit = "/html/body/div[1]/div[1]/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div[1]"
    Delete = "/html/body/div[1]/div[1]/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div[2]"
    Delete_Ok = "/html/body/div[3]/div/div[2]/button[2]"
    # 名称
    Name = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/input"
    # 协议类型
    Protocol = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/input"
    Protocol_PPTP = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/ul/li[1]"
    Protocol_L2TP = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[2]/div/div/ul/li[2]"
    # 服务器
    Server = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[3]/div/div/div/input"
    # 用户名
    Username = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[4]/div/div/div/input"
    # 密码
    Password = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[5]/div/div/div[1]/input"
    # MPPE
    MPPE = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[6]/div[1]/div/div"
    # MPPC
    MPPC = "/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/div[6]/div[2]/div/div"

    Save = "/html/body/div[1]/div[1]/div/div/div[1]/div[2]/div[2]/button"
