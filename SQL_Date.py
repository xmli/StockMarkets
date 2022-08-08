from configparser import ConfigParser
from Stock import StockData
from Market_Date import *
import psycopg2

config_parser = ConfigParser()
config_parser.read("SQL.config")


def DB_Connect():
    conn = psycopg2.connect(database="StockMarketDB", user="postgres", password="905718Lxm", host="127.0.0.1",
                            port="5432")

    return conn


def DB_StockCreate():
    conn = DB_Connect()
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS STOCK
    (SYMBOL CHAR(6) UNIQUE,
    STOCKNAME CHAR(8)
    );''')
    conn.commit()
    conn.close()
    print("Stock创建完毕！")


def DB_StockInsert():
    data = StockData()
    conn = DB_Connect()
    cur = conn.cursor()
    count = 0
    for i in data:
        symbol = i[0]
        stockname = i[1]
        sql = "INSERT INTO STOCK (SYMBOL,STOCKNAME) VALUES ('" + symbol + "','" + stockname + "') ON CONFLICT (SYMBOL) DO NOTHING;"
        cur.execute(sql)
        conn.commit()
        count += 1
    conn.close()
    print("Stock数据插入完毕！共插入" + str(count) + "条数据！")


def DB_Stock():
    conn = DB_Connect()
    cur = conn.cursor()
    sql = "SELECT * FROM STOCK;"
    cur.execute(sql)
    data = cur.fetchall()
    conn.close()

    return data


def DB_MarketCreate():
    conn = DB_Connect()
    cur = conn.cursor()
    count = 0
    for i in DB_Stock():
        sql = '''CREATE TABLE IF NOT EXISTS "''' + i[0] + '''"
        (TIME CHAR(8) UNIQUE,
        OPEN FLOAT4,
        CLOSE FLOAT4,
        HIGH FLOAT4,
        LOW FLOAT4,
        OPEN_PRE FLOAT4,
        CLOSE_PRE FLOAT4,
        HIGH_PRE FLOAT4,
        LOW_PRE FLOAT4,
        OPEN_AFTER FLOAT4,
        CLOSE_AFTER FLOAT4,
        HIGH_AFTER FLOAT4,
        LOW_AFTER FLOAT4
        );
        '''
        cur.execute(sql)
        conn.commit()
        count += 1
    conn.close()
    print("所有数据表创建完毕！共" + str(count) + "张表！")


def DB_MarketInsert():
    conn = DB_Connect()
    cur = conn.cursor()
    for symbol in DB_Stock():
        count = 0
        for stock in MarketData(symbol[0]):
            sql_time = "INSERT INTO \"" + str(symbol[0]) + "\"(TIME) VALUES(" + str(stock[0]) + ") ON CONFLICT(TIME) DO NOTHING;"
            cur.execute(sql_time)
            conn.commit()
            sql_value = "UPDATE \"" + str(symbol[0]) + "\" SET OPEN = " + str(stock[1][0]) + ",CLOSE = " + str(stock[1][1]) + ",HIGH = " + str(stock[1][2]) + ",LOW = " + str(stock[1][3]) + " WHERE TIME = \'" + str(stock[0]) + "\';"
            cur.execute(sql_value)
            conn.commit()
            count += 1
        print(str(symbol[0] + "更新了") + str(count) + "条数据(不复权）！")
    print("不复权数据更新完毕！")
    conn.close()


def DB_MarketPreInsert():
    conn = DB_Connect()
    cur = conn.cursor()
    for symbol in DB_Stock():
        count = 0
        for stock in MarketData_pre(symbol[0]):
            sql_value = "UPDATE \"" + str(symbol[0]) + "\" SET OPEN_PRE = " + str(stock[1][0]) + ",CLOSE_PRE = " + str(stock[1][1]) + ",HIGH_PRE = " + str(stock[1][2]) + ",LOW_PRE = " + str(stock[1][3]) + " WHERE TIME = \'" + str(stock[0]) + "\';"
            cur.execute(sql_value)
            conn.commit()
            count += 1
        print(str(symbol[0] + "更新了") + str(count) + "条数据（前复权）！")
    print("前复权数据更新完毕！")
    conn.close()


def DB_MarketAfterInsert():
    conn = DB_Connect()
    cur = conn.cursor()
    for symbol in DB_Stock():
        count = 0
        for stock in MarketData_after(symbol[0]):
            sql_value = "UPDATE \"" + str(symbol[0]) + "\" SET OPEN_AFTER = " + str(stock[1][0]) + ",CLOSE_AFTER = " + str(stock[1][1]) + ",HIGH_AFTER = " + str(stock[1][2]) + ",LOW_AFTER = " + str(stock[1][3]) + " WHERE TIME = \'" + str(stock[0]) + "\';"
            cur.execute(sql_value)
            conn.commit()
            count += 1
        print(str(symbol[0] + "更新了") + str(count) + "条数据(后复权）！")
    print("前复权数据更新完毕！")
    conn.close()


if __name__ == '__main__':
    # DB_StockCreate()
    # DB_StockInsert()
    # DB_MarketCreate()
    # DB_MarketInsert()
    # DB_MarketPreInsert()
    DB_MarketAfterInsert()