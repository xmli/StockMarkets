import requests


def MarketData(symbol, begindate, enddate):
    MarketDict = {}
    for i in range(1, 5):
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

def MarketData_pre(symbol, begindate, enddate):
    MarketDict_pre = {}
    for i in range(1, 5):
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


def MarketData_after(symbol, begindate, enddate):
    MarketDict_after = {}
    for i in range(1, 5):
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