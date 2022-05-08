from pymongo.collation import Collation
from pymongo import MongoClient, collection, write_concern
import pymongo
import json
import requests
from datetime import date
import datetime
import random

def lambda_handler(event, context):
    
        in_slug_name=(dict(event['queryStringParameters'])['slug'])
        in_token_id=int(dict(event['queryStringParameters'])['tkn_id'])
        
        
        client = MongoClient('mongodb+srv://prabhat:aiotylabs2020%21@cluster0.qgqw9.mongodb.net/test?authSource=admin&replicaSet=atlas-fm1pq5-shard-0&readPreference=primary&appname=MongoDB+Compass&ssl=true')
        database = client['nftgdp']
        coll=database['nftgdp_coll_details']
        
        today_date= date.today() 
        yes_date= Previous_Date = datetime.datetime.today() - datetime.timedelta(days=1)
        y_d=yes_date.strftime ('%Y-%m-%d')
        order_coll=database['date']
        cursor_validate =list(coll.find({'date':'{}'.format(today_date)}))
        mainlist=[]
        total_nfts=0
        mainlist2=[]
        mainlist3=[]
        mainlist4=[]
        db_pg2 = client['nftgdp_coll']
        slug_coll=db_pg2['{}'.format(in_slug_name)]
        total_nfts=slug_coll.count_documents({})
        
        
        
        
                
        
            
        def api_data():
            cursor =list(coll.find({'date':'{}'.format(f_d)}))
            cursor2 =list(slug_coll.find({'token_id': '{}'.format(in_token_id)}))
            for yx in range(len(cursor2)):
            
                yamm="None"
                spyam="None"
                if(str(cursor2[yx]['acc_owner'])!="None"):
                    yamm=str(cursor2[yx]['acc_owner'])
                    spyam=(((yamm.split("?")[0]).split("/")[4])) 
                yam=str(cursor2[yx]['acc_owner'])
                list2=[((cursor2[yx]['rarity_rank'])),
                ((cursor2[yx]['image_url'])),
                (spyam),
                ((cursor2[yx]['acc_owner'])),
                ((cursor2[yx]['token_id'])),
                'None',
                ((cursor2[yx]['perma_url'])),
                ((cursor2[yx]['rarity_score']))]
                list3=[((cursor2[yx]['traits']))][0].values()
                
                mainlist2.insert(yx,list2)
            mainlist3.append(list3)
        
            #print(mainlist2)
            #print("------------------")
        
            
            
            for x in range(len(cursor[0]['nft_collection'].values())):
                if ((list(cursor[0]['nft_collection'].values())[x]['collection']['slug'])==in_slug_name):
                    list1=[(list(cursor[0]['nft_collection'].values())[x]['collection']['slug']),
                    (list(cursor[0]['nft_collection'].values())[x]['collection']['banner_image_url']),
                    (list(cursor[0]['nft_collection'].values())[x]['collection']['image_url']),
                    (list(cursor[0]['nft_collection'].values())[x]['collection']['name'])]
                    #print(list1)
        
                    mainlist.insert(0,list1)
            cursor5 =list(slug_coll.find({}).limit(30).sort('nft_name',pymongo.ASCENDING).collation(Collation(locale='en_US', numericOrdering=False)))
            print(total_nfts)
            xux=0
            for xop in random.sample(range(1, 30), 12):
            
                yamm="None"
                spyam="None"
                if(str(cursor5[xop]['acc_owner'])!="None"):
                    yamm=str(cursor5[xop]['acc_owner'])
                    spyam=(((yamm.split("?")[0]).split("/")[4])) 
                yamm=str(cursor5[xop]['acc_owner'])
                list2=[((cursor5[xop]['rarity_rank'])),
                ((cursor5[xop]['image_url'])),
                (spyam),
                ((cursor5[xop]['token_id'])),'']
                mainlist4.insert(xux,list2)
                xux=xux+1
        
        
            ltt=[]
            
            for elem in range(0,12):
                if(elem<1):
                    ele=mainlist[elem]
                    one={"slug":ele[0],"name":ele[3],"banner_img":ele[1],"image_url":(ele[2])}
                    #ltttt[elem]=(one)
                if(elem<1):
                    ele=mainlist2[elem]
                    twoo={"rarity_rank":ele[0],"image_url":ele[1],"acc_owner":ele[2],"acc_owner_url":ele[3],"token_id":ele[4],"current_listing_price":ele[5],"opensea_url":ele[6],"rarity_score":ele[7]}
                    #lttt[elem]=(one)
                if(elem<12):
                    ele=mainlist4[elem]
                    onee={"rarity_rank":ele[0],"image_url":ele[1],"acc_owner":ele[2],"token_id":ele[3]}
                    ltt.append(onee)
                    
            
            #print(one)
            #print(twoo)
            
            #print((*[mainlist3]))
            page2={'nft_seg_1':one,'nft_seg_2':twoo,'nft_seg_3':([*mainlist3]),'similar_nfts':ltt}
            status_dict={
            "status":200,
            'response':"ok",
            "body":page2
            }
            #print("-------------")
            return(json.dumps(status_dict))
        
            
            
            #print(stltt)
            
        
            #print(mainlist)
            #print("-----------------")
            #print(mainlist2)
            #print("-----------------")
            #print(mainlist3)
        
        if (cursor_validate != []):
            #print(cursor)
            f_d=today_date
            
            return(api_data())
        else:
            yes_date= datetime.datetime.today() - datetime.timedelta(days=1)
            y_d=yes_date.strftime ('%Y-%m-%d')
            #print(y_d)
            f_d=y_d
            
            return(api_data())
            #print(mainlist)
print(lambda_handler({'queryStringParameters':{'slug':'akc','tkn_id':'9999'}},context=0))