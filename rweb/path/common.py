#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun

"""首页"""
class CommonLocators(object):

    """登录页面"""
    SetupWifi = "//div[@class='form']/div[2]/button[@class='btn']"
    InputPassword = "//input"
    Login = "//div[@class='form-item']/button"


    """更新提示框"""


    """我的WiFi"""
    # 一级目录：我的WiFi
    LEVEL_1_MyWifi = "//div[@class='nav-wrap nav-wrap--laptop']/ul/li[1]/div/div"
    # 管理路由器
    Router_Management = "//div[@class='nav-wrap nav-wrap--laptop']/ul/li[1]/ul/li[1]"
    # 接入设备
    Devices = "//div[@class='nav-wrap nav-wrap--laptop']/ul/li[1]/ul/li[2]"
    # 互联网
    Internet = "//div[@class='nav-wrap nav-wrap--laptop']/ul/li[1]/ul/li[3]"






    """设置"""
    # 一级目录：设置
    LEVEL_1_Set = "//div[@class='nav-wrap nav-wrap--laptop']/ul/li[2]/div/div"
    # WiFi设置
    WiFi_Settings = "//div[@class='nav-wrap nav-wrap--laptop']/ul/li[2]/ul/li[1]"
    # 上网设置
    Internet_Settings = "//div[@class='nav-wrap nav-wrap--laptop']/ul/li[2]/ul/li[2]"
    # 管理密码
    Admin_Password = "//div[@class='nav-wrap nav-wrap--laptop']/ul/li[2]/ul/li[3]"
    # 黑名单
    Blacklist = "//div[@class='nav-wrap nav-wrap--laptop']/ul/li[2]/ul/li[4]"
    # 时区
    Timezone = "//div[@class='nav-wrap nav-wrap--laptop']/ul/li[2]/ul/li[5]"
    # 访客WiFi
    Guest_WiFi = "//div[@class='nav-wrap nav-wrap--laptop']/ul/li[2]/ul/li[6]"



    """高级设置"""
    # 一级目录：高级设置
    LEVEL_1_AdvancedSettings = "//div[@class='nav-wrap nav-wrap--laptop']/ul/li[3]/div/div"
    # 端口转发
    PortForwarding = "//div[@class='nav-wrap nav-wrap--laptop']/ul/li[3]/ul/li[1]"
    # DMZ主机
    DMZ_Host = "//div[@class='nav-wrap nav-wrap--laptop']/ul/li[3]/ul/li[2]"
    # DHCP服务
    DHCP = "//div[@class='nav-wrap nav-wrap--laptop']/ul/li[3]/ul/li[3]"
    # Mac与IP绑定
    Static_DHCP_Lease = "//div[@class='nav-wrap nav-wrap--laptop']/ul/li[3]/ul/li[4]"
    # Mac地址克隆
    Clone_MAC_Address = "//div[@class='nav-wrap nav-wrap--laptop']/ul/li[3]/ul/li[5]"
    # DDNS
    DDNS = "//div[@class='nav-wrap nav-wrap--laptop']/ul/li[3]/ul/li[6]"
    # VPN
    VPN = "//div[@class='nav-wrap nav-wrap--laptop']/ul/li[3]/ul/li[7]"
    # 工作方式
    Network_Mode = "//div[@class='nav-wrap nav-wrap--laptop']/ul/li[3]/ul/li[8]"
    # 网络诊断
    Network_Diagnosis = "//div[@class='nav-wrap nav-wrap--laptop']/ul/li[3]/ul/li[9]"
    # 路由器日志
    System_Log = "//div[@class='nav-wrap nav-wrap--laptop']/ul/li[3]/ul/li[10]"
    # 防火墙
    Firewall = "//div[@class='nav-wrap nav-wrap--laptop']/ul/li[3]/ul/li[11]"

    """固件升级"""
    # 一级目录：固件升级
    LEVEL_1_UpgradeFirmware = "//div[@class='nav-wrap nav-wrap--laptop']/ul/li[4]/div/div"
    # 在线升级
    Online_Upgrade = "//div[@class='nav-wrap nav-wrap--laptop']/ul/li[4]/ul/li[1]"
    # 离线升级
    Offline_Upgrade = "//div[@class='nav-wrap nav-wrap--laptop']/ul/li[4]/ul/li[2]"

    """语言"""
    Language = "//span[@class='current-text']"
    Language_Chinese = "//div[@class='right-wrap']/div[1]/ul/li[1]"
    Language_English = "//div[@class='right-wrap']/div[1]/ul/li[2]"
    Language_Deutsch = "//div[@class='right-wrap']/div[1]/ul/li[3]"         # 德语
    Language_Dutch =   "//div[@class='right-wrap']/div[1]/ul/li[4]"         # 荷兰语

    """退出登录"""
    Logout = "//div[@class='exit']"

    """成功的toast"""
    Success_Toast = "//div[@class='toast-container success']"
    """失败的toast"""
    Error_Toast = "//div[@class='toast-container error']/span"
    """空列表"""
    Empty_List = "//p[@class='empty-text']"
    ""
    # 修改的loading元素（好像不生效）
    Loading = "loading-container"
    # 遮罩（如倒计时的）
    Shade = "//div[@class='reboot-model-contanier']"
    Shade_Note = "//div[@class='reboot-model-contanier']/div[3]"

    # 对话框
    Dialog = "//div[@class='dialog-container mask-layer']/div[@class='dialog-content']"
    Dialog_Note = "//div[@class='dialog-container mask-layer']/div[@class='dialog-content']/div[1]"
    Cancel = "//div[@class='dialog-container mask-layer']/div/div[2]/button[1]"
    Confirm = "//div[@class='dialog-container mask-layer']/div/div[2]/button[2]"

    Save = "//button[@class='btn']"
