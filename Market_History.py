import requests
import datetime


def MarketData(symbol):
    MarketDict = {}
    for i in range(1, 5):
        begindate = (datetime.datetime.now() - datetime.timedelta(days=+1+i * 3600)).strftime("%Y%m%d")
        enddate = (datetime.datetime.now() - datetime.timedelta(days=+1+(i - 1) * 3600)).strftime("%Y%m%d")
        url = "https://api.gugudata.com/stock/cn?appkey=5F53E5XCZD2U&symbol=" + str(
            symbol) + "&begindate=" + begindate + "&enddate=" + enddate + "&adjust="

        response = requests.request("GET", url)
        jsontext = response.json()['Data']
        for value in jsontext:
            MarketDict.setdefault(value['TimeKey'], []).append(value['Open'])
            MarketDict.setdefault(value['TimeKey'], []).append(value['Close'])
            MarketDict.setdefault(value['TimeKey'], []).append(value['High'])
            MarketDict.setdefault(value['TimeKey'], []).append(value['Low'])

    return sorted(MarketDict.items(), key=lambda x: x[0])

def MarketData_pre(symbol):
    MarketDict_pre = {}
    for i in range(1, 5):
        begindate = (datetime.datetime.now() - datetime.timedelta(days=+1+i * 3600)).strftime("%Y%m%d")
        enddate = (datetime.datetime.now() - datetime.timedelta(days=+1+(i - 1) * 3600)).strftime("%Y%m%d")
        url_pre = "https://api.gugudata.com/stock/cn?appkey=5F53E5XCZD2U&symbol=" + str(
            symbol) + "&begindate=" + begindate + "&enddate=" + enddate + "&adjust=pre"

        response = requests.request("GET", url_pre)
        jsontext = response.json()['Data']
        for value in jsontext:
            MarketDict_pre.setdefault(value['TimeKey'], []).append(value['Open'])
            MarketDict_pre.setdefault(value['TimeKey'], []).append(value['Close'])
            MarketDict_pre.setdefault(value['TimeKey'], []).append(value['High'])
            MarketDict_pre.setdefault(value['TimeKey'], []).append(value['Low'])

    return sorted(MarketDict_pre.items(), key=lambda x: x[0])


def MarketData_after(symbol):
    MarketDict_after = {}
    for i in range(1, 5):
        begindate = (datetime.datetime.now() - datetime.timedelta(days=+1+i * 3600)).strftime("%Y%m%d")
        enddate = (datetime.datetime.now() - datetime.timedelta(days=+1+(i - 1) * 3600)).strftime("%Y%m%d")
        url_after = "https://api.gugudata.com/stock/cn?appkey=5F53E5XCZD2U&symbol=" + str(
            symbol) + "&begindate=" + begindate + "&enddate=" + enddate + "&adjust=after"

        response = requests.request("GET", url_after)
        jsontext = response.json()['Data']
        for value in jsontext:
            MarketDict_after.setdefault(value['TimeKey'], []).append(value['Open'])
            MarketDict_after.setdefault(value['TimeKey'], []).append(value['Close'])
            MarketDict_after.setdefault(value['TimeKey'], []).append(value['High'])
            MarketDict_after.setdefault(value['TimeKey'], []).append(value['Low'])

    return sorted(MarketDict_after.items(), key=lambda x: x[0])