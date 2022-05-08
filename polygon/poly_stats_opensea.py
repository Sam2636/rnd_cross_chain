import requests
import json
import time
import pymongo
from datetime import date
from collections import namedtuple

def f(event=None,context=None):

    #1-------->aiotydb
    client =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')

    #2---------->db2
    #client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')
    my_db=client['nftgdp_polygon']
    mycol = client['nftgdp_polygon']["polygon_slug"]
    mycol2 = my_db.collection_stats_by_raritytools
    mycol3= my_db["nftgdp_polygon_details"]


    urls = []
    s=[]#----------->

    maindict={}
    subdict={}
    numb=0
    
    
    for x in mycol.distinct("slug_name"):
        #print(x)

        fetch_date=str(date.today())
        url = "https://api.opensea.io/api/v1/collection/{}".format(x)

        response = (requests.request("GET", url)).json()
        #print(response)
        #mycol3.insert_one(response)
        #print(response)
        #print(fetch_date)
        del response["collection"]['editors']
        del response["collection"]['traits']
        del response["collection"]['payment_tokens']


        subdict[x]=response
        numb=numb+1 
        #print(response)
        #print(subdict)

    maindict["date"]=fetch_date
    maindict["blockchain"]='polygon'
    maindict["nft_collection"]=subdict

    print(maindict)

    #mycol3.insert_one(maindict)
    #print(s)
    return s

print(f(event=None,context=None))   