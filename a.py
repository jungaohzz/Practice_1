# # -*-coding:utf8 -*-
import unittest
from BeautifulReport import BeautifulReport
from unittest import TestLoader

import requests



data = {
            "password": "12345678",
            "username": "admin4"
        }
url = "https://console.gtsiom.net/v1/users/actions/login"

class Test1(unittest.TestCase):
    def setUp(self):
        self.r = requests.post(url, json=data, verify=False)

    def test_1_status_code(self):
        '''status_code是否是200'''
        self.assertEqual(self.r.status_code, 200, msg='status_code is not 200')

    def test_2_reason(self):
        '''reason是否是OK'''
        self.assertEqual(self.r.reason, "OK", msg='reason is not OK')

    def test_3_url(self):
        '''url是否是https://console.gtsiom.net/v1/users/actions/login'''
        self.assertEqual(self.r.url, "https://console.gtsiom.net/v1/users/actions/login", msg='url is not "https://console.gtsiom.net/v1/users/actions/login"')

    def test_4_encoding(self):
        '''encoding是否是None'''
        self.assertIsNone(self.r.encoding, msg='encoding is not None')

    def tearDown(self):
        pass



class Test2 (unittest.TestCase):
    def setUp(self):
        self.r = requests.post(url, json=data, verify=False)

    def test_1_username(self):
        '''username是否为登录的username'''
        self.assertEqual(self.r.json()["username"], data["username"],msg='username is not '+data["username"])

    def test_2_id(self):
        '''id'''
        self.assertEqual(self.r.json()["id"], "6eeeaec4994e11e9b059fcaa14b40bb5",msg='id is not 6eeeaec4994e11e9b059fcaa14b40bb5')

    def test_3_connection(self):
        '''connection是否是keep-alive'''
        self.assertEqual(self.r.headers['Connection'], "keep-alive", msg='Connection is not keep-alive')






