import os
from ..common_dir import common_fun, common_conf


class Test_timezone():

    @staticmethod
    #用例-4833 : 修改系统时区为时区A后，系统时间为时区A时间
    # 设置为+8区  中国北京时区
    def test_timezone_1():
        open_telnet = common_fun.Start_telnet.open_telnet()
        print("xxxxxxxxxxxxx")
        if open_telnet == 1:
            command = common_conf.get_timezone
            host = common_conf.host
            username = common_conf.username
            telnet_password = common_conf.telnet_password
            startStr = 'TIMEZONE="'
            current_time = "-8\ 1"
            print("oooooooooooo")
            get_ntp_timezone = common_fun.Router_conf.do_telnet(host, username, telnet_password, command, exit)
            print(get_ntp_timezone)
            startlen = common_fun.Router_conf.getstartIndex(get_ntp_timezone, startStr)
            timezone = get_ntp_timezone[startlen:-5]
            print(timezone)
            if timezone == current_time:
                result = 1
                print("测试成功")
            else:
                result = 0
                print("测试失败")
        else:
            result = 0
            print("测试失败")
        return  result
