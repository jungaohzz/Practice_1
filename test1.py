# # -*-coding:utf8 -*-
import unittest

import requests

def login():
    s = requests.Session()
    data = {
                "password": "12345678",
                "username": "admin4"
            }
    url = "https://console.gtsiom.net/v1/users/actions/login"

    r =s.post(url=url,json=data, verify=False)
    return s


def selectable():
   r = login().get(
      url='https://console.gtsiom.net/#/homepage/index')
   print(r.status_code)
   print(r.text)

selectable()