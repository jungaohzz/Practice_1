import os
import time
import sys
from . import rate_limit
from . import rate_limit_conf

class Test_rate_limit():
    @staticmethod
    #用例-1599:限速：只限制了上行流量，下行流量不受限制（TCP连接），上行限制速度为：500KB
    def test_rate_limit_1():
        rate_upload_conf = rate_limit_conf.rata_upload_1
        iperf_cmd1 = rate_limit_conf.tcp_wired_clienttoserver
        iperf_cmd2 = rate_limit_conf.tcp_wired_servertoclient
        rate_upload_tcp_1 = rate_limit.Rate_test.internetwired_tcprate(iperf_cmd1)
        rate_download_tcp_2 = rate_limit.Rate_test.internetwired_tcprate(iperf_cmd2)
        rate_upload = rate_upload_tcp_1*1000/8
        rate_download = rate_download_tcp_2*1000/8
        print (rate_upload)
        print (rate_download)

        if 400 < rate_upload < 600 and 2000 < rate_download:
            result = 1
        else:
            result = 0
        return result

    @staticmethod
    # 用例-1600:限速：只限制了下行流量，上行流量不受限制（TCP连接），下行限制速度为：500KB
    def test_rate_limit_2():
        rate_download_conf = rate_limit_conf.rata_download_1
        iperf_cmd1 = rate_limit_conf.tcp_wired_clienttoserver
        iperf_cmd2 = rate_limit_conf.tcp_wired_servertoclient
        rate_upload_tcp_1 = rate_limit.Rate_test.internetwired_tcprate(iperf_cmd1)
        rate_download_tcp_2 = rate_limit.Rate_test.internetwired_tcprate(iperf_cmd2)
        rate_upload = rate_upload_tcp_1*1000/8
        rate_download = rate_download_tcp_2*1000/8
        print (rate_upload)
        print (rate_download)
        if 400 < rate_download < 600 and 2000 < rate_upload:
            result = 1
        else:
            result = 0
        return result

    @staticmethod
    # 用例-1601:开启限速功能后，新创建的TCP连接的上行和下行速度被限制，上行限制速度为：1000KB，下行限制速度为：500KB
    def test_rate_limit_3():
        rate_upload_conf = rate_limit_conf.rata_upload_2
        rate_download_conf = rate_limit_conf.rata_download_1
        iperf_cmd1 = rate_limit_conf.tcp_wired_clienttoserver
        iperf_cmd2 = rate_limit_conf.tcp_wired_servertoclient
        rate_upload_tcp_1 = rate_limit.Rate_test.internetwired_tcprate(iperf_cmd1)
        rate_download_tcp_2 = rate_limit.Rate_test.internetwired_tcprate(iperf_cmd2)
        rate_upload = rate_upload_tcp_1*1000/8
        rate_download = rate_download_tcp_2*1000/8
        print (rate_upload)
        print (rate_download)
        if 800 < rate_upload < 1200 and 400 < rate_download < 600:
            result = 1
        else:
            result = 0
        return result
    @staticmethod
    #用例-1603:开启限速功能后，新创建的UDP连接的上行和下行速度被限制，上行限制速度为：500KB，下行限制速度为：1000KB
    def test_rate_limit_4():
        rate_upload_conf = rate_limit_conf.rata_upload_1
        rate_download_conf = rate_limit_conf.rata_download_2
        iperf_cmd1 = rate_limit_conf.udp_wired_clienttoserver
        iperf_cmd2 = rate_limit_conf.udp_wired_servertoclient
        rate_upload_udp_1 = rate_limit.Rate_test.internetwired_udprate(iperf_cmd1)
        time.sleep(10)
        rate_download_udp_2 = rate_limit.Rate_test.internetwired_udprate(iperf_cmd2)
        rate_upload = rate_upload_udp_1*1000/8
        rate_download = rate_download_udp_2*1000/8
        print (rate_upload)
        print (rate_download)
        if 400 < rate_upload < 600 and 800 < rate_download < 1200:
            result = 1
        else:
            result = 0
        return result
    @staticmethod
    #用例-979:关闭限速后，上行和下行速度不被限制
    def test_rate_limit_5():
        iperf_cmd1 = rate_limit_conf.tcp_wired_clienttoserver
        iperf_cmd2 = rate_limit_conf.tcp_wired_servertoclient
        iperf_cmd3 = rate_limit_conf.udp_wired_clienttoserver
        iperf_cmd4 = rate_limit_conf.udp_wired_servertoclient
        rate_upload_tcp_1 = rate_limit.Rate_test.internetwired_tcprate(iperf_cmd1)
        rate_download_tcp_2 = rate_limit.Rate_test.internetwired_tcprate(iperf_cmd2)
        rate_upload_udp_3 = rate_limit.Rate_test.internetwired_udprate(iperf_cmd3)
        rate_download_udp_4 = rate_limit.Rate_test.internetwired_udprate(iperf_cmd4)
        rate_upload_tcp = rate_upload_tcp_1*1000/8
        rate_download_tcp = rate_download_tcp_2*1000/8
        rate_upload_udp = rate_upload_udp_3*1000/8
        rate_download_udp = rate_download_udp_4*1000/8
        if 2000 < rate_upload_tcp and 2000 < rate_download_tcp and 2000 < rate_upload_udp and 2000 < rate_download_udp:
            result = 1
        else:
            result = 0
        return result

    @staticmethod
    #用例-981：对单个设备限速后，不影响其他设备 (对设备A限速成功后，设备B不会被限速)，对设备A限速，设备B不受限制
    def test_rate_limit_6():
        iperf_cmd1 = rate_limit_conf.tcp_5g_clienttoserver
        iperf_cmd2 = rate_limit_conf.tcp_5g_servertoclient
        iperf_cmd3 = rate_limit_conf.udp_5g_clienttoserver
        iperf_cmd4 = rate_limit_conf.udp_5g_servertoclient
        rate_upload_tcp_1 = rate_limit.Rate_test.internet5g_tcprate(iperf_cmd1)
        rate_download_tcp_2 = rate_limit.Rate_test.internet5g_tcprate(iperf_cmd2)
        rate_upload_udp_3 = rate_limit.Rate_test.internet5g_udprate(iperf_cmd3)
        rate_download_udp_4 = rate_limit.Rate_test.internet5g_udprate(iperf_cmd4)
        rate_upload_tcp = rate_upload_tcp_1*1000/8
        rate_download_tcp = rate_download_tcp_2*1000/8
        rate_upload_udp = rate_upload_udp_3*1000/8
        rate_download_udp = rate_download_udp_4*1000/8
        if 5000 < rate_upload_tcp and 5000 < rate_download_tcp and 5000 < rate_upload_udp and 5000 < rate_download_udp:
            result = 1
        else:
            result = 0
        return result

    @staticmethod
    #用例-1611：多个设备同时限速可成功（设备A,B都设置了限速，保存成功后AB都能限速成功），设备A上行限制为500KB,下行限制为1000KB ,设备B上行限制为1500KB,下行限制为2000KB
    def test_rate_limit_7():
        iperf_cmd1 = rate_limit_conf.tcp_wired_clienttoserver
        iperf_cmd2 = rate_limit_conf.tcp_wired_servertoclient
        iperf_cmd3 = rate_limit_conf.udp_wired_clienttoserver
        iperf_cmd4 = rate_limit_conf.udp_wired_servertoclient
        iperf_cmd5 = rate_limit_conf.tcp_5g_clienttoserver
        iperf_cmd6 = rate_limit_conf.tcp_5g_servertoclient
        iperf_cmd7 = rate_limit_conf.udp_5g_clienttoserver
        iperf_cmd8 = rate_limit_conf.udp_5g_servertoclient
        #设备A上行限制为500KB,下行限制为1000KB
        rate_upload_tcp_1 = rate_limit.Rate_test.internetwired_tcprate(iperf_cmd1)
        rate_download_tcp_2 = rate_limit.Rate_test.internetwired_tcprate(iperf_cmd2)
        time.sleep(10)
        #设备B上行限制为1500KB,下行限制为2000KB

        rate_upload_tcp_3 = rate_limit.Rate_test.internet5g_tcprate(iperf_cmd5)
        rate_download_tcp_4 = rate_limit.Rate_test.internet5g_tcprate(iperf_cmd6)

        rate_upload_tcp_1 = rate_upload_tcp_1*1000/8
        rate_download_tcp_2 = rate_download_tcp_2*1000/8
        rate_upload_tcp_3 = rate_upload_tcp_3*1000/8
        rate_download_tcp_4 = rate_download_tcp_4*1000/8

        if 400 < rate_upload_tcp_1 < 600 and 800 < rate_download_tcp_2 < 1200 and 1300 < rate_upload_tcp_3 < 1700 and 1800 < rate_download_tcp_4 < 2200:
            result = 1
        else:
            result = 0
        return result

    @staticmethod
    #用例-1612:无线接入，限速功能可生效 设备A上行限制为1000KB,下行限制为500KB
    def test_rate_limit_8():
        rate_upload_conf = rate_limit_conf.rata_upload_2
        rate_download_conf = rate_limit_conf.rata_download_1
        iperf_cmd1 = rate_limit_conf.tcp_wired_clienttoserver
        iperf_cmd2 = rate_limit_conf.tcp_wired_servertoclient
        rate_upload_tcp_1 = rate_limit.Rate_test.internetwired_tcprate(iperf_cmd1)
        rate_download_tcp_2 = rate_limit.Rate_test.internetwired_tcprate(iperf_cmd2)
        rate_upload = rate_upload_tcp_1*1000/8
        rate_download = rate_download_tcp_2*1000/8
        if 400 < rate_download < 600 and 800 < rate_upload < 1200:
            result = 1
        else:
            result = 0
        return result

    @staticmethod
    #用例-1613:有线接入，限速功能可生效，设备A上行限制为1000KB,下行限制为500KB
    def test_rate_limit_9():
        rate_upload_conf = rate_limit_conf.rata_upload_2
        rate_download_conf = rate_limit_conf.rata_download_1
        iperf_cmd1 = rate_limit_conf.tcp_wired_clienttoserver
        iperf_cmd2 = rate_limit_conf.tcp_wired_servertoclient
        rate_upload_tcp_1 = rate_limit.Rate_test.internetwired_tcprate(iperf_cmd1)
        rate_download_tcp_2 = rate_limit.Rate_test.internetwired_tcprate(iperf_cmd2)
        rate_upload = rate_upload_tcp_1*1000/8
        rate_download = rate_download_tcp_2*1000/8
        if 400 < rate_download < 600 and 800 < rate_upload < 1200:
            result = 1
        else:
            result = 0
        return result