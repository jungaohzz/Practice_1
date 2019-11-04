
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
"""网卡相关配置信息"""
interface5g_1 = "WLAN5G1"
interface2g_1 = "WLAN2G1"
interface5g_2 = "WLAN5G2"
interface2g_2 = "WLAN2G2"
interfacewired_1 = "WIRED1"
interfacewired_2 = "WIRED2"
#===========================================================================
"""WIFI测试相关参数"""
#conf_path = ".\\router\common_dir\wifi_conf\\"
conf_path = ".\wifi_conf\\"
open_conf = "open"
open_auto_conf = "open-auto"
wpa_tkip_conf = "wpa-tkip"
wpa_tkip_auto_conf = "wpa-tkip-auto"
wpa_aes_conf = "wpa-aes"
wpa_aes_auto_conf = "wpa-aes-auto"
wpa2_aes_conf = "wpa2-aes"
wpa2_aes_auto_conf = "wpa2-aes-auto"
wpa2_aes_auto_5g_conf = "wpa2-aes-auto-5g"
wpa2_aes_auto_2g_conf = "wpa2-aes-auto-2g"
#===========================================================================
"""主WIFI 初始化数据"""
ssid_5g = "MERCKU-AutoTest-5G"
ssid_2g = "MERCKU-AutoTest"
mac_5g = "f8:27:2e:01:0e:eb"
mac_2g = "f8:27:2e:01:0e:e8"
wlan_password = "11111111"
#===========================================================================
"""主WIFI修改数据"""
ssid_5g_23b = "MERCKU-LEIGE12345678-5G"
ssid_2g_20b = "MERCKU-LEIGE12345678"
wlan_password_24b = "abcdABCD....123456789012"
ssid_5g_change = "MERCKU-LEIGE-CHANGE-5G"
ssid_2g_change = "MERCKU-LEIGE-CHANGE"
wlan_password_change = "abcdABCD....change"
ssid_5g_1b = "M-5G"
ssid_2g_1b = "M"
wlan_password_8b = "abCD12.."
#===========================================================================
"""Guest wifi初始化数据"""
guest_ssid_5g = "MERCKU-Auto-Guest-5G"
guest_ssid_2g = "MERCKU-Auto-Guest"
guest_mac_5g = "f8:27:2e:01:0e:ec"
guest_mac_2g = "f8:27:2e:01:0e:ed"
guest_wlan_password = "1234guestpassword"
#===========================================================================
"""访客WIFI修改数据"""
guest_ssid_5g_23b = "MERCKU-Guest12345678-5G"
guest_ssid_2g_20b = "MERCKU-Guest12345678"
guest_wlan_password_24b = "ABCDabcd....123456789010"
guset_ssid_5g_change = "MERCKU-GUEST-CHANGE-5G"
guest_ssid_2g_change = "MERCKU-GUEST-CHANGE"
guest_wlan_password_change = "ABCCabcd....change"
guest_ssid_5g_1b = "A-5G"
guest_ssid_2g_1b = "A"
guest_wlan_password_8b = "Abcd12.."
#===========================================================================
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
"""MAC/IP绑定测试相关参数和设备黑名单测试相关参数"""
wired1_mac = "B4-2E-99-51-8A-FA"
wired2_mac = "08-10-7A-05-9C-70"
wlan5g_mac = "08-10-7A-05-9C-71"
wlan2g_mac = "08-10-7A-05-9C-72"
static_ip1 = "192.168.127.160"
static_ip2 = "192.168.127.161"
static_ip3 = "192.168.127.162"
#===========================================================================
get_blacklist_commad = "cat /etc/config/mac_filter_black"
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
udp_wired_servertoclient = "iperf3 -u  -B 192.168.127.201 -c 10.70.100.183 -R -b  30M -t 10"
udp_wired_clienttoserver = "iperf3 -u  -B 192.168.127.201 -c 10.70.100.183 -b 30M -t 10"
tcp_wired_servertoclient = "iperf3 -B 192.168.127.201 -c 10.70.100.183 -R -b 30M -t 10"
tcp_wired_clienttoserver = "iperf3 -B 192.168.127.201 -c 10.70.100.183 -b 30M -t 10"
udp_2g_servertoclient = "iperf3 -u  -B 192.168.127.201 -c 10.70.100.183 -R -b 30M -t 10"
udp_2g_clienttoserver = "iperf3 -u  -B 192.168.127.201 -c 10.70.100.183 -b 30M -t 10"
tcp_2g_servertoclient = "iperf3 -B 192.168.127.201 -c 10.70.100.183 -R -b 30M -t 10"
tcp_2g_clienttoserver = "iperf3 -B 192.168.127.201 -c 10.70.100.183 -b 30M -t 10"
udp_5g_servertoclient = "iperf3 -u  -B 192.168.127.202 -c 10.70.100.183 -R -b 30M -t 10"
udp_5g_clienttoserver = "iperf3 -u  -B 192.168.127.202 -c 10.70.100.183 -b 30M -t 10"
tcp_5g_servertoclient = "iperf3 -B 192.168.127.202 -c 10.70.100.183 -R 30M -t 10"
tcp_5g_clienttoserver = "iperf3 -B 192.168.127.202 -c 10.70.100.183 -b 30M -t 10"
rata_upload_1 = 500 #500KB
rata_download_1 = 500 #500KB
rata_upload_2 = 1000 #1000KB
rata_download_2 = 1000 #1000KB
rata_upload_3 = 1500 #1500KB
rata_download_3 = 1500 #1500KB
rata_upload_4 = 2000 #2000KB
rata_download_4 = 2000 #2000KB
#===========================================================================

