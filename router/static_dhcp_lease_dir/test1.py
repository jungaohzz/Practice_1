import os
import re
# a = os.popen('ipconfig /all').readlines()
# b = "".join(a)
# c = b.split(":\n")
# d = list(filter(lambda x: '1C-1B-0D-BB-8E-25' in x, c))
# e = "".join(d)
# f = e.split("\n")
# g = list(filter(lambda x: 'IPv4 地址 . . . . . . . . . . . . : ' in x, f))
# h = "".join(g)
# if h.find("192.168.127.100") != -1:
#     print ("IpDIZHIZQEWQWERWRE")
# else:
#     print ("xxxxxxxxxxxxxx")
#

interface_mac = "1C-1B-0D-BB-8E-B5"
ip = "192.168.127.100"


def read_networkcard_ip(interface_mac):
    list1 = ("".join(os.popen('ipconfig /all').readlines())).split(":\n")
    str0 = "".join(list(filter(lambda x: '%s' % interface_mac in x, list1)))
    print(type(str0))
    list2 = re.findall(".*IPv4 地址 . . . . . . . . . . . . : (.*)\(首选\).*", str0)
    interface_ip = "".join(list2)
    return interface_ip

n = read_networkcard_ip(interface_mac)
if n == ip:
    print ("成都市ccccccccccccccc")
else:
    print("xxxxxxxxxxxxxxx")
