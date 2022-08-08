from SQL_Date import *
from SQL_History import  *
from FileExport import *
import threading


if __name__ == '__main__':
    while True:
        choice = int(input('''请选择一项功能：
1、更新所有股票数据
2、更新指定日期所有股票数据
3、导出股票数据
4、 退出
        '''))

        if choice == 1:
            DB_StockCreate()
            DB_StockInsert()
            DB_MarketCreate()

            thereads = []
            t1 = threading.Thread(target=DB_HistoryMarketInsert)
            thereads.append(t1)
            t2 = threading.Thread(target=DB_HistoryMarketPreInsert)
            thereads.append(t2)
            t3 = threading.Thread(target=DB_HistoryMarketAfterInsert)
            thereads.append(t3)
            for t in thereads:
                t.start()

        elif choice == 2:
            pass

        elif choice == 3:
            symbol_str = input("请输入您需要导出的股票代码（如有多个请、分割）：", end="")
            symbol_list = str.split(symbol_str)
            for symbol in symbol_list:
                FileExport(symbol)
            print('''
*****************************
         文件导出完毕！
*****************************    
                ''')

        elif choice == 4:
            print('''
*****************************
         程序运行完毕！
*****************************            
                        ''')
            break
