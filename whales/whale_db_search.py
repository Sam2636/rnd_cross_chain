import requests
import pymongo
from requests.models import Response


client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')
#my_db=client2['nftgdp_coll']
#infoz=my_db.acclimatedmooncats
my_db=client2['nftgdp_coll'] #-------1

my_db2=client2['whales_in_db'] #-------2
#infg=my_db2['whale_1']
#info=infoz.find({})

df=my_db.list_collection_names()
print(df)


""" 
check ='0xef764bac8a438e7e498c2e5fccf0f174c3e3f8db'
lp=[]
kl=set()
for il in df:
    print("-<>",il)
    infoz=my_db[il]
    info=infoz.find({})
    for num in info:
        #print(num)
        #print("----->",num['token_id'])
        try:
            idd=num['owner_details']['owner_address']
            tok=num['token_id']
            if idd==check:
                print("sssssss",idd)
                lp.append(il)
                kl.add(il)
                #break
        except:
            pass        
    #print(wqadsfsa)        


    #print("<--->list",lp)
    print(kl,"------------------")

print("success")
fg={
    check:kl
}
print(fg)
#infg.insert_one(fg) """

my_db3=client2['whales'] #-------3
infx=my_db3['eth_whales']
info=infx.find({})

pl=[]   #-------------->every contract address

for o in info:
    print(o['contract_address'])
    asd=o['contract_address']
    pl.append(asd)

#print(pl)


lp=[]
kl=set()

total_no_whale_owning_nft=[]
lo=[]
hj=[]
p=0
for fb in pl:
    p=p+1
    print("---.>>>",fb,"----->",p)

    il="clonex"   #---------------------------------------------------------------->change collecttion_name to get the data
    print("-<>",il)
    infoz=my_db[il]
    info=infoz.find({})

    for num in info:
        #print(num)
        #print("----->",num['token_id'])
        
        try:
            idd=num['owner_details']['owner_address']
            tok=num['token_id']
            if idd==fb:
                print("sssssss",idd)
                print("tok",tok)
                total_no_whale_owning_nft.append(tok)
                lo.append(tok) #------>token_id
                lp.append(fb)
                kl.add(fb)
                #break
                #print(hj)                     
                #print(wqadsfsa)        
        except:
            pass   

    pj={
        fb:lo
    }

    hj.append(pj)
    print(pj)
    lo.clear()

    #print("<--->list",lp)
    print(kl,"------------------")


fg={
    il:list(kl),
    'token_owned_by_whales':total_no_whale_owning_nft,
    'total_whale_nfts':len(total_no_whale_owning_nft),
    'total_no_whales':len(kl)
}
infg=my_db2[il]
infg.insert_one(fg) 
print(fg)


print("---------success-----------")

    #infg.insert_one(fg) 

    



