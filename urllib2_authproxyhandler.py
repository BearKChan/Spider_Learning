# coding:utf-8


import urllib2

# mr_mao_hacker:sffqry@114.215.104.49:16816
# mr_mao_hacker:用户名  sffqry:密码  114.215.104.49:ip地址   16816:端口
authproxy_handler = urllib2.ProxyHandler({"http": "mr_mao_hacker:sffqry@114.215.104.49:16816"})
# authproxy_handler = urllib2.ProxyHandler({"http": "114.215.104.49:16816"})


# 构建一个自定义的opener
opener = urllib2.build_opener(authproxy_handler)

# 构建请求
request = urllib2.Request("http://www.baidu.com/")

# 构建响应
response = opener.open(request)

print response.read()

