import os
import time
from .. common_dir import common_fun, common_conf

class Test_static_dhcp_lease():

    @staticmethod
    # MAC与IP绑定测试前置条件
    def test_static_dhcp_lease_init():
        interfacewired_1 = common_conf.interfacewired_1
        interface5g_1 = common_conf.interface5g_1
        interface2g_1 = common_conf.interface2g_1
        a = os.system('netsh interface set interface "%s" disabled' % interfacewired_1)
        b = os.system('netsh interface set interface "%s" disabled' % interface5g_1)
        c = os.system('netsh interface set interface "%s" disabled' % interface2g_1)
        d = os.system('netsh interface set interface "%s" enabled' % interfacewired_1)
        e = os.system('netsh interface set interface "%s" enabled' % interface5g_1)
        f = os.system('netsh interface set interface "%s" enabled' % interface2g_1)
        print ("测试结果1为：%s,%s,%s,%s,%s,%s"%(a,b,c,d,e,f))
        os.system('netsh wlan delete profile *')
        wired1 = common_fun.Conf_networkcard.ipwired1_dhcp(interfacewired_1)
        wlan5g1 = common_fun.Conf_networkcard.ip5g1_dhcp(interface5g_1)
        wlan2g1 = common_fun.Conf_networkcard.ip2g1_dhcp(interface2g_1)
        print ("测试结果2为：%s,%s,%s"%(wired1,wlan5g1,wlan2g1))
        if wired1 == 1 and wlan5g1 == 1 and wlan2g1 == 1:
            result = 1
        else:
            result = 0
        return result

    @staticmethod
    #  用例-2830 : 配置一条MAC/IP绑定规则（IP未分配），该MAC对应主机发送一个DISCOVER报文，其中可选字段请求IP地址为空，该主机只能获取到绑定的IP地址
    #  用例-3985: 配置一条MAC / IP绑定规则，主路由器下的有线设备会重新获取到绑定的IP地址
    #  配置有线网卡WIRED1的静态IP为static_ip1，能成功获取到对应ip地址
    def test_static_dhcp_lease_1():
        wired1_mac = common_conf.wired1_mac
        static_ip1 = common_conf.static_ip1
        wired1_ip = common_fun.Static_dhcp_lease.read_networkcard_ip(wired1_mac)
        if static_ip1 == wired1_ip:
            result = 1
        else:
            result = 0
        return result

    @staticmethod
    # 用例-7372 : 配置一条MAC/IP绑定规则（IP已分配），原分配到该IP的主机发送一个request报文，原主机不能再分配到该IP
    # 用例-2836: 配置一条MAC / IP绑定规则，其他主机发送一个Request报文，其中可选字段请求IP地址为绑定的IP地址，该主机获取到路由器分配的其他IP
    # 用例-3987 : 配置一条MAC/IP绑定规则，主路由器下的5G设备会重新获取到绑定的IP地址
    # 先配置有线网卡WIRED1的静态IP为static_ip1，执行test_static_dhcp_lease_2_1，测试结果为1时，再将static_ip1绑定到WLAN5G1，生效后执行test_static_dhcp_lease_2_2，然后使得WLAN5G1连接到WiFi并且拿到的ip为static_ip1，并且WIRED1拿到的ip不为static_ip1
    def test_static_dhcp_lease_2_1():
        wired1_mac = common_conf.wired1_mac
        static_ip1 = common_conf.static_ip1
        wired1_ip = common_fun.Static_dhcp_lease.read_networkcard_ip(wired1_mac)
        if static_ip1 == wired1_ip:
            result = 1
        else:
            result = 0
        return result
    @staticmethod
    def test_static_dhcp_lease_2_2():
        wlan0_ssid = common_conf.ssid_2g
        wlan0_password = common_conf.wlan_password
        wlan5g_con_status = common_fun.Wifi_con.wifi_5g_wpa2_aes_connect(wlan0_ssid, wlan0_password)
        print("11111111111111")
        if wlan5g_con_status == 1:
            print("22222222222")
            wired1_mac = common_conf.wired1_mac
            wlan5g_mac = common_conf.wired1_mac
            static_ip1 = common_conf.static_ip1
            wlan5g1_ip = common_fun.Static_dhcp_lease.read_networkcard_ip(wlan5g_mac)
            wired1_ip = common_fun.Static_dhcp_lease.read_networkcard_ip(wired1_mac)
            print("================")
            print("%s,%s,%s,%s,"%(static_ip1,wlan5g1_ip,static_ip1,wired1_ip))
            print("================")
            if static_ip1 == wlan5g1_ip and static_ip1 != wired1_ip:
                result = 1
            else:
                result = 0
        else:
            result = 0
            print("333333333333")

        return result


    @staticmethod
    #  用例-2833 : 配置一条MAC/IP绑定规则，该MAC对应主机发送一个Request报文，其中可选字段请求IP地址不为绑定的IP地址，该主机只能获取到绑定的IP地址
    #  用例-4009 : 修改一条MAC/IP绑定规则，新规则生效，老规则失效
    #  先配置有线网卡WIRED1的静态IP为static_ip1，保存生效，执行test_static_dhcp_lease_3_1，测试结果为1时，修改WIRED1的静态IP为static_ip2，保存生效后再执行test_static_dhcp_lease_3_2
    def test_static_dhcp_lease_3_1():
        wired1_mac = common_conf.wired1_mac
        static_ip1 = common_conf.static_ip1
        wired1_ip = common_fun.Static_dhcp_lease.read_networkcard_ip(wired1_mac)
        if static_ip1 == wired1_ip:
            result = 1
        else:
            result = 0
        return result
    @staticmethod
    def test_static_dhcp_lease_3_2():
        wired1_mac = common_conf.wired1_mac
        static_ip2 = common_conf.static_ip2
        wired1_ip2 = common_fun.Static_dhcp_lease.read_networkcard_ip(wired1_mac)
        if static_ip2 == wired1_ip2:
            result = 1
        else:
            result = 0
        return result

    @staticmethod
    #  用例-2834 : 配置一条MAC/IP绑定规则，该MAC对应主机发送一个Request报文，其中可选字段请求IP地址绑定的IP地址，该主机只能获取到绑定的IP地址
    #  先配置有线网卡WIRED1的静态IP为static_ip1，保存生效后，执行test_static_dhcp_lease_4，测试结果为1时，然后不做任何修改，保存生效后，再执行test_static_dhcp_lease_4，测试结果为1表示通过
    def test_static_dhcp_lease_4():
        wired1_mac = common_conf.wired1_mac
        static_ip1 = common_conf.static_ip1
        wired1_ip = common_fun.Static_dhcp_lease.read_networkcard_ip(wired1_mac)
        if static_ip1 == wired1_ip:
            result = 1
        else:
            result = 0
        return result

    # @staticmethod
    # #  用例-2838 : 删除一条MAC/IP绑定规则，该规则失效
    # #  先配置无线网卡WLAN5G1的静态IP为static_ip1，保存生效后，执行test_static_dhcp_lease_5_1，删除所绑定的MAC/IP绑定规则，保存生效后再执行test_static_dhcp_lease_5_2
    # def test_static_dhcp_lease_5_1():
    #     wlan0_ssid = common_conf.ssid_2g
    #     wlan0_password = common_conf.wlan_password
    #     wlan5g_con_status = common_fun.Wifi_con.wifi_5g_wpa2_aes_connect(wlan0_ssid, wlan0_password)
    #     if wlan5g_con_status == 1:
    #         result = 1
    #     else:
    #         result = 0
    #     return result
    # @staticmethod
    # def test_static_dhcp_lease_5_2():
    #     wlan0_ssid = common_conf.ssid_2g
    #     wlan0_password = common_conf.wlan_password
    #     wlan5g_con_status = common_fun.Wifi_con.wifi_5g_wpa2_aes_connect(wlan0_ssid, wlan0_password)
    #     if wlan5g_con_status == 1:
    #         result = 1
    #     else:
    #         result = 0
    #     return result


