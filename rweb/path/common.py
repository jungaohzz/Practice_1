#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun

"""首页"""
class CommonLocators(object):

    """更新提示框"""


    """我的WiFi"""
    # 一级目录：我的WiFi
    LEVEL_1_MyWifi = "/html/body/div[1]/div/div/div/header/div[2]/ul/li[1]/div/div"
    # 管理路由器
    Router_Management = "/html/body/div[1]/div/div/div/header/div[2]/ul/li[1]/ul/li[1]"
    # 接入设备
    Devices = "/html/body/div[1]/div/div/div/header/div[2]/ul/li[1]/ul/li[2]"
    # 互联网
    Internet = "/html/body/div[1]/div/div/div/header/div[2]/ul/li[1]/ul/li[3]"






    """设置"""
    # 一级目录：设置
    LEVEL_1_Set = "/html/body/div[1]/div/div/div/header/div[2]/ul/li[2]/div/div"
    # WiFi设置
    WiFi_Settings = "/html/body/div[1]/div/div/div/header/div[2]/ul/li[2]/ul/li[1]"
    # 上网设置
    Internet_Settings = "/html/body/div[1]/div/div/div/header/div[2]/ul/li[2]/ul/li[2]"
    # 管理密码
    Admin_Password = "/html/body/div[1]/div/div/div/header/div[2]/ul/li[2]/ul/li[3]"
    # 黑名单
    Blacklist = "/html/body/div[1]/div/div/div/header/div[2]/ul/li[2]/ul/li[4]"
    # 时区
    Timezone = "/html/body/div[1]/div/div/div/header/div[2]/ul/li[2]/ul/li[5]"
    # 访客WiFi
    Guest_WiFi = "/html/body/div[1]/div/div/div/header/div[2]/ul/li[2]/ul/li[6]"

    LEVEL_1_Set_Timezone = "/html/body/div[1]/div/div/div/header/div[2]/ul/li[2]/ul/li[5]"

    """高级设置"""
    # 一级目录：高级设置
    LEVEL_1_AdvancedSettings = "/html/body/div[1]/div/div/div/header/div[2]/ul/li[3]/div/div"
    # 端口转发
    PortForwarding = "/html/body/div[1]/div/div/div/header/div[2]/ul/li[3]/ul/li[1]"
    # DMZ主机
    DMZ_Host = "/html/body/div[1]/div/div/div/header/div[2]/ul/li[3]/ul/li[2]"
    # DHCP服务
    DHCP = "/html/body/div[1]/div/div/div/header/div[2]/ul/li[3]/ul/li[3]"
    # Mac与IP绑定
    Static_DHCP_Lease = "/html/body/div[1]/div/div/div/header/div[2]/ul/li[3]/ul/li[4]"
    # Mac地址克隆
    Clone_MAC_Address = "/html/body/div[1]/div/div/div/header/div[2]/ul/li[3]/ul/li[5]"
    # DDNS
    DDNS = "/html/body/div[1]/div/div/div/header/div[2]/ul/li[3]/ul/li[6]"
    # VPN
    VPN = "/html/body/div[1]/div/div/div/header/div[2]/ul/li[3]/ul/li[7]"
    # 工作方式
    Network_Mode = "/html/body/div[1]/div/div/div/header/div[2]/ul/li[3]/ul/li[8]"
    # 网络诊断
    Network_Diagnosis = "/html/body/div[1]/div/div/div/header/div[2]/ul/li[3]/ul/li[9]"
    # 路由器日志
    System_Log = "/html/body/div[1]/div/div/div/header/div[2]/ul/li[3]/ul/li[10]"
    # 防火墙
    Firewall = "/html/body/div[1]/div/div/div/header/div[2]/ul/li[3]/ul/li[11]"

    """固件升级"""
    # 一级目录：固件升级
    LEVEL_1_UpgradeFirmware = "/html/body/div[1]/div/div/div/header/div[2]/ul/li[4]/div/div"
    # 在线升级
    Online_Upgrade = "/html/body/div[1]/div/div/div/header/div[2]/ul/li[4]/ul/li[1]"
    # 离线升级
    Offline_Upgrade = "/html/body/div[1]/div/div/div/header/div[2]/ul/li[4]/ul/li[2]"

    """语言"""
    Language = "/html/body/div[1]/div/div/div/header/div[4]/div[1]/div/span[1]"
    Language_Chinese = "/html/body/div[1]/div/div/div/header/div[4]/div[1]/ul/li[1]"
    Language_English = "/html/body/div[1]/div/div/div/header/div[4]/div[1]/ul/li[2]"
    Language_Deutsch = "/html/body/div[1]/div/div/div/header/div[4]/div[1]/ul/li[3]"

    """退出登录"""
    Logout = "/html/body/div[1]/div/div/div/header/div[4]/div[3]"

    """成功的toast"""
    Success_Toast = "//div[@class='toast-container success']"
    Loading = "loading-container"
