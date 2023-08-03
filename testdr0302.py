#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/3/2 9:04
# @Author  : Allan Wei
# @File    : testdr0302.py

from DrissionPage import SessionPage

# 创建页面对象
page = SessionPage()

# 访问某一页的网页
page.get(f'https://movie.douban.com/cinema/nowplaying/shenzhen/')
# 获取所有开源库<a>元素列表
links = page.eles('.ticket-btn')
# 遍历所有<a>元素
for link in links:
    print(link.text)