import requests
import pymongo
from requests.models import Response
from pymongo import MongoClient
#nftgdp
#client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')

#dali
host = 'mongodb+srv://sam:JU8k0f21G3gi674Q@letsdali-mongodb-v1-14ea9509.mongo.ondigitalocean.com/letsdali-v1?authSource=admin&replicaSet=letsdali-mongodb-v1&tls=true'
cert = 'C:/Users/user/Downloads/ca-certificate (1).crt'
client2=MongoClient(host, ssl_ca_certs=cert) 


my_db=client2

my_db.nft_coll.renameCollection("nftgdp_coll")

#my_db.renameCollection("nftgdp_coll")
print('done')