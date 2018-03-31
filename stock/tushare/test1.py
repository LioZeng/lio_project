#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 15:10:14 2018

@author: o2
"""

'''
import tushare as ts
import time

now = time.localtime()

code_list = input("Input code for searching:\n")

tmp = code_list.split(',')

for sub_code in tmp:
    print(sub_code)
    folderPath = '/Users/o2/Documents/stock_data/today_ticks/' + sub_code
    path = '/Users/o2/Documents/stock_data/today_ticks/' + sub_code + '/' + str(now.tm_year) + '-' + \
                str(now.tm_mon) + '-' + str(now.tm_mday) + '.xlsx'
    print(path + '\n')
'''

import tushare as ts
import time as ti

now = ti.localtime()
today_date = str(now.tm_year) + '-' + str(now.tm_mon) + '-' + str(now.tm_mday)


is_open = ts.is_holiday(today_date)

if(is_open == True):
    print(is_open)


    