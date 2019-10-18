#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/10/16 9:50
# @Author:  GaoJun

import unittest
import time

from .. base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from rweb import const

from rweb.path.common import CommonLocators
from rweb.path.devices import DevicesLocators
from rweb.path.limitTime import LimitTimeLocators

from . time_limit_testcase import Test_time_limit





class LimitTime(Base):

    # def setUp(self):
    #     super(LimitTime, self).setUp()
    #     # 鼠标移动到切换“我的WiFi”按钮上
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_MyWifi))
    #     )
    #     mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_MyWifi)
    #     ActionChains(self.driver).move_to_element(mouse).perform()
    #     # 点击 接入设备
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
    #         EC.element_to_be_clickable((By.XPATH, CommonLocators.Devices))
    #     ).click()
    #     self.driver.refresh()
    #     # 点击主网-设置
    #     Set = DevicesLocators.Set.format(num=1)
    #     WebDriverWait(self.driver, const.MEDIUM_WAIT + 10).until(
    #         EC.element_to_be_clickable((By.XPATH, Set))
    #     )
    #     time.sleep(0.5)
    #     self.driver.find_element_by_xpath(Set).click()



    def Switch_to_wired_limitTimePage(self):
        flag = False        # 目的：判断是否切换到有线的限时页。False为没有切换到该页，True为切换到该页
        while flag == False:
            try:
                time.sleep(2)
                assert self.driver.find_element_by_xpath(LimitTimeLocators.Page_TimeLimit).is_displayed()
                flag = True
            except:
                # 鼠标移动到切换“我的WiFi”按钮上
                WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                    EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_MyWifi))
                )
                mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_MyWifi)
                ActionChains(self.driver).move_to_element(mouse).perform()
                # 点击 接入设备
                WebDriverWait(self.driver, const.MEDIUM_WAIT + 10).until(
                    EC.element_to_be_clickable((By.XPATH, CommonLocators.Devices))
                )
                time.sleep(1)
                self.driver.find_element_by_xpath(CommonLocators.Devices).click()

                self.driver.refresh()
                # 点击主网-设置
                Set = DevicesLocators.Set.format(num=1)
                WebDriverWait(self.driver, const.MEDIUM_WAIT+5).until(
                    EC.element_to_be_clickable((By.XPATH, Set))
                ).click()







    def Switch_to_5g_limitTimePage(self):
        flag = False        # 目的：判断是否切换到无线的限时页。False为没有切换到该页，True为切换到该页
        while flag == False:
            try:
                time.sleep(2)
                assert self.driver.find_element_by_xpath(LimitTimeLocators.Page_TimeLimit).is_displayed()
                flag = True
            except:
                # 鼠标移动到切换“我的WiFi”按钮上
                WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                    EC.presence_of_element_located((By.XPATH, CommonLocators.LEVEL_1_MyWifi))
                )
                mouse = self.driver.find_element_by_xpath(CommonLocators.LEVEL_1_MyWifi)
                ActionChains(self.driver).move_to_element(mouse).perform()
                # 点击 接入设备
                WebDriverWait(self.driver, const.MEDIUM_WAIT + 10).until(
                    EC.element_to_be_clickable((By.XPATH, CommonLocators.Devices))
                )
                time.sleep(1)
                self.driver.find_element_by_xpath(CommonLocators.Devices).click()

                self.driver.refresh()
                # 点击主网-设置
                Set = DevicesLocators.Set.format(num=2)
                WebDriverWait(self.driver, const.MEDIUM_WAIT+5).until(
                    EC.element_to_be_clickable((By.XPATH, Set))
                ).click()








    #@unittest.skip("跳过")
    def test_A_limitTime_add(self):
        """操作步骤：新增 星期一"""
        self.Switch_to_wired_limitTimePage()
        # 点击 新增 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Add))
        ).click()
        # 选择星期一
        Mondey = LimitTimeLocators.Weeks.format(num=1)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Mondey))
        ).click()
        # 点击 保存 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Insert_Add))
        ).click()

        # 断言:是否操作成功：保存
        # 用例-2028 : 新增框-配置正常，点击“保存”，创建成功，显示在列表中
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言:限时列表中重复时间显示每周一
        self.driver.refresh()
        Repeat = LimitTimeLocators.Repeat.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Repeat))
        )
        assert self.driver.find_element_by_xpath(Repeat).text == "Monday"







    #@unittest.skip("跳过")
    def test_B_limitTime_1(self):
        """【检验】用例-4839 : 设备A添加一个开启状态的限时条目，设备A在限时时间段内无法访问外网(周一不能上网)"""
        self.Switch_to_wired_limitTimePage()
        # 前提条件：有星期一的记录，且开关开启
        try:
            Repeat = LimitTimeLocators.Repeat.format(num="last()")
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, Repeat))
            )
            Week_Name = self.driver.find_element_by_xpath(Repeat).text
            if Week_Name != "Monday":
                print("【备注】该用例无法验证，原因：已添加的显示记录不为：星期一")
                assert False
        except:
            print("【备注】该用例无法验证，原因：限时列表为空")
            assert False


        # 判断开关是否：开启
        Statu = LimitTimeLocators.Statu.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Statu))
        )
        Statu_Class = self.driver.find_element_by_xpath(Statu).get_attribute('class')
        if Statu_Class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：开关为关闭状态")
            assert False

        # 前提已完成，开始检验用例
        Result = Test_time_limit.test_time_limit_1()
        print(Result)
        if Result == 1:
            print("【成功】开关开启，设备A在限时时间段内无法访问外网")
            assert True
        else:
            print("【失败】开关开启，设备A在限时时间段内可以访问外网")
            assert False





    #@unittest.skip("跳过")
    def test_C_limitTime_2(self):
        """【检验】用例-5238 : 设备A添加一个开启状态的限时条目，设备B在设备A的限时时间段内可以访问外网（设备A在周一不能上网，设备B在周一可以让他上网）"""
        self.Switch_to_wired_limitTimePage()
        # 前提条件：有星期一的记录，且开关开启
        try:
            Repeat = LimitTimeLocators.Repeat.format(num="last()")
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, Repeat))
            )
            Week_Name = self.driver.find_element_by_xpath(Repeat).text
            if Week_Name != "Monday":
                print("【备注】该用例无法验证，原因：已添加的显示记录不为：星期一")
                assert False
        except:
            print("【备注】该用例无法验证，原因：限时列表为空")
            assert False

        # 判断开关是否：开启
        Statu = LimitTimeLocators.Statu.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Statu))
        )
        Statu_Class = self.driver.find_element_by_xpath(Statu).get_attribute('class')
        if Statu_Class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：开关为关闭状态")
            assert False

        # 前提已完成，开始检验用例
        Result = Test_time_limit.test_time_limit_2()
        print(Result)
        if Result == 1:
            print("【成功】设备A的限时条目，不会影响设备B的访问")
            assert True
        else:
            print("【失败】设备A的限时条目，会影响设备B的访问")
            assert False






    #@unittest.skip("跳过")
    def test_D_limitTime_editStatu_off(self):
        """操作步骤：将开关关闭"""
        self.Switch_to_wired_limitTimePage()
        # 点击 开关 按钮，由开变为关
        Statu = LimitTimeLocators.Statu.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Statu))
        ).click()
        # 断言:toast提示：关闭成功
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言：开关状态是否为：关闭
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, Statu))
        )
        assert self.driver.find_element_by_xpath(Statu).get_attribute('class') == "switch switch-animation"







    #@unittest.skip("跳过")
    def test_E_limitTime_3(self):
        """【检验】用例-4840 : 设备A添加一个关闭状态的限时条目，设备A在任何时间段都可以访问外网"""
        self.Switch_to_wired_limitTimePage()
        # 前提条件：有星期一的记录，且开关关闭
        try:
            Repeat = LimitTimeLocators.Repeat.format(num="last()")
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, Repeat))
            )
            Week_Name = self.driver.find_element_by_xpath(Repeat).text
            if Week_Name != "Monday":
                print("【备注】该用例无法验证，原因：已添加的显示记录不为：星期一")
                assert False
        except:
            print("【备注】该用例无法验证，原因：限时列表为空")
            assert False

        # 判断开关是否：关闭
        Statu = LimitTimeLocators.Statu.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Statu))
        )
        Statu_Class = self.driver.find_element_by_xpath(Statu).get_attribute('class')
        if Statu_Class != "switch switch-animation":
            print("【备注】该用例无法验证，原因：开关为开启状态")
            assert False

        # 前提已完成，开始检验用例
        Result = Test_time_limit.test_time_limit_3()
        print(Result)
        if Result == 1:
            print("【成功】开关关闭，设备A在任何时间段都可以访问外网")
            assert True
        else:
            print("【失败】开关关闭，设备A在任何时间段不都可以访问外网")
            assert False







    #@unittest.skip("跳过")
    def test_F_limitTime_editValue(self):
        """操作步骤：将星期一修改为星期二，并将开关开启"""
        self.Switch_to_wired_limitTimePage()
        # 点击 编辑 按钮
        Edit = LimitTimeLocators.Edit.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Edit))
        ).click()
        # 取消 星期一，选择 星期二
        Mondey = LimitTimeLocators.Weeks.format(num=1)
        Tuesday = LimitTimeLocators.Weeks.format(num=2)
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Mondey))
        ).click()
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Tuesday))
        ).click()
        # 点击 保存 按钮
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Insert_Add))
        ).click()

        # 断言:是否操作成功：保存
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

        # 断言:判断是否只选中的星期二
        self.driver.refresh()
        Repeat = LimitTimeLocators.Repeat.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Repeat))
        )
        assert self.driver.find_element_by_xpath(Repeat).text == "Tuesday"

        # 开启开关
        Statu = LimitTimeLocators.Statu.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, Statu))
        )
        Statu_Class = self.driver.find_element_by_xpath(Statu).get_attribute('class')
        if Statu_Class != "switch switch-animation checked":
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, Statu))
            ).click()
            # 断言:toast提示：关闭成功
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"






    #@unittest.skip("跳过")
    def test_G_limitTime_4(self):
        """【检验】用例-4841 : 修改设备A的限时时段，新限时时段生效，旧限时时段失效(不能上网时间从周一修改为周二)"""
        self.Switch_to_wired_limitTimePage()
        # 前提条件：有星期二的记录，且开关关闭
        try:
            Repeat = LimitTimeLocators.Repeat.format(num="last()")
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, Repeat))
            )
            Week_Name = self.driver.find_element_by_xpath(Repeat).text
            if Week_Name != "Tuesday":
                print("【备注】该用例无法验证，原因：已添加的显示记录不为：星期二")
                assert False
        except:
            print("【备注】该用例无法验证，原因：限时列表为空")
            assert False

        # 判断开关是否：开启
        Statu = LimitTimeLocators.Statu.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Statu))
        )
        Statu_Class = self.driver.find_element_by_xpath(Statu).get_attribute('class')
        if Statu_Class != "switch switch-animation checked":
            print("【备注】该用例无法验证，原因：开关为关闭状态")
            assert False

        # 前提已完成，开始检验用例
        Result = Test_time_limit.test_time_limit_4()
        print(Result)
        if Result == 1:
            print("【成功】修改限时时段后，新限时时段生效，旧限时时段失效")
            assert True
        else:
            print("【失败】修改限时时段后，未做到：新限时时段生效，旧限时时段失效")
            assert False








    #@unittest.skip("跳过")
    def test_H_limitTime_delete(self):
        """操作步骤：删除限时记录"""
        self.Switch_to_wired_limitTimePage()
        flag = False
        while flag == False:
            try:
                assert self.driver.find_element_by_xpath(LimitTimeLocators.List_Null).is_displayed()
                flag = True
            except:
                Delete = LimitTimeLocators.Delete.format(num="last()")
                WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                    EC.element_to_be_clickable((By.XPATH, Delete))
                ).click()
                # 断言:toast提示：成功
                WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                    EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
                )
                time.sleep(2)






    #@unittest.skip("跳过")
    def test_I_limitTime_adds(self):
        """操作步骤：新增 星期一、星期三、星期五"""
        self.Switch_to_wired_limitTimePage()
        Mondey = LimitTimeLocators.Weeks.format(num=1)
        Wednesday = LimitTimeLocators.Weeks.format(num=3)
        Friday = LimitTimeLocators.Weeks.format(num=5)
        Weeks = [Mondey, Wednesday, Friday]
        i = 1
        while i <= 3:
            # 点击 新增 按钮
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Add))
            ).click()
            # 选择时间
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, Weeks[i-1]))
            ).click()
            # 点击 保存 按钮
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Insert_Add))
            ).click()

            # 断言:是否操作成功：保存
            # 用例-2028 : 新增框-配置正常，点击“保存”，创建成功，显示在列表中
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

            # 断言:限时列表中重复时间显示每周一
            self.driver.refresh()
            Repeat = LimitTimeLocators.Repeat.format(num="last()")
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, Repeat))
            )
            if i == 1:
                assert self.driver.find_element_by_xpath(Repeat).text == "Monday"
            elif i == 2:
                assert self.driver.find_element_by_xpath(Repeat).text == "Wednesday"
            else:
                assert self.driver.find_element_by_xpath(Repeat).text == "Friday"
            i += 1
            time.sleep(1)






    #@unittest.skip("跳过")
    def test_J_limitTime_5(self):
        """【检验】用例-5237 : 设备A添加多个开启状态的限时条目，设备A在限时时间段内无法访问外网 (周一，周三，周五不能上网)"""
        self.Switch_to_wired_limitTimePage()
        # 前提条件：有周一，周三，周五的限时，且开关都为开启
        try:
            Weeks = ["Monday", "Wednesday", "Friday"]
            i = 1
            while i <= 3:
                Repeat = LimitTimeLocators.Repeat.format(num=i)
                WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                    EC.element_to_be_clickable((By.XPATH, Repeat))
                )
                Week_Name = self.driver.find_element_by_xpath(Repeat).text
                assert Week_Name == Weeks[i - 1]
                if Week_Name != Weeks[i - 1]:
                    if i == 1:
                        print("【备注】该用例无法验证，原因：已添加的显示记录不为：星期一")
                    elif i == 2:
                        print("【备注】该用例无法验证，原因：已添加的显示记录不为：星期三")
                    else:
                        print("【备注】该用例无法验证，原因：已添加的显示记录不为：星期五")
                    assert False
                Statu = LimitTimeLocators.Statu.format(num=i)
                WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                    EC.element_to_be_clickable((By.XPATH, Statu))
                )
                Statu_Class = self.driver.find_element_by_xpath(Statu).get_attribute('class')
                if Statu_Class != "switch switch-animation checked":
                    if i == 1:
                        print("【备注】该用例无法验证，原因：星期一的开关为关闭状态")
                    elif i == 2:
                        print("【备注】该用例无法验证，原因：星期三的开关为关闭状态")
                    else:
                        print("【备注】该用例无法验证，原因：星期五的开关为关闭状态")
                    assert False
                i += 1
        except:
            print("【备注】该用例无法验证，原因：不满足条件“周一，周三，周五的限时，且开关都为开启”")
            assert False

        # 前提已完成，开始检验用例
        Result = Test_time_limit.test_time_limit_5()
        print(Result)
        if Result == 1:
            print("【成功】开启多个限时条目，设备A在限时时段内无法访问外网")
            assert True
        else:
            print("【失败】开启多个限时条目，设备A在限时时段内能访问外网")
            assert False






    #@unittest.skip("跳过")
    def test_K_limitTime_edits(self):
        """操作步骤：设备A限时条目为周一、周三，设备B限时条目为周二、周四"""
        # 设备A：修改限时条目，即只需删除周五的条目即可
        self.Switch_to_wired_limitTimePage()
        Delete = LimitTimeLocators.Delete.format(num="last()")
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, Delete))
        ).click()
        # 断言:toast提示：成功
        WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
            EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
        )
        time.sleep(0.5)

        # 设备B：新增限时条目：周二、周四
        self.Switch_to_5g_limitTimePage()
        # 进行新增操作
        Tuesday = LimitTimeLocators.Weeks.format(num=2)
        Thursday = LimitTimeLocators.Weeks.format(num=4)
        Weeks = [Tuesday, Thursday]
        i = 1
        while i <= 2:
            # 点击 新增 按钮
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Add))
            ).click()
            # 选择时间
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, Weeks[i - 1]))
            ).click()
            # 点击 保存 按钮
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, LimitTimeLocators.Insert_Add))
            ).click()

            # 断言:是否操作成功：保存
            # 用例-2028 : 新增框-配置正常，点击“保存”，创建成功，显示在列表中
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
            )
            assert self.driver.find_element_by_xpath(CommonLocators.Success_Toast).text == "Successful operation"

            # 断言:限时列表中重复时间显示每周二、四
            self.driver.refresh()
            Repeat = LimitTimeLocators.Repeat.format(num="last()")
            WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                EC.element_to_be_clickable((By.XPATH, Repeat))
            )
            if i == 1:
                assert self.driver.find_element_by_xpath(Repeat).text == "Tuesday"
            else:
                assert self.driver.find_element_by_xpath(Repeat).text == "Thursday"
            i += 1
            time.sleep(1)






    #@unittest.skip("跳过")
    def test_L_limitTime_6(self):
        """【检验】用例-5239 : 多个设备添加开启状态的限时条目，对应设备在其限时时间段内无法访问外网  (设备A周一周三不能上网，设备B周二周四不能上网)"""

        # 前提条件：设备A限时条目有周一周三，设备B限时条目有周二周四，且开关都为开启
        # 判断设备B
        self.Switch_to_5g_limitTimePage()
        try:
            Weeks = ["Tuesday", "Thursday"]
            i = 1
            while i <= 2:
                Repeat = LimitTimeLocators.Repeat.format(num=i)
                WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                    EC.element_to_be_clickable((By.XPATH, Repeat))
                )
                Week_Name = self.driver.find_element_by_xpath(Repeat).text
                assert Week_Name == Weeks[i - 1]
                if Week_Name != Weeks[i - 1]:
                    if i == 1:
                        print("【备注】该用例无法验证，原因：设备B已添加的显示记录不为：星期二")
                    else:
                        print("【备注】该用例无法验证，原因：设备B已添加的显示记录不为：星期四")
                    assert False
                Statu = LimitTimeLocators.Statu.format(num=i)
                WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                    EC.element_to_be_clickable((By.XPATH, Statu))
                )
                Statu_Class = self.driver.find_element_by_xpath(Statu).get_attribute('class')
                if Statu_Class != "switch switch-animation checked":
                    if i == 1:
                        print("【备注】该用例无法验证，原因：设备B的星期二开关为关闭状态")
                    else:
                        print("【备注】该用例无法验证，原因：设备B的星期四开关为关闭状态")
                    assert False
                i += 1
        except:
            print("【备注】该用例无法验证，原因：设备B不满足条件“具有限时条目周二、周四”")
            assert False

        # 判断设备A
        self.Switch_to_wired_limitTimePage()
        try:
            Weeks = ["Monday", "Wednesday"]
            i = 1
            while i <= 2:
                Repeat = LimitTimeLocators.Repeat.format(num=i)
                WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                    EC.element_to_be_clickable((By.XPATH, Repeat))
                )
                Week_Name = self.driver.find_element_by_xpath(Repeat).text
                assert Week_Name == Weeks[i - 1]
                if Week_Name != Weeks[i - 1]:
                    if i == 1:
                        print("【备注】该用例无法验证，原因：设备A已添加的显示记录不为：星期一")
                    else:
                        print("【备注】该用例无法验证，原因：设备A已添加的显示记录不为：星期三")
                    assert False
                Statu = LimitTimeLocators.Statu.format(num=i)
                WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                    EC.element_to_be_clickable((By.XPATH, Statu))
                )
                Statu_Class = self.driver.find_element_by_xpath(Statu).get_attribute('class')
                if Statu_Class != "switch switch-animation checked":
                    if i == 1:
                        print("【备注】该用例无法验证，原因：设备A的星期一开关为关闭状态")
                    else:
                        print("【备注】该用例无法验证，原因：设备A的星期三开关为关闭状态")
                    assert False
                i += 1
        except:
            print("【备注】该用例无法验证，原因：设备A不满足条件“具有限时条目周一、周三”")
            assert False


        # 前提已完成，开始检验用例
        Result = Test_time_limit.test_time_limit_6()
        print(Result)
        if Result == 1:
            print("【成功】多个设备在其限时时间段内，都无法访问外网")
            assert True
        else:
            print("【失败】多个设备在其限时时间段内，能访问外网")
            assert False






    #@unittest.skip("跳过")
    def test_M_limitTime_delete(self):
        """操作步骤：删除所有限时记录，回到初始状态"""
        # 删除设备A
        self.Switch_to_wired_limitTimePage()
        flag = False
        while flag == False:
            try:
                assert self.driver.find_element_by_xpath(LimitTimeLocators.List_Null).is_displayed()
                flag = True
            except:
                Delete = LimitTimeLocators.Delete.format(num="last()")
                WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                    EC.element_to_be_clickable((By.XPATH, Delete))
                ).click()
                # 断言:toast提示：成功
                WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                    EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
                )
                time.sleep(2)

        # 删除设备B
        self.Switch_to_5g_limitTimePage()
        # 进行删除操作
        flag = False
        while flag == False:
            try:
                assert self.driver.find_element_by_xpath(LimitTimeLocators.List_Null).is_displayed()
                flag = True
            except:
                Delete = LimitTimeLocators.Delete.format(num="last()")
                WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                    EC.element_to_be_clickable((By.XPATH, Delete))
                ).click()
                # 断言:toast提示：成功
                WebDriverWait(self.driver, const.MEDIUM_WAIT).until(
                    EC.presence_of_element_located((By.XPATH, CommonLocators.Success_Toast))
                )
                time.sleep(2)

