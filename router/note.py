#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Time  :  2019/7/24 13:43
# @Author:  GaoJun


"""
1、限速中需要优化的地方，因为5G测速时，是需要先连接好5G的，而代码中没有连接5G的操作，需要手动先连接5G才行，这点是需要优化的

2、主WiFi设置中：未通过测试
   test_K_test_wifi_7
   test_S_test_wifi_13
   test_b_test_wifi_19
   test_h_test_wifi_22
   test_k_test_wifi_24（较大概率失败）
   test_n_test_wifi_26
3、访客WiFi设置中：未通过测试
   test_a_test_guest_wifi_15

4、guestWiFiset最后修改完后，需要将PRECONDITION修改为False

5、staticDhcpLease中：未通过测试
   test_C_init
   test_I_staticDhcpLease_2_2





各模块需要搭建的环境：
【本机有线连接】配置静态IP：192.168.127.201、255.255.0.0、192.168.127.254、192.168.127.254
【无线网卡2.4G】配置静态IP：192.168.127.202
【无线网卡5G】配置动态IP
【另一台同路由器下的电脑，有线连接】配置静态IP:10.70.100.182、255.255.0.0、10.70.0.1、10.70.0.1

【环境搭建】
1. 限时、网址黑名单：
  （1）本机有线连接；（2）无线网卡5G。
   备注：该网卡需要连接5G的SSID

2. 限速
  （1）本机有线连接；（2）另一台同路由器下的电脑，有线连接

3. 主WiFi设置：
  （1）本机有线连接；（2）无线网卡2.4G；（3）无线网卡5G。
   备注：无线网卡2.4G和无线网卡5G不需要连接WiFi即可

4. 修改到限时的set判断了

【注意事项】
1. 最好切换到admin账户下运行（因为主WiFi设置时运行cmd需要管理员权限）


"""
