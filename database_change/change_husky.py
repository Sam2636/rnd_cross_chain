import requests
import pymongo
from requests.models import Response


client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')
#my_db=client2['nftgdp_coll']
#infoz=my_db.acclimatedmooncats
my_db=client2['avalanche_asset']
infoz=my_db["avax_huskypack"]
info=infoz.find({})


po=[]
yu=[]
count=0
pp=0

li=['460','927','2744','368','371','364','366','367','365','373','369','372','370','3183']

for num in info:

    #if num['owned_by'] == find(str("colection")):
    #print(num['token_id'])
    idd=num['token_id']
    if idd==li[13]:
        print('s')
        print(idd)
        infoz.update({"token_id":"{}".format(idd)},{"$set" : {"traits":'None'}},upsert= False ,multi=True)
    #z=num['token_id']
    #z="8320"
    #pk="None"
    #print(num['contract_address'].split('/')[4])
    """ cd=num['contract_address'].split('/')[4]
    url='https://opensea.io/assets/klaytn/{}/{}'.format(cd,idd)
    print(url)

    #print(vcxzcvcxz) """
    
''' mydb2=client2['avalanche_asset']
gh=[]
for coll in mydb2.list_collection_names():
    #print(coll)
    gh.append(coll)
print(gh)
for num in info:
    z=num["slug_name"]
    print(z) '''

    
#    pc=num['image_url']

    #ec=num["contract_address"]
    
    #print(y)
    #fg=https://www.larvalabs.com/cryptopunks/cryptopunk0000.png
    #df="https://www.larvalabs.com/public/images/cryptopunks/punk8348.png"
    #yal=pc.replace("/punk","/cryptopunk").replace("/public/images","")

      
    #yal=pc.replace("/punk","/cryptopunk").replace("/public/images","")  #-------------->normal 
    #yal=pc.replace("s/cryptopunk","s/punk").replace(".com/",".com/public/images/")  #-------------------->reduced
    #print(yal)
    #print(Caedsac)
