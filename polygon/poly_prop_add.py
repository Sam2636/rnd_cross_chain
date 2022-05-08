#https://api.nftrade.com/api/v1/contracts/a6f85fe1-3f70-47af-8b1f-e1a6997ef150/traits

import requests
import pymongo
from requests.models import Response


client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')
#my_db=client2['nftgdp_coll']
#infoz=my_db.acclimatedmooncats
my_db=client2['nft_trade_polygon']
infoz=my_db["poly_slug"]
info=infoz.find({})

po=[]
yu=[]
count=0
pp=0


def api_1(url1):
    url = url1
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers)
    #print(response.json())
    return response.json()


for num in info:
    #print(num)
    #y=num["perma_url"]
    z=num["contract_id"]
    print(z)
    sd=api_1("https://api.nftrade.com/api/v1/contracts/{}/traits".format(z))
    pk=sd['properties']
    dictsmain={}
    op=[]
    for i in pk:
        print("---->",i)
        #dictsmain[pk['{}'.format(i)]]
        fg=pk[i]
        #print("------>",fg)
        gh=[]
        for f in fg:
            pl=[]
            jh=f['value']
            kl=f['tokensCount']
            pl.append(jh)
            pl.append(int(kl))
            gh.append(pl)
        print(gh)    
     
        jk={
            'name':i,
            't_items':gh
        }
        op.append(jk)
        
    print(op)

    infoz.update({"contract_id":"{}".format(z)},{"$set" : {"attributes":op}},upsert= False ,multi=True)
    #print(favsdfgbdds)
        #print(kl)
        #print(fg)
        #print(i)
        #print(i)
    #print(pk)
    #print(dictsmain)
    #print(Fefgfvdfd)

    
    #pc=num['image_url']
