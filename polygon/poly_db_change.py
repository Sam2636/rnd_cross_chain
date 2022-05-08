import requests
import pymongo
from requests.models import Response


client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')
#my_db=client2['nftgdp_coll']
#infoz=my_db.acclimatedmooncats
my_db=client2['polygon_nft_details']
infoz=my_db["eva-hoverboard"]
info=infoz.find({})


po=[]
yu=[]
count=0
pp=0

#

for num in info:
    #if num['owned_by'] == find(str("colection")):
    #print(num['token_id'])
    idd=num['token_id']
    #z=num['token_id']
    #z="8320"
    #pk="None"
    print(num['contract_address'].split('/')[4])
    ct=num['contract_address'].split('/')[4]
    cd=num['perma_url']#.split('/')[4]
    print(idd)
    print(cd)
    url='https://opensea.io/assets/matic/{}/{}'.format(ct,idd)
    print(url)

    infoz.update({"token_id":"{}".format(idd)},{"$set" : {"perma_url":"{}".format(url)}},upsert= False ,multi=True)
    #print(sdfgb)
