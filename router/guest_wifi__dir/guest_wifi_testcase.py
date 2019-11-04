import time
from ..common_dir import common_fun, common_conf


class Test_guest_wifi():

    @staticmethod
    # 配置WiFi set相关前置条件
    def test_guest_wifi_init():
        interfacewired_1 = common_conf.interfacewired_1
        interface5g_1 = common_conf.interface5g_1
        interface2g_1 = common_conf.interface2g_1
        wired1 = common_fun.Conf_networkcard.ipwired1_configure(interfacewired_1)
        wlan5g1 = common_fun.Conf_networkcard.ip5g1_configure(interface5g_1)
        wlan2g1 = common_fun.Conf_networkcard.ip2g1_configure(interface2g_1)
        if wired1 == 1 and wlan5g1 == 1 and wlan2g1 == 1:
            result = 1
        else:
            result = 0
        return result

    @staticmethod
    # 用例-4371 : 开启访客网络后，访客网络生效，5G和2.4G都能连接到访客网络
    def test_guest_wifi_1():
        wlan_ssid = common_conf.guest_ssid_2g
        guest_wlan_password = common_conf.guest_wlan_password
        # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
        con_status_2g = common_fun.Wifi_con.wifi_2g_wpa2_aes_connect(wlan_ssid, guest_wlan_password)
        con_status_5g = common_fun.Wifi_con.wifi_5g_wpa2_aes_connect(wlan_ssid, guest_wlan_password)
        if con_status_2g == 1 and con_status_5g == 1:
            result = 1
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-5003 : “双频合一”开启状态，扫描到的SSID中，5G和2.4G SSID一样
    def test_guest_wifi_2():
        #time.sleep(30)
        wlan_ssid = common_conf.guest_ssid_2g
        guest_mac_5g = common_conf.guest_mac_5g
        guest_mac_2g = common_conf.guest_mac_2g
        # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
        wlan0_list = common_fun.Wifi_scan.wlan0_ssid_scan(wlan_ssid)
        print(wlan0_list)
        # 通过2G ssid筛选出对应的mac，然后判断字符串中是否有路由器2G的mac地址
        wlan1_list = common_fun.Wifi_scan.wlan1_ssid_scan(wlan_ssid)
        print(wlan1_list)
        if wlan0_list != 0 and wlan1_list != 0:
            if wlan0_list.find("%s" % guest_mac_5g) != -1 and wlan1_list.find("%s" % guest_mac_2g) != -1:
                result = 1
            else:
                result = 0
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-5004 : “双频合一”开启状态，2T2R设备能成功连接2.4G SSID，协商速率300M
    def test_guest_wifi_3():
        wlan_ssid = common_conf.guest_ssid_2g
        guest_wlan_password = common_conf.guest_wlan_password
        # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
        con_status = common_fun.Wifi_con.wifi_2g_wpa2_aes_connect(wlan_ssid, guest_wlan_password)
        print(con_status)
        print("###############")
        if con_status == 1:
            linkrate = common_fun.Linkrate_check.wifi_2g_linkrate()
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
    # 用例-5005 : “双频合一”开启状态，2T2R设备能成功连接5G SSID,协商速率正确867M
    def test_guest_wifi_4():
        wlan_ssid = common_conf.guest_ssid_2g
        guest_wlan_password = common_conf.guest_wlan_password
        # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
        con_status = common_fun.Wifi_con.wifi_5g_wpa2_aes_connect(wlan_ssid, guest_wlan_password)
        if con_status == 1:
            linkrate = common_fun.Linkrate_check.wifi_5g_linkrate()
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
    # 用例-5006 : “双频合一”关闭状态，扫描到的SSID中，2.4G SSID为XXXX,5G SSID为XXXX-5G
    def test_guest_wifi_5():
        #time.sleep(30)
        wlan1_ssid = common_conf.guest_ssid_2g
        wlan0_ssid = common_conf.guest_ssid_5g
        guest_mac_5g = common_conf.guest_mac_5g
        guest_mac_2g = common_conf.guest_mac_2g
        # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
        wlan0_list = common_fun.Wifi_scan.wlan0_ssid_scan(wlan0_ssid)
        print(wlan0_list)
        # 通过2G ssid筛选出对应的mac，然后判断字符串中是否有路由器2G的mac地址
        wlan1_list = common_fun.Wifi_scan.wlan1_ssid_scan(wlan1_ssid)
        print(wlan1_list)
        if wlan0_list != 0 and wlan1_list != 0:
            if wlan0_list.find("%s" % guest_mac_5g) != -1 and wlan1_list.find(
                    "%s" % guest_mac_2g) != -1 and wlan0_list.find("%s" % guest_mac_2g) == -1 and wlan1_list.find(
                    "%s" % guest_mac_5g) == -1:
                print("搜索到对应ssid")
                result = 1
            else:
                print("没有搜索到对应ssid")
                result = 0
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-5007 : “双频合一”关闭状态，2T2R设备能成功连接2.4G，协商速率300M
    def test_guest_wifi_6():
        wlan_ssid = common_conf.guest_ssid_2g
        guest_wlan_password = common_conf.guest_wlan_password
        # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
        con_status = common_fun.Wifi_con.wifi_2g_wpa2_aes_connect(wlan_ssid, guest_wlan_password)
        if con_status == 1:
            linkrate = common_fun.Linkrate_check.wifi_2g_linkrate()
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
    # 用例-5008 : “双频合一”关闭状态，2T2R设备能成功连接5G，协商速率867M
    def test_guest_wifi_7():
        wlan_ssid = common_conf.guest_ssid_5g
        guest_wlan_password = common_conf.guest_wlan_password
        # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
        con_status = common_fun.Wifi_con.wifi_5g_wpa2_aes_connect(wlan_ssid, guest_wlan_password)
        if con_status == 1:
            linkrate = common_fun.Linkrate_check.wifi_5g_linkrate()
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
    # 用例-5011 : SSID为20个字节，密码为24个字节，5G设备能成功连接
    def test_guest_wifi_8():
        wlan_ssid = common_conf.guest_ssid_2g_20b
        guest_mac_5g = common_conf.guest_mac_5g
        guest_wlan_password = common_conf.guest_wlan_password_24b
        # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
        wlan0_list = common_fun.Wifi_scan.wlan0_ssid_scan(wlan_ssid)
        print(wlan0_list)
        if wlan0_list != 0:
            if wlan0_list.find("%s" % guest_mac_5g) != -1:
                # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
                con_status = common_fun.Wifi_con.wifi_5g_wpa2_aes_connect(wlan_ssid, guest_wlan_password)
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
    # 用例-5012 : SSID为20个字节，密码为24个字节，2.4G设备能成功连接
    def test_guest_wifi_9():
        wlan_ssid = common_conf.guest_ssid_2g_20b
        guest_mac_2g = common_conf.guest_mac_2g
        guest_wlan_password = common_conf.guest_wlan_password_24b
        # 通过2.4G ssid筛选出对应的mac，然后判断字符串中是否有路由器2.4G的mac地址
        wlan1_list = common_fun.Wifi_scan.wlan1_ssid_scan(wlan_ssid)
        print(wlan1_list)
        if wlan1_list != 0:
            if wlan1_list.find("%s" % guest_mac_2g) != -1:
                # 通过2.4G ssid筛选出对应的mac，然后判断字符串中是否有路由器2.4G的mac地址
                con_status = common_fun.Wifi_con.wifi_2g_wpa2_aes_connect(wlan_ssid, guest_wlan_password)
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
    # 用例-5013 : SSID为1个字节，密码为8个字节，5G设备能成功连接
    def test_guest_wifi_10():
        wlan_ssid = common_conf.guest_ssid_2g_1b
        guest_mac_5g = common_conf.guest_mac_5g
        guest_wlan_password = common_conf.guest_wlan_password_8b
        # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
        wlan0_list = common_fun.Wifi_scan.wlan0_ssid_scan(wlan_ssid)
        print(wlan0_list)
        if wlan0_list != 0:
            if wlan0_list.find("%s" % guest_mac_5g) != -1:
                # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
                con_status = common_fun.Wifi_con.wifi_5g_wpa2_aes_connect(wlan_ssid, guest_wlan_password)
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
    #  用例-5014 : SSID为1个字节，密码为8个字节，2.4G设备能成功连接
    def test_guest_wifi_11():
        wlan_ssid = common_conf.guest_ssid_2g_1b
        guest_mac_2g = common_conf.guest_mac_2g
        guest_wlan_password = common_conf.guest_wlan_password_8b
        # 通过2.4G ssid筛选出对应的mac，然后判断字符串中是否有路由器2.4G的mac地址
        wlan1_list = common_fun.Wifi_scan.wlan1_ssid_scan(wlan_ssid)
        print(wlan1_list)
        if wlan1_list != 0:
            if wlan1_list.find("%s" % guest_mac_2g) != -1:
                # 通过2.4G ssid筛选出对应的mac，然后判断字符串中是否有路由器2.4G的mac地址
                con_status = common_fun.Wifi_con.wifi_2g_wpa2_aes_connect(wlan_ssid, guest_wlan_password)
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
    # 用例-4337 : 修改SSID后，新SSID生效，旧SSID失效
    def test_guest_wifi_12():
        wlan_ssid = common_conf.guest_ssid_2g
        guest_mac_5g = common_conf.guest_mac_5g
        guest_wlan_password = common_conf.guest_wlan_password
        wlan_ssid_change = common_conf.guest_ssid_2g_change
        guest_mac_2g = common_conf.guest_mac_2g
        # guest_wlan_password_change = wifi_set_conf.guest_wlan_password_change
        # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
        wlan0_list = common_fun.Wifi_scan.wlan0_ssid_scan(wlan_ssid)
        wlan1_list = common_fun.Wifi_scan.wlan1_ssid_scan(wlan_ssid)
        print("-1-1-1-1-1-1--1-1-1-1")
        print(wlan0_list)
        print(wlan1_list)
        if wlan0_list == 0 and wlan1_list == 0:
            print("00000000000000")
            wlan0_change_list = common_fun.Wifi_scan.wlan0_ssid_scan(wlan_ssid_change)
            wlan1_change_list = common_fun.Wifi_scan.wlan1_ssid_scan(wlan_ssid_change)

            # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
            if wlan0_change_list != 0 and wlan1_change_list != 0:
                print("1111111111111111111")
                if wlan0_change_list.find("%s" % guest_mac_5g) != -1 and wlan1_change_list.find(
                        "%s" % guest_mac_2g) != -1:
                    print("22222222222222")
                    con_status_5g = common_fun.Wifi_con.wifi_5g_wpa2_aes_auto_connect(wlan_ssid, guest_wlan_password)
                    con_status_2g = common_fun.Wifi_con.wifi_2g_wpa2_aes_auto_connect(wlan_ssid, guest_wlan_password)
                    con_status_5g_change = common_fun.Wifi_con.wifi_5g_wpa2_aes_connect(wlan_ssid_change,
                                                                                        guest_wlan_password)
                    con_status_2g_change = common_fun.Wifi_con.wifi_2g_wpa2_aes_connect(wlan_ssid_change,
                                                                                        guest_wlan_password)
                    print(
                        "连接状态：%s，%s，%s，%s" % (con_status_5g, con_status_2g, con_status_5g_change, con_status_2g_change))
                    if con_status_5g == 0 and con_status_2g == 0 and con_status_5g_change == 1 and con_status_2g_change == 1:
                        print("333333333333333333")
                        result = 1
                    else:
                        result = 0
                else:
                    result = 0
            else:
                result = 0
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-4317 : 修改密码后，新密码生效，旧密码失效
    def test_guest_wifi_13():
        wlan_ssid = common_conf.guest_ssid_2g
        guest_mac_5g = common_conf.guest_mac_5g
        guest_wlan_password = common_conf.guest_wlan_password
        wlan_ssid_change = common_conf.guest_ssid_2g_change
        guest_mac_2g = common_conf.guest_mac_2g
        guest_wlan_password_change = common_conf.guest_wlan_password_change
        # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
        wlan0_list = common_fun.Wifi_scan.wlan0_ssid_scan(wlan_ssid)
        wlan1_list = common_fun.Wifi_scan.wlan1_ssid_scan(wlan_ssid)
        print("-1-1-1-1-1-1-1-1-1-1-1-1--1")
        print(wlan0_list)
        print("000000000000")
        print(wlan1_list)
        print("11111111111")
        if wlan0_list != 0 and wlan1_list != 0:
            print("22222222222")
            if wlan0_list.find("%s" % guest_mac_5g) != -1 and wlan1_list.find("%s" % guest_mac_2g) != -1:
                print("333333333333")
                con_status_5g = common_fun.Wifi_con.wifi_5g_wpa2_aes_auto_connect(wlan_ssid, guest_wlan_password)
                con_status_2g = common_fun.Wifi_con.wifi_2g_wpa2_aes_auto_connect(wlan_ssid, guest_wlan_password)
                con_status_5g_change = common_fun.Wifi_con.wifi_5g_wpa2_aes_connect(wlan_ssid,
                                                                                    guest_wlan_password_change)
                con_status_2g_change = common_fun.Wifi_con.wifi_2g_wpa2_aes_connect(wlan_ssid,
                                                                                    guest_wlan_password_change)
                print("连接状态：%s，%s，%s，%s" % (con_status_5g, con_status_2g, con_status_5g_change, con_status_2g_change))
                if con_status_5g == 0 and con_status_2g == 0 and con_status_5g_change == 1 and con_status_2g_change == 1:
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
    # 用例-5020 : 加密方式为open，5G和2.4G设备可以不需要密码连接到WIFI
    def test_guest_wifi_14():
        wlan_ssid = common_conf.guest_ssid_2g
        con_status_5g = common_fun.Wifi_con.wifi_5g_open_connect(wlan_ssid)
        con_status_2g = common_fun.Wifi_con.wifi_2g_open_connect(wlan_ssid)
        if con_status_5g == 1 and con_status_2g == 1:
            result = 1
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    #  用例-5021 : 加密方式为WPA，5G和2.4G设备可以通过WPA认证方式连接到WIFI
    def test_guest_wifi_15():
        wlan_ssid = common_conf.guest_ssid_2g
        guest_wlan_password = common_conf.guest_wlan_password
        con_status_2g_aes = common_fun.Wifi_con.wifi_2g_wpa_aes_connect(wlan_ssid, guest_wlan_password)
        con_status_2g_tkip = common_fun.Wifi_con.wifi_2g_wpa_tkip_connect(wlan_ssid, guest_wlan_password)
        con_status_5g_aes = common_fun.Wifi_con.wifi_5g_wpa_aes_connect(wlan_ssid, guest_wlan_password)
        con_status_5g_tkip = common_fun.Wifi_con.wifi_5g_wpa_tkip_connect(wlan_ssid, guest_wlan_password)
        if con_status_2g_aes == 1 and con_status_2g_tkip == 1 and con_status_5g_aes == 1 and con_status_5g_tkip == 1:
            result = 1
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-5035 : 加密方式为WPA，5G和2.4G设备不可以通过WPA2认证方式连接到WIFI
    def test_guest_wifi_16():
        wlan_ssid = common_conf.guest_ssid_2g
        guest_wlan_password = common_conf.guest_wlan_password
        con_status_2g_aes = common_fun.Wifi_con.wifi_2g_wpa2_aes_connect(wlan_ssid, guest_wlan_password)
        con_status_5g_aes = common_fun.Wifi_con.wifi_5g_wpa2_aes_connect(wlan_ssid, guest_wlan_password)
        print("+++++++++")
        print("%s,%s"%(con_status_2g_aes,con_status_5g_aes))
        print("+++++++++")
        if con_status_2g_aes == 0 and con_status_5g_aes == 0:
            result = 1
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    #  用例-5022 : 加密方式为WPA2，5G和2.4G设备可以通过WPA2认证方式连接到WIFI
    def test_guest_wifi_17():
        wlan_ssid = common_conf.guest_ssid_2g
        guest_wlan_password = common_conf.guest_wlan_password
        con_status_2g_aes = common_fun.Wifi_con.wifi_2g_wpa2_aes_connect(wlan_ssid, guest_wlan_password)
        con_status_5g_aes = common_fun.Wifi_con.wifi_5g_wpa2_aes_connect(wlan_ssid, guest_wlan_password)
        if con_status_2g_aes == 1 and con_status_5g_aes == 1:
            result = 1
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-4827 : 加密方式为WPA2，5G和2.4G设备不可以通过WPA认证方式连接到WIFI
    def test_guest_wifi_18():
        wlan_ssid = common_conf.guest_ssid_2g
        guest_wlan_password = common_conf.guest_wlan_password
        con_status_2g_aes = common_fun.Wifi_con.wifi_2g_wpa_aes_connect(wlan_ssid, guest_wlan_password)
        con_status_2g_tkip = common_fun.Wifi_con.wifi_2g_wpa_tkip_connect(wlan_ssid, guest_wlan_password)
        con_status_5g_aes = common_fun.Wifi_con.wifi_5g_wpa_aes_connect(wlan_ssid, guest_wlan_password)
        con_status_5g_tkip = common_fun.Wifi_con.wifi_5g_wpa_tkip_connect(wlan_ssid, guest_wlan_password)
        if con_status_2g_aes == 0 and con_status_2g_tkip == 0 and con_status_5g_aes == 0 and con_status_5g_tkip == 0:
            result = 1
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-4352 : 加密方式为WPA/WPA2-PSK，5G和2.4G设备可以通过WPA认证方式连接到该WIFI
    def test_guest_wifi_19():
        wlan_ssid = common_conf.guest_ssid_2g
        guest_wlan_password = common_conf.guest_wlan_password
        con_status_2g_aes = common_fun.Wifi_con.wifi_2g_wpa_aes_connect(wlan_ssid, guest_wlan_password)
        con_status_2g_tkip = common_fun.Wifi_con.wifi_2g_wpa_tkip_connect(wlan_ssid, guest_wlan_password)
        con_status_5g_aes = common_fun.Wifi_con.wifi_5g_wpa_aes_connect(wlan_ssid, guest_wlan_password)
        con_status_5g_tkip = common_fun.Wifi_con.wifi_5g_wpa_tkip_connect(wlan_ssid, guest_wlan_password)
        if con_status_2g_aes == 1 and con_status_2g_tkip == 1 and con_status_5g_aes == 1 and con_status_5g_tkip == 1:
            result = 1
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-4828 : 加密方式为WPA/WPA2-PSK，5G和2.4G设备可以通过WPA2认证方式连接到该WIFI
    def test_guest_wifi_20():
        wlan_ssid = common_conf.guest_ssid_2g
        guest_wlan_password = common_conf.guest_wlan_password
        con_status_2g_aes = common_fun.Wifi_con.wifi_2g_wpa2_aes_connect(wlan_ssid, guest_wlan_password)
        con_status_5g_aes = common_fun.Wifi_con.wifi_5g_wpa2_aes_connect(wlan_ssid, guest_wlan_password)
        if con_status_2g_aes == 1 and con_status_5g_aes == 1:
            result = 1
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result

    @staticmethod
    # 用例-4372 : 关闭访客网络后，访客网络生效，5G和2.4G都不能连接到访客网络
    def test_guest_wifi_21():
        wlan_ssid = common_conf.guest_ssid_2g
        guest_wlan_password = common_conf.guest_wlan_password
        # 通过5G ssid筛选出对应的mac，然后判断字符串中是否有路由器5G的mac地址
        con_status_2g = common_fun.Wifi_con.wifi_2g_wpa2_aes_auto_connect(wlan_ssid, guest_wlan_password)
        con_status_5g = common_fun.Wifi_con.wifi_5g_wpa2_aes_auto_connect(wlan_ssid, guest_wlan_password)
        if con_status_2g == 0 and con_status_5g == 0:
            result = 1
        else:
            result = 0
        # result为0表示测试失败，result为1表示测试成功
        return result
