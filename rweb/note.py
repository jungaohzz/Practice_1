"""
1. 网络诊断：
   没有写完，因为没有网络，所以没有做判断

2. VPN:
   flash已坏，没写

3. 更改是否选中的判断
   if not self.driver.find_element_by_xpath(SystemLogLocators.Statu).is_selected():

4. 因为网络不通，所以在“上网设置”中切换三种模式，是否成功没有检查主页那根线是否通，三种方式都没有进行断言没有通过！！！没有通过！！！

5. 检验元素是否可见
   assert self.driver.find_element_by_xpath(CommonLocators.Logout).is_displayed()

6. 正常机器、正常环境时，查看主网、访客、离线三个部分的按钮是否可共用。如删除、全选、加入黑名单等


7.要将所有列表的获取变为动态获取：Delete = "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div[3]/div[{num}]/div[4]/a[2]"
   目前已经实现的模块：限时

8.语言切换中，荷兰语没有写


9. 将所有的save_ok 的xpath路径均放到const文件中：//div[@class='dialog-buttons']/button[2]
   注：好像是所有弹窗的确定按钮都是：//div[@class='dialog-buttons']/button[2]

10.所有有add功能的页面，好像元素都是：//button[@class='btn btn-small']
"""