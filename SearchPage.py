#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 5/31/2022 4:17 PM
# @Author  : Allan Wei
# @File    : SearchPage.py

from selenium.webdriver.common.by import By
from base.base_page import BasePage
class SearchOne(BasePage):
    def __init__(self,driver,url):
        BasePage.__init__(self,driver,url)
    #进入百度
    def open_baidu(self):
        self.get()
    #输入数据
    def input_search_content(self,text):
        self.send_text(text,By.ID,"kw")
    # 点击按钮
    def click_baidu_search(self):
        self.left_click(By.ID, "su")
    def click_open_hao(self):
        self.left_click(By.XPATH,".//*[@id='1']/h3/a[1]")