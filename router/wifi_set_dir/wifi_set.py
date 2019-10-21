import os
import time
import telnetlib
import requests
from . import wifi_set_conf


# ping网关检查
class Wifi_scan:
    @staticmethod
    # 是否能扫描到某个SSID
    def wlan0_status(wlan0_ssid):
        internet_interface_5g = wifi_set_conf.interface5g
        internet_interface_2g = wifi_set_conf.interface2g
        os.system('netsh interface set interface "%s" disabled' % internet_interface_2g)
        os.system('netsh interface set interface "%s" enabled' % internet_interface_5g)
        time.sleep(5)
        wifi_list = str(os.popen('netsh wlan show all').readlines())
        print (wifi_list)
        if wifi_list.find(wlan0_ssid) != -1:
            print("可以搜索到 SSID:" + wlan0_ssid)
            result = 1
        else:
            print("不可以搜索到 SSID:" + wlan0_ssid)
            result = 0
        return result

    @staticmethod
    # 是否能扫描到某个SSID
    def wlan1_status(wlan1_ssid):
        internet_interface_5g = wifi_set_conf.interface5g
        internet_interface_2g = wifi_set_conf.interface2g
        os.system('netsh interface set interface "%s" disabled' % internet_interface_5g)
        os.system('netsh interface set interface "%s" enabled' % internet_interface_2g)
        time.sleep(5)
        wifi_list = str(os.popen('netsh wlan show all').readlines())
        print (wifi_list)
        if wifi_list.find(wlan1_ssid) != -1:
            print("可以搜索到 SSID: " + wlan1_ssid)
            result = 1
        else:
            print("不可以搜索到 SSID: " + wlan1_ssid)
            result = 0
        return result

    @staticmethod
    # 某个SSID对应的BSSID列表
    def wlan0_ssid_scan(wlan0_ssid):
        internet_interface_5g = wifi_set_conf.interface5g
        internet_interface_2g = wifi_set_conf.interface2g
        os.system('netsh interface set interface "%s" enabled' % internet_interface_2g)
        os.system('netsh interface set interface "%s" enabled' % internet_interface_5g)
        time.sleep(10)
        os.system('netsh interface set interface "%s" disabled' % internet_interface_2g)
        os.system('netsh interface set interface "%s" enabled' % internet_interface_5g)
        time.sleep(5)
        a = os.popen('netsh wlan show all').readlines()
        print (a)
        b = "".join(a)
        c = b.split("\nSSID")
        d = list(filter(lambda x: '%s'% wlan0_ssid in x, c))
        print (d)
        print ("dddddddddddddddddddddddddddd")
        wlan0_list = "".join(d)
        if wlan0_list.strip() == "":
            print ("没有对应SSID")
            result = 0
        else:
            print ("有对应SSID")
            print (wlan0_list)
            result = wlan0_list
        print (result)
        return result

    @staticmethod
    # 某个SSID对应的BSSID列表
    def wlan1_ssid_scan(wlan1_ssid):
        internet_interface_5g = wifi_set_conf.interface5g
        internet_interface_2g = wifi_set_conf.interface2g
        os.system('netsh interface set interface "%s" enabled' % internet_interface_2g)
        os.system('netsh interface set interface "%s" enabled' % internet_interface_5g)
        time.sleep(10)
        os.system('netsh interface set interface "%s" disabled' % internet_interface_5g)
        os.system('netsh interface set interface "%s" enabled' % internet_interface_2g)
        time.sleep(5)
        a = os.popen('netsh wlan show all').readlines()
        print (a)
        b = "".join(a)
        c = b.split("\nSSID")
        d = list(filter(lambda x: '%s'% wlan1_ssid in x, c))
        wlan1_list = "".join(d)
        if wlan1_list.strip() == "":
            print ("没有对应SSID")
            result = 0
        else:
            print ("有对应SSID")
            result = wlan1_list
        print (result)
        return result

class Wifi_con:
    @staticmethod
    # 无线连接检测
    def wifi_5g_open_connect(wlan0_ssid):
        # 连接WIFI过程
        interface2g = wifi_set_conf.interface2g
        interface5g = wifi_set_conf.interface5g
        conf_path = wifi_set_conf.conf_path
        open_conf = wifi_set_conf.open_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(10)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, open_conf, interface5g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (open_conf, wlan0_ssid))
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(10)
        con_status = os.system('netsh wlan connect name=%s ssid=%s' % (open_conf, wlan0_ssid))
        if con_status == 0:
            result = 1
        else:
            result = 0
        # result = 1 表示连接成功，0 表示连接失败
        return result

    @staticmethod
    def wifi_5g_open_auto_connect(wlan0_ssid):
        # 连接WIFI过程
        interface2g = wifi_set_conf.interface2g
        interface5g = wifi_set_conf.interface5g
        conf_path = wifi_set_conf.conf_path
        open_auto_conf = wifi_set_conf.open_auto_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(10)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system(
            'netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, open_auto_conf, interface5g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (open_auto_conf, wlan0_ssid))
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(10)
        con_status = os.system('netsh wlan connect name=%s ssid=%s' % (open_auto_conf, wlan0_ssid))
        if con_status == 0:
            result = 1
        else:
            result = 0
        # result = 1 表示连接成功，0 表示连接失败
        return result

    @staticmethod
    # 无线连接检测
    def wifi_5g_wpa_tkip_connect(wlan0_ssid, wlan0_password):
        # 连接WIFI过程
        interface2g = wifi_set_conf.interface2g
        interface5g = wifi_set_conf.interface5g
        conf_path = wifi_set_conf.conf_path
        wpa_tkip_conf = wifi_set_conf.wpa_tkip_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(10)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa_tkip_conf, interface5g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa_tkip_conf, wlan0_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa_tkip_conf, wlan0_password))
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(10)
        con_status = os.system('netsh wlan connect name=%s ssid=%s' % (wpa_tkip_conf, wlan0_ssid))
        if con_status == 0:
            result = 1
        else:
            result = 0
        # result = 1 表示连接成功，0 表示连接失败
        return result

    @staticmethod
    # 无线连接检测
    def wifi_5g_wpa_tkip_auto_connect(wlan0_ssid, wlan0_password):
        # 连接WIFI过程
        interface2g = wifi_set_conf.interface2g
        interface5g = wifi_set_conf.interface5g
        conf_path = wifi_set_conf.conf_path
        wpa_tkip_auto_conf = wifi_set_conf.wpa_tkip_auto_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(10)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system(
            'netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa_tkip_auto_conf, interface5g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa_tkip_auto_conf, wlan0_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa_tkip_auto_conf, wlan0_password))

        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(10)
        con_status = os.system('netsh wlan connect name=%s ssid=%s' % (wpa_tkip_auto_conf, wlan0_ssid))
        if con_status == 0:
            result = 1
        else:
            result = 0
        # result = 1 表示连接成功，0 表示连接失败
        return result

    @staticmethod
    # 无线连接检测
    def wifi_5g_wpa_aes_connect(wlan0_ssid,wlan0_password):
        # 连接WIFI过程
        interface2g = wifi_set_conf.interface2g
        interface5g = wifi_set_conf.interface5g
        conf_path = wifi_set_conf.conf_path
        wpa_aes_conf = wifi_set_conf.wpa_aes_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(10)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa_aes_conf, interface5g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa_aes_conf, wlan0_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa_aes_conf, wlan0_password))

        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(10)
        con_status = os.system('netsh wlan connect name=%s ssid=%s' % (wpa_aes_conf, wlan0_ssid))
        if con_status == 0:
            result = 1
        else:
            result = 0
        # result = 1 表示连接成功，0 表示连接失败
        return result

    @staticmethod
    # 无线连接检测
    def wifi_5g_wpa_aes_auto_connect(wlan0_ssid, wlan0_password):
        # 连接WIFI过程
        interface2g = wifi_set_conf.interface2g
        interface5g = wifi_set_conf.interface5g
        conf_path = wifi_set_conf.conf_path
        wpa_aes_auto_conf = wifi_set_conf.wpa_aes_auto_conf
        wlan_password = wifi_set_conf.wlan_password
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(10)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system(
            'netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa_aes_auto_conf, interface5g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa_aes_auto_conf, wlan0_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa_aes_auto_conf, wlan0_password))

        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(10)
        con_status = os.system('netsh wlan connect name=%s ssid=%s' % (wpa_aes_auto_conf, wlan0_ssid))
        if con_status == 0:
            result = 1
        else:
            result = 0
        # result = 1 表示连接成功，0 表示连接失败
        return result

    @staticmethod
    # 无线连接检测
    def wifi_5g_wpa_tkip_connect(wlan0_ssid, wlan0_password):
        # 连接WIFI过程
        interface2g = wifi_set_conf.interface2g
        interface5g = wifi_set_conf.interface5g
        conf_path = wifi_set_conf.conf_path
        wpa_tkip_conf = wifi_set_conf.wpa_tkip_conf
        wlan_password = wifi_set_conf.wlan_password
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(10)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa_tkip_conf, interface5g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa_tkip_conf, wlan0_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa_tkip_conf, wlan0_password))
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(10)
        con_status = os.system('netsh wlan connect name=%s ssid=%s' % (wpa_tkip_conf, wlan0_ssid))
        time.sleep(10)
        if con_status == 0:
            result = 1
        else:
            result = 0
        # result = 1 表示连接成功，0 表示连接失败
        return result

    @staticmethod
    # 无线连接检测
    def wifi_5g_wpa2_aes_connect(wlan0_ssid, wlan0_password):
        # 连接WIFI过程
        interface2g = wifi_set_conf.interface2g
        interface5g = wifi_set_conf.interface5g
        conf_path = wifi_set_conf.conf_path
        wpa2_aes_conf = wifi_set_conf.wpa2_aes_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(20)
        print ("eeeeeeeeeeeee")
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa2_aes_conf, interface5g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa2_aes_conf, wlan0_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa2_aes_conf, wlan0_password))
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(10)
        con_status = os.system('netsh wlan connect name=%s ssid=%s' % (wpa2_aes_conf, wlan0_ssid))
        time.sleep(10)
        if con_status == 0:
            result = 1
        else:
            result = 0
        # result = 1 表示连接成功，0 表示连接失败
        return result

    @staticmethod
    # 无线连接检测
    def wifi_5g_wpa2_aes_auto_connect(wlan0_ssid, wlan0_password):
        # 连接WIFI过程
        interface2g = wifi_set_conf.interface2g
        interface5g = wifi_set_conf.interface5g
        conf_path = wifi_set_conf.conf_path
        wpa2_aes_auto_conf = wifi_set_conf.wpa2_aes_auto_conf
        wlan_password = wifi_set_conf.wlan_password
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(10)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system(
            'netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa2_aes_auto_conf, interface5g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa2_aes_auto_conf, wlan0_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa2_aes_auto_conf, wlan0_password))
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(10)
        con_status = os.system('netsh wlan connect name=%s ssid=%s' % (wpa2_aes_auto_conf, wlan0_ssid))
        time.sleep(10)

        if con_status == 0:
            result = 1
        else:
            result = 0
        # result = 1 表示连接成功，0 表示连接失败
        return result

    @staticmethod
    # 无线连接检测
    def wifi_2g_open_connect(wlan1_ssid):
        # 连接WIFI过程
        interface2g = wifi_set_conf.interface2g
        interface5g = wifi_set_conf.interface5g
        conf_path = wifi_set_conf.conf_path
        open_conf = wifi_set_conf.open_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(10)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, open_conf, interface2g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (open_conf, wlan1_ssid))
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        time.sleep(10)
        con_status = os.system('netsh wlan connect name=%s ssid=%s' % (open_conf, wlan1_ssid))
        if con_status == 0:
            result = 1
        else:
            result = 0
        # result = 1 表示连接成功，0 表示连接失败
        return result

    @staticmethod
    def wifi_2g_open_auto_connect(wlan1_ssid):
        # 连接WIFI过程
        interface2g = wifi_set_conf.interface2g
        interface5g = wifi_set_conf.interface5g
        conf_path = wifi_set_conf.conf_path
        open_auto_conf = wifi_set_conf.open_auto_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(10)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system(
            'netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, open_auto_conf, interface2g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (open_auto_conf, wlan1_ssid))
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        time.sleep(10)
        con_status = os.system('netsh wlan connect name=%s ssid=%s' % (open_auto_conf, wlan1_ssid))
        if con_status == 0:
            result = 1
        else:
            result = 0
        # result = 1 表示连接成功，0 表示连接失败
        return result

    @staticmethod
    # 无线连接检测
    def wifi_2g_wpa_tkip_connect(wlan1_ssid, wlan1_password):
        # 连接WIFI过程
        interface2g = wifi_set_conf.interface2g
        interface5g = wifi_set_conf.interface5g
        conf_path = wifi_set_conf.conf_path
        wpa_tkip_conf = wifi_set_conf.wpa_tkip_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(10)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa_tkip_conf, interface2g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa_tkip_conf, wlan1_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa_tkip_conf, wlan1_password))

        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        time.sleep(10)
        con_status = os.system('netsh wlan connect name=%s ssid=%s' % (wpa_tkip_conf, wlan1_ssid))
        if con_status == 0:
            result = 1
        else:
            result = 0
        # result = 1 表示连接成功，0 表示连接失败
        return result

    @staticmethod
    # 无线连接检测
    def wifi_2g_wpa_tkip_auto_connect(wlan1_ssid, wlan1_password):
        # 连接WIFI过程
        interface2g = wifi_set_conf.interface2g
        interface5g = wifi_set_conf.interface5g
        conf_path = wifi_set_conf.conf_path
        wpa_tkip_auto_conf = wifi_set_conf.wpa_tkip_auto_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(10)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system(
            'netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa_tkip_auto_conf, interface2g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa_tkip_auto_conf, wlan1_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa_tkip_auto_conf, wlan1_password))

        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        time.sleep(10)
        con_status = os.system('netsh wlan connect name=%s ssid=%s' % (wpa_tkip_auto_conf, wlan1_ssid))
        if con_status == 0:
            result = 1
        else:
            result = 0
        # result = 1 表示连接成功，0 表示连接失败
        return result

    @staticmethod
    # 无线连接检测
    def wifi_2g_wpa_aes_connect(wlan1_ssid, wlan1_password):
        # 连接WIFI过程
        interface2g = wifi_set_conf.interface2g
        interface5g = wifi_set_conf.interface5g
        conf_path = wifi_set_conf.conf_path
        wpa_aes_conf = wifi_set_conf.wpa_aes_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(10)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa_aes_conf, interface2g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa_aes_conf, wlan1_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa_aes_conf, wlan1_password))

        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        time.sleep(10)
        con_status = os.system('netsh wlan connect name=%s ssid=%s' % (wpa_aes_conf, wlan1_ssid))
        if con_status == 0:
            result = 1
        else:
            result = 0
        # result = 1 表示连接成功，0 表示连接失败
        return result

    @staticmethod
    # 无线连接检测
    def wifi_2g_wpa_aes_auto_connect(wlan1_ssid, wlan1_password):
        # 连接WIFI过程
        interface2g = wifi_set_conf.interface2g
        interface5g = wifi_set_conf.interface5g
        conf_path = wifi_set_conf.conf_path
        wpa_aes_auto_conf = wifi_set_conf.wpa_aes_auto_conf
        wlan_password = wifi_set_conf.wlan_password
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(10)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system(
            'netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa_aes_auto_conf, interface2g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa_aes_auto_conf, wlan1_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa_aes_auto_conf, wlan1_password))

        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        time.sleep(10)
        con_status = os.system('netsh wlan connect name=%s ssid=%s' % (wpa_aes_auto_conf, wlan1_ssid))
        if con_status == 0:
            result = 1
        else:
            result = 0
        # result = 1 表示连接成功，0 表示连接失败
        return result

    @staticmethod
    # 无线连接检测
    def wifi_2g_wpa_tkip_connect(wlan1_ssid, wlan1_password):
        # 连接WIFI过程
        interface2g = wifi_set_conf.interface2g
        interface5g = wifi_set_conf.interface5g
        conf_path = wifi_set_conf.conf_path
        wpa_tkip_conf = wifi_set_conf.wpa_tkip_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(10)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa_tkip_conf, interface2g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa_tkip_conf, wlan1_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa_tkip_conf, wlan1_password))
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        time.sleep(10)
        con_status = os.system('netsh wlan connect name=%s ssid=%s' % (wpa_tkip_conf, wlan1_ssid))
        if con_status == 0:
            result = 1
        else:
            result = 0
        # result = 1 表示连接成功，0 表示连接失败
        return result

    @staticmethod
    # 无线连接检测
    def wifi_2g_wpa2_aes_connect(wlan1_ssid, wlan1_password):
        # 连接WIFI过程
        interface2g = wifi_set_conf.interface2g
        interface5g = wifi_set_conf.interface5g
        conf_path = wifi_set_conf.conf_path
        wpa2_aes_conf = wifi_set_conf.wpa2_aes_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(10)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa2_aes_conf, interface2g))
        a = 'netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa2_aes_conf, interface2g)
        print ("aaaaaaaaaaaaaaaaa%s"%a)
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa2_aes_conf, wlan1_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa2_aes_conf, wlan1_password))
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        time.sleep(10)
        con_status = os.system('netsh wlan connect name=%s ssid=%s' % (wpa2_aes_conf, wlan1_ssid))
        time.sleep(10)
        print("@#@#@#")
        print(con_status)
        if con_status == 0:
            result = 1
        else:
            result = 0
        # result = 1 表示连接成功，0 表示连接失败
        return result

    @staticmethod
    # 无线连接检测
    def wifi_2g_wpa2_aes_auto_connect(wlan1_ssid, wlan1_password):
        # 连接WIFI过程
        interface2g = wifi_set_conf.interface2g
        interface5g = wifi_set_conf.interface5g
        conf_path = wifi_set_conf.conf_path
        wpa2_aes_auto_conf = wifi_set_conf.wpa2_aes_auto_conf
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(10)
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        os.system(
            'netsh wlan add profile filename="%s%s.xml" interface="%s"' % (conf_path, wpa2_aes_auto_conf, interface2g))
        os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wpa2_aes_auto_conf, wlan1_ssid))
        os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wpa2_aes_auto_conf, wlan1_password))
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        time.sleep(10)
        con_status = os.system('netsh wlan connect name=%s ssid=%s' % (wpa2_aes_auto_conf, wlan1_ssid))
        time.sleep(10)

        if con_status == 0:
            result = 1
        else:
            result = 0
        # result = 1 表示连接成功，0 表示连接失败
        return result


    @staticmethod
    def wifi_connectstatus(configure_path, wlan_configure, internet_interface, wlan_password, wlan_ssid):
        # 连接WIFI过程
        if wlan_configure == "openconfigure" or wlan_configure == "openautoconfigure":
            os.system('netsh wlan delete profile *')
            os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (
                configure_path, wlan_configure, internet_interface))
            os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wlan_configure, wlan_ssid))
            os.system('netsh interface set interface "%s" disabled' % internet_interface)
            os.system('netsh interface set interface "%s" enabled' % internet_interface)
            time.sleep(10)
            connect_status = os.system('netsh wlan connect name=%s ssid=%s' % (wlan_configure, wlan_ssid))
        else:
            os.system('netsh wlan delete profile *')
            os.system('netsh wlan add profile filename="%s%s.xml" interface="%s"' % (
                configure_path, wlan_configure, internet_interface))
            os.system('netsh wlan set profileparameter name=%s SSIDname=%s' % (wlan_configure, wlan_ssid))
            os.system('netsh wlan set profileparameter name=%s keyMaterial=%s' % (wlan_configure, wlan_password))
            os.system('netsh interface set interface "%s" disabled' % internet_interface)
            os.system('netsh interface set interface "%s" enabled' % internet_interface)
            time.sleep(10)
            connect_status = os.system('netsh wlan connect name=%s ssid=%s' % (wlan_configure, wlan_ssid))
        time.sleep(5)
        if connect_status == 0:
            wificon_status = 1
            print("wifi_connect=" + "%s" % (connect_status))
        else:
            wificon_status = 0
            os.system('netsh wlan delete profile *')
        return wificon_status


class Internet_check:
    @staticmethod
    # 有线联网状态检查
    def internetwired_connect():
        # ping过程
        pingstatus_1 = os.system('ping www.baidu.com -S 192.168.127.8  -n 2')
        pingstatus_2 = os.system('ping 192.168.127.254 -S 192.168.127.8  -n 2')
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
        pingstatus_1 = os.system('ping www.baidu.com -S 192.168.127.18  -n 2')
        pingstatus_2 = os.system('ping 192.168.127.254 -S 192.168.127.18  -n 2')
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
        pingstatus_1 = os.system('ping www.baidu.com -S 192.168.127.28  -n 2')
        pingstatus_2 = os.system('ping 192.168.127.254 -S 192.168.127.28  -n 2')
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
        interface2g = wifi_set_conf.interface2g
        interface5g = wifi_set_conf.interface5g
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(10)
        os.system('netsh interface set interface "%s" disabled' % interface2g)
        time.sleep(10)
        a = os.popen('netsh wlan  show interfaces').readlines()
        time.sleep(5)
        b = list(filter(lambda x: '接收速率(Mbps)' in x, a))
        c = "".join(b)
        result = c[25:-1]
        print(result)
        return result

    @staticmethod
    def wifi_2g_linkrate():
        interface2g = wifi_set_conf.interface2g
        interface5g = wifi_set_conf.interface5g
        os.system('netsh interface set interface "%s" enabled' % interface2g)
        os.system('netsh interface set interface "%s" enabled' % interface5g)
        time.sleep(10)
        os.system('netsh interface set interface "%s" disabled' % interface5g)
        time.sleep(10)
        a = os.popen('netsh wlan  show interfaces').readlines()
        time.sleep(5)
        b = list(filter(lambda x: '接收速率(Mbps)' in x, a))
        c = "".join(b)
        result = c[25:-1]
        print(result)
        return result

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
        return text_string
        # 终止连接
        tn.read_until(b"#", timeout=10)
        tn.write(exit.encode('ascii') + b'\n')

    @staticmethod
    # 获取初始的长度
    def GetstartIndex(content, startStr):
        startIndex = content.index(startStr)
        if startIndex >= 0:
            startIndex += len(startStr)
        return startIndex


class Conf_networkcard:
    @staticmethod
    # 配置有线网卡IP
    def ipwired_configure(internet_interface):
        os.system(
            'Netsh interface IP Set Addr "%s" Static 192.168.127.201 255.255.255.0 192.168.127.254 1' % internet_interface)
        os.system('Netsh interface IP Set dns "%s" static 192.168.127.254 primary' % internet_interface)

    @staticmethod
    # 配置5G网卡IP
    def ip5g_configure(internet_interface):
        os.system(
            'Netsh interface IP Set Addr "%s" Static 192.168.127.202 255.255.255.0 192.168.127.254 1' % internet_interface)
        os.system('Netsh interface IP Set dns "%s" static 192.168.127.254 primary' % internet_interface)

    @staticmethod
    # 配置2.4G网卡IP
    def ip2g_configure(internet_interface):
        os.system(
            'Netsh interface IP Set Addr "%s" Static 192.168.127.203 255.255.255.0 192.168.127.254 1' % internet_interface)
        os.system('Netsh interface IP Set dns "%s" static 192.168.127.254 primary' % internet_interface)

    @staticmethod
    # 初始化无线网卡
    def interface_init(internet_interface1, internet_interface2):
        os.system('netsh wlan delete profile *')
        os.system('netsh interface set interface "%s" disabled' % internet_interface1)
        os.system('netsh interface set interface "%s" disabled' % internet_interface2)
        os.system('netsh interface set interface "%s" enabled' % internet_interface1)
