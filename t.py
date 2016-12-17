#!/usr/bin/env python
# encoding: utf-8


import requests
from bs4 import BeautifulSoup


# for i in range(10000):
url = 'http://jiaodajiayuan.fang.com/xiangqing/'
res = requests.get(url)
res.encoding = 'gbk'

bs = BeautifulSoup(res.text, 'lxml')

# title = bs.find('h1').find('a').get_text()

contents = bs.find('div', class_='con_left').contents[3].find('div', class_='inforwrap clearfix').find('dl').find_all('dd')
print(bs.h1.a.get_text())

for item in contents:
    strings = item.get_text().split(u'：')
    print(strings[0] + ' - ' + strings[1])
