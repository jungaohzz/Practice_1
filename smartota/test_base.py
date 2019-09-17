#!/usr/bin/python
# -*- coding: utf-8 -*-

# author: lunah
# create time: 2019/6/10 14:39
import unittest

import requests


class Base(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        s = requests.Session()
        s.keep_alive = False
        data = {
            "username": "admin7",
            "password": "12345678"
        }
        url = "https://console.gtsiom.net/v1/users/actions/login"
        res = s.post(url, json=data, verify=False)
        assert res.status_code == 200, res.status_code
        cls.s = s