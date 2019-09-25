import os
import time
import telnetlib

#开启路由器telnet
def start_telnet(mercku_url,telnet_data ):
    start_telnetstatus = str(requests.post(url=mercku_url, data=telnet_data))
    if start_telnetstatus.find("[200]") == -1:
        telnet_status = 0
    else:
        telnet_status = 1
    return telnet_status

#telnet获取配置参数函数
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

#获取字段
def GetstartIndex(content, startStr):
    '''获取初始的长度'''
    startIndex = content.index(startStr)
    if startIndex >= 0:
        startIndex += len(startStr)
    return startIndex

#获取 黑名单列表
def get_black_list(host, username, telnet_password, get_blacklist_command, exit):
    list1 = do_telnet(host, username, telnet_password, get_blacklist_command, exit)
    list2 = list1.split("config sta")
    black_totalnum = len(list2) - 1
    black_list = list2[1:black_totalnum]
    return  black_list ,black_totalnum

#获取 SSID
def get_ssid(host, username, telnet_password, get_ssid_command, exit):
    startStr = 'SSID="' #startStr字符
    get_ssid = do_telnet(host, username, telnet_password, get_ssid_command, exit)
    Startlen = GetstartIndex(get_ssid,startStr)
    SSID = get_ssid[Startlen:-5]
    return SSID

#获取 ENCRYPT
def get_encrypt(host, username, telnet_password, get_encrypt_command, exit):
    startStr = 'ENCRYPT=' #startStr字符
    get_encrypt = do_telnet(host, username, telnet_password, get_encrypt_command, exit)
    Startlen = GetstartIndex(get_encrypt,startStr)
    ENCRYPT= int(get_encrypt[Startlen:-3])
    return ENCRYPT

# 获取 无线密码
def get_psk(host, username, telnet_password, get_psk_command, exit):
    startStr = 'WPA_PSK="' #startStr字符
    get_psk = do_telnet(host, username, telnet_password, get_psk_command, exit)
    Startlen = GetstartIndex(get_psk,startStr)
    PSK= get_psk[Startlen:-5]
    return PSK

# 获取 HIDDEN
def get_hidden(host, username, telnet_password, get_hidden_command, exit):
    startStr = 'HIDDEN_SSID=' #startStr字符
    get_hidden = do_telnet(host, username, telnet_password, get_hidden_command, exit)
    Startlen = GetstartIndex(get_hidden,startStr)
    HIDDEN = int(get_hidden[Startlen:-3])
    return  HIDDEN

#获取 设备黑名单
def get_black_list(host, username, telnet_password, get_black_list_command, exit):
    list1 = do_telnet(host, username, telnet_password, get_black_list_command, exit)
    list2 = list1.split("config sta")
    len_list2 = len(list2)
    black_num = len_list2 - 1
    black_list = list2[1:len_list2]
    return  black_list ,black_num

#获取 admin 密码
def get_admin_password(host, username, telnet_password, get_admin_password_command, exit):
    startStr = 'PASSWORD="'
    get_admin_password = do_telnet(host, username, telnet_password, get_admin_password_command, exit)
    Startlen = GetstartIndex(get_admin_password,startStr)
    admin_password = get_admin_password[Startlen:-5]
    return admin_password

#获取 root 密码
def get_root_password(host, username, telnet_password, get_root_password_command, exit):
    startStr = 'PASSWORD="'
    get_root_password = do_telnet(host, username, telnet_password, get_root_password_command, exit)
    Startlen = GetstartIndex(get_root_password,startStr)
    root_password = get_root_password[Startlen:-5]
    return root_password

#获取 系统时区
def get_ntp_timezone(host, username, telnet_password, get_ntp_timezone_command, exit):
    startStr = 'TIMEZONE="'
    get_ntp_timezone = do_telnet(host, username, telnet_password, get_ntp_timezone_command, exit)
    Startlen = GetstartIndex(get_ntp_timezone,startStr)
    timezone = get_ntp_timezone[Startlen:-5]
    return timezone

#获取 端口转发列表
def get_portfw_list(host, username, telnet_password, get_portfw_list_command, exit):
    list1 = do_telnet(host, username, telnet_password, get_portfw_list_command, exit)
    list2 = list1.split("\r\n")
    list_len = len(list2)
    portfw_list = list2[1:list_len - 1]
    return  portfw_list

#获取 端口转发列表数量
def get_portfw_list_num(host, username, telnet_password, get_portfw_list_num_command, exit):
    startStr = 'PORTFW_TBL_NUM='
    get_portfw_list_num = do_telnet(host, username, telnet_password, get_portfw_list_num_command, exit)
    Startlen = GetstartIndex(get_portfw_list_num,startStr)
    portfw_list_num = int(get_portfw_list_num[Startlen:-4])
    return portfw_list_num

#获取 DMZ开关状态
def get_dmz_status(host, username, telnet_password, get_dmz_status_command, exit):
    startStr = 'ENABLED='
    get_dmz_status = do_telnet(host, username, telnet_password, get_dmz_status_command, exit)
    Startlen = GetstartIndex(get_dmz_status,startStr)
    dmz_status = int(get_dmz_status[Startlen:-4])
    return dmz_status

#获取 DMZ主机地址
def get_dmz_host(host, username, telnet_password, get_dmz_host_command, exit):
    startStr = 'DMZ_HOST='
    get_dmz_host = do_telnet(host, username, telnet_password, get_dmz_host_command, exit)
    Startlen = GetstartIndex(get_dmz_host,startStr)
    dmz_host = get_dmz_host[Startlen:-4]
    return dmz_host

#获取 LAN IP配置地址
def get_lan_ip(host, username, telnet_password, get_lan_ip_command, exit):
    startStr = 'IP_ADDR='
    get_lan_ip = do_telnet(host, username, telnet_password, get_lan_ip_command, exit)
    Startlen = GetstartIndex(get_lan_ip,startStr)
    lan_ip = get_lan_ip[Startlen:-4]
    return lan_ip

#获取 DHCP地址池配置开始IP
def get_dhcppool_start(host, username, telnet_password, get_dhcppool_start_command, exit):
    startStr = 'START='
    get_dhcppool_start = do_telnet(host, username, telnet_password, get_dhcppool_start_command, exit)
    Startlen = GetstartIndex(get_dhcppool_start,startStr)
    dhcppool_start = get_dhcppool_start[Startlen:-4]
    return dhcppool_start

#获取 DHCP地址池配置结束IP
def get_dhcppool_end(host, username, telnet_password, get_dhcppool_end_command, exit):
    startStr = 'END='
    get_dhcppool_end = do_telnet(host, username, telnet_password, get_dhcppool_end_command, exit)
    Startlen = GetstartIndex(get_dhcppool_end,startStr)
    dhcppool_end = get_dhcppool_end[Startlen:-4]
    return dhcppool_end

#获取 DHCP地址池配置续租时间
def get_dhcp_lease_time(host, username, telnet_password, get_dhcp_lease_time_command, exit):
    startStr = 'TIME='
    get_dhcp_lease_time = do_telnet(host, username, telnet_password, get_dhcp_lease_time_command, exit)
    Startlen = GetstartIndex(get_dhcp_lease_time,startStr)
    dhcp_lease_time = int(get_dhcp_lease_time[Startlen:-4])
    return dhcp_lease_time

#获取 LAN IP生效地址
def get_lan_ip_apply(host, username, telnet_password, get_lan_ip_apply_command, exit):
    startStr = 'router '
    get_lan_ip_apply = do_telnet(host, username, telnet_password, get_lan_ip_apply_command, exit)
    Startlen = GetstartIndex(get_lan_ip_apply,startStr)
    lan_ip_apply = get_lan_ip_apply[Startlen:-4]
    return lan_ip_apply

#获取 DHCP地址池生效起始IP
def get_dhcppool_start_apply(host, username, telnet_password, get_dhcppool_start_apply_command, exit):
    startStr = 'start '
    get_dhcppool_start_apply = do_telnet(host, username, telnet_password, get_dhcppool_start_apply_command, exit)
    Startlen = GetstartIndex(get_dhcppool_start_apply,startStr)
    dhcppool_start_apply = get_dhcppool_start_apply[Startlen:-4]
    return lan_ip_apply

#获取 DHCP地址池生效结束IP
def get_dhcppool_end_apply(host, username, telnet_password, get_dhcppool_end_apply_command, exit):
    startStr = 'end '
    get_dhcppool_end_apply = do_telnet(host, username, telnet_password, get_dhcppool_end_apply_command, exit)
    Startlen = GetstartIndex(get_dhcppool_end_apply,startStr)
    dhcppool_end_apply = get_dhcppool_end_apply[Startlen:-4]
    return lan_ip_apply

#获取 DHCP地址池配置生效续租时间
def get_dhcp_lease_time_apply(host, username, telnet_password, get_dhcp_lease_time_apply_command, exit):
    startStr = 'lease '
    get_dhcp_lease_time_apply = do_telnet(host, username, telnet_password, get_dhcp_lease_time_apply_command, exit)
    Startlen = GetstartIndex(get_dhcp_lease_time_apply,startStr)
    dhcp_lease_time_apply = int(get_dhcp_lease_time_apply[Startlen:-4])
    return dhcp_lease_time_apply

#获取 DHCP地址池配置生效子网掩码
def get_dhcp_netmask_apply(host, username, telnet_password, get_dhcp_netmask_apply_command, exit):
    startStr = 'subnet '
    get_dhcp_netmask_apply = do_telnet(host, username, telnet_password, get_dhcp_netmask_apply_command, exit)
    Startlen = GetstartIndex(get_dhcp_netmask_apply,startStr)
    dhcp_netmask_apply = int(get_dhcp_netmask_apply[Startlen:-4])
    return dhcp_netmask_apply

#获取 DHCP地址池配置生效DNS
def get_dhcp_dns_apply(host, username, telnet_password, get_dhcp_dns_apply_command, exit):
    startStr = 'dns '
    get_dhcp_dns_apply = do_telnet(host, username, telnet_password, get_dhcp_dns_apply_command, exit)
    Startlen = GetstartIndex(get_dhcp_dns_apply,startStr)
    dhcp_dns_apply = int(get_dhcp_dns_apply[Startlen:-4])
    return dhcp_dns_apply

#获取 DHCP地址池配置生效DNS
def get_dhcp_domain_apply(host, username, telnet_password, get_dhcp_domain_apply_command, exit):
    startStr = 'domain '
    get_dhcp_domain_apply = do_telnet(host, username, telnet_password, get_dhcp_domain_apply_command, exit)
    Startlen = GetstartIndex(get_dhcp_domain_apply,startStr)
    dhcp_domain_apply = int(get_dhcp_domain_apply[Startlen:-4])
    return dhcp_domain_apply

#获取 MAC/IP地址绑定配置信息列表
def get_dhcprsvdip_tbl(host, username, telnet_password, get_dhcprsvdip_tbl_command, exit,static_mac,static_ip,static_name):
    dhcprsvdip_tbl = do_telnet(host, username, telnet_password, get_dhcprsvdip_tbl_command, exit)
    n = dhcprsvdip_tbl.count("\r\n")
    dhcprsvdip_list = dhcprsvdip_tbl.split("\r\n")
    i = 0
    while i < n:
        i = i + 1
        if dhcprsvdip_list[i].find("%s" %static_mac) != -1 and dhcprsvdip_list[i].find("%s" %static_ip) != -1 and dhcprsvdip_list[i].find("%s" %static_name) != -1:
            static_status = "true"
            static_num = i
            print (dhcprsvdip_list[i])
            break
        else:
            static_status = "false"
            static_num = "false"
    return static_status, static_num

#获取 MAC/IP地址绑定生效列表
def get_dhcprsvdip_apply_tbl(host, username, telnet_password, get_staticlease_command, exit,static_mac,static_ip):
    dhcprsvdip_tbl = do_telnet(host, username, telnet_password, get_staticlease_command, exit)
    n = dhcprsvdip_tbl.count("\r\n")
    dhcprsvdip_list = dhcprsvdip_tbl.split("\r\n")
    i = 0
    while i < n:
        i = i + 1
        if dhcprsvdip_list[i].find("%s" %static_mac) != -1 and dhcprsvdip_list[i].find("%s" %static_ip) != -1:
            static_apply_status = "true"
            static_apply_num = i
            print (dhcprsvdip_list[i])
            break
        else:
            static_apply_status = "false"
            static_apply_num = "false"
    return static_apply_status, static_apply_num

#获取WAN口MAC地址
def get_wan_mac_config(host, username, telnet_password, get_wan_mac_config_command, exit):
    startStr = 'ADDR='
    get_wan_mac_config = do_telnet(host, username, telnet_password, get_wan_mac_config_command, exit)
    Startlen = GetstartIndex(get_wan_mac_config,startStr)
    wan_mac_config = get_wan_mac_config[Startlen:-4]
    return wan_mac_config

#获取WAN口MAC生效地址
def get_wan_mac_apply_config(host, username, telnet_password, get_wan_mac_apply_config_command, exit):
    startStr = 'HWaddr '
    get_wan_mac_apply_config = do_telnet(host, username, telnet_password, get_wan_mac_apply_config_command, exit)
    Startlen = GetstartIndex(get_wan_mac_apply_config,startStr)
    wan_mac_apply_config = get_wan_mac_apply_config[Startlen:-4]
    return wan_mac_apply_config

#获取DDNS当前状态
def get_ddns_status(host, username, telnet_password, get_ddns_status_command, exit):
    startStr = 'DDNS_ENABLED='
    get_ddns_status = do_telnet(host, username, telnet_password, get_ddns_status_command, exit)
    Startlen = GetstartIndex(get_ddns_status,startStr)
    ddns_status = int(get_ddns_status[Startlen:-4])
    return ddns_status

#获取DDNS配置信息
def get_ddns_config(host, username, telnet_password, get_ddns_type_command, get_ddns_domain_name_command, get_ddns_user_command, get_ddns_password_command, exit):

    startStr_1 = 'TYPE='
    get_ddns_type = do_telnet(host, username, telnet_password, get_ddns_type_command, exit)
    Startlen_1 = GetstartIndex(get_ddns_type,startStr_1)
    ddns_type_code = int(get_ddns_type[Startlen_1:-4])
    if ddns_type_code == 0:
        ddns_type = "DynDNS"
    else :
        ddns_type = "Oray"

    startStr_2 = 'DOMAIN_NAME="'
    get_ddns_damain_name = do_telnet(host, username, telnet_password, get_ddns_domain_name_command, exit)
    Startlen_2 = GetstartIndex(get_ddns_damain_name,startStr_2)
    ddns_damain_name = get_ddns_damain_name[Startlen_2:-5]

    startStr_3 = 'USER="'
    get_ddns_type_ = do_telnet(host, username, telnet_password, get_ddns_user_command, exit)
    Startlen_3 = GetstartIndex(get_ddns_type_,startStr_3)
    ddns_name = get_ddns_type_[Startlen_3:-5]


    startStr_4 = 'PASSWORD="'
    get_ddns_type_ = do_telnet(host, username, telnet_password, get_ddns_password_command, exit)
    Startlen_4 = GetstartIndex(get_ddns_type_,startStr_4)
    ddns_password = get_ddns_type_[Startlen_4:-5]

    return ddns_type,ddns_damain_name,ddns_name,ddns_password

#获取VPN开关状态
def get_vpn_status(host, username, telnet_password, get_vpn_status_command, exit):
    startStr = "enabled '"
    get_vpn_status = do_telnet(host, username, telnet_password, get_vpn_status_command, exit)
    Startlen = GetstartIndex(get_vpn_status,startStr)
    vpn_status = int(get_vpn_status[Startlen:-5])
    return vpn_status

#获取VPN连接状态
def get_vpn_con_status(host, username, telnet_password, get_vpn_con_status_command, exit):
    startStr = "option status '"
    get_vpn_con_status = do_telnet(host, username, telnet_password, get_vpn_con_status_command, exit)
    Startlen = GetstartIndex(get_vpn_con_status,startStr)
    vpn_con_status = get_vpn_con_status[Startlen:-5]
    return vpn_con_status

#获取VPN当前连接的ID是哪个
def get_vpn_cur_id(host, username, telnet_password, get_vpn_cur_id_command, exit):
    startStr = "vpnid '"
    get_vpn_cur_id = do_telnet(host, username, telnet_password, get_vpn_cur_id_command, exit)
    Startlen = GetstartIndex(get_vpn_cur_id,startStr)
    vpn_cur_id = int(get_vpn_cur_id[Startlen:-5])
    return vpn_cur_id

#获取 VPN列表
def get_vpn_list(host, username, telnet_password, get_vpn_list_num,get_vpn_list, exit):
    list1 = do_telnet(host, username, telnet_password, get_vpn_list_num, exit)
    list2 = list1.split("\r\n")
    vpn_list_num = int(list2[1])
    list3 = do_telnet(host, username, telnet_password, get_vpn_list, exit)
    list4 = list3.split("\r\nconfig ")
    vpn_list = list4[2:vpn_list_num + 2]
    return vpn_list_num,vpn_list


#获取 路由器工作模式
def get_network_mode(host, username, telnet_password, get_network_mode_command, exit):
    startStr = 'OP_MODE='
    get_network_mode = do_telnet(host, username, telnet_password, get_network_mode_command, exit)
    Startlen = GetstartIndex(get_network_mode,startStr)
    network_mode = int(get_network_mode[Startlen:-4])
    if network_mode == 0:
        router_wan_network_mode = "路由模式"
    elif network_mode == 0:
        router_wan_network_mode = "桥接模式"
    return network_mode,router_wan_network_mode

#获取 路由器工作模式
def get_network_mode(host, username, telnet_password, get_network_mode_command, exit):
    startStr = 'OP_MODE='
    get_network_mode = do_telnet(host, username, telnet_password, get_network_mode_command, exit)
    Startlen = GetstartIndex(get_network_mode,startStr)
    network_mode = int(get_network_mode[Startlen:-4])
    if network_mode == 0:
        router_wan_network_mode = "路由模式"
    elif network_mode == 0:
        router_wan_network_mode = "桥接模式"
    return network_mode,router_wan_network_mode

#获取路由器在线设备个数
def get_online_device_num(host, username, telnet_password, get_online_device_num_command, exit):
    list1 = do_telnet(host, username, telnet_password, get_online_device_num_command, exit)
    list2 = list1.split("\r\n")
    online_device_num = int(list2[1])
    return online_device_num

#获取路由器离线设备个数
def get_offline_device_num(host, username, telnet_password, get_offline_device_num_command, exit):
    list1 = do_telnet(host, username, telnet_password, get_offline_device_num_command, exit)
    list2 = list1.split("\r\n")
    offline_device_num = int(list2[1])
    return offline_device_num

#获取设备限时总开关状态
def get_timelimit_main_switch_status(host, username, telnet_password, get_timelimit_main_switch_status_command, exit):
    list1 = do_telnet(host, username, telnet_password, get_timelimit_main_switch_status_command, exit)
    list2 = list1.split("\r\nconfig ")
    list3 = list2[1]
    startStr = 'option enabled \''
    Startlen = GetstartIndex(list3,startStr)
    switch_status = list3[Startlen:-3]
    if switch_status == "true":
            main_switch_status = 1
    elif  switch_status == "false":
            main_switch_status = 0
    return main_switch_status

#获取某个设备限时总开关状态
def get_sta_timelimit_list(host, username, telnet_password, get_sta_timelimit_list_command,timelimit_mac, exit):
    list1 = do_telnet(host, username, telnet_password, get_sta_timelimit_list_command, exit)
    list2 = list1.split("\r\nconfig ")[2:]
    n = len(list2)
    i = 0
    while i < n:
        if list2[i].find("%s" %timelimit_mac) != -1 :
            sta_timelimit_rule = list2[i]
            break
        else:
            sta_timelimit_rule = "null"
        i = i + 1
    return  sta_timelimit_rule

#获取某个设备限时开关状态
def get_sta_timelimit_status(host, username, telnet_password, get_sta_timelimit_list_command,timelimit_mac, exit):
    list1 = get_sta_timelimit_list(host, username, telnet_password, get_sta_timelimit_list_command,timelimit_mac, exit)
    list3 = list1.split("\r\n")[2]
    startStr = 'enabled \''
    Startlen = GetstartIndex(list3,startStr)
    switch_status = list3[Startlen:-1]
    return  switch_status

#获取某个设备限时开关状态
def get_sta_timelimit_status(host, username, telnet_password, get_sta_timelimit_list_command,timelimit_mac, exit):
    list1 = get_sta_timelimit_list(host, username, telnet_password, get_sta_timelimit_list_command,timelimit_mac, exit)
    list3 = list1.split("\r\n")[2]
    startStr = 'enabled \''
    Startlen = GetstartIndex(list3,startStr)
    switch_status = list3[Startlen:-1]
    return  switch_status


n = get_sta_timelimit_status("192.168.127.254","root","123456789","cat mercku/config/timelimits ", 'bc4cc48fff7f',"exit")
print (n)