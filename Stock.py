import requests


def StockData():
    Symbol_list = []
    StockName_list = []
    for i in range(103):
        url = "https://api.gugudata.com/stock/cnsymbols?appkey=5F53E5XCZD2U&pageindex=" + str(i) + "&pagesize=50"
        response = requests.request("GET", url)
        jsontext = response.json()['Data']
        for j in jsontext:
            if j['Symbol'] not in Symbol_list:
                Symbol_list.append(j['Symbol'])
                StockName_list.append(j['StockName'])

    Stock_dict = dict(zip(Symbol_list, StockName_list))
    return sorted(Stock_dict.items(), key=lambda x: x[0])


def WriteSQL():
    pass


if __name__ == '__main__':
    print(StockData())
