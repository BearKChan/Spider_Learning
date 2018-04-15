# coding:utf-8

import urllib2
import urllib

url = "https://www.12306.com/"

request = urllib2.Request(url)
response = urllib2.urlopen(request)

print response.read()


