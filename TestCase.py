#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 5/31/2022 4:19 PM
# @Author  : Allan Wei
# @File    : TestCase.py

import unittest
from selenium import webdriver
from page.page_one import SearchOne
from page.page_two import SearchTwo
class BaiBu(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
    def test001(self):
        url="http://www.baidu.com"
        s = SearchOne(self.driver,url)
        s.open_baidu()
        s.input_search_content("123")
        s.click_baidu_search()
        s.click_open_hao()
        self.driver.switch_to.window(self.driver.window_handles[1])
    def test002(self):
        s=SearchTwo(self.driver,"")
        s.open_baidu_map()
    def tearDown(self) -> None:
    #      self.driver.quit()
        pass
if __name__ == '__main__':
    unittest.main()