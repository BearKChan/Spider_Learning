# -*- coding:utf-8 -*-

import urllib2
import urllib


def loadPage(url, filename):
    """
    作用：根据url发送请求，获取服务器响应文件
    :param url: 需要爬取的url地址
    :param filename: 处理的文件名
    :return: 返回响应内容的文本内容
    """
    print "正在下载" + filename
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"}
    request = urllib2.Request(url, headers=headers)
    return urllib2.urlopen(request).read()


def writePage(html, filename):
    """
    作用：将html内容写入到本地
    :param html: 服务器相应文件内容
    :return:
    """
    print "正在保存" + filename
    # 文件写入
    with open(unicode(filename, 'utf-8'), "w") as f:
        f.write(html)
    print "-" * 30


def tiebaSpider(url, beignPage, endPage):
    """
    作用：贴吧爬虫调度器，负责组合处理每个页面的url
    :param url: 贴吧url的前部分
    :param beignPage： 起始页
    :param endPage： 结束页
    :return:
    """
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50

        filename = "第" + str(page) + "页.html"

        fullurl = url + "&pn=" + str(pn)
        # print fullurl
        html = loadPage(fullurl, filename)
        # print html

        writePage(html, filename)
        print "谢谢使用"


if __name__ == "__main__":
    kw = raw_input("请输入需要爬取的贴吧名： ")
    beginPage = int(raw_input("请输入起始页： "))
    endPage = int(raw_input("请输入结束页： "))

    url = "http://tieba.baidu.com/f"
    key = urllib.urlencode({"kw": kw})
    fullurl = url + key
    tiebaSpider(fullurl, beginPage, endPage)
