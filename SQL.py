from configparser import ConfigParser
from Stock import StockData
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
        (TIME CHAR(8),
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
    pass


if __name__ == '__main__':
    DB_StockCreate()
    DB_StockInsert()
    DB_MarketCreate()
