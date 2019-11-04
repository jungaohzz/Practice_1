from ..common_dir import common_fun, common_conf
import os

class Test_wifi_device_black():

    @staticmethod
    # 设备黑名单测试前置条件
    def test_wifi_device_black_init():
        interfacewired_1 = common_conf.interfacewired_1
        interface5g_1 = common_conf.interface5g_1
        interface2g_1 = common_conf.interface2g_1
        wlan_ssid = common_conf.ssid_2g
        wlan_password = common_conf.wlan_password
        os.system('netsh interface set interface "%s" enabled' % interface5g_1)
        os.system('netsh interface set interface "%s" enabled' % interface2g_1)
        wired1 = common_fun.Conf_networkcard.ipwired1_configure(interfacewired_1)
        wlan5g1 = common_fun.Conf_networkcard.ip5g1_configure(interface5g_1)
        wlan2g1 = common_fun.Conf_networkcard.ip2g1_configure(interface2g_1)
        os.system('netsh wlan delete profile *')
        wlan5g_con = common_fun.Wifi_con.wifi_5g_wpa2_aes_auto_connect_undelete(wlan_ssid, wlan_password)
        wlan2g_con = common_fun.Wifi_con.wifi_2g_wpa2_aes_auto_connect_undelete(wlan_ssid, wlan_password)
        print("%s,%s,%s,%s,%s"% (wired1, wlan5g1, wlan2g1, wlan5g_con, wlan2g_con))
        if wired1 == 1 and wlan5g1 == 1 and wlan2g1 == 1 and wlan5g_con == 1 and wlan2g_con == 1:
            result = 1
        else:
            result = 0
        return result

    @staticmethod
    # 用例-7724 : 拉黑一个主WiFi下的5G设备，该设备会被立即踢下线，其他2G设备不会被提下线
    def test_device_black_1():
        con_5g_status = common_fun.Wifi_con.wlan_5g_con_status()
        con_2g_status = common_fun.Wifi_con.wlan_2g_con_status()
        if con_5g_status == 0 and con_2g_status == 1:
            result = 1
        else:
            result = 0
        return result

    # @staticmethod
    # #  用例-7725 : 拉黑一个主WiFi下的5G设备，该设备会被立即踢下线，其他5G设备不会被提下线
    # def test_device_black_2():
    #     con_5g_status = common_fun.Wifi_con.wlan_5g_con_status()
    #     con_2g_status = common_fun.Wifi_con.wlan_2g_con_status()
    #     if con_5g_status == 1 and con_2g_status == 1:
    #         result = 1
    #     else:
    #         result = 0
    #     return result

    @staticmethod
    # 用例-7726 : 拉黑一个主WiFi下的2G设备，该设备会被立即踢下线，其他5G设备不会被提下线
    def test_device_black_3():
        con_5g_status = common_fun.Wifi_con.wlan_5g_con_status()
        con_2g_status = common_fun.Wifi_con.wlan_2g_con_status()
        if con_5g_status == 1 and con_2g_status == 0:
            result = 1
        else:
            result = 0
        return result

    # @staticmethod
    # # 用例-7727 :: 版本: 1 :: 拉黑一个主WiFi下的2G设备，该设备会被立即踢下线，其他2G设备不会被提下线
    # def test_device_black_4():
    #     con_5g_status = common_fun.Wifi_con.wlan_5g_con_status()
    #     con_2g_status = common_fun.Wifi_con.wlan_2g_con_status()
    #     if con_5g_status == 1 and con_2g_status == 1:
    #         result = 1
    #     else:
    #         result = 0
    #     return result

    @staticmethod
    # 用例-7732 : 黑名单中的设备无法连接主WIFI 5G ssid
    def test_device_black_5():
        wlan_ssid = common_conf.ssid_2g
        wlan_password = common_conf.wlan_password
        con_status = common_fun.Wifi_con.wifi_5g_wpa2_aes_connect(wlan_ssid, wlan_password)
        if con_status == 0:
            result = 1
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-7733 : 黑名单中的设备无法连接主WIFI 2G ssid
    def test_device_black_6():
        wlan_ssid = common_conf.ssid_2g
        wlan_password = common_conf.wlan_password
        con_status = common_fun.Wifi_con.wifi_2g_wpa2_aes_connect(wlan_ssid, wlan_password)
        if con_status == 0:
            result = 1
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-7734 : 黑名单中的设备无法连接主guest WIFI 5G ssid
    def test_device_black_7():
        wlan_ssid = common_conf.guest_ssid_2g
        wlan_password = common_conf.guest_wlan_password
        con_status = common_fun.Wifi_con.wifi_5g_wpa2_aes_connect(wlan_ssid, wlan_password)
        if con_status == 0:
            result = 1
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-7735 : 黑名单中的设备无法连接主guest WIFI 2G ssid
    def test_device_black_8():
        wlan_ssid = common_conf.guest_ssid_2g
        wlan_password = common_conf.guest_wlan_password
        con_status = common_fun.Wifi_con.wifi_2g_wpa2_aes_connect(wlan_ssid, wlan_password)
        if con_status == 0:
            result = 1
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-7737 : 拉黑一个有线设备，该设备无法访问外网
    def test_device_black_9():
        internet_status = common_fun.Internet_check.internetwired_connect()
        url_test_status = common_fun.Url_check.internetwired_connect("www.baidu.com")
        print(internet_status)
        print(url_test_status)
        if internet_status == 0 and url_test_status == 0:
            print("测试成功")
            result = 1
        else:
            print("测试失败")
            result = 0
        return result

    @staticmethod
    # 用例-7738 : 删除黑名单中设备后，该设备可以连接主WIFI 5G ssid
    def test_device_black_10():
        wlan_ssid = common_conf.ssid_2g
        wlan_password = common_conf.wlan_password
        con_status = common_fun.Wifi_con.wifi_5g_wpa2_aes_connect(wlan_ssid, wlan_password)
        if con_status == 1:
            result = 1
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-7739 : 删除黑名单中设备后，该设备可以连接主WIFI 2G ssid
    def test_device_black_11():
        wlan_ssid = common_conf.ssid_2g
        wlan_password = common_conf.wlan_password
        con_status = common_fun.Wifi_con.wifi_2g_wpa2_aes_connect(wlan_ssid, wlan_password)
        if con_status == 1:
            result = 1
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-7740 : 删除黑名单中设备后，该设备可以连接访客WIFI 5G ssid
    def test_device_black_12():
        wlan_ssid = common_conf.guest_ssid_2g
        wlan_password = common_conf.guest_wlan_password
        con_status = common_fun.Wifi_con.wifi_5g_wpa2_aes_connect(wlan_ssid, wlan_password)
        if con_status == 1:
            result = 1
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-7741 : 删除黑名单中设备后，该设备可以连接访客WiFi 2G ssid
    def test_device_black_13():
        wlan_ssid = common_conf.guest_ssid_2g
        wlan_password = common_conf.guest_wlan_password
        con_status = common_fun.Wifi_con.wifi_2g_wpa2_aes_connect(wlan_ssid, wlan_password)
        if con_status == 1:
            result = 1
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-7742 :: 版本: 1 :: 删除黑名单中有线设备后，该设备可以访问外网
    def test_device_black_14():
        internet_status = common_fun.Internet_check.internetwired_connect()
        url_test_status = common_fun.Url_check.internetwired_connect("www.baidu.com")
        print (internet_status)
        print (url_test_status)
        if internet_status == 0 and url_test_status == 0:
            print("测试成功")
            result = 1
        else:
            print("测试失败")
            result = 0
        return result

class Test_guestwifi_device_black():

    @staticmethod
    # 网址黑名单测试前置条件
    def test_guestwifi_device_black_init():
        interfacewired_1 = common_conf.interfacewired_1
        interface5g_1 = common_conf.interface5g_1
        interface2g_1 = common_conf.interface2g_1
        wlan_ssid = common_conf.guest_ssid_2g
        wlan_password = common_conf.guest_wlan_password
        os.system('netsh interface set interface "%s" enabled' % interface5g_1)
        os.system('netsh interface set interface "%s" enabled' % interface2g_1)
        wired1 = common_fun.Conf_networkcard.ipwired1_configure(interfacewired_1)
        wlan5g1 = common_fun.Conf_networkcard.ip5g1_configure(interface5g_1)
        wlan2g1 = common_fun.Conf_networkcard.ip2g1_configure(interface2g_1)
        os.system('netsh wlan delete profile *')
        wlan5g_con = common_fun.Wifi_con.wifi_5g_wpa2_aes_auto_connect_undelete(wlan_ssid, wlan_password)
        wlan2g_con = common_fun.Wifi_con.wifi_2g_wpa2_aes_auto_connect_undelete(wlan_ssid, wlan_password)
        print("%s,%s,%s,%s,%s"% (wired1, wlan5g1, wlan2g1, wlan5g_con, wlan2g_con))
        if wired1 == 1 and wlan5g1 == 1 and wlan2g1 == 1 and wlan5g_con == 1 and wlan2g_con == 1:
            result = 1
        else:
            result = 0
        return result

    @staticmethod
    #  用例-7728 : 拉黑一个访客WiFi下的5G设备，该设备会被立即踢下线，其他2G设备不会被提下线
    def test_device_black_15():
        con_5g_status = common_fun.Wifi_con.wlan_5g_con_status()
        con_2g_status = common_fun.Wifi_con.wlan_2g_con_status()
        if con_5g_status == 0 and con_2g_status == 1:
            result = 1
        else:
            result = 0
        return result

    # @staticmethod
    # # 用例-7729 :: 版本: 1 :: 拉黑一个访客WiFi下的5G设备，该设备会被立即踢下线，其他5G设备不会被提下线
    # def test_device_black_16():
    #     con_5g_status = common_fun.Wifi_con.wlan_5g_con_status()
    #     con_2g_status = common_fun.Wifi_con.wlan_2g_con_status()
    #     if con_5g_status == 1 and con_2g_status == 1:
    #         result = 1
    #     else:
    #         result = 0
    #     return result

    @staticmethod
    # 用例-7730 : 拉黑一个访客WiFi下的2G设备，该设备会被立即踢下线，其他5G设备不会被提下线
    def test_device_black_17():
        con_5g_status = common_fun.Wifi_con.wlan_5g_con_status()
        con_2g_status = common_fun.Wifi_con.wlan_2g_con_status()
        if con_5g_status == 1 and con_2g_status == 0:
            result = 1
        else:
            result = 0
        return result

    # @staticmethod
    # # 用例-7731 :: 版本: 1 :: 拉黑一个访客WiFi下的2G设备，该设备会被立即踢下线，其他2G设备不会被提下线
    # def test_device_black_18():
    #     con_5g_status = common_fun.Wifi_con.wlan_5g_con_status()
    #     con_2g_status = common_fun.Wifi_con.wlan_2g_con_status()
    #     if con_5g_status == 1 and con_2g_status == 1:
    #         result = 1
    #     else:
    #         result = 0
    #     return result