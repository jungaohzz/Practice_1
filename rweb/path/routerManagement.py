#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun


class RouterManagementLocators(object):
    """mesh拓扑图"""
    Mesh_Topology = "//div[@class='mesh-info']/div[1]/div/div[1]"
    # mesh穿墙
    Increase_Mesh_Coverage_Icon = "//div[@class='switch-wrap']/div[1]/label/div/div/div[1]/img"
    Increase_Mesh_Coverage_Note = "//div[@class='switch-wrap']/div[1]/label/div/div/div[2]/div[{num}]"
    Increase_Mesh_Coverage_Statu = "//div[@class='switch-wrap']/div[1]/div/div"
    # 完整拓扑
    Complete_Graph_Icon = "//div[@class='switch-wrap']/div[2]/label/div/div/div[1]/img"
    Complete_Graph_Note ="//div[@class='switch-wrap']/div[2]/label/div/div/div[2]/div[{num}]"
    Complete_Graph_Statu = "//div[@class='switch-wrap']/div[2]/div/div"


    """列表"""
    List = "//div[@class='mesh-info']/div[1]/div/div[2]"
    PrimaryRoute_Name = "//div[@class='table-content']/div[1]/div[1]/div[2]/div[1]"
    PrimaryRoute_EditName = "//div[@class='edit']"
    # 重启
    PrimaryRoute_Reboot = "//div[@class='table-content']/div/div[7]/span[1]"
    # 恢复出厂
    PrimaryRoute_Factory_Reset = "//div[@class='table-content']/div/div[7]/span[2]"


    """修改设备名称弹框"""
    Box = "//div[@class='modal-dialog edit-name-modal']/div[@class='modal-content']"
    Box_Title = "//div[@class='modal-dialog edit-name-modal']/div[@class='modal-content']/div/div/div/div/label"
    Box_DeviceName = "//div[@class='select']/input"
    # 下拉框是否打开的状态
    Box_On_or_Off = "//div[@class='select']/div/span"
    # 下拉框中可选择的名字
    Box_Optional_Name = "//div[@class='select']/ul/li[{num}]"
    Box_Error = "//span[@class='error-message']"
    Box_Cancel = "//div[@class='modal-dialog edit-name-modal']/div[@class='modal-content']/div/div[2]/button[1]"
    Box_Confirm = "//div[@class='modal-dialog edit-name-modal']/div[@class='modal-content']/div/div[2]/button[2]"

    """添加节点 按钮"""
    Add_Node = "//div[@class='mesh-info']/div[1]/button[1]"