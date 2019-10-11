from . import website_blacklist
from . import website_blacklist_conf

url_test = website_blacklist.Url_check()
url_list = website_blacklist_conf

class Test_website_blacklist():
    @staticmethod
    #用例-5032:开关开启，设备A添加一个完整的网址黑名单a，设备A不可以访问网址a(设备a不可以访问www.baidu.com)
    def test_website_blacklist_1():
        black_url1 = url_list.baidu_url1
        url_test_status = url_test.internetwired_connect(black_url1)
        print (url_test_status)
        if url_test_status == 1:
            print("测试失败")
            website_blacklist_reuslt = 0
        else:
            print("测试成功")
            website_blacklist_reuslt = 1
        return website_blacklist_reuslt

    @staticmethod
    #用例-7216:开关开启，设备A添加一个完整的网址黑名单a，设备A可以访问非网址a的网址（设备a不可以访问www.baidu.com，但是可以访问new.baidu.com,www.jd.com）
    def test_website_blacklist_2():
        # 设备a不可以访问www.baidu.com
        white_url1 = url_list.baidu_url2
        url_test_status1 = url_test.internetwired_connect(white_url1)
        # 可以访问new.baidu.com, www.jd.com
        white_url2 = url_list.jd_url1
        url_test_status2 = url_test.internetwired_connect(white_url2)
        print (url_test_status1, url_test_status2)
        if url_test_status1 == 1 and url_test_status2 == 1:
            print("测试成功")
            website_blacklist_reuslt = 1
        else:
            print("测试失败")
            website_blacklist_reuslt = 0
        return website_blacklist_reuslt

    @staticmethod
    #用例-7214:开关开启，设备A添加一个完整的网址黑名单a，设备B可以访问网址a（设备a不可以访问www.baidu.com，设备b不可以访问www.baidu.com）
    def test_website_blacklist_3():
        # 设备a不可以访问www.baidu.com，设备b不可以访问www.baidu.com
        black_url1 = url_list.baidu_url1
        url_test_status = url_test.internet5g_connect(black_url1)
        print (url_test_status)
        if url_test_status == 1:
            print("测试成功")
            website_blacklist_reuslt = 1
        else:
            print("测试失败")
            website_blacklist_reuslt = 0
        return website_blacklist_reuslt

    @staticmethod
    #用例-4836:开关开启，设备A删除一个网址黑名单a，设备A可以访问网址a（设备a不可以访问www.baidu.com，删除设备a的网址黑名单www.baidu.com）
    def test_website_blacklist_4():
        # 设备a存在网址黑名单www.baidu.com，删除设备A的网址黑名单后，设备A可以访问www.baidu.com
        black_url1 = url_list.baidu_url1
        url_test_status = url_test.internetwired_connect(black_url1)
        print (url_test_status)
        if url_test_status == 1:
            print("测试成功")
            website_blacklist_reuslt = 1
        else:
            print("测试失败")
            website_blacklist_reuslt = 0
        return website_blacklist_reuslt


    @staticmethod
    #用例-7215:开关开启，设备A添加一个主域名的网址黑名单，设备A无法访问主域名相关的所有网址（设备a不可以访问主域名baidu，那么设备a就不能访问www.baidu.com,news.baidu.com,tieba.baidu.com,jingyan.baidu.com）
    def test_website_blacklist_5():
        # 设备a存在网址黑名单www.baidu.com，删除设备A的网址黑名单后，设备A可以访问www.baidu.com
        black_url1 = url_list.baidu_url1
        url_test_status1 = url_test.internetwired_connect(black_url1)

        black_url2 = url_list.baidu_url2
        url_test_status2 = url_test.internetwired_connect(black_url2)

        black_url3 = url_list.baidu_url3
        url_test_status3 = url_test.internetwired_connect(black_url3)

        black_url4 = url_list.baidu_url4
        url_test_status4 = url_test.internetwired_connect(black_url4)

        print (url_test_status1, url_test_status2, url_test_status3, url_test_status4)
        if url_test_status1 == 0 and url_test_status2 == 0 and  url_test_status3 == 0 and url_test_status4 == 0:
            print("测试成功")
            website_blacklist_reuslt = 1
        else:
            print("测试失败")
            website_blacklist_reuslt = 0
        return website_blacklist_reuslt

    @staticmethod
    #用例-5240:开关开启，设备A添加多个网址黑名单，设备A不可以访问黑名单网址(设备a不可以访问www.baidu.com)
    def test_website_blacklist_6():
        black_url1 = url_list.baidu_url1
        url_test_status1 = url_test.internetwired_connect(black_url1)

        black_url2 = url_list.baidu_url2
        url_test_status2 = url_test.internetwired_connect(black_url2)

        black_url3 = url_list.jd_url1
        url_test_status3 = url_test.internetwired_connect(black_url3)

        black_url4 = url_list.jd_url2
        url_test_status4 = url_test.internetwired_connect(black_url4)

        print (url_test_status1, url_test_status2, url_test_status3, url_test_status4)
        if url_test_status1 == 0 and url_test_status2 == 0 and url_test_status3 == 0 and url_test_status4 == 0:
            print("测试成功")
            website_blacklist_reuslt = 1
        else:
            print("测试失败")
            website_blacklist_reuslt = 0
        return website_blacklist_reuslt


    @staticmethod
    #用例-7217:设备A的网址黑名单关闭，设备A可以访问任何网址，设备B的网址黑名单开启，设备B不可以访问网址黑名单中的网址
    def test_website_blacklist_7():
        black_url1 = url_list.baidu_url1
        url_test_status1 = url_test.internetwired_connect(black_url1)

        black_url2 = url_list.jd_url1
        url_test_status2 = url_test.internet5g_connect(black_url2)

        print (url_test_status1, url_test_status2)
        if url_test_status1 == 1 and url_test_status2 == 0:
            print("测试成功")
            website_blacklist_reuslt = 1
        else:
            print("测试失败")
            website_blacklist_reuslt = 0
        return website_blacklist_reuslt

    @staticmethod
    #用例-4835:开关开启，多个设备添加多个网址黑名单，功能生效
    def test_website_blacklist_8():
        black_url1 = url_list.baidu_url1
        url_test_status1 = url_test.internetwired_connect(black_url1)

        black_url2 = url_list.baidu_url2
        url_test_status2 = url_test.internetwired_connect(black_url2)

        black_url3 = url_list.jd_url1
        url_test_status3 = url_test.internet5g_connect(black_url3)

        black_url4 = url_list.jd_url2
        url_test_status4 = url_test.internet5g_connect(black_url4)

        print (url_test_status1, url_test_status2, url_test_status3, url_test_status4)
        if url_test_status1 == 0 and url_test_status2 == 0 and url_test_status3 == 0 and url_test_status4 == 0:
            print("测试成功")
            website_blacklist_reuslt = 1
        else:
            print("测试失败")
            website_blacklist_reuslt = 0
        return website_blacklist_reuslt

    @staticmethod
    # 用例 - 4838: 开关关闭，设备A添加一个网址黑名单a，设备A可以访问网址a，设备B可以访问网址a
    def test_website_blacklist_9():
        black_url1 = url_list.baidu_url1
        url_test_status1 = url_test.internetwired_connect(black_url1)
        url_test_status2 = url_test.internet5g_connect(black_url1)

        print (url_test_status1, url_test_status2)
        if url_test_status1 == 1 and url_test_status2 == 1:
            print("测试成功")
            website_blacklist_reuslt = 1
        else:
            print("测试失败")
            website_blacklist_reuslt = 0
        return website_blacklist_reuslt

