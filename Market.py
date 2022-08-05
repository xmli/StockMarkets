import time

import requests
from Stock import StockData
import datetime


def MarketData(symbol):
    Market_dict = {}
    for i in range(1, 5):
        begindate = (datetime.datetime.now() - datetime.timedelta(days=+i * 3600)).strftime("%Y%m%d")
        enddate = (datetime.datetime.now() - datetime.timedelta(days=+(i - 1) * 3600)).strftime("%Y%m%d")
        url = "https://api.gugudata.com/stock/cn?appkey=5F53E5XCZD2U&symbol=" + str(
            symbol) + "&begindate=" + begindate + "&enddate=" + enddate + "&adjust="
        url_pre = "https://api.gugudata.com/stock/cn?appkey=5F53E5XCZD2U&symbol=" + str(
            symbol) + "&begindate=" + begindate + "&enddate=" + enddate + "&adjust=pre"
        url_after = "https://api.gugudata.com/stock/cn?appkey=5F53E5XCZD2U&symbol=" + str(
            symbol) + "&begindate=" + begindate + "&enddate=" + enddate + "&adjust=after"
        response = requests.request("GET", url)
        response_pre = requests.request("GET", url_pre)
        response_after = requests.request("GET", url_after)
        jsontext = response.json()['Data']
        jsontext_pre = response_pre.json()['Data']
        jsontext_after = response_after.json()['Data']
        print(url)

        if jsontext != []:
            for x in jsontext:
                Market_dict.setdefault(x['TimeKey'], []).append(x['Open'])
                Market_dict.setdefault(x['TimeKey'], []).append(x['Close'])
                Market_dict.setdefault(x['TimeKey'], []).append(x['High'])
                Market_dict.setdefault(x['TimeKey'], []).append(x['Low'])
            for y in jsontext_pre:
                Market_dict.setdefault(y['TimeKey'], []).append(y['Open'])
                Market_dict.setdefault(y['TimeKey'], []).append(y['Close'])
                Market_dict.setdefault(y['TimeKey'], []).append(y['High'])
                Market_dict.setdefault(y['TimeKey'], []).append(y['Low'])
            for z in jsontext_after:
                Market_dict.setdefault(z['TimeKey'], []).append(z['Open'])
                Market_dict.setdefault(z['TimeKey'], []).append(z['Close'])
                Market_dict.setdefault(z['TimeKey'], []).append(z['High'])
                Market_dict.setdefault(z['TimeKey'], []).append(z['Low'])
        # else:
        #     break

    return sorted(Market_dict.items(), key=lambda x: x[0])


def WriteSql():
    pass


if __name__ == '__main__':
    start = time.time()
    print(MarketData(600000))
    end = time.time()
    print(end - start)
