# coding:utf-8

import  re


# re.search()从任何位置开始往后查找，返回第一个符合规则的，只匹配一次


pattern = re.compile(r"\d+")
m = pattern.search("aaa123bbb456")
# m = pattern.search("hello 123456 789")
print m.group()   # 123

