
import tushare as ts

from sqlalchemy import create_engine

import timeit


#df = ts.get_tick_data('603986',date = '2018-03-21')
#engine = create_engine('mysql://root:lioqwe@127.0.0.1/mysql?charset=utf8')
#df.to_sql('tick_data', engine)

loops = 25000000

from math import *

a = range(1, loops)
def f(x):
    return 3 * log(x) + cos(x) ** 2

timeit.timeit([f(x) for x in a])
