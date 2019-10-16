import os
import time
import sys
from . import rate_limit
from . import rate_limit_conf

class Test_rate_limit():
    @staticmethod
    #用例-1599:限速：只限制了上行流量，下行流量不受限制（TCP连接）
    def test_rate_limit_1():
        iperf_cmd1 = rate_limit_conf.tcp_wired_clienttoserver   # 上传
        iperf_cmd2 = rate_limit_conf.tcp_wired_servertoclient   # 下载
        rate_upload_tcp_1 = rate_limit.Rate_test.internetwired_rate(iperf_cmd1)     # 上传
        rate_download_tcp_2 = rate_limit.Rate_test.internetwired_rate(iperf_cmd2)   # 下载
        return rate_upload_tcp_1, rate_download_tcp_2

    @staticmethod
    #用例-1600:限速：只限制了下行流量，上行流量不受限制（TCP连接）
    def test_rate_limit_2():
        iperf_cmd1 = rate_limit_conf.tcp_wired_clienttoserver
        iperf_cmd2 = rate_limit_conf.tcp_wired_servertoclient
        rate_upload_tcp_1 = rate_limit.Rate_test.internetwired_rate(iperf_cmd1)
        rate_download_tcp_2 = rate_limit.Rate_test.internetwired_rate(iperf_cmd2)
        return rate_upload_tcp_1, rate_download_tcp_2

    @staticmethod
    #用例-1601:开启限速功能后，新创建的TCP连接的上行和下行速度被限制
    def test_rate_limit_3():
        iperf_cmd1 = rate_limit_conf.tcp_wired_clienttoserver
        iperf_cmd2 = rate_limit_conf.tcp_wired_servertoclient
        rate_upload_tcp_1 = rate_limit.Rate_test.internetwired_rate(iperf_cmd1)
        rate_download_tcp_2 = rate_limit.Rate_test.internetwired_rate(iperf_cmd2)
        return rate_upload_tcp_1, rate_download_tcp_2

    @staticmethod
    #用例-1603:开启限速功能后，新创建的UDP连接的上行和下行速度被限制
    def test_rate_limit_4():
        iperf_cmd1 = rate_limit_conf.udp_wired_clienttoserver
        iperf_cmd2 = rate_limit_conf.udp_wired_servertoclient
        rate_upload_udp_1 = rate_limit.Rate_test.internetwired_rate(iperf_cmd1)
        rate_download_udp_2 = rate_limit.Rate_test.internetwired_rate(iperf_cmd2)
        return rate_upload_udp_1, rate_download_udp_2

    @staticmethod
    #用例-979:关闭限速后，上行和下行速度不被限制
    def test_rate_limit_5():
        iperf_cmd1 = rate_limit_conf.tcp_wired_clienttoserver
        iperf_cmd2 = rate_limit_conf.tcp_wired_servertoclient
        iperf_cmd3 = rate_limit_conf.udp_wired_clienttoserver
        iperf_cmd4 = rate_limit_conf.udp_wired_servertoclient
        rate_upload_tcp_1 = rate_limit.Rate_test.internetwired_rate(iperf_cmd1)
        rate_download_tcp_2 = rate_limit.Rate_test.internetwired_rate(iperf_cmd2)
        rate_upload_udp_3 = rate_limit.Rate_test.internetwired_rate(iperf_cmd3)
        rate_download_udp_4 = rate_limit.Rate_test.internetwired_rate(iperf_cmd4)
        return rate_upload_tcp_1, rate_download_tcp_2,rate_upload_udp_3, rate_download_udp_4

    @staticmethod
    #用例-981：对单个设备限速后，不影响其他设备 (对设备A限速成功后，设备B不会被限速)
    def test_rate_limit_6():
        iperf_cmd1 = rate_limit_conf.tcp_5g_clienttoserver
        iperf_cmd2 = rate_limit_conf.tcp_5g_servertoclient
        iperf_cmd3 = rate_limit_conf.udp_5g_clienttoserver
        iperf_cmd4 = rate_limit_conf.udp_5g_servertoclient
        rate_upload_tcp_1 = rate_limit.Rate_test.internet5g_rate(iperf_cmd1)
        rate_download_tcp_2 = rate_limit.Rate_test.internet5g_rate(iperf_cmd2)
        rate_upload_udp_3 = rate_limit.Rate_test.internet5g_rate(iperf_cmd3)
        rate_download_udp_4 = rate_limit.Rate_test.internet5g_rate(iperf_cmd4)
        #测试结果应该在大于50Mb/S
        return rate_upload_tcp_1, rate_download_tcp_2,rate_upload_udp_3, rate_download_udp_4

    @staticmethod
    #用例-1611：多个设备同时限速可成功（设备A,B都设置了限速，保存成功后AB都能限速成功）
    def test_rate_limit_7():
        iperf_cmd1 = rate_limit_conf.tcp_wired_clienttoserver
        iperf_cmd2 = rate_limit_conf.tcp_wired_servertoclient
        iperf_cmd3 = rate_limit_conf.udp_wired_clienttoserver
        iperf_cmd4 = rate_limit_conf.udp_wired_servertoclient
        iperf_cmd5 = rate_limit_conf.tcp_5g_clienttoserver
        iperf_cmd6 = rate_limit_conf.tcp_5g_servertoclient
        iperf_cmd7 = rate_limit_conf.udp_5g_clienttoserver
        iperf_cmd8 = rate_limit_conf.udp_5g_servertoclient

        rate_upload_tcp_1 = rate_limit.Rate_test.internetwired_rate(iperf_cmd1)
        rate_download_tcp_2 = rate_limit.Rate_test.internetwired_rate(iperf_cmd2)
        rate_upload_udp_3 = rate_limit.Rate_test.internetwired_rate(iperf_cmd3)
        rate_download_udp_4 = rate_limit.Rate_test.internetwired_rate(iperf_cmd4)
        time.sleep(10)
        rate_upload_tcp_5 = rate_limit.Rate_test.internet5g_rate(iperf_cmd5)
        rate_download_tcp_6 = rate_limit.Rate_test.internet5g_rate(iperf_cmd6)
        rate_upload_udp_7 = rate_limit.Rate_test.internet5g_rate(iperf_cmd7)
        rate_download_udp_8 = rate_limit.Rate_test.internet5g_rate(iperf_cmd8)
        return rate_upload_tcp_1, rate_download_tcp_2, rate_upload_udp_3, rate_download_udp_4, rate_upload_tcp_5, rate_download_tcp_6, rate_upload_udp_7, rate_download_udp_8

    @staticmethod
    #用例-1612:无线接入，限速功能可生效
    def test_rate_limit_8():
        iperf_cmd1 = rate_limit_conf.tcp_5g_clienttoserver
        iperf_cmd2 = rate_limit_conf.tcp_5g_servertoclient
        iperf_cmd3 = rate_limit_conf.udp_5g_clienttoserver
        iperf_cmd4 = rate_limit_conf.udp_5g_servertoclient
        rate_upload_tcp_1 = rate_limit.Rate_test.internet5g_rate(iperf_cmd1)
        rate_download_tcp_2 = rate_limit.Rate_test.internet5g_rate(iperf_cmd2)
        rate_upload_udp_3 = rate_limit.Rate_test.internet5g_rate(iperf_cmd3)
        rate_download_udp_4 = rate_limit.Rate_test.internet5g_rate(iperf_cmd4)
        return rate_upload_tcp_1, rate_download_tcp_2, rate_upload_udp_3, rate_download_udp_4

    @staticmethod
    #用例-1613:有线接入，限速功能可生效
    def test_rate_limit_9():
        iperf_cmd1 = rate_limit_conf.tcp_wired_clienttoserver
        iperf_cmd2 = rate_limit_conf.tcp_wired_servertoclient
        iperf_cmd3 = rate_limit_conf.udp_wired_clienttoserver
        iperf_cmd4 = rate_limit_conf.udp_wired_servertoclient
        rate_upload_tcp_1 = rate_limit.Rate_test.internetwired_rate(iperf_cmd1)
        rate_download_tcp_2 = rate_limit.Rate_test.internetwired_rate(iperf_cmd2)
        rate_upload_udp_3 = rate_limit.Rate_test.internetwired_rate(iperf_cmd3)
        rate_download_udp_4 = rate_limit.Rate_test.internetwired_rate(iperf_cmd4)
        return rate_upload_tcp_1, rate_download_tcp_2,rate_upload_udp_3, rate_download_udp_4
