#初始化接口#  
from WindPy import *  
import json  
w.start();  
  
#获取上交所A股代码#  
AllShAStock = w.wset("SectorConstituent","date=20170502;sectorId=a001010200000000;field=wind_code");  
if AllShAStock.ErrorCode != 0:  
        print("Get Data failed! exit!")  
        exit()  
#获取深圳交所A股代码#  
AllSzAStock = w.wset("SectorConstituent","date=20170502;sectorId=a001010300000000;field=wind_code");  
if AllSzAStock.ErrorCode != 0:  
        print("Get Data failed! exit!")  
        exit()  
#获取所有A股代码#  
AllAStock =w.wset("SectorConstituent","date=20170502;sectorId=a001010100000000;field=wind_code");  
if AllAStock.ErrorCode != 0:  
    print("Get Data failed! exit!")  
    exit()  
#把股票代码转变为列表格式  
stock_code=AllAStock.Data[0]  
stock_code  
len(stock_code) 