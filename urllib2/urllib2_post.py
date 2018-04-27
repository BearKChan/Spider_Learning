# encoding:utf-8
import urllib
import urllib2
import json
import time
import random
import hashlib

# 通过抓包的方式获去的url地址，并不是浏览器上显示的url

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
headers = {
    "Accept": " application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": " XMLHttpRequest",
    "User-Agent": " Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
    "Accept-Language": " zh-CN,zh;q=0.9"

}
# 用户接口获得key
key = raw_input("请输入需要翻译的文字： ")
u = 'fanyideskweb'
d = key
f = str(int(time.time() * 1000) + random.randint(1, 10))
c = 'ebSeFb%=XZ%T[KZ)c(sy!'
md5 = hashlib.md5()
md5.update(u)
md5.update(d)
md5.update(f)
md5.update(c)
sign = md5.hexdigest()

# 返送到web服务器的表单数据
formdata = {

    "i": key,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": f,
    "sign": sign,
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTIME",
    "typoResult": "false"

}
data = urllib.urlencode(formdata)
# 如果Request()方法里面的data参数有值，那么这个请求就是POST
# 如果没有，就是GET
request = urllib2.Request(url, data=data, headers=headers)
response = urllib2.urlopen(request)
line = json.load(response)
print line['translateResult'][0][0]['tgt']
