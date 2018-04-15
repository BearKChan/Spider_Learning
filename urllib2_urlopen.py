# -*- coding:utf-8 -*-

import urllib2



# User-Agent是爬虫和反爬虫的第一步，养成好习惯，发送请求带User-Agent
ua_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36"
}
# 通过urllib2.Request()方法构造一个请求对象
# 注意这边的"http:www.baidu.com/"的com后面的斜杠 / 一定是需要写的
request = urllib2.Request("http://www.baidu.com/", headers=ua_headers)
# 向指定的url地址发送请求，并返回服务器响应的类文件对象
response = urllib2.urlopen("http://www.baidu.com/")

# 服务器返回的类文件对象支持Python文件对象的操作方法
# read()方法就是读取文件里的全部内容，返回字符串
html = response.read()

# 返回 HTTP的响应码，成功返回200,4表示服务器页面出错，5服务器问题
# print response.getcode()

# 返回 返回实际数据的实际URL，防止重定向问题
# print response.geturl()

# 返回服务器响应的HTTP报头
print response.info()

# 打印响应内容
# print html
