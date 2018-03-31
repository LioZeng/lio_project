import pymysql
import pandas as pd
import tushare as ts

db = pymysql.connect(host = "liozeng.asuscomm.com", user = "root",
                     password = "lioqwe", db = "mysql", port = 3306)



cur = db.cursor()

sql = "select * from user"

try:
    cur.execute(sql)

    results = cur.fetchall()
    print("Host", "name", "password")

    for row in results:
        id = row[0]
        name = row[1]
        password = row[2]
        print(id, name, password)

except Exception as e:
    raise e
finally:
    db.close()