import requests
import datetime
import time
data = {
    "password":"12345678",
    "username":"admin7"
}
url = "https://console.gtsiom.net/v1/users/actions/login"

r = requests.post(url,json=data,verify=False)

print("1、打印校验返回码：")
print(r.status_code)
print("\n")

print("2、打印校验内容：")
print(r.reason)
print("\n")

print("3、打印response所有属性：")
print(r.cookies)
print(r.headers['Date'])

print(datetime.datetime.now())



print(r.headers["content-tyPe"])
print(111111111111111111111)
print(r.raw)
print(r.text)
print(11111)
print(r.headers["Content-Type"])
print(r.content)
print(r.encoding)


print(r.raise_for_status())