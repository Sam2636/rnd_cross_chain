import requests,json,time
import pymongo
from pymongo.collation import Collation
from pymongo import MongoClient
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry



session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

#session.get(url)

#ghgjgjgjgjgjhgjgjgjhgjgjggjghgjgjhggjhghj

client =MongoClient('mongodb+srv://prabhat:aiotylabs2020%21@cluster0.qgqw9.mongodb.net/test?authSource=admin&replicaSet=atlas-fm1pq5-shard-0&readPreference=primary&appname=MongoDB+Compass&ssl=true')

slug_db=client['klaytn_nft_details']

all=[]
asus=0
testfortemp=[]
for document in slug_db.list_collection_names():
    demon={}
    main_poet=[]
    if((len(list(client['nftgdp_klaytn_details'][document].find({}))))==0):
        document='the-meta-kongz'
        print(document)
        

        nft_name=document


        countt=0
        maindict={}
        numb=0



        url = "https://api.opensea.io/api/v1/collection/{}".format(document)#undoneekbaLJSLF

        response_traits = requests.request("GET", url)
        tttt=(json.loads(response_traits.text))
        #total_nfts=tttt['collection']['stats']['count']#len(list(slug_db[document].find({})))
        total_nfts=10000
        print(total_nfts)
        #print(asdcfvgbhn)

        ##print(tttt)
        maidict={}

        for key in tttt['collection']['traits']:
            tttt['collection']['traits'][key].pop('none', None)

        for keysz in tttt['collection']['traits'].keys():
            qwert={}
            qwert['name']=keysz.lower()
            tem_dict=[]

            count_ttds=0
            for valuee in tttt['collection']['traits']['{}'.format(keysz)]:
                ##print(valuee)
                tem_tem=[] 
                tem_tem.append(valuee.replace("_"," "))
                tem_tem.append(tttt['collection']['traits']['{}'.format(keysz)]['{}'.format(valuee)])
                tem_dict.append(tem_tem)

                count_ttds=count_ttds+(tttt['collection']['traits']['{}'.format(keysz)]['{}'.format(valuee)])
            null_countzz=['none',(total_nfts-count_ttds)]

            tem_dict.insert(0,null_countzz)





            qwert['t_items']=tem_dict
            main_poet.append(qwert)
        if (document=='alap-the-lost-pioneers'):
            del main_poet[0]
        print(main_poet)


        #for zui in slug_db[document].find({}):
            #print(zui)
            #print(aksjbf)


        di={}

        for xxi in main_poet:
            di[xxi['name']]="yes"
        all=list(slug_db[document].find({}))
        nonedict={}
        for r in (all):
            ##print(r)
            #print(len(r['traits']))
            
            dictsmain={}

            for i in (r['traits']):
                dictsmain[i]={'trait_type': r['traits'][i]['trait_type'], 'trait_value':r['traits'][i]['value']}              
                dictsmain['Trait Count']={
                    'trait_type': 'Trait Count', 'trait_value': str(len(r['traits']))
                }

            xret=int(len(r['traits']))
            #print("===",xret,"=",demon.keys())
            if xret in demon.keys():
                ytwq=int(demon[xret])
                demon[xret]=ytwq+1
            else:
                demon[xret]=1


            
            #print(dictsmain)
            for ioi in main_poet:                
                #print(ioi['name'])
                if ((ioi['name']).lower()) not in (pog.lower() for pog in list(dictsmain.keys())):
                    #print(ioi['name'])
                    #print(dictsmain.keys())
                    
                    #print("////////////////////////////////////////////////////")
                    ##############################print(ioi)

                    dictsmain[ioi['name']]={'trait_type':ioi['name'],'trait_value':ioi['t_items'][0][0],'trait_count':ioi['t_items'][0][1]}
                for pogg in list(dictsmain.keys()):
                    if pogg.lower()==ioi['name'].lower():
                        #print(dictsmain[pogg]['trait_value'])
                        ggez=dictsmain[pogg]['trait_value'].lower()
                        ''' if ggez=="dress purple":
                            ggez="dress_purple"
                        if ggez=="beanie w":
                            ggez="beanie_w" '''

                        wert=next((i for i, (j, ele) in enumerate(ioi['t_items']) if j == (ggez)), None)
                        print("-----",wert)
                        print(ggez)

                        print("<>",ioi['t_items'][wert][1])
                        dictsmain[pogg]['trait_count']=ioi['t_items'][wert][1]
                        
                    
                #print(dictsmain)
               
            ##print(dictsmain)
            maidict[r['token_id']]=dictsmain
            del r['traits']
            r['traits']=dictsmain
            #print(r)
            
            
            ##print(fhfusg)
                ##print(afasdlgjdiyec)
                ##print(dictsmain)
            ##print(dictsmain)
            #client['automation_test']['azuki'].update({"token_id":"{}".format(r['token_id'])},{"$set":{"traits":dictsmain}},upsert= False, multi=True)
            #"{}".format(r['token_id'])

            #print("=====================================")

    #print(maidict['28'])
    #print(demon)



    for vali in range((0+asus),((len(all))+asus)):
        try:
            maidict['{}'.format(vali)]['Trait Count']['trait_count']=demon[int(maidict['{}'.format(vali)]['Trait Count']['trait_value'])]
            #print(maidict['{}'.format(vali)])
            for oi in all:
                if(str(vali)==oi['token_id']):
                    oi['traits']=maidict['{}'.format(vali)]
                    #print(oi)
        except:
            pass

    for keyszr in demon.keys():

            qwert={}
            qwert['name']='Trait Count'
            tem_dict=[]

            count_ttds=0
            for valuee in demon:
                #print(valuee)
                tem_tem=[] 
                tem_tem.append(str(valuee))
                tem_tem.append(demon[int(valuee)])
                tem_dict.append(tem_tem)
                count_ttds=count_ttds+int(demon[int(valuee)])
            null_countzz=['None',(total_nfts-count_ttds)]

            tem_dict.insert(0,null_countzz)

            qwert['t_items']=tem_dict
            main_poet.append(qwert)
    #print(main_poet)

    #print(" total nfts :",total_nfts)
    leng=len(main_poet)
    attri_no=leng
    #print("total attributes :",attri_no)
    sugumarcons=100
    total_nfts=10000
    sv=total_nfts * attri_no *sugumarcons
    #print("sam vlaue :",sv)
    maindict={}
    for x in range(leng):
        #print(collzdtkn['basePropDefs'][x])
        attri_name=(main_poet[x]['name']).lower()
        no_attri_traits=int(len(main_poet[x]['t_items']))
        #print("no of tratis attributes :",no_attri_traits)
        vv=sv/no_attri_traits
        #print("vivin value :",vv)
        maindict[attri_name]={}
        for xx in range(0,no_attri_traits):
            trait_name=(str(main_poet[x]['t_items'][xx][0])).lower()
            t_sub_count=int(main_poet[x]['t_items'][xx][1])
            if t_sub_count!=0:
                nv=vv/t_sub_count
                maindict[attri_name][trait_name]=nv
            else:
                maindict[attri_name][trait_name]=0
            #print("trait_value:",nv)
        #print(maindict)
    #print(" nishanth value :",maindict)

    mdit={}

    liistt=[]
    #print("fffffffffffffffffffffffffffff:",total_nfts)


    
    #print(all)

    for xyea in slug_db[document].find({}).limit(1).sort('token_id',pymongo.ASCENDING).collation(Collation(locale='en_US', numericOrdering=True)):
        if (int(xyea['token_id'])==0):
            yx=0
        else:
            yx=1
    for yaar in all:
        
        #print(yaar['token_id'])
        if yaar['token_id']=="8320":
            del yaar['owned_by']
            yaar['owned_by']="None"
        if 'owner_details' not in yaar:
            yaar['owner_details']={
                "owner_name":"None",
                "owner_address":yaar['owned_by'],
                "owner_profile_img_rl":"None"
            }

        if 'acc_owner' not in yaar:
            if (yaar['owned_by'] == "None"):
                yaar['acc_owner']="None"
            else:
                yaar['acc_owner']="https://opensea.io/"+yaar['owned_by']
            del yaar['owned_by']
        if 'image_url' not in yaar:
            yaar['image_url']=yaar['nft_image_url']
            del yaar['nft_image_url']

        #print(yaar)
        tokenn_iid=int(yaar['token_id'])
#print(tokenn_iid)
#print("==============================")
        to_to_score=0
        lisscore=[]
        mdit['{}'.format(tokenn_iid)]={}


        for yxx in yaar['traits']:
            #print(yxx)
            if (yxx!='trait count'):

                tt=(yaar['traits']['{}'.format(yxx)]['trait_type']).lower()

                #print(yaar['traits'])
                tv=(yaar['traits']['{}'.format(yxx)]['trait_value']).lower()

                try:
                    to_to_score=to_to_score+float(maindict['{}'.format(tt)]['{}'.format(tv)])
                except:
                    to_to_score=to_to_score+float(maindict['{}'.format(tt)]['{}'.format(tv.replace(" ","_"))])


        #print(yaar)
        to_to_score=to_to_score/(len(yaar['traits']))
        to_to_score=round(to_to_score,2)
        #print(to_to_score)
        #print(tokenn_iid)
        yaar['rarity_score']=str(to_to_score)
        #print(yaar)
        for x in (list(yaar['traits'].keys())):
            try:
                yaar['traits']['{}'.format(x)]['trait_score']=(maindict['{}'.format(x.lower())]['{}'.format((yaar['traits']['{}'.format(x)]['trait_value']).lower())])
            except:
                yaar['traits']['{}'.format(x)]['trait_score']=(maindict['{}'.format(x.lower())]['{}'.format((yaar['traits']['{}'.format(x)]['trait_value']).lower().replace(" ","_"))])
        lisscore.append(tokenn_iid)
        lisscore.append(to_to_score)
        liistt.append(lisscore)
        yx=yx+1


    #sorted(all, key=lambda key_value: ["score"], reverse=True)

    liistt.sort(key = lambda x: x[1],reverse=True) #Desending order by score
    for xix in range(len(liistt)):

        if (xix==0):
            liistt[xix].insert(0,(xix+1))
        elif ((liistt[xix-1][2])==(liistt[xix][1])):
            liistt[xix].insert(0,(liistt[xix-1][0]))
        else:
            liistt[xix].insert(0,(xix+1))
    #liistt[xix][2]=(liistt[xix][2])
    print(liistt)
    for yx in liistt:
        #print("==============================")
        for yaar in all:
            if (int(yaar['token_id'])==yx[1]):
                yaar['rarity_rank']=yx[0]
                #print(yx[0])
                print(yaar)
    


    #print(kjbf)


