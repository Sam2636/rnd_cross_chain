# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 15:57:24 2022

@author: User
"""

import requests
import pymongo
from requests.models import Response


client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')
#my_db=client2['nftgdp_coll']
#infoz=my_db.acclimatedmooncats
my_db=client2['klaytn_nft_details']
infoz=my_db["alap-the-lost-pioneers"]
info=infoz.find({})

po=[]
yu=[]
count=0
pp=0

huh=0
for num in info:
    #print(num)
    #y=num["perma_url"]
#huh=huh+1
    #if (huh>103):
        
    tk=num["token_id"]
    print(tk)
    z=num['traits']
    #print("zzzzz",z)
    for key,values in z.items():
        p=num['traits'][key]['value'].lower()
        #print("---->",key)
        #print("ppppp",p)
    
        url = "https://api.opensea.io/api/v1/collection/alap-the-lost-pioneers"
        response = (requests.request("GET", url)).json()#.replace(" ","").replace("_"," ")

        #print(response)
        dic={'trait':
                {'Eye':{
                'eye legend 4':	1,	
                'eye legend 3':	1,	
                'eye legend 2':	1,	
                'eye legend 1':	1,	
                'eye acb 8': 1,
                'eye acb 9': 2,	
                'eye acb 6': 7,	
                'eye acb 5': 9,	
                'eye acb 7': 11,	
                'eye acb 4': 14,	
                'eye acb 2': 20,	
                'eye acb 3': 23,	
                'eye acb 1': 24,
                'eye 9':	93	,
                'eye 8':	108	,
                'eye 4':	114	,
                'eye 6':	121	,
                'eye 3':	124	,
                'eye 5':	132	,
                'eye 7':	133	,
                'eye 2':	133	,
                'eye 1':	149	,

            },
            'Face':
            {
                'face acb 11':	3	,
                'face acb 10'	: 4	,
                'face acb 9':	7	,
                'face 13':	7	,
                'face 17': 7	,
                'face 16': 7	,
                'face acb 5':	8,	
                'face acb 7':	8,	
                'face acb 6':	10,	
                'face acb 8':	12,	
                'face 12':	12	,
                'face acb 1':	13,	
                'face 14'	: 14	,
                'face 15'	: 14	,
                'face acb 4':	14,	
                'face acb 2':	15,	
                'face acb 3':	17,	
                'face 9':	31	,
                'face 7':	35	,
                'face 8':	36	,
                'face 11':	 41	,
                'face 10'	: 44	,
                'face 6':	159	,
                'face 4':	166	,
                'face 2':	169	,
                'face 5':	180	,
                'face 3':	185	
                                } ,

                'Hair':{
                    'hair legend 4':	1	,
                        'hair legend 1':	1	,
                        'hair legend 2':	1	,
                        'hair legend 3':	1	,
                        'hair 27':35	,
                        'hair 7':35	,
                        'hair 25':35	,
                        'hair 13':36	,
                        'hair 3':36	,
                        'hair 26':36	,
                        'hair 9':40	,
                        'hair 17':41	,
                        'hair 15':41	,
                        'hair 5':42	,
                        'hair 21':42	,
                        'hair 1':43	,
                        'hair 6':43	,
                        'hair 19':44	,
                        'hair 12':44	,
                        'hair 20':44	,
                        'hair 18':46	,
                        'hair 4':46	,
                        'hair 22':48	,
                        'hair 10':49	,
                        'hair 8':51	,
                        'hair 11':52	,
                        'hair 23':55	,
                        'hair 14':56	,
                        'hair 2':57	,
                        'hair 24':59	,
                        'hair 16':62	,
                },
                'Mouth':{
                        'mouth legend 1':	1	,
                        'mouth legend 4':	1	,
                        'mouth legend 2':	1	,
                        'mouth legend 3':	1	,
                        'mouth 3':	211	,
                        'mouth 5':	222	,
                        'mouth 2':	225	,
                        'mouth 4':	229	,
                        'mouth 1':	331	
                }

            }
        }
        a=dic["trait"][key]
        #print("----------")
        #print(key)
        for keyy,values in a.items():
            #sd=num['traits'][key]['value'].lower()
            #print("--->>>>>>",key.replace("_"," "))
            op=keyy.replace("_"," ")
            #print("opopopop",op)
            
            if op==p:
                print(values)
                zk=values
                num['traits'][key]['trait_count']=zk
    yumh=num['traits']
    print("->",yumh)
    infoz.update({"token_id":"{}".format(tk)},{"$set" :{"traits":yumh}},upsert= False ,multi=True)
        #print(dfsdf)
            
