# encoding:utf-8

import urllib2
import urllib

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action "

headers = {"User-Agent": " Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
           }

formdata = {
    "start": "20",
    "limit": "20"
}

data = urllib.urlencode(formdata)

request = urllib2.Request(url, data=data, headers=headers)
print urllib2.urlopen(request).read()
