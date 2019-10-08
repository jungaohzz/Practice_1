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
    # 重启
    Reboot = "//div[@class='table-content']/div/div[7]/span[1]"
    # 恢复出厂
    Factory_Reset = "//div[@class='table-content']/div/div[7]/span[2]"




    """添加节点 按钮"""
    Add_Node = "//div[@class='mesh-info']/div[1]/button[1]"