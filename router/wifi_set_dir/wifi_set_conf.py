
#===========================================================================
"""开启TELNET进程参数"""
url ="http://mywifi.mercku.tech/app"
data = {"method": "factory.start.telnetd"}

#===========================================================================
"""登录TELNET相关参数"""
host = "mywifi.mercku.tech"
username = "root"
telnet_password = "11111111"
exit = "exit"
#===========================================================================
"""WIFI测试相关参数"""
conf_path = ".\\router\wifi_set_dir\wifi_conf\\"
open_conf = "open"
open_auto_conf = "open-auto"
wpa_tkip_conf = "wpa-tkip"
wpa_tkip_auto_conf = "wpa-tkip-auto"
wpa_aes_conf = "wpa-aes"
wpa_aes_auto_conf = "wpa-aes-auto"
wpa2_aes_conf = "wpa2-aes"
wpa2_aes_auto_conf = "wpa2-aes-auto"
interface5g = "WLAN5G1"
interface2g = "WLAN2G1"
# ssid_5g = "MerckLEI-5G"
# ssid_2g = "MerckLEI"
ssid_5g = "MERCKU-AutoTest-5G"
ssid_2g = "MERCKU-AutoTest"
mac_5g = "f8:27:2e:01:0e:eb"
mac_2g = "f8:27:2e:01:0e:e8"
wlan_password = "11111111"
wlan_vap_password = "11111111"

ssid_5g_23b = "MERCKU-LEIGE12345678-5G"
ssid_2g_20b = "MERCKU-LEIGE12345678"
wlan_password_24b = "abcdABCD....123456789012"
wlan_vap_password_24b = "ABCDabcd....123456789012"

ssid_5g_change = "MERCKU-LEIGE-CHANGE-5G"
ssid_2g_change = "MERCKU-LEIGE-CHANGE"
wlan_password_change = "abcdABCD....change"
wlan_vap_password_change = "ABCDabcd....change"


ssid_5g_1b = "M-5G"
ssid_2g_1b = "M"
wlan_password_8b = "abCD12.."
wlan_vap_password_8b = "ABcd12.."

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
"""限时相关配置"""
#周一
set_sys_time_mon = "date -s \"2019-10-7 15:00:00\""
#周二
set_sys_time_tue ="date -s \"2019-10-8 15:00:00\""
#周三
set_sys_time_wed = "date -s \"2019-10-9 15:00:00\""
#周四
set_sys_time_thu = "date -s \"2019-10-10 15:00:00\""
#周五
set_sys_time_fri ="date -s \"2019-10-11 15:00:00\""
#周六
set_sys_time_sat = "date -s \"2019-10-12 15:00:00\""
#周日
set_sys_time_sun = "date -s \"2019-10-13 15:00:00\""
#===========================================================================
"""网址黑名单限制相关条目"""
baidu_url1 = "www.baidu.com"
baidu_url2 = "news.baidu.com"
baidu_url3 = "jingyan.baidu.com"
baidu_url4 = "tieba.baidu.com"
jd_url1 = "www.jd.com"
jd_url2 = "jiadian.jd.com"
jd_url3 = "beauty.jd.com"
jd_url4 = "passport.jd.com"
#===========================================================================
"""限速相关配置"""
udp_wired_servertoclient = "iperf -u  -B 192.168.127.201 -c 10.70.100.182 -R -b  100M -t 3"
udp_wired_clienttoserver = "iperf -u  -B 192.168.127.201 -c 10.70.100.182 -b 100M -t 3"
tcp_wired_servertoclient = "iperf -B 192.168.127.201 -c 10.70.100.182 -R -b 100M -t 3"
tcp_wired_clienttoserver = "iperf -B 192.168.127.201 -c 10.70.100.182 -b 100M -t 3"

udp_2g_servertoclient = "iperf -u  -B 192.168.127.201 -c 10.70.100.182 -R -b 100M -t 3"
udp_2g_clienttoserver = "iperf -u  -B 192.168.127.201 -c 10.70.100.182 -b 100M -t 3"
tcp_2g_servertoclient = "iperf -B 192.168.127.201 -c 10.70.100.182 -R -b 100M -t 3"
tcp_2g_clienttoserver = "iperf -B 192.168.127.201 -c 10.70.100.182 -b 100M -t 3"

udp_5g_servertoclient = "iperf -u  -B 192.168.127.202 -c 10.70.100.182 -R -b 100M -t 3"
udp_5g_clienttoserver = "iperf -u  -B 192.168.127.202 -c 10.70.100.182 -b 100M -t 3"
tcp_5g_servertoclient = "iperf -B 192.168.127.202 -c 10.70.100.182 -R 100M -t 3"
tcp_5g_clienttoserver = "iperf -B 192.168.127.202 -c 10.70.100.182 -b 100M -t 3"
#===========================================================================

