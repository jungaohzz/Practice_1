import os
import time
import telnetlib
import requests
import http
import re
import socket
from . import common_conf


# ping网关检查
class Wifi_scan:
    @staticmethod
    # 是否能扫描到某个5G SSID
    def wlan0_status(wlan0_ssid):
        internet_interface_5g = common_conf.interface5g_1
        internet_interface_2g = common_conf.interface2g_1
        os.system('netsh interface set interface "%s" disabled' % internet_interface_2g)
        os.system('netsh interface set interface "%s" disabled' % internet_interface_5g)
        os.system('netsh interface set interface "%s" enabled' % internet_interface_5g)
        time.sleep(5)
        wifi_list = str(os.popen('netsh wlan show all').readlines())
        print(wifi_list)
        if wifi_list.find(wlan0_ssid) != -1:
            print("可以搜索到 SSID:" + wlan0_ssid)
            result = 1
        else:
            print("不可以搜索到 SSID:" + wlan0_ssid)
            result = 0
        return result

    @staticmethod
    # 是否能扫描到某个2G SSID
    def wlan1_status(wlan1_ssid):
        internet_interface_5g = common_conf.interface5g_1
        internet_interface_2g = common_conf.interface2g_1
        os.system('netsh interface set interface "%s" disabled' % internet_interface_5g)
        os.system('netsh interface set interface "%s" disabled' % internet_interface_2g)
        os.system('netsh interface set interface "%s" enabled' % internet_interface_2g)
        time.sleep(5)
        wifi_list = str(os.popen('netsh wlan show all').readlines())
        print(wifi_list)
        if wifi_list.find(wlan1_ssid) != -1:
            print("可以搜索到 SSID: " + wlan1_ssid)
            result = 1
        else:
            print("不可以搜索到 SSID: " + wlan1_ssid)
            result = 0
        return result

    @staticmethod
    # 某个SSID对应的5G BSSID列表
    def wlan0_ssid_scan(wlan0_ssid):
        internet_interface_5g = common_conf.interface5g_1
        internet_interface_2g = common_conf.interface2g_1
        os.system('netsh interface set interface "%s" disabled' % internet_interface_2g)
        os.system('netsh interface set interface "%s" disabled' % internet_interface_5g)
        os.system('netsh interface set interface "%s" enabled' % internet_interface_5g)
        time.sleep(10)
        a = os.popen('netsh wlan show all').readlines()
        print(a)
        b = "".join(a)
        c = b.split("\nSSID")
        d = list(filter(lambda x: '%s' % wlan0_ssid in x, c))
        wlan0_list = "".join(d)
        if wlan0_list.strip() == "":
            print("没有对应SSID")
            result = 0
        else:
            print("有对应SSID")
            print(wlan0_list)
            result = wlan0_list
        print(result)
        return result

    @staticmethod
    # 某个SSID对应的5G BSSID列表
    def wlan1_ssid_scan(wlan1_ssid):
        internet_interface_5g = common_conf.interface5g_1
        internet_interface_2g = common_conf.interface2g_1
        os.system('netsh interface set interface "%s" disabled' % internet_interface_2g)
        os.system('netsh interface set interface "%s" disabled' % internet_interface_5g)
        os.system('netsh interface set interface "%s" enabled' % internet_interface_2g)
        time.sleep(15)
        a = os.popen('netsh wlan show all').readlines()
        print(a)
        b = "".join(a)
        c = b.split("\nSSID")
        d = list(filter(lambda x: '%s' % wlan1_ssid in x, c))
        wlan1_list = "".join(d)
        if wlan1_list.strip() == "":
            print("没有对应SSID")
            result = 0
        else:
            print("有对应SSID")
            result = wlan1_list
        print(result)
        return result


class Wifi_con:

    @staticmethod
    # 检查WLAN5G接口是否连接成功
    def wlan_5g_con_status():
        interface = common_conf.interface5g_1
        a = os.popen('netsh wlan  show interfaces').readlines()
        print(type(a))
        print(a)
        d = str(a)
        e = d.split("名称                   :")
        n = len(e)
        print(n)
        i = 0
        while i < n:
            i = i + 1
            if e[i].find("%s"%interface) != -1:
                f = e[i].split("\n")
                b = list(filter(lambda x: '状态                   :' in x, f))
                c = "".join(b)
                print(c)

                if c.find("已连接") != -1:
                    result = 1
                    print("连接成功")
                elif c.find("已断开") != -1:
                    result = 0
                    print("连接失败")
                else:
                    result = -1
                    print("连接异常")
                break
        # result = 0 表示连接成功，result = 0表示连接失败
        return result

    @staticmethod
    # 检查WLAN2G接口是否连接成功
    def wlan_2g_con_status():
        interface = common_conf.interface2g_1
        a = os.popen('netsh wlan  show interfaces').readlines()
        print(type(a))
        print(a)
        d = str(a)
        e = d.split("名称                   :")
        n = len(e)
        print(n)
        i = 0
        while i < n:
            i = i + 1
            if e[i].find("%s"%interface) != -1:
                f = e[i].split("\n")
                b = list(filter(lambda x: '状态                   :' in x, f))
                c = "".join(b)
                print(c)
                if c.find("已连接") != -1:
                    result = 1
                    print("连接成功")
                elif c.find("已断开") != -1:
                    result = 0
                    print("连接失败")
                else:
                    result = -1
                    print("连接异常")
                break
        # result = 0 表示连接成功，result = 0表示连接失败
        return result

    @staticmethod
    # 无线连接检测
    def wifi_5g_open_connect(wlan0_ssid):
        # 连接WIFI过程
        interface2g = common_conf.interface2g_1
        interface5g = common_conf.interface5g_1
        conf_path = common_conf.conf_path
        open_conf = common_conf.open_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, open_conf, interface5g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (open_conf, wlan0_ssid))
        con = os.system('netsh wlan connect name=%s ssid=%s interface=%s' % (open_conf, wlan0_ssid, interface5g))
        time.sleep(20)
        con_status = Wifi_con.wlan_5g_con_status()
        if con_status == 1:
            result = 1
            print("连接成功")
        elif con_status == 0:
            result = 0
            print("连接失败")
        else:
            result = -1
            print("表示网卡异常")
        # result = 1 表示连接成功，0 表示连接失败, -1表示网卡异常
        return result

    @staticmethod
    def wifi_5g_open_auto_connect(wlan0_ssid):
        # 连接WIFI过程
        interface2g = common_conf.interface2g_1
        interface5g = common_conf.interface5g_1
        conf_path = common_conf.conf_path
        open_auto_conf = common_conf.open_auto_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, open_auto_conf, interface5g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (open_auto_conf, wlan0_ssid))
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        con = os.system('netsh wlan connect name=%s ssid=%s interface=%s' % (open_auto_conf, wlan0_ssid, interface5g))
        time.sleep(20)
        con_status = Wifi_con.wlan_5g_con_status()
        if con_status == 1:
            result = 1
            print("连接成功")
        elif con_status == 0:
            result = 0
            print("连接失败")
        else:
            result = -1
            print("表示网卡异常")
        # result = 1 表示连接成功，0 表示连接失败, -1表示网卡异常
        return result

    @staticmethod
    # 无线连接检测
    def wifi_5g_wpa_tkip_connect(wlan0_ssid, wlan0_password):
        # 连接WIFI过程
        interface2g = common_conf.interface2g_1
        interface5g = common_conf.interface5g_1
        conf_path = common_conf.conf_path
        wpa_tkip_conf = common_conf.wpa_tkip_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa_tkip_conf, interface5g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa_tkip_conf, wlan0_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa_tkip_conf, wlan0_password))
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        con = os.system('netsh wlan connect name=%s ssid=%s  interface=%s' % (wpa_tkip_conf, wlan0_ssid, interface5g))
        time.sleep(20)
        con_status = Wifi_con.wlan_5g_con_status()
        if con_status == 1:
            result = 1
            print("连接成功")
        elif con_status == 0:
            result = 0
            print("连接失败")
        else:
            result = -1
            print("表示网卡异常")
        # result = 1 表示连接成功，0 表示连接失败, -1表示网卡异常
        return result

    @staticmethod
    # 无线连接检测
    def wifi_5g_wpa_tkip_auto_connect(wlan0_ssid, wlan0_password):
        # 连接WIFI过程
        interface2g = common_conf.interface2g_1
        interface5g = common_conf.interface5g_1
        conf_path = common_conf.conf_path
        wpa_tkip_auto_conf = common_conf.wpa_tkip_auto_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa_tkip_auto_conf, interface5g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa_tkip_auto_conf, wlan0_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa_tkip_auto_conf, wlan0_password))
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        con = os.system('netsh wlan connect name=%s ssid=%s  interface=%s' % (wpa_tkip_auto_conf, wlan0_ssid, interface5g))
        time.sleep(20)
        con_status = Wifi_con.wlan_5g_con_status()
        if con_status == 1:
            result = 1
            print("连接成功")
        elif con_status == 0:
            result = 0
            print("连接失败")
        else:
            result = -1
            print("表示网卡异常")
        # result = 1 表示连接成功，0 表示连接失败, -1表示网卡异常
        return result

    @staticmethod
    # 无线连接检测
    def wifi_5g_wpa_aes_connect(wlan0_ssid, wlan0_password):
        # 连接WIFI过程
        interface2g = common_conf.interface2g_1
        interface5g = common_conf.interface5g_1
        conf_path = common_conf.conf_path
        wpa_aes_conf = common_conf.wpa_aes_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa_aes_conf, interface5g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa_aes_conf, wlan0_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa_aes_conf, wlan0_password))
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        status = os.system('netsh wlan connect name=%s ssid=%s  interface=%s' % (wpa_aes_conf, wlan0_ssid, interface5g))
        time.sleep(20)
        con_status = Wifi_con.wlan_5g_con_status()
        if con_status == 1:
            result = 1
            print("连接成功")
        elif con_status == 0:
            result = 0
            print("连接失败")
        else:
            result = -1
            print("表示网卡异常")
        # result = 1 表示连接成功，0 表示连接失败, -1表示网卡异常
        return result

    @staticmethod
    # 无线连接检测
    def wifi_5g_wpa_aes_auto_connect(wlan0_ssid, wlan0_password):
        # 连接WIFI过程
        interface2g = common_conf.interface2g_1
        interface5g = common_conf.interface5g_1
        conf_path = common_conf.conf_path
        wpa_aes_auto_conf = common_conf.wpa_aes_auto_conf
        wlan_password = common_conf.wlan_password
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa_aes_auto_conf, interface5g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa_aes_auto_conf, wlan0_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa_aes_auto_conf, wlan0_password))
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        con = os.system('netsh wlan connect name=%s ssid=%s  interface=%s' % (wpa_aes_auto_conf, wlan0_ssid,  interface5g))
        time.sleep(20)
        con_status = Wifi_con.wlan_5g_con_status()
        if con_status == 1:
            result = 1
            print("连接成功")
        elif con_status == 0:
            result = 0
            print("连接失败")
        else:
            result = -1
            print("表示网卡异常")
        # result = 1 表示连接成功，0 表示连接失败, -1表示网卡异常
        return result

    @staticmethod
    # 无线连接检测
    def wifi_5g_wpa_tkip_connect(wlan0_ssid, wlan0_password):
        # 连接WIFI过程
        interface2g = common_conf.interface2g_1
        interface5g = common_conf.interface5g_1
        conf_path = common_conf.conf_path
        wpa_tkip_conf = common_conf.wpa_tkip_conf
        wlan_password = common_conf.wlan_password
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa_tkip_conf, interface5g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa_tkip_conf, wlan0_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa_tkip_conf, wlan0_password))
        con = os.system('netsh wlan connect name=%s ssid=%s  interface=%s' % (wpa_tkip_conf, wlan0_ssid,  interface5g))
        time.sleep(20)
        con_status = Wifi_con.wlan_5g_con_status()
        if con_status == 1:
            result = 1
            print("连接成功")
        elif con_status == 0:
            result = 0
            print("连接失败")
        else:
            result = -1
            print("表示网卡异常")
        # result = 1 表示连接成功，0 表示连接失败, -1表示网卡异常
        return result

    @staticmethod
    # 无线连接检测
    def wifi_5g_wpa_tkip_auto_connect(wlan0_ssid, wlan0_password):
        # 连接WIFI过程
        interface2g = common_conf.interface2g_1
        interface5g = common_conf.interface5g_1
        conf_path = common_conf.conf_path
        wpa_tkip_auto_conf = common_conf.wpa_tkip_auto_conf
        wlan_password = common_conf.wlan_password
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa_tkip_auto_conf, interface5g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa_tkip_auto_conf, wlan0_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa_tkip_auto_conf, wlan0_password))
        con = os.system('netsh wlan connect name=%s ssid=%s  interface=%s' % (wpa_tkip_auto_conf, wlan0_ssid, interface5g))
        time.sleep(20)
        con_status = Wifi_con.wlan_5g_con_status()
        if con_status == 1:
            result = 1
            print("连接成功")
        elif con_status == 0:
            result = 0
            print("连接失败")
        else:
            result = -1
            print("表示网卡异常")
        # result = 1 表示连接成功，0 表示连接失败, -1表示网卡异常
        return result

    @staticmethod
    # 无线连接检测
    def wifi_5g_wpa2_aes_connect(wlan0_ssid, wlan0_password):
        # 连接WIFI过程
        interface2g = common_conf.interface2g_1
        interface5g = common_conf.interface5g_1
        conf_path = common_conf.conf_path
        wpa2_aes_conf = common_conf.wpa2_aes_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa2_aes_conf, interface5g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa2_aes_conf, wlan0_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa2_aes_conf, wlan0_password))
        con = os.system('netsh wlan connect name=%s ssid=%s  interface=%s ' % (wpa2_aes_conf, wlan0_ssid, interface5g))
        time.sleep(20)
        con_status = Wifi_con.wlan_5g_con_status()
        if con_status == 1:
            result = 1
            print("连接成功")
        elif con_status == 0:
            result = 0
            print("连接失败")
        else:
            result = -1
            print("表示网卡异常")
        # result = 1 表示连接成功，0 表示连接失败, -1表示网卡异常
        return result

    @staticmethod
    # 无线连接检测
    def wifi_5g_wpa2_aes_auto_connect(wlan0_ssid, wlan0_password):
        # 连接WIFI过程
        interface2g = common_conf.interface2g_1
        interface5g = common_conf.interface5g_1
        conf_path = common_conf.conf_path
        wpa2_aes_auto_conf = common_conf.wpa2_aes_auto_conf
        wlan_password = common_conf.wlan_password
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa2_aes_auto_conf, interface5g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa2_aes_auto_conf, wlan0_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa2_aes_auto_conf, wlan0_password))
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        con = os.system('netsh wlan connect name=%s ssid=%s  interface=%s' % (wpa2_aes_auto_conf, wlan0_ssid, interface5g))
        time.sleep(20)
        con_status = Wifi_con.wlan_5g_con_status()
        if con_status == 1:
            result = 1
            print("连接成功")
        elif con_status == 0:
            result = 0
            print("连接失败")
        else:
            result = -1
            print("表示网卡异常")
        # result = 1 表示连接成功，0 表示连接失败, -1表示网卡异常
        return result

    @staticmethod
    # 无线连接检测
    def wifi_2g_open_connect(wlan1_ssid):
        # 连接WIFI过程
        interface2g = common_conf.interface2g_1
        interface5g = common_conf.interface5g_1
        conf_path = common_conf.conf_path
        open_conf = common_conf.open_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, open_conf, interface2g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (open_conf, wlan1_ssid))
        con = os.system('netsh wlan connect name=%s ssid=%s  interface=%s' % (open_conf, wlan1_ssid, interface2g))
        time.sleep(20)
        con_status = Wifi_con.wlan_2g_con_status()
        if con_status == 1:
            result = 1
            print("连接成功")
        elif con_status == 0:
            result = 0
            print("连接失败")
        else:
            result = -1
            print("表示网卡异常")
        # result = 1 表示连接成功，0 表示连接失败, -1表示网卡异常
        return result

    @staticmethod
    def wifi_2g_open_auto_connect(wlan1_ssid):
        # 连接WIFI过程
        interface2g = common_conf.interface2g_1
        interface5g = common_conf.interface5g_1
        conf_path = common_conf.conf_path
        open_auto_conf = common_conf.open_auto_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, open_auto_conf, interface2g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (open_auto_conf, wlan1_ssid))
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        con = os.system('netsh wlan connect name=%s ssid=%s  interface=%s' % (open_auto_conf, wlan1_ssid, interface2g))
        time.sleep(20)
        con_status = Wifi_con.wlan_2g_con_status()
        if con_status == 1:
            result = 1
            print("连接成功")
        elif con_status == 0:
            result = 0
            print("连接失败")
        else:
            result = -1
            print("表示网卡异常")
        # result = 1 表示连接成功，0 表示连接失败, -1表示网卡异常
        return result

    @staticmethod
    # 无线连接检测
    def wifi_2g_wpa_tkip_connect(wlan1_ssid, wlan1_password):
        # 连接WIFI过程
        interface2g = common_conf.interface2g_1
        interface5g = common_conf.interface5g_1
        conf_path = common_conf.conf_path
        wpa_tkip_conf = common_conf.wpa_tkip_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa_tkip_conf, interface2g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa_tkip_conf, wlan1_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa_tkip_conf, wlan1_password))
        con = os.system('netsh wlan connect name=%s ssid=%s  interface=%s' % (wpa_tkip_conf, wlan1_ssid, interface2g))
        time.sleep(20)
        con_status = Wifi_con.wlan_2g_con_status()
        if con_status == 1:
            result = 1
            print("连接成功")
        elif con_status == 0:
            result = 0
            print("连接失败")
        else:
            result = -1
            print("表示网卡异常")
        # result = 1 表示连接成功，0 表示连接失败, -1表示网卡异常
        return result

    @staticmethod
    # 无线连接检测
    def wifi_2g_wpa_tkip_auto_connect(wlan1_ssid, wlan1_password):
        # 连接WIFI过程
        interface2g = common_conf.interface2g_1
        interface5g = common_conf.interface5g_1
        conf_path = common_conf.conf_path
        wpa_tkip_auto_conf = common_conf.wpa_tkip_auto_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa_tkip_auto_conf, interface2g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa_tkip_auto_conf, wlan1_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa_tkip_auto_conf, wlan1_password))
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        con = os.system('netsh wlan connect name=%s ssid=%s  interface=%s' % (wpa_tkip_auto_conf, wlan1_ssid, interface2g))
        time.sleep(20)
        con_status = Wifi_con.wlan_2g_con_status()
        if con_status == 1:
            result = 1
            print("连接成功")
        elif con_status == 0:
            result = 0
            print("连接失败")
        else:
            result = -1
            print("表示网卡异常")
        # result = 1 表示连接成功，0 表示连接失败, -1表示网卡异常
        return result

    @staticmethod
    # 无线连接检测
    def wifi_2g_wpa_aes_connect(wlan1_ssid, wlan1_password):
        # 连接WIFI过程
        interface2g = common_conf.interface2g_1
        interface5g = common_conf.interface5g_1
        conf_path = common_conf.conf_path
        wpa_aes_conf = common_conf.wpa_aes_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa_aes_conf, interface2g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa_aes_conf, wlan1_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa_aes_conf, wlan1_password))
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        con = os.system('netsh wlan connect name=%s ssid=%s  interface=%s' % (wpa_aes_conf, wlan1_ssid, interface2g))
        time.sleep(20)
        con_status = Wifi_con.wlan_2g_con_status()
        if con_status == 1:
            result = 1
            print("连接成功")
        elif con_status == 0:
            result = 0
            print("连接失败")
        else:
            result = -1
            print("表示网卡异常")
        # result = 1 表示连接成功，0 表示连接失败, -1表示网卡异常
        return result

    @staticmethod
    # 无线连接检测
    def wifi_2g_wpa_aes_auto_connect(wlan1_ssid, wlan1_password):
        # 连接WIFI过程
        interface2g = common_conf.interface2g_1
        interface5g = common_conf.interface5g_1
        conf_path = common_conf.conf_path
        wpa_aes_auto_conf = common_conf.wpa_aes_auto_conf
        wlan_password = common_conf.wlan_password
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa_aes_auto_conf, interface2g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa_aes_auto_conf, wlan1_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa_aes_auto_conf, wlan1_password))
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        con = os.system('netsh wlan connect name=%s ssid=%s  interface=%s' % (wpa_aes_auto_conf, wlan1_ssid, interface2g))
        time.sleep(20)
        con_status = Wifi_con.wlan_2g_con_status()
        if con_status == 1:
            result = 1
            print("连接成功")
        elif con_status == 0:
            result = 0
            print("连接失败")
        else:
            result = -1
            print("表示网卡异常")
        # result = 1 表示连接成功，0 表示连接失败, -1表示网卡异常
        return result

    @staticmethod
    # 无线连接检测
    def wifi_2g_wpa_tkip_connect(wlan1_ssid, wlan1_password):
        # 连接WIFI过程
        interface2g = common_conf.interface2g_1
        interface5g = common_conf.interface5g_1
        conf_path = common_conf.conf_path
        wpa_tkip_conf = common_conf.wpa_tkip_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa_tkip_conf, interface2g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa_tkip_conf, wlan1_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa_tkip_conf, wlan1_password))
        con = os.system('netsh wlan connect name=%s ssid=%s  interface=%s' % (wpa_tkip_conf, wlan1_ssid, interface2g))
        time.sleep(20)
        con_status = Wifi_con.wlan_2g_con_status()
        if con_status == 1:
            result = 1
            print("连接成功")
        elif con_status == 0:
            result = 0
            print("连接失败")
        else:
            result = -1
            print("表示网卡异常")
        # result = 1 表示连接成功，0 表示连接失败, -1表示网卡异常
        return result

    @staticmethod
    # 无线连接检测
    def wifi_2g_wpa_tkip_auto_connect(wlan1_ssid, wlan1_password):
        # 连接WIFI过程
        interface2g = common_conf.interface2g_1
        interface5g = common_conf.interface5g_1
        conf_path = common_conf.conf_path
        wpa_tkip_auto_conf = common_conf.wpa_tkip_auto_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa_tkip_auto_conf, interface2g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa_tkip_auto_conf, wlan1_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa_tkip_auto_conf, wlan1_password))
        con = os.system('netsh wlan connect name=%s ssid=%s  interface=%s' % (wpa_tkip_auto_conf, wlan1_ssid, interface2g))
        time.sleep(20)
        con_status = Wifi_con.wlan_2g_con_status()
        if con_status == 1:
            result = 1
            print("连接成功")
        elif con_status == 0:
            result = 0
            print("连接失败")
        else:
            result = -1
            print("表示网卡异常")
        # result = 1 表示连接成功，0 表示连接失败, -1表示网卡异常
        return result

    @staticmethod
    # 无线连接检测
    def wifi_2g_wpa2_aes_connect(wlan1_ssid, wlan1_password):
        # 连接WIFI过程
        interface2g = common_conf.interface2g_1
        interface5g = common_conf.interface5g_1
        conf_path = common_conf.conf_path
        wpa2_aes_conf = common_conf.wpa2_aes_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa2_aes_conf, interface2g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa2_aes_conf, wlan1_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa2_aes_conf, wlan1_password))
        con = os.system('netsh wlan connect name=%s ssid=%s  interface=%s' % (wpa2_aes_conf, wlan1_ssid,  interface2g))
        time.sleep(20)
        con_status = Wifi_con.wlan_2g_con_status()
        if con_status == 1:
            result = 1
            print("连接成功")
        elif con_status == 0:
            result = 0
            print("连接失败")
        else:
            result = -1
            print("表示网卡异常")
        # result = 1 表示连接成功，0 表示连接失败, -1表示网卡异常
        return result

    @staticmethod
    # 无线连接检测
    def wifi_2g_wpa2_aes_auto_connect(wlan1_ssid, wlan1_password):
        # 连接WIFI过程
        interface2g = common_conf.interface2g_1
        interface5g = common_conf.interface5g_1
        conf_path = common_conf.conf_path
        wpa2_aes_auto_conf = common_conf.wpa2_aes_auto_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa2_aes_auto_conf, interface2g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa2_aes_auto_conf, wlan1_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa2_aes_auto_conf, wlan1_password))
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        con = os.system('netsh wlan connect name=%s ssid=%s  interface=%s' % (wpa2_aes_auto_conf, wlan1_ssid, interface2g))
        time.sleep(20)
        con_status = Wifi_con.wlan_2g_con_status()
        if con_status == 1:
            result = 1
            print("连接成功")
        elif con_status == 0:
            result = 0
            print("连接失败")
        else:
            result = -1
            print("表示网卡异常")
        # result = 1 表示连接成功，0 表示连接失败, -1表示网卡异常
        return result

    @staticmethod
    # 2g无线连接，不删除配置
    def wifi_2g_wpa2_aes_auto_connect_undelete(wlan1_ssid, wlan1_password):
        # 连接WIFI过程
        interface2g = common_conf.interface2g_1
        interface5g = common_conf.interface5g_1
        conf_path = common_conf.conf_path
        wpa2_aes_auto_2g_conf = common_conf.wpa2_aes_auto_2g_conf
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa2_aes_auto_2g_conf, interface2g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa2_aes_auto_2g_conf, wlan1_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa2_aes_auto_2g_conf, wlan1_password))
        con = os.system('netsh wlan connect name=%s ssid=%s  interface=%s' % (wpa2_aes_auto_2g_conf, wlan1_ssid,interface2g))
        time.sleep(20)
        con_status = Wifi_con.wlan_2g_con_status()
        if con_status == 1:
            result = 1
            print("连接成功")
        elif con_status == 0:
            result = 0
            print("连接失败")
        else:
            result = -1
            print("表示网卡异常")
        # result = 1 表示连接成功，0 表示连接失败, -1表示网卡异常
        return result

    @staticmethod
    # 5g无线连接，不删除配置
    def wifi_5g_wpa2_aes_auto_connect_undelete(wlan0_ssid, wlan0_password):
        # 连接WIFI过程
        interface2g = common_conf.interface2g_1
        interface5g = common_conf.interface5g_1
        conf_path = common_conf.conf_path
        wpa2_aes_auto_5g_conf = common_conf.wpa2_aes_auto_5g_conf
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa2_aes_auto_5g_conf, interface5g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa2_aes_auto_5g_conf, wlan0_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa2_aes_auto_5g_conf, wlan0_password))
        con = os.system('netsh wlan connect name=%s ssid=%s  interface=%s' % (wpa2_aes_auto_5g_conf, wlan0_ssid, interface5g))
        time.sleep(20)
        con_status = Wifi_con.wlan_5g_con_status()
        if con_status == 1:
            result = 1
            print("连接成功")
        elif con_status == 0:
            result = 0
            print("连接失败")
        else:
            result = -1
            print("表示网卡异常")
        # result = 1 表示连接成功，0 表示连接失败, -1表示网卡异常
        return result

class Internet_check:
    @staticmethod
    # 有线联网状态检查
    def internetwired_connect():
        # ping过程
        pingstatus_1 = os.system('ping www.baidu.com -S 192.168.127.201  -n 2')
        pingstatus_2 = os.system('ping 192.168.127.254 -S 192.168.127.201  -n 2')
        time.sleep(5)
        print("pingstatus_1=" + "%s" % (pingstatus_1))
        print("pingstatus_2=" + "%s" % (pingstatus_2))
        if pingstatus_1 == 0 and pingstatus_2 == 0:
            internet_status = 1
        else:
            os.system('netsh wlan delete profile *')
            internet_status = 0
        return internet_status

    @staticmethod
    # 5G联网状态检查
    def internet5g_connect():
        # ping过程
        pingstatus_1 = os.system('ping www.baidu.com -S 192.168.127.202  -n 2')
        pingstatus_2 = os.system('ping 192.168.127.254 -S 192.168.127.202  -n 2')
        time.sleep(5)
        print("pingstatus_1=" + "%s" % (pingstatus_1))
        print("pingstatus_2=" + "%s" % (pingstatus_2))
        if pingstatus_1 == 0 and pingstatus_2 == 0:
            internet_status = 1
        else:
            os.system('netsh wlan delete profile *')
            internet_status = 0
        return internet_status

    @staticmethod
    # 2.4G联网状态检查
    def internet2g_connect():
        # ping过程
        pingstatus_1 = os.system('ping www.baidu.com -S 192.168.127.203  -n 2')
        pingstatus_2 = os.system('ping 192.168.127.254 -S 192.168.127.203  -n 2')
        time.sleep(5)
        print("pingstatus_1=" + "%s" % (pingstatus_1))
        print("pingstatus_2=" + "%s" % (pingstatus_2))
        if pingstatus_1 == 0 and pingstatus_2 == 0:
            internet_status = 1
        else:
            os.system('netsh wlan delete profile *')
            internet_status = 0
        return internet_status


class Linkrate_check:

    @staticmethod
    # 无线协商速率检测
    def wifi_5g_linkrate():
        interface2g = common_conf.interface2g_1
        interface5g = common_conf.interface5g_1
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        time.sleep(20)
        a = os.popen('netsh wlan  show interfaces').readlines()
        time.sleep(5)
        b = list(filter(lambda x: '接收速率(Mbps)' in x, a))
        c = "".join(b)
        result = c[25:-1]
        print(result)
        return result

    @staticmethod
    def wifi_2g_linkrate():
        interface2g = common_conf.interface2g_1
        interface5g = common_conf.interface5g_1
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        time.sleep(20)
        a = os.popen('netsh wlan  show interfaces').readlines()
        time.sleep(5)
        b = list(filter(lambda x: '接收速率(Mbps)' in x, a))
        c = "".join(b)
        result = c[25:-1]
        print(result)
        return result

# ping网关检查
class Rate_test:
    @staticmethod
    # 有线联网状态检查
    def internetwired_tcprate(iperf_cmd):
        # 获取iperf路径，并且通过dos执行对应iperf语句
        local_path = os.path.dirname(os.path.abspath(__file__))
        print(iperf_cmd)
        cmd = 'cd/d  %s &\
               %s' % (local_path, iperf_cmd)
        list1 = str(os.popen("%s" % cmd).read())
        n = list1.count("\n")
        list2 = list1.split("\n")
        list3 = list2[n - 4]
        print(n)
        print(list2)
        print(list3)
        result = re.findall(".*MBytes  (.*) Mbits/sec.*", list3)
        for x in result:
            print("吞吐量测试结果为： %s" % x)
            b = float(x)
            result = b
        return result
        # x为吞吐量值

    @staticmethod
    # 5G联网状态检查
    def internet5g_tcprate(iperf_cmd):
        # 获取iperf路径，并且通过dos执行对应iperf语句
        local_path = os.path.dirname(os.path.abspath(__file__))
        print(iperf_cmd)
        cmd = 'cd/d  %s &\
               %s' % (local_path, iperf_cmd)
        list1 = str(os.popen("%s" % cmd).read())
        n = list1.count("\n")
        list2 = list1.split("\n")
        list3 = list2[n - 4]
        result = re.findall(".*MBytes  (.*) Mbits/sec.*", list3)
        for x in result:
            print("吞吐量测试结果为： %s" % x)
            b = float(x)
            result = b
        return result
        # x为吞吐量值

    @staticmethod
    # 2.4G联网状态检查
    def internet2g_tcprate(iperf_cmd):
        # 获取iperf路径，并且通过dos执行对应iperf语句
        local_path = os.path.dirname(os.path.abspath(__file__))
        print(iperf_cmd)
        cmd = 'cd/d  %s &\
               %s' % (local_path, iperf_cmd)
        list1 = str(os.popen("%s" % cmd).read())
        n = list1.count("\n")
        list2 = list1.split("\n")
        list3 = list2[n - 4]
        result = re.findall(".*MBytes  (.*) Mbits/sec.*", list3)
        for x in result:
            print("吞吐量测试结果为： %s" % x)
            b = float(x)
            result = b
        return result
        # x为吞吐量值

    @staticmethod
    # 有线联网状态检查
    def internetwired_udprate(iperf_cmd):
        # 获取iperf路径，并且通过dos执行对应iperf语句
        local_path = os.path.dirname(os.path.abspath(__file__))
        print(iperf_cmd)
        cmd = 'cd/d  %s &\
               %s' % (local_path, iperf_cmd)
        list1 = str(os.popen("%s" % cmd).read())
        n = list1.count("\n")
        list2 = list1.split("\n")
        list3 = list2[n - 4]
        a = re.findall(".*sec  (.*) MBytes.*", list3)
        for b in a:
            print("吞吐量测试结果为： %s" % b)
            x = float(b)
        c = re.findall(".* \((.*)\).*", list3)
        for d in c:
            print("吞吐量测试结果为： %s" % d)
            e = float(d.strip('%')) / 100.0
            print(type(e))
            y = 1 - e
        result = x * y
        return result
        # x为吞吐量值

    @staticmethod
    # 5G联网状态检查
    def internet5g_udprate(iperf_cmd):
        # 获取iperf路径，并且通过dos执行对应iperf语句
        local_path = os.path.dirname(os.path.abspath(__file__))
        print(iperf_cmd)
        cmd = 'cd/d  %s &\
               %s' % (local_path, iperf_cmd)
        list1 = str(os.popen("%s" % cmd).read())
        n = list1.count("\n")
        list2 = list1.split("\n")
        list3 = list2[n - 4]
        a = re.findall(".*sec  (.*) MBytes.*", list3)
        for b in a:
            print("吞吐量测试结果为： %s" % b)
            x = float(b)

        c = re.findall(".* \((.*)\).*", list3)
        for d in c:
            print("吞吐量测试结果为： %s" % d)
            e = float(d.strip('%')) / 100.0
            print(type(e))
            y = 1 - e
        result = x * y
        return result
        # x为吞吐量值

    @staticmethod
    # 2.4G联网状态检查
    def internet2g_udpprate(iperf_cmd):
        # 获取iperf路径，并且通过dos执行对应iperf语句
        local_path = os.path.dirname(os.path.abspath(__file__))
        print(iperf_cmd)
        cmd = 'cd/d  %s &\
               %s' % (local_path, iperf_cmd)
        list1 = str(os.popen("%s" % cmd).read())
        n = list1.count("\n")
        list2 = list1.split("\n")
        list3 = list2[n - 4]
        a = re.findall(".*sec  (.*) MBytes.*", list3)
        for b in a:
            print("吞吐量测试结果为： %s" % b)
            x = float(b)
        c = re.findall(".* \((.*)\).*", list3)
        for d in c:
            print("吞吐量测试结果为： %s" % d)
            e = float(d.strip('%')) / 100.0
            print(type(e))
            y = 1 - e
        result = x * y
        return result
        # x为吞吐量值


class Start_telnet():
    @staticmethod
    # 检测是否能访问路由器
    def ping_gateway():
        # ping过程
        pingstatus = os.system('ping mywifi.mercku.tech -n 2')
        print("pingstatus=" + "%s" % (pingstatus))
        if pingstatus == 0:
            reuslt = 1
        else:
            reuslt = 0
        return reuslt
        #  reuslt：0：连接路由器失败 1：连接路由器成功

    @staticmethod
    # 开启路由器telnet
    def open_telnet():
        # 先检测是否能开启telnet
        a = Start_telnet.ping_gateway()
        if a == 1:
            start_telnetstatus = str(
                requests.post(url="http://mywifi.mercku.tech/app", json={"method": "factory.start.telnetd"}))
            if start_telnetstatus.find("[200]") != -1:
                result = 1
                print("开启telnet成功")
            else:
                print("开启telnet失败")
                result = 0
        else:
            print("连接路由器失败")
            result = 0
        return result
        # result：0：开启telnet路由器失败 1：连接路由器成功


class Router_conf():
    @staticmethod
    # telnet获取/设置配置参数函数
    def do_telnet(host, username, telnet_password, command, exit):
        # Telnet远程登录：Windows客户端连接Linux服务器
        # 连接Telnet服务器
        tn = telnetlib.Telnet(host, port=23, timeout=10)
        tn.set_debuglevel(0)
        # 输入登录用户名
        tn.read_until(b"login: ", timeout=10)
        tn.write(username.encode('ascii') + b'\n')
        # 输入登录密码
        tn.read_until(b"Password: ", timeout=10)
        tn.write(telnet_password.encode('ascii') + b'\n')
        # 输入命令
        tn.read_until(b"#", timeout=10)
        tn.write(command.encode('ascii') + b'\n')
        time.sleep(1)
        text = tn.read_very_eager()
        text_string = text.decode()
        tn.read_until(b"#", timeout=10)
        tn.write(exit.encode('ascii') + b'\n')
        return text_string
        # 终止连接

    @staticmethod
    # 获取初始的长度
    def GetstartIndex(content, startStr):
        startIndex = content.index(startStr)
        if startIndex >= 0:
            startIndex += len(startStr)
        return startIndex


class Url_check:
    @staticmethod
    # 有线联网状态检查
    def internetwired_connect(black_url):
        # 通过request方式检测url是否能访问
        a = os.system('ipconfig /flushdns')
        i = 1
        while a != 0 and i < 5:
            print("清楚缓存失败")
            b = os.system('ipconfig /flushdns')
            i += 1
            print(i)
        else:
            print("执行http request")
            try:
                conn = http.client.HTTPConnection("%s" % black_url, source_address=("192.168.127.201", 0))
                conn.request("GET", "/")
                conn_status = conn.getresponse().status
                print(conn_status)
                if conn_status == 200 or conn_status == 301 or conn_status == 302:
                    print("可以访问")
                    result = 1
                else:
                    print("不可以正常访问")
                    result = 0
            except Exception as e:
                print("无法访问" + str(e))
                result = 0
        print(result)
        return result
        #  result：0：访问外网失败 1：表示访问外网成功

    @staticmethod
    # 5G联网状态检查
    def internet5g_connect(black_url):
        # 通过request方式检测url是否能访问
        a = os.system('ipconfig /flushdns')
        i = 1
        while a != 0 and i < 5:
            print("清楚缓存失败")
            b = os.system('ipconfig /flushdns')
            i += 1
            print(i)
        else:
            print("执行http request")
            try:
                conn = http.client.HTTPConnection("%s" % black_url, source_address=("192.168.127.202", 0))
                conn.request("GET", "/")
                conn_status = conn.getresponse().status
                print(conn_status)
                if conn_status == 200 or conn_status == 301 or conn_status == 302:
                    print("可以访问")
                    result = 1
                else:
                    print("不可以正常访问")
                    result = 0
            except Exception as e:
                print("无法访问" + str(e))
                result = 0
        print(result)
        return result
        #  result：0：访问外网失败 1：表示访问外网成功

    @staticmethod
    # 2.4G联网状态检查
    def internet2g_connect(black_url):
        # 通过ping检测
        # 通过request方式检测url是否能访问
        a = os.system('ipconfig /flushdns')
        i = 1
        while a != 0 and i < 5:
            print("清楚缓存失败")
            b = os.system('ipconfig /flushdns')
            i += 1
            print(i)
        else:
            print("执行http request")
            try:
                conn = http.client.HTTPConnection("%s" % black_url, source_address=("192.168.127.203", 0))
                conn.request("GET", "/")
                conn_status = conn.getresponse().status
                print(conn_status)
                if conn_status == 200 or conn_status == 301 or conn_status == 302:
                    print("可以访问")
                    result = 1
                else:
                    print("不可以正常访问")
                    result = 0
            except Exception as e:
                print("无法访问" + str(e))
                result = 0
        print(result)
        return result
        #  result：0：访问外网失败 1：表示访问外网成功

class Conf_networkcard:
    @staticmethod
    # 配置有线网卡1 IP
    def ipwired1_configure(internet_interface):
        a = os.system(
            'Netsh interface IP Set Addr "%s" Static 192.168.127.201 255.255.255.0 192.168.127.254 1' % internet_interface)
        b = os.system('Netsh interface IP Set dns "%s" static 192.168.127.254 primary' % internet_interface)
        if a == 0 and b == 0:
            reuslt = 1
        else:
            reuslt = 0
        return reuslt

    @staticmethod
    # 配置有线网卡2 IP
    def ipwired2_configure(internet_interface):
        a = os.system(
            'Netsh interface IP Set Addr "%s" Static 10.0.0.201 255.255.255.0 192.168.127.254 1' % internet_interface)
        b = os.system('Netsh interface IP Set dns "%s" static 10.0.0.1 primary' % internet_interface)
        if a == 0 and b == 0:
            reuslt = 1
        else:
            reuslt = 0
        return reuslt

    @staticmethod
    # 配置5G网卡1 IP
    def ip5g1_configure(internet_interface):
        a = os.system(
            'Netsh interface IP Set Addr "%s" Static 192.168.127.202 255.255.255.0 192.168.127.254 1' % internet_interface)
        b = os.system('Netsh interface IP Set dns "%s" static 192.168.127.254 primary' % internet_interface)
        if a == 0 and b == 0:
            reuslt = 1
        else:
            reuslt = 0
        return reuslt

    @staticmethod
    # 配置2.4G网卡1 IP
    def ip2g1_configure(internet_interface):
        a = os.system(
            'Netsh interface IP Set Addr "%s" Static 192.168.127.203 255.255.255.0 192.168.127.254 1' % internet_interface)
        b = os.system('Netsh interface IP Set dns "%s" static 192.168.127.254 primary' % internet_interface)
        if a == 0 and b == 0:
            reuslt = 1
        else:
            reuslt = 0
        return reuslt

    @staticmethod
    # 配置5G网卡2 IP
    def ip5g2_configure(internet_interface):
        a = os.system(
            'Netsh interface IP Set Addr "%s" Static 192.168.127.204 255.255.255.0 192.168.127.254 1' % internet_interface)
        b = os.system('Netsh interface IP Set dns "%s" static 192.168.127.254 primary' % internet_interface)
        if a == 0 and b == 0:
            reuslt = 1
        else:
            reuslt = 0
        return reuslt

    @staticmethod
    # 配置2G网卡2 IP
    def ip2g2_configure(internet_interface):
        a = os.system(
            'Netsh interface IP Set Addr "%s" Static 192.168.127.205 255.255.255.0 192.168.127.254 1' % internet_interface)
        b = os.system('Netsh interface IP Set dns "%s" static 192.168.127.254 primary' % internet_interface)
        if a == 0 and b == 0:
            reuslt = 1
        else:
            reuslt = 0
        return reuslt

    @staticmethod
    # 配置有线网卡1 IP
    def ipwired1_dhcp(internet_interface):
        a = os.system('Netsh interface IP Set Addr "%s"  dhcp' % internet_interface)
        if a == 0 :
            reuslt = 1
        else:
            reuslt = 0
        return reuslt

    @staticmethod
    # 配置有线网卡1 IP
    def ipwired2_dhcp(internet_interface):
        a = os.system('Netsh interface IP Set Addr "%s"  dhcp' % internet_interface)
        if a == 0 :
            reuslt = 1
        else:
            reuslt = 0
        return reuslt

    @staticmethod
    # 配置有线网卡1 IP
    def ip5g1_dhcp(internet_interface):
        a = os.system('Netsh interface IP Set Addr "%s"  dhcp' % internet_interface)
        if a == 0 :
            reuslt = 1
        else:
            reuslt = 0
        return reuslt

    @staticmethod
    # 配置有线网卡1 IP
    def ip5g2_dhcp(internet_interface):
        a = os.system('Netsh interface IP Set Addr "%s"  dhcp' % internet_interface)
        if a == 0 :
            reuslt = 1
        else:
            reuslt = 0
        return reuslt

    @staticmethod
    # 配置有线网卡1 IP
    def ip2g1_dhcp(internet_interface):
        a = os.system('Netsh interface IP Set Addr "%s"  dhcp' % internet_interface)
        if a == 0 :
            reuslt = 1
        else:
            reuslt = 0
        return reuslt

    @staticmethod
    # 配置有线网卡1 IP
    def ip2g2_dhcp(internet_interface):
        a = os.system('Netsh interface IP Set Addr "%s"  dhcp' % internet_interface)
        if a == 0 :
            reuslt = 1
        else:
            reuslt = 0
        return reuslt

    @staticmethod
    # 初始化无线网卡
    def interface_init(internet_interface):
        a = os.system('netsh wlan delete profile *')
        b = os.system('netsh interface set interface "%s" disabled' % internet_interface)
        if a == 0 and b == 0:
            reuslt = 1
        else:
            reuslt = 0
        return reuslt


class Static_dhcp_lease:

    @staticmethod
    # 查看某个mac对应的ip为多少？
    def read_networkcard_ip(interface_mac):
        list1 = ("".join(os.popen('ipconfig /all').readlines())).split(":\n")
        str0 = "".join(list(filter(lambda x: '%s' % interface_mac in x, list1)))
        print(type(str0))
        list2 = re.findall(".*IPv4 地址 . . . . . . . . . . . . : (.*)\(首选\).*", str0)
        print (list2)
        print ("xxxxxxxxxxxxxx")
        interface_ip = "".join(list2)
        print (interface_ip)
        print ("%s ip地址为%s"%(interface_mac,interface_ip))
        return interface_ip
