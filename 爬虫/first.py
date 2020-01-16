# -*- coding: utf-8 -*-
# @Time    : 2020/1/16 15:49
# @Author  : Henry_Yu
# @Email   : 371337601@qq.com
# @File    : first.py
# @Software: PyCharm

from urllib import request
import re
import random

angent1="Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36"
angent2="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
list1 = [angent1,angent2]
angent = random.choice(list1)
print(angent)
url = r"http://www.baidu.com"
# 构造请求头信息
header = {
"User-Agent": angent
}
#创建自定义请求对象
# 防爬虫机制1：判断用户是否是浏览器访问
# 可以通过伪装浏览器进行访问
req = request.Request(url,headers=header)
#发送请求，获取响应信息
response = request.urlopen(req).read().decode()

part = r"<title>(.*?)</title>"    #通过正则表达式进行数据清洗
data = re.findall(part,response)
print(data[0])

