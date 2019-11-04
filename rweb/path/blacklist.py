#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/9/21 16:43
# @Author:  GaoJun

"""黑名单"""

class BlacklistLocators(object):
    Add = "//div[@class='btns']/div"
    Delete_Alls = "//div[@class='btns']/button"



    # 点击新增后显示的表单
    Form_Devices_Check = "//div[@class='modal']/div[2]/div[2]/div[{num}]/div[1]"
    Form_Devices_Mac = "//div[@class='modal']/div[2]/div[2]/div[{num}]/div[2]/p[2]"
    Add_to_Blacklist = "//div[@class='modal']/div[2]/div[3]/button"




    # 全选按钮
    Check_All = "//div[@class='table-header']/div[1]/div[1]/div/label/div"
    # 空列表
    Empty_List = "//div[@class='empty']/p"

    Device_Mac = "//div[@class='table-content']/div[{num}]/div[2]"



