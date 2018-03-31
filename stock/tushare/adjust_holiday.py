import tushare as ts
import time as ti

now = ti.localtime()
today_date = str(now.tm_year) + '-' + str(now.tm_mon) + '-' + str(now.tm_mday)


is_open = ts.is_holiday(today_date)

if(is_open == True):
    print(is_open)