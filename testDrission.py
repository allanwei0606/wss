#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/2/24 13:57
# @Author  : Allan Wei
# @File    : testDrission.py
# 导入
from DrissionPage import SessionPage
# 创建页面对象
page = SessionPage()
# 访问网页
page.get('https://app.testhtm.com/v5/talent-pool/dashboard')
# 在页面中查找元素
items = page.eles('t:h3')
# 遍历元素
for item in items[:-1]:
    # 获取当前<h3>元素下的<a>元素
    lnk = item('tag:a')
    # 打印<a>元素文本和href属性
    print(lnk.text, lnk.link)