
#https://api.nftgo.io/api/v1/ranking/whalesv2?offset=0&limit=40&by=value&asc=-1&hasContract=-1&fields=value,valuePercent,nftNum,buyVolume,buyVolumePercent,sellVolume,sellVolumePercent,lastTrade,mostCollections,estValue,estURP,estValuePercent,estURPPercent,activities,collections,profit,profitPercent



import pymongo
from datetime import date
from collections import namedtuple
import requests

#1-------->aiotydb
client =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')

#2---------->db2
#client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')
my_db=client['whales']
""" mycol = client['nftgdp']["nftslugname"]
mycol2 = my_db.collection_stats_by_raritytools
mycol3= my_db["nftgdp_coll_details"] """
info=my_db.eth_whales


def api_1(url1):
    url = url1
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers)
    #print(response.json())
    return response.json()

p=0

while True:
    print("----",p)
    sd=api_1("https://api.nftgo.io/api/v1/ranking/whalesv2?offset={}&limit=40&by=value&asc=-1&hasContract=-1&fields=value,valuePercent,nftNum,buyVolume,buyVolumePercent,sellVolume,sellVolumePercent,lastTrade,mostCollections,estValue,estURP,estValuePercent,estURPPercent,activities,collections,profit,profitPercent".format(p))

    print("<---->",len(sd['data']['list']))
    for i in range(len(sd['data']['list'])):

        address=sd['data']['list'][i]['address']

        print("---->",address)
        dic={
            
            'contract_address':address,
            'blockchain':'eth'

        }
        print(dic) 
        info.insert_one(dic)

    print("-------------------------------------------")
    p=p+40
    if len(sd['data']['list'])==0:
        print("completed",len(sd['data']['list']))
        break
