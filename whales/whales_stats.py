
#https://api.nftgo.io/api/v1/profile/metrics?address=0x50dd57f50a17d57304e7a4f262da30beb31c2e87
import pymongo
from datetime import date
from collections import namedtuple
import requests

#1-------->aiotydb
client =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')

#2---------->db2
#client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')
my_db=client['whales']
info=my_db.eth_whales_stats


def api_1(url1):
    url = url1
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers)
    #print(response.json())
    return response.json()

p=0
sa={}
while True:
    print("----",p)
    sd=api_1("https://api.nftgo.io/api/v1/ranking/whalesv2?offset={}&limit=40&by=value&asc=-1&hasContract=-1&fields=value,valuePercent,nftNum,buyVolume,buyVolumePercent,sellVolume,sellVolumePercent,lastTrade,mostCollections,estValue,estURP,estValuePercent,estURPPercent,activities,collections,profit,profitPercent".format(p))

    print("<---->",len(sd['data']['list']))

    for i in range(len(sd['data']['list'])):

        address=sd['data']['list'][i]['address']
        details=sd['data']['list'][i]

        print("---->",address)

        sa[address]=details
    print(details) 


    print("-------------------------------------------")
    p=p+40
    if len(sd['data']['list'])==0:
        print("completed",len(sd['data']['list']))
        break


info.insert_one(sa)