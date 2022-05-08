
import pymongo
from datetime import date
from collections import namedtuple


#1-------->aiotydb
client =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')

#2---------->db2
#client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')
my_db=client['nftgdp_polygon']
mycol = client['nftgdp']["nftslugname"]
mycol2 = my_db.collection_stats_by_raritytools
mycol3= my_db["nftgdp_coll_details"]
info=my_db.polygon_slug

listt=["charity-raccoon", "inverseape", "led-punks-classic-club", "bored-octopus-club", "chumbivalleyofficial", "derace-horses", "eva-hoverboard", "crypto-unicorns-market", "baby-otters", "cybee"]

for ik in listt:
    dic={
        'slug_name':ik, 
        'blockchain':'polygon'

    }

    info.insert_one(dic)
