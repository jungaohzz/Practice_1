import os
import time
import telnetlib
import requests
import http

# ping网关检查
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
