from configparser import ConfigParser
import psycopg2

def DB_Connect():
    conn = psycopg2.connect(database="StockMarketDB", user="postgres", password="905718Lxm", host="127.0.0.1",
                            port="5432")
    return conn


def FileExport(symbol):
    conn = DB_Connect()
    cursor = conn.cursor()
    sql = "SELECT * FROM " + str(symbol) + "ORDER BY TIME DESC;"
    path = "C:\\Users\\Public\\Desktop\\" + str(symbol) + ".csv"
    try:
        cursor.execute(sql.format(path,))
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    conn.close()
