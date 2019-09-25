import os
import sys
import time

#===========================================================================
"""开启TELNET进程参数"""
url ="http://mywifi.mercku.tech/app"
data = {"method": "factory.start.telnetd"}

#===========================================================================
"""登录TELNET相关参数"""
host = "mywifi.mercku.tech"
username = "root"
telnet_password = "123456789"
exit = "exit"
#===========================================================================
"""WIFI测试相关参数"""
configurepath = ".\cfg\\"
openconfigure = "open"
openautoconfigure = "open-auto"
wpatkipconfigure = "wpa-tkip"
wpatkipautoconfigure = "wpa-tkip-auto"
wpaaesconfigure = "wpa-aes"
wpaaesautoconfigure = "wpa-aes-auto"
wpa2aesconfigure = "wpa2-aes"
wpa2aesautoconfigure = "wpa2-aes-auto"
interface5g = "WLAN5G"
interface2g = "WLAN24G"
get_5g_SSID_commad = "flash get WLAN0_SSID"
get_2g_SSID_commad = "flash get WLAN1_SSID"
get_5g_ENCRYPT_commad = "flash get WLAN0_ENCRYPT"
get_2g_ENCRYPT_commad = "flash get WLAN1_ENCRYPT"
get_5g_PSK_commad = "flash get WLAN0_WPA_PSK"
get_2g_PSK_commad = "flash get WLAN1_WPA_PSK"
get_5g_HIDDEN_commad = "flash get WLAN0_HIDDEN_SSID"
get_2g_HIDDEN_commad = "flash get WLAN1_HIDDEN_SSID"
get_5g_guest_SSID_commad = "flash get WLAN0_VAP0_SSID"
get_2g_guest_SSID_commad = "flash get WLAN1_VAP0_SSID"
get_5g_guest_ENCRYPT_commad = "flash get WLAN1_VAP0_ENCRYPT"
get_2g_guest_ENCRYPT_commad = "flash get WLAN1_VAP0_ENCRYPT"
get_5g_guest_PSK_commad = "flash get WLAN1_VAP0_WPA_PSK"
get_2g_guest_PSK_commad = "flash get WLAN1_VAP0_WPA_PSK"

#===========================================================================
"""MAC/IP绑定测试相关参数"""
static_mac = "1c1b0dbb8eb5"
static_ip = "192.168.127.112"
static_name = "DESKTOP-M47"
get_list_commad = "flash get DHCPRSVDIP_TBL"
get_staticlease_commad = "cat /var/udhcpd.conf  |grep static_lease"
static_mac_info = "物理地址. . . . . . . . . . . . . : 1C-1B-0D-BB-8E-B5"
next_adaptor_info = "无线局域网适配器 本地连接* 16"
static_ip_info = "IPv4 地址 . . . . . . . . . . . . : 192.168.127.112"
#===========================================================================
"""设备黑名单测试相关参数"""
get_blacklist_commad = "cat /etc/config/mac_filter_black"
#===========================================================================
"""有线设备"""
interfacewireless = "WIRED"
#===========================================================================
"""获取VPN相关参数"""
get_vpn_list_num = " cat etc/config/vpn  | grep  \"option valid '1'\"  | wc -l"
get_vpn_list = "cat etc/config/vpn"
#===========================================================================
"""获取VPN相关参数"""
set_sys_time_true = "date -s \"2018-4-9 15:00:00\""
set_sys_time_false = "date -s \"2018-4-10 15:00:00\""
#===========================================================================


