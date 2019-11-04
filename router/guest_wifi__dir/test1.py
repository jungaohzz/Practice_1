import os
import time

# a = wifi_set.Wifi_con.wifi_2g_wpa2_aes_connect("flefllefl000jj01","1234562789")


b = os.popen('netsh wlan  show interfaces').readlines()
time.sleep(5)
c = list(filter(lambda x: '状态                   :' in x, b))
d = "".join(c)
print(d)
if d.find("已连接") != -1:
    print("连接成功")
elif d.find("已断开") != -1:
    print("连接失败")


