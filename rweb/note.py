"""
1. 网络诊断：
   没有写完，因为没有网络，所以没有做判断


3. 更改是否选中的判断
   if not self.driver.find_element_by_xpath(SystemLogLocators.Statu).is_selected():

4. 因为网络不通，所以在“上网设置”中切换三种模式，是否成功没有检查主页那根线是否通，三种方式都没有进行断言没有通过！！！没有通过！！！

5. 检验元素是否可见
   assert self.driver.find_element_by_xpath(CommonLocators.Logout).is_displayed()

6. 正常机器、正常环境时，查看主网、访客、离线三个部分的按钮是否可共用。如删除、全选、加入黑名单等


7. 要将所有列表的获取变为动态获取：Delete = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div[3]/div[{num}]/div[4]/a[2]"
   目前已经实现的模块：限时

8.  遮罩验证的用例：
    用例-5613 : 确认框，一切正常，点击“确定”，弹出【等待页面】
                查看页面是否有文字提示：重启中，请等待...《trans0322》 ： 是
                查看页面是否从60s开始倒计时 ： 是
                倒计时过程中，轮询判断 ： 是
    验证的代码如下：
    # 断言：查看页面是否有文字提示：重启中，请等待...《trans0322》 ： 是
    Shade_Note = self.driver.find_element_by_xpath("//div[@class='reboot-model-contanier']/div[3]").text[:-3]
    assert Shade_Note == "Successful operation, please wait...", Shade_Note
    # 断言：查看页面是否从60s开始倒计时 ： 是
    Shade_StartTime = int(self.driver.find_element_by_xpath("//div[@class='reboot-model-contanier']/div[3]").text[-3:-1])
    assert Shade_StartTime == 60, Shade_StartTime
    # 断言：倒计时过程中，轮询判断 ： 是（这里验证5秒的倒计时轮询即可）
    i = 1
    while i <= 5:
        time.sleep(1)
        Shade_Time = int(
            self.driver.find_element_by_xpath("//div[@class='reboot-model-contanier']/div[3]").text[-3:-1])
        print(Shade_Time)
        assert Shade_Time == 60 - i, Shade_Time
        i += 1

9. 将所有的save_ok 的xpath路径均放到const文件中：//div[@class='dialog-buttons']/button[2]
   注：好像是所有弹窗的确定按钮都是：//div[@class='dialog-buttons']/button[2]

10.所有有add功能的页面，好像元素都是：//button[@class='btn btn-small']

11.模拟双击和删除键
    from selenium.webdriver.common.keys import Keys
    # 模拟鼠标双击
    inputBox = self.driver.find_element_by_xpath(LimitRateLocators.Download)
    action_chains = ActionChains(self.driver)
    action_chains.double_click(inputBox).perform()
    # 模拟键盘删除键
    self.driver.find_element_by_xpath(LimitRateLocators.Download).send_keys(Keys.BACK_SPACE)

12. （1）在“test_limitWebsiteBlacklist.py”中，有条用例的最后一点没有实现检验
    用例-1974 : 网址列表-单个设备添加的总网址数量超过15条，点击“新增”，有文字提示
                给连接的任意一个设备，增加15条网址黑名单
                这个设备，再次点击“新增”，看是否提示“已经达到上限。trans0060” ： 是
                其他设备，点击“新增”，看是否不提示，而是弹出新增框 ： 是                  ->   这一点没有检验

    （2）在“test_routerManagement.py”中，有2条用例的最后一点没有实现检验
    用例-5526 : 开启开关成功
                开启开关，看是否可成功 ： 是
                查看（mesh组网通道）配置项，是否2.4G和5G组网通道都已开启 ： 是            ->   这一点没有检验
    用例-5527 : 关闭开关成功
                关闭开关，看是否可成功 ： 是
                查看（mesh组网通道）配置项，是否2.4G通道关闭，5G通道开启 ： 是            ->   这一点没有检验

    （3）在“test_devices.py”中，有1条用例的一点没有实现检验
    用例-1854 : 单条设备元素检测
                    查看 设备名称 字段包含的元素：图标、连接类型标识、设备名称、接入时长、编辑按钮    ->   “接入时长”没有检验，因为有线连接没有接入时长
                    查看 IP字段包含的元素：ip地址
                    查看 MAC 字段包含的元素：mac地址
                    查看 实时速率 字段包含的元素：上行图标 + 上行速率、下行图片 + 下行速率
                    查看 流量消耗 字段包含的元素：消耗的流量值
                    查看 限制 字段包含的元素：限时图标、限速图标、网址黑名单图标
                    查看 操作 字段包含的元素：“加入黑名单”文本


13. 需要动态接收的参数：固件版本 -> 目的：“管理路由器”中验证版本号
"""