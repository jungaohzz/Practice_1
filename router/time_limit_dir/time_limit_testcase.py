import time_limit
import time_limit_conf

internet_check = time_limit.Internet_check()
start_telnet = time_limit.Start_telnet()
router_conf = time_limit.Router_conf()
host = time_limit_conf.host
username = time_limit_conf.username
telnet_password = time_limit_conf.telnet_password

class Test_time_limit():
    @staticmethod
    #设备A添加一个开启状态的限时条目，设备A在限时时间段内无法访问外网(周一不能上网)
    def test_time_limit_1():
        open_telnet = start_telnet.open_telnet()
        if open_telnet == 1:
            command = time_limit_conf.set_sys_time_mon
            config_router_time = router_conf.do_telnet(host, username, telnet_password, command, exit)
            internet_status = internet_check.internetwired_connect()
            print (internet_status)
            if internet_status == 1:
                print("测试失败")
                time_limit_reuslt = 0
            else:
                print("测试成功")
                time_limit_reuslt = 1
        else:
            print("测试失败")
            time_limit_reuslt = 0
        return time_limit_reuslt

    @staticmethod
    # 设备A添加一个关闭状态的限时条目，设备A在任何时间段都可以访问外网（周一不能上网）
    def test_time_limit_2():
        open_telnet = start_telnet.open_telnet()
        if open_telnet == 1:
            command = time_limit_conf.set_sys_time_mon
            config_router_time = router_conf.do_telnet(host, username, telnet_password, command, exit)
            internet_status = internet_check.internetwired_connect()
            print (internet_status)
            if internet_status == 1:
                print("测试成功")
                time_limit_reuslt = 1
            else:
                print("测试失败")
                time_limit_reuslt = 1
        else:
            print("测试失败")
            time_limit_reuslt = 0
        return time_limit_reuslt

    @staticmethod
    # 修改设备A的限时是段，新限时时段生效，旧限时时段失效(不能上网时间从周一修改为周二)
    def test_time_limit_3():
        old_limit = Test_time_limit.test_time_limit_2()
        if old_limit == 1:
            open_telnet = start_telnet.open_telnet()
            if open_telnet == 1:
                command = time_limit_conf.set_sys_time_thu
                config_router_time = router_conf.do_telnet(host, username, telnet_password, command, exit)
                internet_status = internet_check.internetwired_connect()
                print (internet_status)
                if internet_status == 1:
                    print("测试成功")
                    time_limit_reuslt = 1
                else:
                    print("测试失败")
                    time_limit_reuslt = 1
            else:
                print("测试失败")
                time_limit_reuslt = 0
        else :
            time_limit_reuslt = 0
        return time_limit_reuslt

    @staticmethod
    #  设备A添加一个开启状态的限时条目，设备B在设备A的限时时间段内可以访问外网（设备A在周一不能上网，设备B在周一可以让他上网）
    def test_time_limit_4():
        open_telnet = start_telnet.open_telnet()
        if open_telnet == 1:
            command = time_limit_conf.set_sys_time_mon
            config_router_time = router_conf.do_telnet(host, username, telnet_password, command, exit)
            internet_status = internet_check.internet5g_connect()
            print (internet_status)
            if internet_status == 1:
                print("测试成功")
                time_limit_reuslt = 1
            else:
                print("测试失败")
                time_limit_reuslt = 1
        else:
            print("测试失败")
            time_limit_reuslt = 0
        return time_limit_reuslt

    @staticmethod
    #设备A添加多个开启状态的限时条目，设备A在限时时间段内无法访问外网 (周一，周三，周五不能上网)
    def test_time_limit_5():
        open_telnet = start_telnet.open_telnet()
        if open_telnet == 1:
            command1 = time_limit_conf.set_sys_time_mon
            config_router_time1 = router_conf.do_telnet(host, username, telnet_password, command1, exit)
            internet_status1 = internet_check.internetwired_connect()

            command2 = time_limit_conf.set_sys_time_wed
            config_router_time2 = router_conf.do_telnet(host, username, telnet_password, command2, exit)
            internet_status2 = internet_check.internetwired_connect()

            command3 = time_limit_conf.set_sys_time_fri
            config_router_time3 = router_conf.do_telnet(host, username, telnet_password, command3, exit)
            internet_status3 = internet_check.internetwired_connect()

            print ("ping 的结果为%s,%s,%s" %(internet_status1,internet_status2,internet_status3))
            if internet_status1 == 1 or internet_status2 == 1 or internet_status3 == 1:
                print("测试失败")
                time_limit_reuslt = 0
            else:
                print("测试成功")
                time_limit_reuslt = 1
        else:
            print("测试失败")
            time_limit_reuslt = 0
        return time_limit_reuslt

    @staticmethod
    #多个设备添加开启状态的限时条目，对应设备在其限时时间段内无法访问外网  (设备A周一周三不能上网，设备B周二周四不能上网)
    def test_time_limit_6():
        open_telnet = start_telnet.open_telnet()
        if open_telnet == 1:
            command1 = time_limit_conf.set_sys_time_mon
            config_router_time1 = router_conf.do_telnet(host, username, telnet_password, command1, exit)
            internet_status1 = internet_check.internetwired_connect()

            command2 = time_limit_conf.set_sys_time_tue
            config_router_time2 = router_conf.do_telnet(host, username, telnet_password, command2, exit)
            internet_status2 = internet_check.internetwired_connect()

            command3 = time_limit_conf.set_sys_time_wed
            config_router_time3 = router_conf.do_telnet(host, username, telnet_password, command3, exit)
            internet_status3 = internet_check.internetwired_connect()

            command4 = time_limit_conf.set_sys_time_mon
            config_router_time4 = router_conf.do_telnet(host, username, telnet_password, command4, exit)
            internet_status4 = internet_check.internet5g_connect()

            command5 = time_limit_conf.set_sys_time_tue
            config_router_time5 = router_conf.do_telnet(host, username, telnet_password, command5, exit)
            internet_status5 = internet_check.internet5g_connect()

            command6 = time_limit_conf.set_sys_time_thu
            config_router_time6 = router_conf.do_telnet(host, username, telnet_password, command6, exit)
            internet_status6 = internet_check.internet5g_connect()

            print ("ping 的结果为 %s,%s,%s,%s,%s,%s" %(internet_status1,internet_status2,internet_status3,internet_status4,internet_status5,internet_status6))
            if internet_status1 == 0 and internet_status2 == 1 and internet_status3 == 0 and internet_status4 == 1 and internet_status5 == 0 and internet_status6 ==0:
                print("测试失败")
                time_limit_reuslt = 0
            else:
                print("测试成功")
                time_limit_reuslt = 1
        else:
            print("测试失败")
            time_limit_reuslt = 0
        return time_limit_reuslt