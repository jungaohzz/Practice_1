#所有的配置

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


