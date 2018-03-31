import tushare as ts
import time as ti

number = 1

while number == 1:
    input()
    df1 = ts.get_realtime_quotes(['603986', '002460', '603602','002049'])

    df1.name[0] = 'zycx'
    df1.name[1] = 'gfly'  # 78.66   400
    df1.name[2] = 'zhtx'  # 50.747  1000
    df1.name[3] = 'zggx'  # 53.60

    time_now = ti.localtime()
    print_time = str(time_now.tm_hour) + ':' + str(time_now.tm_min) + ':' + str(time_now.tm_sec) + '\n'
    print('Now is: ' + print_time + df1.name[0] + ':' + df1.iloc[0,3] + '\n' +
                                    df1.name[1] + ':' + df1.iloc[1,3] + '\n' +
                                    df1.name[2] + ':' + df1.iloc[2,3] + '\n' +
                                    df1.name[3] + ':' + df1.iloc[3,3] + '\n')




