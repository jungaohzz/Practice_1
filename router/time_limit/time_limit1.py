import os
import time
import telnetlib
import requests


#ping网关检查
def ping_gateway( ):
    # ping过程
    pingstatus = os.system('ping mywifi.mercku.tech -n 2')
    time.sleep(3)
    print ("pingstatus=" + "%s" %(pingstatus))
    if pingstatus == 0:
        gateway_status = 1
    else:
        gateway_status = 0
    return gateway_status

#开启路由器telnet
def start_telnet(mercku_url,telnet_data):
    gateway_status = ping_gateway()
    if gateway_status == 1:
        start_telnetstatus = str(requests.post(url=mercku_url, json=telnet_data))
        if start_telnetstatus.find("[200]") == -1:
            telnet_status = 0
        else:
            telnet_status = 1
    else :
        print ("连接路由器失败")
        telnet_status = 0
    print (telnet_status)
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

#配置有线网卡IP
def ipwired_configure(internet_interface):
    os.system('Netsh interface IP Set Addr "%s" Static 192.168.127.8 255.255.255.0 192.168.127.254 1' % internet_interface)
    os.system('Netsh interface IP Set dns "%s" static 192.168.127.254 primary' % internet_interface)

#配置5G网卡IP
def ip5g_configure(internet_interface):
    os.system('Netsh interface IP Set Addr "%s" Static 192.168.127.18 255.255.255.0 192.168.127.254 1' % internet_interface)
    os.system('Netsh interface IP Set dns "%s" static 192.168.127.254 primary' % internet_interface)

#配置2.4G网卡IP
def ip2g_configure(internet_interface):
    os.system('Netsh interface IP Set Addr "%s" Static 192.168.127.28 255.255.255.0 192.168.127.254 1' % internet_interface)
    os.system('Netsh interface IP Set dns "%s" static 192.168.127.254 primary' % internet_interface)

#初始化无线网卡
def interface_init(internet_interface1,internet_interface2):
    os.system('netsh wlan delete profile *')
    os.system('netsh interface set interface "%s" disabled' % internet_interface1)
    os.system('netsh interface set interface "%s" disabled' % internet_interface2)
    os.system('netsh interface set interface "%s" enabled' % internet_interface1)

#有线联网状态检查
def internetwired_connect( ):
    # ping过程
    flushdns = os.system("ipconfig  /flushdns ")
    pingstatus_1 = os.system('ping www.baidu.com -S 192.168.127.100  -n 2')
    pingstatus_2 = os.system('ping www.sina.com.cn  -S 192.168.127.100  -n 2')
    print("dhasdhask")
    print(pingstatus_1)
    print(pingstatus_2)

    time.sleep(5)
    print ("pingstatus_1=" + "%s" %(pingstatus_1))
    print ("pingstatus_2=" + "%s" %(pingstatus_2))
    if pingstatus_1 == 0 and pingstatus_2 == 0:
        result = 1
        # 1代表能ping通
    elif pingstatus_1 == 1 and pingstatus_2 == 1:
        result = 0
        # 0代表不能ping通
    else:
        result = 2
        # 2代表ping异常
    print("090130123")
    print(result)
    print(3123)
    return result

#5G联网状态检查
def internet5g_connect( ):
    # ping过程
    flushdns = os.system("ipconfig  /flushdns ")
    pingstatus_1 = os.system('ping www.baidu.com -S 192.168.127.18  -n 2')
    pingstatus_2 = os.system('ping www.sina.com.cn  -S 192.168.127.18  -n 2')


    time.sleep(5)
    print ("pingstatus_1=" + "%s" %(pingstatus_1))
    print ("pingstatus_2=" + "%s" %(pingstatus_2))
    if pingstatus_1 == 0 and pingstatus_2 == 0:
        result = 1
    elif pingstatus_1 == 1 and pingstatus_2 == 1:
        result = 0
    else:
        result = -1
    return result

#2.4G联网状态检查
def internet2g_connect( ):
    # ping过程
    pingstatus_1 = os.system('ping www.baidu.com -S 192.168.127.28  -n 2')
    pingstatus_2 = os.system('ping www.sina.com.cn -S 192.168.127.28  -n 2')
    time.sleep(5)
    print ("pingstatus_1=" + "%s" %(pingstatus_1))
    print ("pingstatus_2=" + "%s" %(pingstatus_2))
    if pingstatus_1 == 0 and pingstatus_2 == 0:
        result = 1
    elif pingstatus_1 == 1 and pingstatus_2 == 1:
        result = 0
    else:
        result = 2
    return result
