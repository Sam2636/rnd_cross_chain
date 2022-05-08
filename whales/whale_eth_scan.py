#https://api.etherscan.io/api?module=account&action=txlist&address=0xa2bA5e0eaFB7A7A44515D02c47fB0E519F5bd002 

import pymongo
from datetime import date
from collections import namedtuple
import requests

#1-------->aiotydb
client =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')

#2---------->db2
#client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')
my_db=client['whales']
info=my_db.eth_whales
infoz=info.find({})

def api_1(url1):
    url = url1
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers)
    #print(response.json())
    return response.json()

def api_2(url1):
    url = url1
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',"Accept": "application/json",'X-API-Key':'nTn7bQFYVjxOPyb3rLhdDkahNUPnwHbzbeMzuJ1S0ST7D0xdK5kBPXnzPAEC9p15'}
    response = requests.request("GET", url, headers=headers)
    #print(response.json())
    return response.json()


for i in infoz:
    chain="eth"
    print(i['contract_address'])
    io=i['contract_address']
    #df=api_1("https://api.etherscan.io/api?module=account&action=txlist&address={}".format(io))
    nft_data=api_2("https://deep-index.moralis.io/api/v2/{}/nft?chain={}&format=decimal".format(io,chain))
    print(nft_data['total'])
    kp= nft_data['total']
    lp=nft_data
    name=[]
    mk=set()
    for ij in range(kp):
        print("----->",ij)
        try:
            print(lp['result'][ij]['token_uri'])
        except:
            pass    
        try:
            print(lp['result'][ij]['contract_type'])
        except:
            pass   
        try:    
            print(lp['result'][ij]['name'])
            name.append(lp['result'][ij]['name'])
            mk.add(lp['result'][ij]['name'])
        except:
            pass   
        try:
            print(lp['result'][ij]['metadata'])
        except:
            pass   
    
    print(name)
    print(mk)
    print(Asdfc)