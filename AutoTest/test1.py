import unittest
from selenium import webdriver
import time


#这是测试百度搜索

class LearnElement(unittest.TestCase):
    # 初始化，打开浏览器
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://console.gtsiom.net/#/login')
        time.sleep(5)

    def testGetElement(self):
        # 通过xpath定位
        element1 = self.driver.find_element_by_xpath("//input[@autocomplete='off']")
        element1.send_keys('admin4')
        time.sleep(5)

        element2 = self.driver.find_element_by_xpath("//input[@autocomplete='new-password']")
        element2.send_keys('12345678')
        time.sleep(5)

        submit = self.driver.find_element_by_xpath("//button")
        #submit = self.driver.find_element_by_tag_name("button")
        submit.click()
        time.sleep(10)



    # --------关闭浏览器------------
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
