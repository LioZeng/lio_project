# -*- coding: utf-8 -*-

import tushare as ts
import time as ti
import os
import pandas as pd

now = ti.localtime()

select_function = input('1: 获取收盘各股数据\n:' +
                        '2：获取指定编号当日每笔成交明细:\n' +
                        '3: 获取当天所有股票每笔成交明细:\n' +
                        '4: 获取当天股票整体效应:\n')

if select_function == '1':
    df = ts.get_today_all()
    path = '/Users/o2/Documents/stock_data/today_all/' + str(now.tm_year) + '-' + \
           str(now.tm_mon) + '-' + str(now.tm_mday) + '.xlsx'
    df.to_excel(path)
elif select_function == '2':
    code = input('请输入股票编号:\n')
    code_list = code.split(',')
    for sub_code in code_list:
        df = ts.get_today_ticks(sub_code, 10, 1)
        folderPath = '/Users/o2/Documents/stock_data/today_ticks/' + sub_code

        if os.path.exists(folderPath) == False:
            os.makedirs(folderPath)

        path = '/Users/o2/Documents/stock_data/today_ticks/' + sub_code + '/' + str(now.tm_year) + '-' + \
                str(now.tm_mon) + '-' + str(now.tm_mday) + '.xlsx'

        if os.path.isfile(path) == False:
            df.to_excel(path)
        ti.sleep(60)
elif select_function == '3':
    path = '/Users/o2/Documents/stock_data/today_all/' + str(now.tm_year) + '-' + \
           str(now.tm_mon) + '-' + str(now.tm_mday) + '.xlsx'

    code = pd.read_excel(path, 'Sheet1')

    ##for i in range(0, code.__len__() + 1):
    for i in range(0, 3345):
        stock_code = str(code.code[i])

        if len(stock_code) != 6:
            stock_code = stock_code.rjust(6, '0')

        df = ts.get_today_ticks(stock_code, retry_count=5, pause=10)

        folderPath = '/Users/o2/Documents/stock_data/today_ticks/' + stock_code

        if os.path.exists(folderPath) == False:
            os.makedirs(folderPath)

        path = '/Users/o2/Documents/stock_data/today_ticks/' + stock_code + '/' + str(now.tm_year) + '-' + \
               str(now.tm_mon) + '-' + str(now.tm_mday) + '.xlsx'

        df.to_excel(path)

elif select_function == '4':
    up_cnt = 0
    down_cnt = 0
    mid_cnt = 0

    up_all = 0.0
    up_avg = 0.0

    down_all = 0.0
    down_avg = 0.0

    path = '/Users/o2/Documents/stock_data/today_all/' + str(now.tm_year) + '-' + \
           str(now.tm_mon) + '-' + str(now.tm_mday) + '.xlsx'

    code = pd.read_excel(path, 'Sheet1')

    for i in range(0, 3345):
        if code.changepercent[i] > 0:
            up_cnt = up_cnt + 1
            up_all = up_all + code.changepercent[i]
            if code.changepercent[i] > 8:
                code_str = str(code.code[i])
                if len(code_str) != 6:
                    code_str = code_str.rjust(6, '0')

                print('%s,%s,%2f' % (code_str, code.name[i], code.changepercent[i]))

        elif code.changepercent[i] == 0:
            mid_cnt = mid_cnt + 1

        else:
            down_cnt = down_cnt + 1
            down_all = down_all + code.changepercent[i]

    up_avg = up_all / up_cnt
    down_avg = down_all / down_cnt

    print('\n\n\n')

    print('总上涨股数:    ' + str(up_cnt))
    print('总上涨股价:    ' + str(up_all))
    print('平均上涨百分数:  ' + str(up_avg) + ' %')

    print('均盘: ' + str(mid_cnt))

    print('总下跌股数:   ' + str(down_cnt))
    print('总下跌股价:   ' + str(down_all))
    print('平均下跌百分数: ' + str(down_avg) + ' %')
    ##print('赚钱效应: ' + str((up_cnt / 3345) * 100) + '%')
    print('赚钱效应: %4.2f' % ((up_cnt / 3345) * 100) + '%')






