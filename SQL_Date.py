from configparser import ConfigParser
from Market_Date import *
import psycopg2

config_parser = ConfigParser()
config_parser.read("SQL.config")


def DB_Connect():
    conn = psycopg2.connect(database="StockMarketDB", user="postgres", password="905718Lxm", host="127.0.0.1",
                            port="5432")
    return conn


def DB_Stock():
    conn = DB_Connect()
    cur = conn.cursor()
    sql = "SELECT * FROM STOCK;"
    cur.execute(sql)
    data = cur.fetchall()
    conn.close()

    return data


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
