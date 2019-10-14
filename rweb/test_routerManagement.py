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
from selenium.webdriver.common.keys import Keys

from rweb.path.common import CommonLocators
from rweb.path.devices import DevicesLocators
from rweb.path.routerManagement import RouterManagementLocators






class RouterManagement(Base):


    @unittest.skip("跳过")
    def test_A_routerManagement_elementsCheck(self):
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
        assert self.driver.find_element_by_xpath(RouterManagementLocators.Complete_Graph_Statu).is_displayed()

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
        assert self.driver.find_element_by_xpath(RouterManagementLocators.PrimaryRoute_Reboot).is_displayed()
        assert self.driver.find_element_by_xpath(RouterManagementLocators.PrimaryRoute_Factory_Reset).is_displayed()
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
        assert self.driver.find_element_by_xpath(RouterManagementLocators.Complete_Graph_Statu).is_displayed()

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



    @unittest.skip("跳过")
    def test_D_routerManagement_confirmBox(self):
        """管理路由器-Mesh穿墙/完整拓扑-确认框元素检查及取消按钮"""
        """
        用例-5611 : 确认框，元素检测
                    文字：该操作将重启Wi-Fi并导致Wi-Fi下的所有设备断开连接，是否继续？《trans0229》
                    按钮：取消，确定
        用例-5612 : 确认框，点击取消，关闭弹框
        """
        Statu_Class = self.driver.find_element_by_xpath(RouterManagementLocators.Increase_Mesh_Coverage_Statu).get_attribute("class")

        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Increase_Mesh_Coverage_Statu))
        ).click()

        # 断言：用例-5611 : 确认框，元素检测
        # 确认框是否有文字：该操作将重启Wi-Fi并导致Wi-Fi下的所有设备断开连接，是否继续？《trans0229》
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Dialog))
        )
        Note_Text = self.driver.find_element_by_xpath("//div[@class='dialog-container mask-layer']/div[@class='dialog-content']/div[1]").text
        assert Note_Text == "This will cause all devices to be disconnected. Do you wish to proceed?", Note_Text
        # 确认框是否有按钮：取消
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Cancel))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Cancel).is_displayed()
        # 确认框是否有按钮：确定
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Confirm))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Confirm).is_displayed()
        print(1111111)


        # 断言：用例-5612 : 确认框，点击取消，关闭弹框
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Cancel))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until_not(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Dialog))
        )




    @unittest.skip("跳过")
    def test_E_routerManagement_increaseMeshCoverage_on(self):
        """管理路由器-Mesh穿墙-开启成功"""
        """
        用例-5609 : 点击开关开启，弹出确认框
        用例-5613 : 确认框，一切正常，点击“确定”，弹出【等待页面】
                    查看页面是否有文字提示：重启中，请等待...《trans0322》 ： 是
                    查看页面是否从60s开始倒计时 ： 是
                    倒计时过程中，轮询判断 ： 是
        用例-5526 : 开启开关成功
                    开启开关，看是否可成功 ： 是
                    查看（mesh组网通道）配置项，是否2.4G和5G组网通道都已开启 ： 是
        """
        # 默认是关闭的，如果是关闭的才进行下面的if打开操作
        Statu_Class = self.driver.find_element_by_xpath(RouterManagementLocators.Increase_Mesh_Coverage_Statu).get_attribute("class")
        if Statu_Class == "switch switch-animation":
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

            # 断言：用例-5613 : 确认框，一切正常，点击“确定”，弹出【等待页面】
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Shade))
            )
            # 断言：查看页面是否有文字提示：重启中，请等待...《trans0322》 ： 是
            Shade_Note = self.driver.find_element_by_xpath("//div[@class='reboot-model-contanier']/div[3]").text[:-3]
            assert Shade_Note == "Successful operation, please wait...", Shade_Note
            # 断言：查看页面是否从60s开始倒计时 ： 是
            Shade_StartTime = int(
                self.driver.find_element_by_xpath("//div[@class='reboot-model-contanier']/div[3]").text[-3:-1])
            assert Shade_StartTime == 60, Shade_StartTime
            # 断言：倒计时过程中，轮询判断 ： 是（这里验证5秒的倒计时轮询即可）
            i = 1
            while i <= 5:
                time.sleep(1)
                Shade_Time = int(self.driver.find_element_by_xpath("//div[@class='reboot-model-contanier']/div[3]").text[-3:-1])
                assert Shade_Time == 60 - i, Shade_Time
                i += 1

            # 重启的60s，检查成功后是否有toast提示
            WebDriverWait(self.driver, const.REBOOT_WAIT-5).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
            time.sleep(1)

            # 断言：用例-5526 : 开启开关成功
            Statu_Class = self.driver.find_element_by_xpath(RouterManagementLocators.Increase_Mesh_Coverage_Statu).get_attribute("class")
            assert Statu_Class == "switch switch-animation checked", Statu_Class

        else:
            print("备注：开关默认不为关，故暂未验证开启功能")
            assert 2 == 1       # 作用：使该用例失败




    @unittest.skip("跳过")
    def test_F_routerManagement_increaseMeshCoverage_off(self):
        """管理路由器-Mesh穿墙-关闭成功"""
        """
        用例-5610 : 点击开关关闭，弹出确认框
        用例-5613 : 确认框，一切正常，点击“确定”，弹出【等待页面】
                    查看页面是否有文字提示：重启中，请等待...《trans0322》 ： 是
                    查看页面是否从60s开始倒计时 ： 是
                    倒计时过程中，轮询判断 ： 是
        用例-5527 : 关闭开关成功
                    关闭开关，看是否可成功 ： 是
                    查看（mesh组网通道）配置项，是否2.4G通道关闭，5G通道开启 ： 是
        """
        # 开关理应是打开的，如果是打开的才进行下面的if关闭操作
        Statu_Class = self.driver.find_element_by_xpath(
            RouterManagementLocators.Increase_Mesh_Coverage_Statu).get_attribute("class")
        if Statu_Class == "switch switch-animation checked":
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Increase_Mesh_Coverage_Statu))
            ).click()

            # 断言：用例-5610 : 点击开关关闭，弹出确认框
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Dialog))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Dialog).is_displayed()

            # 点击 确定 按钮
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, CommonLocators.Confirm))
            ).click()

            # 断言：用例-5613 : 确认框，一切正常，点击“确定”，弹出【等待页面】
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Shade))
            )
            # 断言：查看页面是否有文字提示：重启中，请等待...《trans0322》 ： 是
            Shade_Note = self.driver.find_element_by_xpath("//div[@class='reboot-model-contanier']/div[3]").text[:-3]
            assert Shade_Note == "Successful operation, please wait...", Shade_Note
            # 断言：查看页面是否从60s开始倒计时 ： 是
            Shade_StartTime = int(
                self.driver.find_element_by_xpath("//div[@class='reboot-model-contanier']/div[3]").text[-3:-1])
            assert Shade_StartTime == 60, Shade_StartTime
            # 断言：倒计时过程中，轮询判断 ： 是（这里验证5秒的倒计时轮询即可）
            i = 1
            while i <= 5:
                time.sleep(1)
                Shade_Time = int(self.driver.find_element_by_xpath("//div[@class='reboot-model-contanier']/div[3]").text[-3:-1])
                assert Shade_Time == 60 - i, Shade_Time
                i += 1

            # 重启的60s，检查成功后是否有toast提示
            WebDriverWait(self.driver, const.REBOOT_WAIT-5).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"
            time.sleep(1)

            # 断言：用例-5527 : 关闭开关成功
            Statu_Class = self.driver.find_element_by_xpath(RouterManagementLocators.Increase_Mesh_Coverage_Statu).get_attribute("class")
            assert Statu_Class == "switch switch-animation", Statu_Class

        else:
            print("备注：开关理应不是打开状态，故暂未验证关闭功能")
            assert 2 == 1  # 作用：使该用例失败





    @unittest.skip("跳过")
    def test_G_routerManagement_completeGraph_default_note(self):
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





    @unittest.skip("跳过")
    def test_H_routerManagement_editDeviceName_elementsCheck(self):
        """管理路由器-修改设备名称-元素检查"""
        """
        用例-1730 : 设备名称编辑按钮，点击弹出编辑框
                    点击设备名称编辑按钮，看是否弹出编辑框 ： 是
        用例-1731 : 设备名称编辑框-元素检测
                    查看标题是否为：修改设备名称 ： 是
                    查看是否有按钮：取消，确定 ： 是
        用例-1732 : 设备名称编辑框-输入框中默认显示当前设备名称
        用例-1733 : 设备名称编辑框-点击弹出设备名称下拉框
                    点击设备名称编辑框，查看是否弹出设备名称下拉框 ： 是
        用例-1734 : 设备名称编辑框-下拉框显示信息检测
                    查看下拉框中显示的信息是否有：客厅、主卧、书房、客房、儿童房、杂物间、衣帽间、游戏室、
                                                厨房、前厅、门厅、餐厅、卫生间、地下室、车库
        """
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.List))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.PrimaryRoute_Name))
        )
        PrimaryRoute_Name_Default = self.driver.find_element_by_xpath(RouterManagementLocators.PrimaryRoute_Name).text

        # 断言：用例-1730 : 设备名称编辑按钮，点击弹出编辑框
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.PrimaryRoute_EditName))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Box))
        )
        assert self.driver.find_element_by_xpath(RouterManagementLocators.Box).is_displayed()

        # 断言：用例-1731 : 设备名称编辑框-元素检测
        # 断言：标题是否为：设备名称
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Box_Title))
        )
        Title_Text = self.driver.find_element_by_xpath(RouterManagementLocators.Box_Title).text
        assert Title_Text== "Device", Title_Text
        # 断言：是否有按钮：取消
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Box_Cancel))
        )
        assert self.driver.find_element_by_xpath(RouterManagementLocators.Box_Cancel).is_displayed()
        # 断言：是否有按钮：确定
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Box_Confirm))
        )
        assert self.driver.find_element_by_xpath(RouterManagementLocators.Box_Confirm).is_displayed()

        # 断言：用例-1732 : 设备名称编辑框-输入框中默认显示当前设备名称
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Box_DeviceName))
        )
        DeviceName = self.driver.find_element_by_xpath(RouterManagementLocators.Box_DeviceName).get_attribute('value')
        assert DeviceName == PrimaryRoute_Name_Default, DeviceName

        # 断言：用例-1733 : 设备名称编辑框-点击弹出设备名称下拉框
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Box_DeviceName))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Box_On_or_Off))
        )
        Select_Statu = self.driver.find_element_by_xpath(RouterManagementLocators.Box_On_or_Off).get_attribute('class')
        assert Select_Statu == "icon open", Select_Statu

        # 断言：用例-1734 : 设备名称编辑框-下拉框显示信息检测
        Optional_Name_List = [
            "Living Room", "Bedroom", "Study", "Guest Room", "Children's Room",
            "Utility room", "Locker room", "Game room", "Kitchen", "Lobby",
            "Hallway", "Dining room", "Bathroom", "Basement", "Garage"
        ]
        i = 1
        while i <= 15:
            Optional_Name =self.driver.find_element_by_xpath(RouterManagementLocators.Box_Optional_Name.format(num=i)).text
            assert Optional_Name == Optional_Name_List[i-1], Optional_Name
            i += 1





    @unittest.skip("跳过")
    def test_I_routerManagement_editDeviceName_edit(self):
        """管理路由器-修改设备名称-编辑"""
        """
        用例-1738 : 设备名称编辑框-输入空或全部空格，错误提示
        用例-1737 : 设备名称编辑框-输入内容长度超限，错误提示
        用例-1736 : 设备名称编辑框-可以输入任意字符
                    在设备名称编辑框中输入任意字符（数字，字母，符号，汉字） ： 是
        用例-1735 : 设备名称编辑框-点击设备名称下拉框中的设备名能成功选中并替换设备框中的内容
                    点击设备名称下拉框中任意一设备名称，查看是否成功选中并替换设备名称栏中的设备名 ： 是
        用例-1741 : 设备名称编辑框-点击“取消”按钮，关闭弹框，不修改
                    设备名称编辑框，点击“取消”按钮，看是否关闭弹框，不修改，保持当前页面不变 ： 是
        """
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.List))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.PrimaryRoute_EditName))
        ).click()

        # 获取初始的设备名字，用于校验：用例-1741
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.PrimaryRoute_Name))
        )
        PrimaryRoute_Name_Default = self.driver.find_element_by_xpath(RouterManagementLocators.PrimaryRoute_Name).text

        # 断言：用例-1738 : 设备名称编辑框-输入空或全部空格，错误提示
        # 断言：输入空
        # 模拟键盘删除键
        i = 1
        while i <= 7:
            self.driver.find_element_by_xpath(RouterManagementLocators.Box_DeviceName).send_keys(Keys.BACK_SPACE)
            i += 1
        time.sleep(0.5)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Box_Confirm))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Box_Error))
        )
        Error_Text = self.driver.find_element_by_xpath(RouterManagementLocators.Box_Error).text
        assert Error_Text == "The name should not be empty", Error_Text
        # 断言：输入全部为空格，如4个空格
        self.driver.find_element_by_xpath(RouterManagementLocators.Box_DeviceName).send_keys("    ")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Box_Confirm))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Box_Error))
        )
        Error_Text = self.driver.find_element_by_xpath(RouterManagementLocators.Box_Error).text
        assert Error_Text == "The name should not be empty", Error_Text


        # 断言：用例-1737 : 设备名称编辑框-输入内容长度超限，错误提示
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Box_DeviceName))
        ).clear()
        self.driver.find_element_by_xpath(RouterManagementLocators.Box_DeviceName).send_keys("123456789012345678901")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Box_Confirm))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Box_Error))
        )
        Error_Text = self.driver.find_element_by_xpath(RouterManagementLocators.Box_Error).text
        assert Error_Text == "The name is too long", Error_Text


        # 断言：用例-1736 : 设备名称编辑框-可以输入任意字符
        # 断言：输入：数字
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Box_DeviceName))
        ).clear()
        self.driver.find_element_by_xpath(RouterManagementLocators.Box_DeviceName).send_keys("12345")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Box_DeviceName))
        )
        DeviceName = self.driver.find_element_by_xpath(RouterManagementLocators.Box_DeviceName).get_attribute('value')
        assert DeviceName == "12345", DeviceName
        # 断言：输入：字母
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Box_DeviceName))
        ).clear()
        self.driver.find_element_by_xpath(RouterManagementLocators.Box_DeviceName).send_keys("abcde")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Box_DeviceName))
        )
        DeviceName = self.driver.find_element_by_xpath(RouterManagementLocators.Box_DeviceName).get_attribute('value')
        assert DeviceName == "abcde", DeviceName
        # 断言：输入：符号
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Box_DeviceName))
        ).clear()
        self.driver.find_element_by_xpath(RouterManagementLocators.Box_DeviceName).send_keys("!@#$%")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Box_DeviceName))
        )
        DeviceName = self.driver.find_element_by_xpath(RouterManagementLocators.Box_DeviceName).get_attribute('value')
        assert DeviceName == "!@#$%", DeviceName
        # 断言：输入：汉字
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Box_DeviceName))
        ).clear()
        self.driver.find_element_by_xpath(RouterManagementLocators.Box_DeviceName).send_keys("主路由")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Box_DeviceName))
        )
        DeviceName = self.driver.find_element_by_xpath(RouterManagementLocators.Box_DeviceName).get_attribute('value')
        assert DeviceName == "主路由", DeviceName
        # 断言：组合输入
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Box_DeviceName))
        ).clear()
        self.driver.find_element_by_xpath(RouterManagementLocators.Box_DeviceName).send_keys("M2l@主路由")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Box_DeviceName))
        )
        DeviceName = self.driver.find_element_by_xpath(RouterManagementLocators.Box_DeviceName).get_attribute('value')
        assert DeviceName == "M2l@主路由", DeviceName


        # 断言：用例-1735 : 设备名称编辑框-点击设备名称下拉框中的设备名能成功选中并替换设备框中的内容
        time.sleep(1)
        # 选择3个进行判断
        # 第1个
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Box_DeviceName))
        ).click()
        Select_1 = RouterManagementLocators.Box_Optional_Name.format(num=1)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Select_1))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Box_DeviceName))
        )
        DeviceName = self.driver.find_element_by_xpath(RouterManagementLocators.Box_DeviceName).get_attribute('value')
        assert DeviceName == "Living Room", DeviceName
        # 第2个
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Box_DeviceName))
        ).click()
        Select_7 = RouterManagementLocators.Box_Optional_Name.format(num=7)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Select_7))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Box_DeviceName))
        )
        DeviceName = self.driver.find_element_by_xpath(RouterManagementLocators.Box_DeviceName).get_attribute('value')
        assert DeviceName == "Locker room", DeviceName
        # 第3个
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Box_DeviceName))
        ).click()
        Select_15 = RouterManagementLocators.Box_Optional_Name.format(num=15)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Select_15))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Box_DeviceName))
        )
        DeviceName = self.driver.find_element_by_xpath(RouterManagementLocators.Box_DeviceName).get_attribute('value')
        assert DeviceName == "Garage", DeviceName

        # 断言：用例-1741 : 设备名称编辑框-点击“取消”按钮，关闭弹框，不修改
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Box_Cancel))
        ).click()
        # 检验设备名还是初始的名字
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.PrimaryRoute_Name))
        )
        PrimaryRoute_Name = self.driver.find_element_by_xpath(RouterManagementLocators.PrimaryRoute_Name).text
        assert PrimaryRoute_Name == PrimaryRoute_Name_Default, PrimaryRoute_Name



    @unittest.skip("跳过")
    def test_J_routerManagement_editDeviceName_errorNotSave(self):
        """管理路由器-修改设备名称-有异常提示时不能保存"""
        """
        用例-1739 : 设备名称编辑框-输入框有异常提示，点击“确定”按钮，保持弹框不变，显示异常提示
                    输入异常的内容，使得输入框下方有异常提示，点击“确定”按钮，保持弹框不变，仍然显示异常提示 ： 是
        """
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.List))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.PrimaryRoute_EditName))
        ).click()

        # 模拟2种异常情况
        # 第1种：为空异常
        i = 1
        while i <= 7:
            self.driver.find_element_by_xpath(RouterManagementLocators.Box_DeviceName).send_keys(Keys.BACK_SPACE)
            i += 1
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Box_Confirm))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Box_Error))
        )
        # 第一次点击 保存 按钮，检验异常提示是否还在
        self.driver.find_element_by_xpath(RouterManagementLocators.Box_Confirm).click()
        Error_Text = self.driver.find_element_by_xpath(RouterManagementLocators.Box_Error).text
        assert Error_Text == "The name should not be empty", Error_Text
        # 第二次点击 保存 按钮，检验异常提示是否还在
        self.driver.find_element_by_xpath(RouterManagementLocators.Box_Confirm).click()
        Error_Text = self.driver.find_element_by_xpath(RouterManagementLocators.Box_Error).text
        assert Error_Text == "The name should not be empty", Error_Text

        # 第2种：超过长度异常
        self.driver.find_element_by_xpath(RouterManagementLocators.Box_DeviceName).send_keys("123456789012345678901")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Box_Confirm))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.Box_Error))
        )
        # 第一次点击 保存 按钮，检验异常提示是否还在
        self.driver.find_element_by_xpath(RouterManagementLocators.Box_Confirm).click()
        Error_Text = self.driver.find_element_by_xpath(RouterManagementLocators.Box_Error).text
        assert Error_Text == "The name is too long", Error_Text
        # 第二次点击 保存 按钮，检验异常提示是否还在
        self.driver.find_element_by_xpath(RouterManagementLocators.Box_Confirm).click()
        Error_Text = self.driver.find_element_by_xpath(RouterManagementLocators.Box_Error).text
        assert Error_Text == "The name is too long", Error_Text




    @unittest.skip("跳过")
    def test_K_routerManagement_editDeviceName_save_ok(self):
        """管理路由器-修改设备名称-保存成功"""
        """
        用例-1740 : 设备名称编辑框-输入正确的设备名称，点击“确定”按钮，关闭弹框，修改成功
                    选择或输入一个正确的设备名称，点击确定按钮 ： 1. 关闭弹框
                                                                2. 设备名称显示修改后的名称
        用例-1742 : 主路由修改设备名称，可成功
                    修改主路由m2的设备名称，查看是否修改成功 ： 是
        """
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.List))
        ).click()

        # 模拟2种情况
        # 第1种：手动输入设备名能成功保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.PrimaryRoute_EditName))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Box_DeviceName))
        ).clear()
        self.driver.find_element_by_xpath(RouterManagementLocators.Box_DeviceName).send_keys("M2主路由")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Box_Confirm))
        ).click()
        # 断言：关闭弹框
        WebDriverWait(self.driver, const.MEDIUM_WAIT+5).until_not(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Box))
        )
        # 断言：设备名称显示修改后的名称
        self.driver.refresh()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.PrimaryRoute_Name))
        )
        PrimaryRoute_Name = self.driver.find_element_by_xpath(RouterManagementLocators.PrimaryRoute_Name).text
        assert PrimaryRoute_Name == "M2主路由", PrimaryRoute_Name
        time.sleep(1)

        # 第2种：下拉列表中选择任一能成功保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.PrimaryRoute_EditName))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Box_DeviceName))
        ).click()
        Select_7 = RouterManagementLocators.Box_Optional_Name.format(num=7)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Select_7))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Box_Confirm))
        ).click()
        # 断言：关闭弹框
        WebDriverWait(self.driver, const.MEDIUM_WAIT + 5).until_not(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Box))
        )
        # 断言：设备名称显示修改后的名称
        self.driver.refresh()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, RouterManagementLocators.PrimaryRoute_Name))
        )
        PrimaryRoute_Name = self.driver.find_element_by_xpath(RouterManagementLocators.PrimaryRoute_Name).text
        assert PrimaryRoute_Name == "Locker room", PrimaryRoute_Name




    @unittest.skip("跳过")
    def test_L_routerManagement_reboot_elementsCheck(self):
        """管理路由器-重启-元素检查"""
        """
        用例-1761 : 重启按钮点击弹出重启确认框
                    点击操作栏中的重启按钮，查看是否弹出重启确认框 ： 是
        用例-1762 : 重启确认框元素显示检测
                    查看重启确认框中是否显示提示语句：重启后将会中断当前所有连接，大概需要1分钟。《trans0121》 ： 是
                    查看重启确认框是否显示“重启”、“取消”按钮 ： 是
        用例-1763 : 重启确认框取消按钮点击后弹框消失
                    点击重启确认框的取消按钮，查看是否弹框消失，路由器不重启 ： 是
        """
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.List))
        ).click()

        # 断言：用例-1761 : 重启按钮点击弹出重启确认框
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.PrimaryRoute_Reboot))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Dialog))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Dialog).is_displayed()

        # 断言：用例-1762 : 重启确认框元素显示检测
        # 断言：提示语句是否为：重启后将会中断当前所有连接，大概需要1分钟。
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Dialog_Note))
        )
        Dialog_Note = self.driver.find_element_by_xpath(CommonLocators.Dialog_Note).text
        assert Dialog_Note == "All connections will be interrupted for about 1 min for rebooting", Dialog_Note
        # 断言：是否有按钮：取消
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Cancel))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Cancel).is_displayed()
        # 断言：是否有按钮：重启
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Confirm))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Confirm).is_displayed()

        # 断言：用例-1763 : 重启确认框取消按钮点击后弹框消失
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Cancel))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until_not(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Dialog))
        )
        # 断言：假设可以切换到“mesh拓扑图”页则判断为没有进行重启
        time.sleep(2)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Mesh_Topology))
        ).click()






    @unittest.skip("跳过")
    def test_M_routerManagement_reboot_ok(self):
        """管理路由器-重启-重启成功检查"""
        """
        用例-1764 : 重启确认框-主路由，点击“重启路由器”按钮，弹出【等待页面】
                    主路由，在弹出的重启确认框中，点击重启路由器按钮，看是否弹出【等待页面】 ： 是
        用例-5096 : web-主路由重启：【等待页面】显示操作检测
                    查看页面是否有文字提示： 重启中，请等待...《trans0322》 ： 是
                                            查看页面是否从60s开始倒计时 ： 是
                                            倒计时过程中，轮询判断 ： 是
        用例-1769 : 主路由能重启成功
                    主路由，点击重启路由器，看是否可正常重启成功 ： 是
        """
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.List))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.PrimaryRoute_Reboot))
        ).click()
        # 点击 确定 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Confirm))
        ).click()

        # 断言：用例-1764 : 重启确认框-主路由，点击“重启路由器”按钮，弹出【等待页面】
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Shade))
        )

        # 断言：用例-5096 : web-主路由重启：【等待页面】显示操作检测
        # 断言：查看页面是否有文字提示：重启中，请等待...《trans0322》 ： 是
        Shade_Note = self.driver.find_element_by_xpath(CommonLocators.Shade_Note).text[:-3]
        assert Shade_Note == "Successful operation, please wait...", Shade_Note
        # 断言：查看页面是否从60s开始倒计时 ： 是
        Shade_StartTime = int(
            self.driver.find_element_by_xpath(CommonLocators.Shade_Note).text[-3:-1])
        assert Shade_StartTime == 60, Shade_StartTime
        # 断言：倒计时过程中，轮询判断 ： 是（这里验证5秒的倒计时轮询即可）
        i = 1
        while i <= 5:
            time.sleep(1)
            Shade_Time = int(self.driver.find_element_by_xpath(CommonLocators.Shade_Note).text[-3:-1])
            assert Shade_Time == 60 - i, Shade_Time
            i += 1

        # 断言：用例-1769 : 主路由能重启成功
        # 断言：重启的60s，修改成功后会跳转到登录页面，则查看是否有登录按钮即可
        WebDriverWait(self.driver, const.REBOOT_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Login))
        )
        # 断言：可重新登录，即判断为重启成功
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.InputPassword))
        ).send_keys(const.PASSWORD)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Login))
        ).click()
        # 判断有“退出登录”即可
        time.sleep(2)
        WebDriverWait(self.driver, const.REBOOT_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Logout))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Logout).is_displayed()






    @unittest.skip("跳过")
    def test_N_routerManagement_factoryReset_elementsCheck(self):
        """管理路由器-恢复出厂设置-元素检查"""
        """
        用例-1772 : 主路由，恢复出厂设置按钮点击弹出恢复出厂设置确认框
                    点击主路由列表中的“恢复出厂设置”按钮，查看是否弹出恢复出厂设置确认框 ： 是
        用例-1773 : 主路由，恢复出厂设置确认框显示元素检测
                    查看恢复出厂设置确认框中是否显示提示信息“恢复出厂设置，路由器将恢复到出厂状态。所有连接将中断并且解除组网关系/trans0206” ： 是
                    查看是否显示“取消/trans0025”、“恢复出厂设置/trans0205”按钮 ： 是
        用例-1774 : 主路由，恢复出厂设置确认框取消按钮点击后，确认框消失
                    点击恢复出厂设置确认框中的取消按钮，查看确认提示框是否消失，路由器不会有任何操作 ： 是
        """
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.List))
        ).click()

        # 断言：用例-1772 : 主路由，恢复出厂设置按钮点击弹出恢复出厂设置确认框
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.PrimaryRoute_Factory_Reset))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Dialog))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Dialog).is_displayed()

        # 断言：用例-1773 : 主路由，恢复出厂设置确认框显示元素检测
        # 断言：提示语句是否为：恢复出厂设置，路由器将恢复到出厂状态。所有连接将中断并且解除组网关系
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Dialog_Note))
        )
        Dialog_Note = self.driver.find_element_by_xpath(CommonLocators.Dialog_Note).text
        assert Dialog_Note == "Resetting will cause all devices to be disconnected and the mesh network to be terminated.", Dialog_Note
        # 断言：是否有按钮：取消
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Cancel))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Cancel).is_displayed()
        # 断言：是否有按钮：恢复出厂设置
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Confirm))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Confirm).is_displayed()

        # 断言：用例-1774 : 主路由，恢复出厂设置确认框取消按钮点击后，确认框消失
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Cancel))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until_not(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Dialog))
        )
        # 断言：假设可以切换到“mesh拓扑图”页则判断为没有进行重启
        time.sleep(2)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.Mesh_Topology))
        ).click()






    #@unittest.skip("跳过")
    def test_O_routerManagement_factoryReset_ok(self):
        """管理路由器-恢复出厂设置-恢复出厂设置成功检查"""
        """
        用例-1775 : 主路由，恢复出厂设置确认框“恢复出厂设置”按钮点击后，弹出【等待页面】
                    主路由，在弹出的重置确认框中，点击重置路由器按钮，看是否弹出60S重置倒计时遮罩 ： 是
        用例-5097 : web-主路由重置：【等待页面】显示操作检测
                    查看页面是否有文字提示： 重启中，请等待...《trans0322》 ： 是
                                            查看页面是否从60s开始倒计时 ： 是
                                            倒计时过程中，轮询判断 ： 是
        用例-1779 : 主路由，恢复出厂设置能成功
                    主路由，恢复出厂设置，看是否可成功 ： 是
        """
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.List))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, RouterManagementLocators.PrimaryRoute_Factory_Reset))
        ).click()
        # 点击 确定 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, CommonLocators.Confirm))
        ).click()

        # 断言：用例-1775 : 主路由，恢复出厂设置确认框“恢复出厂设置”按钮点击后，弹出【等待页面】
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Shade))
        )

        # 断言：用例-5097 : web-主路由重置：【等待页面】显示操作检测
        # 断言：查看页面是否有文字提示：重启中，请等待...《trans0322》 ： 是
        Shade_Note = self.driver.find_element_by_xpath(CommonLocators.Shade_Note).text[:-3]
        assert Shade_Note == "Successful operation, please wait...", Shade_Note
        # 断言：查看页面是否从60s开始倒计时 ： 是
        Shade_StartTime = int(
            self.driver.find_element_by_xpath(CommonLocators.Shade_Note).text[-3:-1])
        assert Shade_StartTime == 60, Shade_StartTime
        # 断言：倒计时过程中，轮询判断 ： 是（这里验证5秒的倒计时轮询即可）
        i = 1
        while i <= 5:
            time.sleep(1)
            Shade_Time = int(self.driver.find_element_by_xpath(CommonLocators.Shade_Note).text[-3:-1])
            assert Shade_Time == 60 - i, Shade_Time
            i += 1

        # 用例-1779 : 主路由，恢复出厂设置能成功
        # 断言：重启的60s，重置成功后会跳转到“设置路由器”页，查看是否有“设置路由器”按钮即可
        WebDriverWait(self.driver, const.REBOOT_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.SetupWifi))
        )
        SetupWifi_Text = self.driver.find_element_by_xpath(CommonLocators.SetupWifi).text
        assert SetupWifi_Text == "Setup Wi-Fi", SetupWifi_Text

