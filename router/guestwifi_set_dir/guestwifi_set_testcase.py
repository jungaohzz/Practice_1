import os
import time
import sys
from . import guestwifi_set
from . import guestwifi_set_conf

class Test_wifi():

    @staticmethod
    # 用例-3384:“双频合一”开启状态，扫描到的SSID中，5G和2.4G SSID一样
    def test_wifi_1():
        time.sleep(30)
        wlan_ssid = guestwifi_set_conf.ssid_2g
        mac_5g = guestwifi_set_conf.mac_5g
        mac_2g = guestwifi_set_conf.mac_2g
        # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
        wlan0_list = guestwifi_set.Wifi_scan.wlan0_ssid_scan(wlan_ssid)
        print (wlan0_list)
        # 通过2G ssid筛选出对应的mac，然后判断字符串中是否有路由器2G的mac地址
        wlan1_list = guestwifi_set.Wifi_scan.wlan1_ssid_scan(wlan_ssid)
        print (wlan1_list)
        if wlan0_list != 0 and wlan1_list != 0:
            if wlan0_list.find("%s" % mac_5g) != -1 and wlan1_list.find("%s" % mac_2g) != -1:
                result = 1
            else:
                result = 0
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-3510 :“双频合一”开启状态，2T2R设备能成功连接2.4G SSID，协商速率300M
    def test_wifi_2():
        wlan_ssid = guestwifi_set_conf.ssid_2g
        wlan_password = guestwifi_set_conf.wlan_password
        # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
        con_status = guestwifi_set.Wifi_con.wifi_2g_wpa2_aes_connect(wlan_ssid, wlan_password)
        print(con_status)
        print("###############")
        if con_status == 1:
            linkrate = guestwifi_set.Linkrate_check.wifi_2g_linkrate()
            print("xxxxxxxxxxxxxx")
            print(linkrate)
            if linkrate == "300":
                result = 1
            else:
                result = 0
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-3509 :“双频合一”开启状态，2T2R设备能成功连接5G SSID,协商速率正确867M
    def test_wifi_3():
        wlan_ssid = guestwifi_set_conf.ssid_2g
        wlan_password = guestwifi_set_conf.wlan_password
        # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
        con_status = guestwifi_set.Wifi_con.wifi_5g_wpa2_aes_connect(wlan_ssid, wlan_password)
        if con_status == 1:
            linkrate = guestwifi_set.Linkrate_check.wifi_5g_linkrate()
            print("xxxxxxxxxxxxxx")
            print(linkrate)
            if linkrate == '867' or linkrate == '866.7':
                result = 1
            else:
                result = 0
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-2734 :“双频合一”关闭状态，扫描到的SSID中，2.4G SSID为XXXX,5G SSID为XXXX-5G
    def test_wifi_4():
        time.sleep(30)
        wlan1_ssid = guestwifi_set_conf.ssid_2g
        wlan0_ssid = guestwifi_set_conf.ssid_5g
        mac_5g = guestwifi_set_conf.mac_5g
        mac_2g = guestwifi_set_conf.mac_2g
        # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
        wlan0_list = guestwifi_set.Wifi_scan.wlan0_ssid_scan(wlan0_ssid)
        print (wlan0_list)
        # 通过2G ssid筛选出对应的mac，然后判断字符串中是否有路由器2G的mac地址
        wlan1_list = guestwifi_set.Wifi_scan.wlan1_ssid_scan(wlan1_ssid)
        print (wlan1_list)
        if wlan0_list != 0 and wlan1_list != 0:
            if wlan0_list.find("%s" % mac_5g) != -1 and wlan1_list.find("%s" % mac_2g) != -1 and wlan0_list.find("%s" % mac_2g) == -1 and wlan1_list.find("%s" % mac_5g) == -1:
                print ("搜索到对应ssid")
                result = 1
            else:
                print ("没有搜索到对应ssid")
                result = 0
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-3075 :“双频合一”关闭状态，2T2R设备能成功连接2.4G，协商速率300M
    def test_wifi_5():
        wlan_ssid = guestwifi_set_conf.ssid_2g
        wlan_password = guestwifi_set_conf.wlan_password
        # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
        con_status = guestwifi_set.Wifi_con.wifi_2g_wpa2_aes_connect(wlan_ssid, wlan_password)
        if con_status == 1:
            linkrate = guestwifi_set.Linkrate_check.wifi_2g_linkrate()
            print("xxxxxxxxxxxxxx")
            print(linkrate)

            if linkrate == '300':
                result = 1
            else:
                result = 0
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-3076 :“双频合一”开启状态，2T2R设备能成功连接5G，协商速率867M
    def test_wifi_6():
        wlan_ssid = guestwifi_set_conf.ssid_5g
        wlan_password = guestwifi_set_conf.wlan_password
        # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
        con_status = guestwifi_set.Wifi_con.wifi_5g_wpa2_aes_connect(wlan_ssid, wlan_password)
        if con_status == 1:
            linkrate = guestwifi_set.Linkrate_check.wifi_5g_linkrate()
            print("xxxxxxxxxxxxxx")
            print(linkrate)
            if linkrate == '867' or linkrate == '866.7':
                result = 1
            else:
                result = 0
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-3378 :隐藏SSID关闭状态，5G设备可以扫描到5G SSID，并可以正常连接
    def test_wifi_7():
        wlan_ssid = guestwifi_set_conf.ssid_5g
        mac_5g = guestwifi_set_conf.mac_5g
        wlan_password = guestwifi_set_conf.wlan_password
        # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
        wlan0_list = guestwifi_set.Wifi_scan.wlan0_ssid_scan(wlan_ssid)
        print (wlan0_list)
        if wlan0_list != 0:
            if wlan0_list.find("%s" % mac_5g) != -1:
                # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
                con_status = guestwifi_set.Wifi_con.wifi_5g_wpa2_aes_connect(wlan_ssid, wlan_password)
                if con_status == 1:
                    result = 1
                else:
                    result = 0
            else:
                result = 0
        else:
            result = 0
        #result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-4973 :隐藏SSID关闭状态，2.4G设备可以扫描到2.4G SSID，并可以正常连接
    def test_wifi_8():
        wlan_ssid = guestwifi_set_conf.ssid_2g
        mac_2g = guestwifi_set_conf.mac_2g
        wlan_password = guestwifi_set_conf.wlan_password
        # 通过2G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
        wlan1_list = guestwifi_set.Wifi_scan.wlan1_ssid_scan(wlan_ssid)
        print (wlan1_list)
        if wlan1_list != 0:
            if wlan1_list.find("%s" % mac_2g) != -1:
                # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
                con_status = guestwifi_set.Wifi_con.wifi_2g_wpa2_aes_connect(wlan_ssid, wlan_password)
                if con_status == 1:
                    result = 1
                else:
                    result = 0
            else:
                result = 0
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-3377 :隐藏SSID开启状态，5G设备无法扫描到5G SSID
    def test_wifi_9():
        wlan_ssid = guestwifi_set_conf.ssid_5g
        mac_5g = guestwifi_set_conf.mac_5g
        # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
        wlan0_list = guestwifi_set.Wifi_scan.wlan0_ssid_scan(wlan_ssid)
        print (wlan0_list)
        if wlan0_list != 0:
            if wlan0_list.find("%s" % mac_5g) != -1:
                result = 0
            else:
                result = 1
        else:
            result = 1
        #result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-4971 :隐藏SSID开启状态，2.4G设备无法扫描到2.4G SSID
    def test_wifi_10():
        wlan_ssid = guestwifi_set_conf.ssid_2g
        mac_2g = guestwifi_set_conf.mac_2g
        # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
        wlan1_list = guestwifi_set.Wifi_scan.wlan1_ssid_scan(wlan_ssid)
        print (wlan1_list)
        if wlan1_list != 0:
            if wlan1_list.find("%s" % mac_2g) != -1:
                result = 0
            else:
                result = 1
        else:
            result = 1
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-1513 :隐藏SSID开启，5G设备可通过手动添加SSID和密码连接到路由器
    def test_wifi_11():
        wlan_ssid = guestwifi_set_conf.ssid_5g
        mac_5g = guestwifi_set_conf.mac_5g
        wlan_password = guestwifi_set_conf.wlan_password
        # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
        wlan0_list = guestwifi_set.Wifi_scan.wlan0_ssid_scan(wlan_ssid)
        print (wlan0_list)
        if wlan0_list != 0:
            if wlan0_list.find("%s" % mac_5g) == -1:
                # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
                con_status = guestwifi_set.Wifi_con.wifi_5g_wpa2_aes_auto_connect(wlan_ssid, wlan_password)
                if con_status == 1:
                    result = 1
                else:
                    result = 0
            else:
                con_status = guestwifi_set.Wifi_con.wifi_5g_wpa2_aes_auto_connect(wlan_ssid, wlan_password)
                if con_status == 1:
                    result = 1
                else:
                    result = 0
        else:
            con_status = guestwifi_set.Wifi_con.wifi_5g_wpa2_aes_auto_connect(wlan_ssid, wlan_password)
            if con_status == 1:
                result = 1
            else:
                result = 0
        #result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-4970 :隐藏SSID开启，2.4G设备可通过手动添加SSID和密码连接到路由器
    def test_wifi_12():
        wlan_ssid = guestwifi_set_conf.ssid_2g
        mac_2g = guestwifi_set_conf.mac_2g
        wlan_password = guestwifi_set_conf.wlan_password
        # 通过2.4G ssid筛选出对应的mac，然后判断字符串中是否有路由器2.4G的mac地址
        wlan1_list = guestwifi_set.Wifi_scan.wlan1_ssid_scan(wlan_ssid)
        print (wlan1_list)
        if wlan1_list != 0:
            if wlan1_list.find("%s" % mac_2g) == -1:
                # 通过2.4G ssid筛选出对应的mac，然后判断字符串中是否有路由器2.4G的mac地址
                con_status = guestwifi_set.Wifi_con.wifi_2g_wpa2_aes_auto_connect(wlan_ssid, wlan_password)
                if con_status == 1:
                    result = 1
                else:
                    result = 0
            else:
                con_status = guestwifi_set.Wifi_con.wifi_2g_wpa2_aes_auto_connect(wlan_ssid, wlan_password)
                if con_status == 1:
                    result = 1
                else:
                    result = 0
        else:
            con_status = guestwifi_set.Wifi_con.wifi_2g_wpa2_aes_auto_connect(wlan_ssid, wlan_password)
            if con_status == 1:
                result = 1
            else:
                result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-4974 :隐藏SSID关闭，5G设备可通过手动添加SSID和密码连接到路由器
    def test_wifi_13():
        wlan_ssid = guestwifi_set_conf.ssid_5g
        mac_5g = guestwifi_set_conf.mac_5g
        wlan_password = guestwifi_set_conf.wlan_password
        # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
        wlan0_list = guestwifi_set.Wifi_scan.wlan0_ssid_scan(wlan_ssid)
        print (wlan0_list)
        if wlan0_list != 0:
            if wlan0_list.find("%s" % mac_5g) != -1:
                # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
                con_status = guestwifi_set.Wifi_con.wifi_5g_wpa2_aes_connect(wlan_ssid, wlan_password)
                if con_status == 1:
                    result = 1
                else:
                    result = 0
            else:
                result = 0
        else:
            result = 0
        #result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-4975 :隐藏SSID关闭，2.4G设备可通过手动添加SSID和密码连接到路由器
    def test_wifi_14():
        wlan_ssid = guestwifi_set_conf.ssid_2g
        mac_2g = guestwifi_set_conf.mac_2g
        wlan_password = guestwifi_set_conf.wlan_password
        # 通过2.4G ssid筛选出对应的mac，然后判断字符串中是否有路由器2.4G的mac地址
        wlan1_list = guestwifi_set.Wifi_scan.wlan1_ssid_scan(wlan_ssid)
        print (wlan1_list)
        if wlan1_list != 0:
            if wlan1_list.find("%s" % mac_2g) != -1:
                # 通过2.4G ssid筛选出对应的mac，然后判断字符串中是否有路由器2.4G的mac地址
                con_status = guestwifi_set.Wifi_con.wifi_2g_wpa2_aes_connect(wlan_ssid, wlan_password)
                if con_status == 1:
                    result = 1
                else:
                    result = 0
            else:
                result = 0
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-4967 :SSID为20个字节，密码为24个字节，5G设备能成功连接
    def test_wifi_15():
        wlan_ssid = guestwifi_set_conf.ssid_2g_20b
        mac_5g = guestwifi_set_conf.mac_5g
        wlan_password = guestwifi_set_conf.wlan_password_24b
        # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
        wlan0_list = guestwifi_set.Wifi_scan.wlan0_ssid_scan(wlan_ssid)
        print (wlan0_list)
        if wlan0_list != 0:
            if wlan0_list.find("%s" % mac_5g) != -1:
                # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
                con_status = guestwifi_set.Wifi_con.wifi_5g_wpa2_aes_connect(wlan_ssid, wlan_password)
                if con_status == 1:
                    result = 1
                else:
                    result = 0
            else:
                result = 0
        else:
            result = 0
        #result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-4969 :SSID为20个字节，密码为24个字节，2.4G设备能成功连接
    def test_wifi_16():
        wlan_ssid = guestwifi_set_conf.ssid_2g_20b
        mac_2g = guestwifi_set_conf.mac_2g
        wlan_password = guestwifi_set_conf.wlan_password_24b
        # 通过2.4G ssid筛选出对应的mac，然后判断字符串中是否有路由器2.4G的mac地址
        wlan1_list = guestwifi_set.Wifi_scan.wlan1_ssid_scan(wlan_ssid)
        print (wlan1_list)
        if wlan1_list != 0:
            if wlan1_list.find("%s" % mac_2g) != -1:
                # 通过2.4G ssid筛选出对应的mac，然后判断字符串中是否有路由器2.4G的mac地址
                con_status = guestwifi_set.Wifi_con.wifi_2g_wpa2_aes_connect(wlan_ssid, wlan_password)
                if con_status == 1:
                    result = 1
                else:
                    result = 0
            else:
                result = 0
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-4999 :SSID为1个字节，密码为8个字节，5G设备能成功连接
    def test_wifi_17():
        wlan_ssid = guestwifi_set_conf.ssid_2g_1b
        mac_5g = guestwifi_set_conf.mac_5g
        wlan_password = guestwifi_set_conf.wlan_password_8b
        # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
        wlan0_list = guestwifi_set.Wifi_scan.wlan0_ssid_scan(wlan_ssid)
        print (wlan0_list)
        if wlan0_list != 0:
            if wlan0_list.find("%s" % mac_5g) != -1:
                # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
                con_status = guestwifi_set.Wifi_con.wifi_5g_wpa2_aes_connect(wlan_ssid, wlan_password)
                if con_status == 1:
                    result = 1
                else:
                    result = 0
            else:
                result = 0
        else:
            result = 0
        #result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    #  用例-5000 :SSID为1个字节，密码为8个字节，2.4G设备能成功连接
    def test_wifi_18():
        wlan_ssid = guestwifi_set_conf.ssid_2g_1b
        mac_2g = guestwifi_set_conf.mac_2g
        wlan_password = guestwifi_set_conf.wlan_password_8b
        # 通过2.4G ssid筛选出对应的mac，然后判断字符串中是否有路由器2.4G的mac地址
        wlan1_list = guestwifi_set.Wifi_scan.wlan1_ssid_scan(wlan_ssid)
        print (wlan1_list)
        if wlan1_list != 0:
            if wlan1_list.find("%s" % mac_2g) != -1:
                # 通过2.4G ssid筛选出对应的mac，然后判断字符串中是否有路由器2.4G的mac地址
                con_status = guestwifi_set.Wifi_con.wifi_2g_wpa2_aes_connect(wlan_ssid, wlan_password)
                if con_status == 1:
                    result = 1
                else:
                    result = 0
            else:
                result = 0
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result


    @staticmethod
    # 用例-5017 :: 版本: 1 :: 修改SSID后，新SSID生效，旧SSID失效
    def test_wifi_19():
        wlan_ssid = guestwifi_set_conf.ssid_2g
        mac_5g = guestwifi_set_conf.mac_5g
        wlan_password = guestwifi_set_conf.wlan_password
        wlan_ssid_change = guestwifi_set_conf.ssid_2g_change
        mac_2g = guestwifi_set_conf.mac_2g
        # wlan_password_change = wifi_set_conf.wlan_password_change
        # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
        wlan0_list = guestwifi_set.Wifi_scan.wlan0_ssid_scan(wlan_ssid)
        wlan1_list = guestwifi_set.Wifi_scan.wlan1_ssid_scan(wlan_ssid)
        print ("-1-1-1-1-1-1--1-1-1-1")
        print (wlan0_list)
        print (wlan1_list)
        if wlan0_list == 0 and wlan1_list == 0:
            print ("00000000000000")
            wlan0_change_list = guestwifi_set.Wifi_scan.wlan0_ssid_scan(wlan_ssid_change)
            wlan1_change_list = guestwifi_set.Wifi_scan.wlan1_ssid_scan(wlan_ssid_change)

            # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
            if wlan0_change_list != 0 and wlan1_change_list != 0:
                print ("1111111111111111111")
                if wlan0_change_list.find("%s" % mac_5g) != -1 and wlan1_change_list.find("%s" % mac_2g) != -1:
                    print ("22222222222222")
                    con_status_5g = guestwifi_set.Wifi_con.wifi_5g_wpa2_aes_auto_connect(wlan_ssid, wlan_password)
                    con_status_2g = guestwifi_set.Wifi_con.wifi_2g_wpa2_aes_auto_connect(wlan_ssid, wlan_password)
                    con_status_5g_change = guestwifi_set.Wifi_con.wifi_5g_wpa2_aes_connect(wlan_ssid_change, wlan_password)
                    con_status_2g_change = guestwifi_set.Wifi_con.wifi_2g_wpa2_aes_connect(wlan_ssid_change, wlan_password)
                    print ("连接状态：%s，%s，%s，%s" %(con_status_5g,con_status_2g,con_status_5g_change,con_status_2g_change))
                    if con_status_5g == 0 and con_status_2g == 0 and con_status_5g_change == 1 and con_status_2g_change == 1:
                        print ("333333333333333333")
                        result = 1
                    else:
                        result = 0
                else:
                    result = 0
            else:
                result = 0
        else:
            result = 0
        #result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-5018 :: 版本: 1 :: 修改密码后，新密码生效，旧密码失效
    def test_wifi_20():
        wlan_ssid = guestwifi_set_conf.ssid_2g
        mac_5g = guestwifi_set_conf.mac_5g
        wlan_password = guestwifi_set_conf.wlan_password
        wlan_ssid_change = guestwifi_set_conf.ssid_2g_change
        mac_2g = guestwifi_set_conf.mac_2g
        wlan_password_change = guestwifi_set_conf.wlan_password_change
        # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
        wlan0_list = guestwifi_set.Wifi_scan.wlan0_ssid_scan(wlan_ssid)
        wlan1_list = guestwifi_set.Wifi_scan.wlan1_ssid_scan(wlan_ssid)
        print ("-1-1-1-1-1-1-1-1-1-1-1-1--1")
        print (wlan0_list)
        print ("000000000000")
        print (wlan1_list)
        print ("11111111111")
        if wlan0_list != 0 and wlan1_list != 0:
            print ("22222222222")
            if wlan0_list.find("%s" % mac_5g) != -1 and wlan1_list.find("%s" % mac_2g) != -1:
                print ("333333333333")
                con_status_5g = guestwifi_set.Wifi_con.wifi_5g_wpa2_aes_auto_connect(wlan_ssid, wlan_password)
                con_status_2g = guestwifi_set.Wifi_con.wifi_2g_wpa2_aes_auto_connect(wlan_ssid, wlan_password)
                con_status_5g_change = guestwifi_set.Wifi_con.wifi_5g_wpa2_aes_connect(wlan_ssid, wlan_password_change)
                con_status_2g_change = guestwifi_set.Wifi_con.wifi_2g_wpa2_aes_connect(wlan_ssid, wlan_password_change)
                print("连接状态：%s，%s，%s，%s" % (con_status_5g, con_status_2g, con_status_5g_change, con_status_2g_change))
                if con_status_5g == 0 and con_status_2g == 0 and con_status_5g_change == 1 and con_status_2g_change == 1:
                    result = 1
                else:
                    result = 0
            else:
                result = 0
        else:
            result = 0
        #result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-5684 :加密方式为open，5G和2.4G设备可以不需要密码连接到WIFI
    def test_wifi_21():
        wlan_ssid = guestwifi_set_conf.ssid_2g
        con_status_5g = guestwifi_set.Wifi_con.wifi_5g_open_connect(wlan_ssid)
        con_status_2g = guestwifi_set.Wifi_con.wifi_2g_open_connect(wlan_ssid)
        if con_status_5g == 1 and con_status_2g == 1:
            result = 1
        else:
            result = 0
        #result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    #  用例-5685 :加密方式为WPA，5G和2.4G设备可以通过WPA认证方式连接到WIFI
    def test_wifi_22():
        wlan_ssid = guestwifi_set_conf.ssid_2g
        wlan_password = guestwifi_set_conf.wlan_password
        con_status_2g_aes = guestwifi_set.Wifi_con.wifi_2g_wpa_aes_connect(wlan_ssid, wlan_password)
        con_status_2g_tkip = guestwifi_set.Wifi_con.wifi_2g_wpa_tkip_connect(wlan_ssid, wlan_password)
        con_status_5g_aes = guestwifi_set.Wifi_con.wifi_5g_wpa_aes_connect(wlan_ssid, wlan_password)
        con_status_5g_tkip = guestwifi_set.Wifi_con.wifi_5g_wpa_tkip_connect(wlan_ssid, wlan_password)
        if con_status_2g_aes == 1 and con_status_2g_tkip == 1 and con_status_5g_aes == 1  and con_status_5g_tkip == 1:
            result = 1
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-5686 :加密方式为WPA，5G和2.4G设备不可以通过WPA2认证方式连接到WIFI
    def test_wifi_23():
        wlan_ssid = guestwifi_set_conf.ssid_2g
        wlan_password = guestwifi_set_conf.wlan_password
        con_status_2g_aes = guestwifi_set.Wifi_con.wifi_2g_wpa2_aes_connect(wlan_ssid, wlan_password)
        con_status_5g_aes = guestwifi_set.Wifi_con.wifi_5g_wpa2_aes_connect(wlan_ssid, wlan_password)
        if con_status_2g_aes == 0 and con_status_5g_aes == 0:
            result = 1
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result


    @staticmethod
    #  用例-5687 :: 版本: 1 :: 加密方式为WPA2，5G和2.4G设备可以通过WPA2认证方式连接到WIFI
    def test_wifi_24():
        wlan_ssid = guestwifi_set_conf.ssid_2g
        wlan_password = guestwifi_set_conf.wlan_password
        con_status_2g_aes = guestwifi_set.Wifi_con.wifi_2g_wpa2_aes_connect(wlan_ssid, wlan_password)
        con_status_5g_aes = guestwifi_set.Wifi_con.wifi_5g_wpa2_aes_connect(wlan_ssid, wlan_password)
        if con_status_2g_aes == 1 and con_status_5g_aes == 1:
            result = 1
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-5688 :: 版本: 1 :: 加密方式为WPA2，5G和2.4G设备不可以通过WPA认证方式连接到WIFI
    def test_wifi_25():
        wlan_ssid = guestwifi_set_conf.ssid_2g
        wlan_password = guestwifi_set_conf.wlan_password
        con_status_2g_aes = guestwifi_set.Wifi_con.wifi_2g_wpa_aes_connect(wlan_ssid, wlan_password)
        con_status_2g_tkip = guestwifi_set.Wifi_con.wifi_2g_wpa_tkip_connect(wlan_ssid, wlan_password)
        con_status_5g_aes = guestwifi_set.Wifi_con.wifi_5g_wpa_aes_connect(wlan_ssid, wlan_password)
        con_status_5g_tkip = guestwifi_set.Wifi_con.wifi_5g_wpa_tkip_connect(wlan_ssid, wlan_password)
        if con_status_2g_aes == 0 and con_status_2g_tkip == 0 and con_status_5g_aes == 0  and con_status_5g_tkip == 0:
            result = 1
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-5689 :: 版本: 1 :: 加密方式为WPA/WPA2-PSK，5G和2.4G设备可以通过WPA认证方式连接到该WIFI
    def test_wifi_26():
        wlan_ssid = guestwifi_set_conf.ssid_2g
        wlan_password = guestwifi_set_conf.wlan_password
        con_status_2g_aes = guestwifi_set.Wifi_con.wifi_2g_wpa_aes_connect(wlan_ssid, wlan_password)
        con_status_2g_tkip = guestwifi_set.Wifi_con.wifi_2g_wpa_tkip_connect(wlan_ssid, wlan_password)
        con_status_5g_aes = guestwifi_set.Wifi_con.wifi_5g_wpa_aes_connect(wlan_ssid, wlan_password)
        con_status_5g_tkip = guestwifi_set.Wifi_con.wifi_5g_wpa_tkip_connect(wlan_ssid, wlan_password)
        if con_status_2g_aes == 1 and con_status_2g_tkip == 1 and con_status_5g_aes == 1 and con_status_5g_tkip == 1:
            result = 1
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-5690 :: 版本: 1 :: 加密方式为WPA/WPA2-PSK，5G和2.4G设备可以通过WPA2认证方式连接到该WIFI
    def test_wifi_27():
        wlan_ssid = guestwifi_set_conf.ssid_2g
        wlan_password = guestwifi_set_conf.wlan_password
        con_status_2g_aes = guestwifi_set.Wifi_con.wifi_2g_wpa2_aes_connect(wlan_ssid, wlan_password)
        con_status_5g_aes = guestwifi_set.Wifi_con.wifi_5g_wpa2_aes_connect(wlan_ssid, wlan_password)
        if con_status_2g_aes == 1 and con_status_5g_aes == 1:
            result = 1
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

