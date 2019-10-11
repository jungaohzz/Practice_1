import os
import time
import telnetlib
import requests
import socket

# ping网关检查
class Internet_check:
    @staticmethod
    # 有线联网状态检查
    def internetwired_connect():
        # 通过ping检测
        a = os.system('ping www.huawei.com -S 192.168.127.201  -n 2')
        print("aaaaaaaaaaa  %s" % a)
        b = os.system('ping www.cnblogs.com  -S 192.168.127.201  -n 2')
        print("bbbbbbbbbbb %s" % b)
        a1 = str(os.popen('ping www.huawei.com -S 192.168.127.201  -n 2').read())
        b1 = str(os.popen('ping www.cnblogs.com  -S 192.168.127.201  -n 2').read())
        print("a1a1a1a1a1a1 %s" % a1)
        print("b1b1b1b1b1b1 %s" % b1)
        # a和b都返回0时表示都ping通了对应url
        if a == 0 and b == 0:
            # 能在ping响应中找到对“平均”两个字符时，表示有ping的响应
            if a1.find("平均") != -1 and b1.find("平均") != -1:
                result = 1
                print("ping 成功")
            else:
                print("ping 失败111")
                result = 0
        else:
            print("ping 失败222")
            result = 0
        print(result)
        return result
        #  result：0：访问外网失败 1：表示访问外网成功

    @staticmethod
    # 5G联网状态检查
    def internet5g_connect():
        # 通过ping检测
        a = os.system('ping www.huawei.com -S 192.168.127.202  -n 2')
        b = os.system('ping www.cnblogs.com  -S 192.168.127.202  -n 2')
        a1 = str(os.popen('ping www.huawei.com -S 192.168.127.202  -n 2').read())
        b1 = str(os.popen('ping www.cnblogs.com  -S 192.168.127.202  -n 2').read())
        print(a1)
        print(b1)
        # a和b都返回0时表示都ping通了对应url
        if a == 0 and b == 0:
            # 能在ping响应中找到对“平均”两个字符时，表示有ping的响应
            if a1.find("平均") != -1 and b1.find("平均") != -1:
                result = 1
            else:
                result = 0
        else:
            result = 0
        print(result)
        return result

    #  result：0：访问外网失败 1：表示访问外网成功

    @staticmethod
    # 2.4G联网状态检查
    def internet2g_connect():
        # 通过ping检测
        a = os.system('ping www.huawei.com -S 192.168.127.203  -n 2')
        b = os.system('ping www.cnblogs.com  -S 192.168.127.203  -n 2')
        a1 = str(os.popen('ping www.huawei.com -S 192.168.127.203  -n 2').read())
        b1 = str(os.popen('ping www.cnblogs.com  -S 192.168.127.203  -n 2').read())
        print(a1)
        print(b1)
        # a和b都返回0时表示都ping通了对应url
        if a == 0 and b == 0:
            # 能在ping响应中找到对“平均”两个字符时，表示有ping的响应
            if a1.find("平均") != -1 and b1.find("平均") != -1:
                result = 1
            else:
                result = 0
        else:
            result = 0
        print(result)
        return result
        #  result：0：访问外网失败 1：表示访问外网成功


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
