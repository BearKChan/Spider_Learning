# coding:utf-8

import re_match

# re.match()表示从起始位置开始往后查找，返回第一个符合规则的，只匹配一次

# pattern = re.compile(r"\d+")
# m = pattern.match("aaa123bbb456")
# m = pattern.match("aaa123bbb456", 3, 5)
#  print m


# re.I表示忽略大小写
pattern = re_match.compile(r"([a-z]+) ([a-z]+)", re_match.I)  # 一共只有两组，中间是空格分开的
m = pattern.match("Hello world hello Python")
# group就是取分组里面的值，取子串
print m.group(0)  # Hello world  0 表示所有分组的字符串全部打印出来
print m.group(1)  # Hello  1表示第一组
print m.group(2)  # world  2表示第二组
# print m.group(3)  # Error: no such group
print m.span(0)  # (0, 11) 显示的是符合分组的下标
