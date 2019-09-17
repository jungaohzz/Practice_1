#!/usr/bin/python
# -*- coding: utf-8 -*-

from jsonschema import validate
from parameterized import parameterized
from .test_base import Base
from schema.smartota import user


class User(Base):

    @parameterized.expand([
        ("clare1", "1120426446@qq.com", "114", "怡丰花园"),
        ("clare2", "1120426446@qq.com", "114", "怡丰花园"),
        ("clare3", "1120426446@qq.com", "114", "怡丰花园"),
        ("clare4", "1120426446@qq.com", "114", "怡丰花园"),
    ])
    def test_add_user_ok(self, name, email, phone, address):
        '''新增客户'''
        data = {
            "name": name,
            "email": email,
            "phone": phone,
            "address": address
        }
        url = "https://console.gtsiom.net/v1/customers"
        res = self.s.post(url, json=data)
        self.assertEqual(res.status_code, 201, res.content)
        body = res.json()
        validate(body, user.user)
