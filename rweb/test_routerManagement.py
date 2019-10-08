#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun


import unittest
import time
from selenium import webdriver
from .test_base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from . import const

from rweb.path.common import CommonLocators
from rweb.path.devices import DevicesLocators
from rweb.path.routerManagement import RouterManagementLocators


from router.time_limit import test_time_limit_add_1



class RouterManagement(Base):


    @unittest.skip("跳过")
    def test_A_routerManagement_elementCheck(self):
        """管理路由器-元素检测"""
        """
        用例-1705 : 元素检测
                    查看是否有tab：Mesh拓扑图《trans0312》、列表《trans0384》 ： 是
                    查看是否有按钮：添加节点《trans0194》 ： 是
        """
        # 断言：是否有tab：Mesh拓扑图
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Mesh_Topology))
        )
        Mesh_Topology_Text = self.driver.find_element_by_xpath(RouterManagementLocators.Mesh_Topology).text
        assert Mesh_Topology_Text == "Mesh Topology", Mesh_Topology_Text

        # 断言：是否有tab：列表
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.List))
        )
        List_Text = self.driver.find_element_by_xpath(RouterManagementLocators.List).text
        assert List_Text == "List", List_Text

        # 断言：是否有按钮：添加节点
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Add_Node))
        )
        Add_Node_Text = self.driver.find_element_by_xpath(RouterManagementLocators.Add_Node).text
        assert Add_Node_Text == "Add a node", Add_Node_Text


    #@unittest.skip("跳过")
    def test_B_routerManagement_page(self):
        """管理路由器-默认页及页面切换"""
        """
        用例-1706 : 默认进入“Mesh拓扑图”tab页
                    初始化进入【互联网状态】页，查看是否默认进入的"Mesh拓扑图"tab页 ： 是
        用例-1707 : “Mesh拓扑图”和“列表”可正常点击切换
                    点击切换“Mesh拓扑图”和“列表”，查看是否可正常切换到对应页面 ： 是
        用例-1708 : 点击“添加节点”，进入添加节点流程的【选择节点类型】页
                    点击“添加节点”，看是否进入添加节点流程的【选择节点类型】页 ： 是
        """
        # 断言：用例-1706 : 默认进入“Mesh拓扑图”tab页
        time.sleep(1)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Mesh_Topology))
        )
        Mesh_Topology_Class = self.driver.find_element_by_xpath(RouterManagementLocators.Mesh_Topology).get_attribute('class')
        # 断言：是否选中“Mesh拓扑图”tab页
        assert Mesh_Topology_Class == "tab selected", Mesh_Topology_Class
        # 断言：是否显示“Mesh拓扑图”tab页下的“Mesh穿墙” 和 “完整拓扑”
        assert self.driver.find_element_by_xpath(RouterManagementLocators.Increase_Mesh_Coverage).is_displayed()
        assert self.driver.find_element_by_xpath(RouterManagementLocators.Complete_Graph).is_displayed()

        # 断言：用例-1707 : “Mesh拓扑图”和“列表”可正常点击切换

        # 断言：用例-1708 : 点击“添加节点”，进入添加节点流程的【选择节点类型】页

