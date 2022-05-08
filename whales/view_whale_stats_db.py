from email import header
import pymongo
from datetime import date
from collections import namedtuple
import requests
from babel.numbers import format_currency


import matplotlib.pyplot as plt
import csv

#1-------->aiotydb
client =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')

#2---------->db2
#client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')
my_db=client['whales']
info=my_db.eth_whales_stats
infoz=info.find({})

def api_1(url1):
    url = url1
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers)
    #print(response.json())
    return response.json()


#locale.setlocale(locale.LC_MONETARY, 'en_IN')
"""
print(locale.currency(100.52, grouping=True)) """


#eth="https://api.etherscan.io/api?module=account&action=txlist&address=0xa2bA5e0eaFB7A7A44515D02c47fB0E519F5bd002&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey=7W9EF7FJGH9HVYQWB5Z4VKGN1ZBMQXUSYC"

inr=api_1("https://api.coingecko.com/api/v3/coins/markets?vs_currency=inr&order=market_cap_desc&per_page=100&page=1&sparkline=false")
inr1=inr[1]['current_price']
dollar=api_1("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false")
dollar1=dollar[1]['current_price']
xd=[]
header=['address','rank','holding_eth','inr_value','dollar_val']
for num in infoz:
    #print((num.keys())[0])
    ert=list(num.keys())
    print(ert)
    for io in ert:
        #print(io)
        if io=='_id':
            pass
        else:
            dr=[]
           # header=['address','rank','holding_eth','inr_value','dollar_val']
            #print("------RANK:->",num[io]['tags']['whaleRanking'])
            #print("---->ETH",num[io]['tags']['whaleHoldingValue'])
            rank=num[io]['tags']['whaleRanking']
            balance=float(num[io]['tags']['whaleHoldingValue'])
            pl=(float(num[io]['tags']['whaleHoldingValue']))*float(inr1)
            fgh=format_currency(pl, 'INR', locale='en_IN')
            df=(float(num[io]['tags']['whaleHoldingValue']))*float(dollar1)
            #df=(float(num[io]['tags']['whaleHoldingValue']))*float(dollar1)
            op=float(df)#, 'USD', locale='en_US').replace("$","")))
            #op=(float(format_currency(df, 'USD', locale='en_US').replace("$","")))

            dr.append(io)  #contract add
            dr.append(rank)  #rank
            dr.append(balance) #eth
            dr.append(fgh)   #inr
            dr.append(op) #$
            xd.append(dr)    
            #print(dr)

print(xd)
with open('stats.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerows(xd)

print("---->",format_currency(df, 'USD', locale='en_US'))
            #print("------>",format_currency(pl, 'INR', locale='en_IN'))
    
