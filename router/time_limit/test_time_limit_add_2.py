import os
import time
import sys
import time_limit1
import telnetlib
import time_limit_conf


mercku_url = time_limit_conf.url
telnet_data = time_limit_conf.data
host = time_limit_conf.host
username = time_limit_conf.username
telnet_password = time_limit_conf.telnet_password
command = time_limit_conf.set_sys_time_true
start_telnet = time_limit1.start_telnet(mercku_url, telnet_data)

if start_telnet == 1:
    telnet_status = time_limit1.do_telnet(host, username, telnet_password, command, exit)
    status = time_limit1.internetwired_connect()
    if status == 1:
        result = 1
    elif status == 0:
        result = 0
    else:
        result = 0
    print (result)
else :
    print ("开启telnet失败")