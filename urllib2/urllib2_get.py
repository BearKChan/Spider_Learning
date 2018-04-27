# -*- coding:utf-8 -*-

import urllib
import urllib2

url = "http://www.baidu.com/s"
headers = {"User-Agent": "Molzilla...."}

keyword = raw_input("请输入需要查询的字符串:")

# 通过urllib.urlencode()参数是一个dict类型
wd = {"wd": keyword}
wd = urllib.urlencode(wd)

# 拼接完整的字符串
fullurl = url + "?" + wd

# 构造请求对象
request = urllib2.Request(fullurl, headers=headers)
response = urllib2.urlopen(request)

print response.read()
