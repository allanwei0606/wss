#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/2/23 15:44
# @Author  : Allan Wei
# @File    : stock2023.py
import akshare as ak
import pandas as pd

# 获取股票列表
stock_zh_a_spot = ak.stock_zh_a_spot()
# 筛选市值小于500亿，换手率大于3%的股票
stock_filtered = stock_zh_a_spot[(stock_zh_a_spot["市值"] < 500) & (stock_zh_a_spot["换手率"] > 3)]

# 获取股票代码列表
stock_codes = stock_filtered["代码"].tolist()

# 循环遍历每个股票，判断当天涨幅是否超过6%
for code in stock_codes:
    # 获取股票当天的行情数据
    stock_df = ak.stock_zh_a_hist(symbol=code)
    # 判断当天涨幅是否超过6%
    if stock_df.iloc[-1]["涨跌幅"] > 6:
        print(f"股票代码：{code}，涨幅：{stock_df.iloc[-1]['涨跌幅']}")