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




    @unittest.skip("跳过")
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
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Mesh_Topology))
        )
        Mesh_Topology_Class = self.driver.find_element_by_xpath(RouterManagementLocators.Mesh_Topology).get_attribute('class')
        # 断言：是否选中“Mesh拓扑图”tab页
        assert Mesh_Topology_Class == "tab selected", Mesh_Topology_Class
        # 断言：是否显示“Mesh拓扑图”tab页下的“Mesh穿墙” 和 “完整拓扑” 状态开关
        assert self.driver.find_element_by_xpath(RouterManagementLocators.Increase_Mesh_Coverage_Statu).is_displayed()
        assert self.driver.find_element_by_xpath(RouterManagementLocators.Complete_Graph).is_displayed()

        # 断言：用例-1707 : “Mesh拓扑图”和“列表”可正常点击切换
        # 切换到“列表”页
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.List))
        ).click()
        time.sleep(1)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.List))
        )
        List_Class = self.driver.find_element_by_xpath(RouterManagementLocators.List).get_attribute('class')
        # 断言：是否选中“Mesh拓扑图”tab页
        assert List_Class == "tab selected", List_Class
        # 断言：是否显示“重启” 和 “恢复出厂设置” 按钮
        assert self.driver.find_element_by_xpath(RouterManagementLocators.Reboot).is_displayed()
        assert self.driver.find_element_by_xpath(RouterManagementLocators.Factory_Reset).is_displayed()
        # 再切换回“Mesh拓扑图”页
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Mesh_Topology))
        ).click()
        time.sleep(1)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Mesh_Topology))
        )
        Mesh_Topology_Class = self.driver.find_element_by_xpath(RouterManagementLocators.Mesh_Topology).get_attribute("class")
        # 断言：是否选中“Mesh拓扑图”tab页
        assert Mesh_Topology_Class == "tab selected", Mesh_Topology_Class
        # 断言：是否显示“Mesh拓扑图”tab页下的“Mesh穿墙” 和 “完整拓扑” 状态开关
        assert self.driver.find_element_by_xpath(RouterManagementLocators.Increase_Mesh_Coverage_Statu).is_displayed()
        assert self.driver.find_element_by_xpath(RouterManagementLocators.Complete_Graph).is_displayed()

        # 断言：用例-1708 : 点击“添加节点”，进入添加节点流程的【选择节点类型】页
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Add_Node))
        ).click()
        time.sleep(1)
        # 断言：判断当前网址是否是添加节点的网址：
        Add_Node_Url = self.driver.current_url
        assert Add_Node_Url == "http://mywifi.mercku.tech/#/mesh/add", Add_Node_Url
        # 断言：标题是否是：添加节点
        Title_Text = self.driver.find_element_by_xpath("//div[@class='page']/div[1]").text
        assert Title_Text == "Add a node", Title_Text
        # 断言：是否有添加节点的 开始 按钮
        Start_Button = self.driver.find_element_by_xpath("//div[@class='page']/div[2]/div[1]/div[2]/button")
        assert Start_Button.is_displayed()



    @unittest.skip("跳过")
    def test_C_routerManagement_increaseMeshCoverage_default_note(self):
        """管理路由器-Mesh穿墙-默认状态及提示"""
        """
        用例-5523 : 开关默认关闭
                    全新（恢复出场设置）路由器，初始化进入，查看开关，是否默认关闭 ： 是
        用例-5522 : 点击开关旁叹号，弹出提示
                    点击开关旁的叹号，看是否弹出文字提示框 ： 是
                    标题：Mesh穿墙《trans0526》
                    提示文字：开启Mesh穿墙后，WiFi覆盖范围更大，但是速度会相应变慢。《trans0558》
        """
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Increase_Mesh_Coverage_Statu))
        )

        # 断言：用例-5523 : 开关默认关闭
        IncreaseMeshCoverage_Class = self.driver.find_element_by_xpath(RouterManagementLocators.Increase_Mesh_Coverage_Statu).get_attribute("class")
        assert IncreaseMeshCoverage_Class == "switch switch-animation", IncreaseMeshCoverage_Class

        # 断言：用例-5522 : 点击开关旁叹号，弹出提示
        # 鼠标模拟移动到“？”上
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Increase_Mesh_Coverage_Icon))
        )
        mouse = self.driver.find_element_by_xpath(RouterManagementLocators.Increase_Mesh_Coverage_Icon)
        ActionChains(self.driver).move_to_element(mouse).perform()

        Note_Title = RouterManagementLocators.Increase_Mesh_Coverage_Note.format(num=2)
        Note_Title_Text = self.driver.find_element_by_xpath(Note_Title).text
        assert Note_Title_Text == "Increase Mesh coverage", Note_Title_Text
        Note_Content = RouterManagementLocators.Increase_Mesh_Coverage_Note.format(num=3)
        Note_Content_Text = self.driver.find_element_by_xpath(Note_Content).text
        assert Note_Content_Text == 'Once "Increase mesh coverage" enabled, Wi-Fi coverage will increase.', Note_Content_Text




    #@unittest.skip("跳过")
    def test_D_routerManagement_increaseMeshCoverage_on(self):
        """管理路由器-Mesh穿墙-开启成功"""
        """
        用例-5609 : 点击开关开启，弹出确认框
        用例-5526 : 开启开关成功
        """
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Increase_Mesh_Coverage_Statu))
        ).click()


        # 断言：用例-5609 : 点击开关开启，弹出确认框
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Dialog))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Dialog).is_displayed()

        # 点击 确定 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Confirm))
        ).click()

        # Statu_Class = self.driver.find_element_by_xpath(RouterManagementLocators.Increase_Mesh_Coverage_Statu).get_attribute("class")
        #
        # print(111111)
        # print(Statu_Class)
        time.sleep(10)








    @unittest.skip("跳过")
    def test_E_routerManagement_increaseMeshCoverage_off(self):
        """管理路由器-Mesh穿墙-关闭成功"""







    @unittest.skip("跳过")
    def test_K_routerManagement_completeGraph_default_note(self):
        """管理路由器-完整拓扑-默认状态及提示"""
        """
        用例-7095 : 开关默认开启
        用例-7096 : 点击开关旁边叹号，弹出提示
        """
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Complete_Graph_Statu))
        )

        # 断言：用例-5523 : 开关默认关闭
        CompleteGraph_Class = self.driver.find_element_by_xpath(RouterManagementLocators.Complete_Graph_Statu).get_attribute("class")
        assert CompleteGraph_Class == "switch switch-animation", CompleteGraph_Class

        # 断言：用例-5522 : 点击开关旁叹号，弹出提示
        # 鼠标模拟移动到“？”上
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Complete_Graph_Icon))
        )
        mouse = self.driver.find_element_by_xpath(RouterManagementLocators.Complete_Graph_Icon)
        ActionChains(self.driver).move_to_element(mouse).perform()

        Note_Title = RouterManagementLocators.Complete_Graph_Note.format(num=2)
        Note_Title_Text = self.driver.find_element_by_xpath(Note_Title).text
        assert Note_Title_Text == "Complete Graph", Note_Title_Text
        Note_Content = RouterManagementLocators.Complete_Graph_Note.format(num=3)
        Note_Content_Text = self.driver.find_element_by_xpath(Note_Content).text
        assert Note_Content_Text == 'All available connections will be illustrated in complete graph mode. Since Mercku nodes are able to pick up the best connections automatically, unused connections will be omitted when disabling complete graph, which describes the mesh link status more clearly.', Note_Content_Text