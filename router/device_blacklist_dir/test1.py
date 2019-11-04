import os


a = os.popen('netsh wlan  show interfaces').readlines()
print(type(a))
print(a)
d = str(a)
e = d.split("名称                   :")
n = len(e)
print(n)
i = 0
while i < n:
    i = i + 1
    if e[i].find("WLAN2G") != -1:
        f = e[i].split("\n")
        b = list(filter(lambda x: '状态                   :' in x, f))
        c = "".join(b)
        print(c)

        if c.find("已连接") != -1:
            result = 1
            print("连接成功")
        elif c.find("已断开") != -1:
            result = 0
            print("连接失败")
        else:
            result = -1
            print("连接异常")
        break
