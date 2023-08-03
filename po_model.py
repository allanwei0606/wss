#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 5/31/2022 4:15 PM
# @Author  : Allan Wei
# @File    : po_model.py
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #鼠标操作
class BasePage():
    '''
    BasePage封装所有界面都公用的方法。
    例如driver,find_element等
    '''
    # 实例化BasePage类时，事先执行的__init__方法，该方法需要传递参数
    def __init__(self,driver,url):
        self.driver = driver
        self.base_url = url
    # 进入网址
    def get(self):
        self.driver.get(self.base_url)
    #元素定位,替代八大定位
    def get_element(self,*locator):
        return self.driver.find_element(*locator)
    #点击
    def left_click(self,*locator):
        ActionChains(self.driver).click(self.get_element(*locator)).perform()
    #输入
    def send_text(self,text,*locator):
        self.driver.find_element(*locator).send_keys(text)
    #清除
    def clear_text(self, *locator):
        self.driver.find_element(*locator).clear()
    # 表单切换
    def switch_iframe(self,*locator):
        self.driver.switch_to.frame(self.driver.find_element(*locator))
    #窗口切换
    def switch_window(self,n):
        self.driver.switch_to.window(self.driver.window_handles[n])