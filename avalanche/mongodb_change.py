import pymongo

client =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')

#2---------->db2
client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')
''' my_db=client['nftgdp_solanart']
#mycol = my_db['avalanche_slug']

infoz=mycol.find({})
#mycol2 = my_db.collection_stats_by_raritytools
#mycol3= my_db["nftgdp_coll_details"]
info=my_db.avalanche_slug

 '''
db = client2['avalanche_details']#original database
db2 = client2['avalanche_asset']#database to be copied to

#cursor = db["<collection to copy from>"].find()
cursor = db["AVAX PUNKS"].find()
for data in cursor:
    db2["avax_avaxpunks"].insert(data)

print('success')