from pydoc import doc
import requests,json,time
import pymongo
from pymongo import MongoClient
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry



session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)


client =MongoClient('mongodb+srv://prabhat:aiotylabs2020%21@cluster0.qgqw9.mongodb.net/test?authSource=admin&replicaSet=atlas-fm1pq5-shard-0&readPreference=primary&appname=MongoDB+Compass&ssl=true')

avalanche_asset=client['avalanche_asset']   #----------->1

avax_s=client['nftgdp_avalanche']    #------------>2
my_slug=avax_s['avalanche_slug']
info=my_slug.find({})




all=[]
asus=0
testfortemp=[]

#type -------------->this is to find the exact value  of overall attributes from the database
''' def dsf(item_pass):
    items=num['attributes'][str(k)]['t_items']
    print(items)
    for ol in items:
        mk=ol[0]
        if mk==item_pass:
            print('<>',ol[1])'''

def dsf(item_pass):
    items=num['attributes'][str(k)]['t_items']
    print(items)
    for ol in items:
        mk=ol[0]
        if mk==item_pass:
            print('<>',ol[1])


def traits_pass(sad):
    for un in mydoce:
        #print(un['traits'])
        print("---------------------")
        qwe=un['traits']
        for k,v in qwe.items():
            print(str(k))
        tr=un['traits'][sad]['value']
        print("--->",tr)    #-----> trait-type
        dsf(tr)         #calls the value
        #print(lkjhg)



for document in avalanche_asset.list_collection_names():
    if (document=='avax_avaxlions'):
        my_collection=avalanche_asset[document]
        mydoc = my_collection.find().count()
        mydoce = my_collection.find()
        print("total_number_nft :--->",mydoc)   #--------------->1 total number of nftd in database
        for num in info:
            z=num["slug_name"]
            if z==document:
                #print(z)
                #print(num['attributes'][0]['t_items'])    #---------------->2 items 
                for un in mydoce:
                    print("----------------------------------------------->",un['token_id'])
                    print(un['traits'])
                    tyu=un['traits']
                    for k,v in tyu.items():
                        print(str(k),"----->",v['value'])
                        fg=num['attributes'][0]['name']
                        we=num['attributes']
                        for l in we :
                            #print("------------------------------------------------------------------",l['name'])
                            if l['name']==str(k):
                                print(v['value'])
                                er=v['value']
                                dsf(er)

                    print(cxzxvg)
                '''          tr=un['traits'][sad]['value']
                    dsf(tr)
                    print(tr) '''
              
                ''' fg=num['attributes'][0]['name']
                we=num['attributes']
                print(we)
                qs=[]
                for l in we :
                    print("------------------------------------------------------------------",l['name'])
                    qs.append(l['name'])
              '''
                
                ''' print(qs)
                for un in mydoce:
                    print("---------------------")
                    print(un['traits'])
                    tr=un['traits'][sad]['value']
                    dsf(tr)
                    print(tr)
                    print(lkjhg) '''
                    #break

            

        demon={}
        main_poet=[]
        #print(document)
        '''         if(1>=0):
            #print(len(document))

            nft_name=document
            

            countt=0
            maindict={}
            numb=0 '''
            
            
        ''' 
            ##print(tttt)
            maidict={}
            
            for key in tttt['collection']['traits']:
                tttt['collection']['traits'][key].pop('none', None)

            for keysz in tttt['collection']['traits'].keys():
                qwert={}
                qwert['name']=keysz
                tem_dict=[]

                count_ttds=0
                for valuee in tttt['collection']['traits']['{}'.format(keysz)]:
                    ##print(valuee)
                    tem_tem=[] 
                    tem_tem.append(valuee)
                    tem_tem.append(tttt['collection']['traits']['{}'.format(keysz)]['{}'.format(valuee)])
                    tem_dict.append(tem_tem)
                    
                    count_ttds=count_ttds+(tttt['collection']['traits']['{}'.format(keysz)]['{}'.format(valuee)])
                null_countzz=['None',(total_nfts-count_ttds)]

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
            
            for r in (slug_db[document].find({})):
    
                ##print(r)
                #print(len(r['traits']))
                dictsmain={}

                for i in (r['traits']):
                    ##print("=====================================")
                    #print(i)
                    #print(r['traits'][i])
                    dictsmain[i]=r['traits'][i]
                    dictsmain['Trait Count']={
                        'trait_type': 'Trait Count', 'value': str(len(r['traits']))
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
                    if dictsmain.get(ioi['name']) is None:
                        #print("////////////////////////////////////////////////////")
                        #print(ioi)

                        dictsmain[ioi['name']]={'trait_type':ioi['name'],'value':ioi['t_items'][0][0],'trait_count':ioi['t_items'][0][1]}
                ##print(dictsmain)
                maidict[r['token_id']]=dictsmain
                r['traits']=dictsmain
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
                maidict['{}'.format(vali)]['Trait Count']['trait_count']=demon[int(maidict['{}'.format(vali)]['Trait Count']['value'])]
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
        
        
        all=list(slug_db[document].find({}))
        #print(all)
        
        for yx in range(total_nfts):
            #print(yx)
            #print("fffffffffffffffffffffffffffff")
            #print("==============================")
            for yaar in all:

                if (int(yaar['token_id'])==yx):
                    #print(yaar['token_id'])
                    yaar['owner_details']={
                        "owner_name":"None",
                        "owner_address":yaar['owned_by'],
                        "owner_profile_img_url":"None"
                    }
                    yaar['acc_owner']="https://opensea.io/"+yaar['owned_by']
                    yaar['image_url']=yaar['nft_image_url']
                    del yaar['nft_image_url']
                    del yaar['owned_by']
                    print(yaar)
                    

                    tokenn_iid=yx
            #print(tokenn_iid)
            #print("==============================")
                    to_to_score=0
                    lisscore=[]
                    mdit['{}'.format(tokenn_iid)]={}


                    for yxx in yaar['traits']:
                        #print(yxx)
                        if (yxx!='trait count'):
                            #print(yxx)
                            #print(type(yxx))
                            tt=(yaar['traits']['{}'.format(yxx)]['trait_type']).lower()
                            #if (tt=="hat hair"):
                                #tt="hat-hair"
                            #print(tt)
                            #print(type(tt))

                            tv=(yaar['traits']['{}'.format(yxx)]['value']).lower().replace(" ","_")

                            #print(tv)
                            #print(type(tv))
                            #print("==============================")
                            #print(maindict['{}'.format(tt)]['{}'.format(tv)])
                            to_to_score=to_to_score+float(maindict['{}'.format(tt)]['{}'.format(tv)])

                    #print(yaar)
                    to_to_score=to_to_score/(len(yaar['traits']))
                    to_to_score=round(to_to_score,2)
                    #print(to_to_score)
                    #print(tokenn_iid)
                    yaar['rarity_score']=str(to_to_score)
                    #print(yaar)
                    for x in (list(yaar['traits'].keys())):
                        
                        yaar['traits']['{}'.format(x)]['trait_score']=(maindict['{}'.format(x.lower())]['{}'.format((yaar['traits']['{}'.format(x)]['value']).lower().replace(" ","_"))])
                    lisscore.append(tokenn_iid)
                    lisscore.append(to_to_score)
                    liistt.append(lisscore)
                    
        
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
                     '''
                    
                    


                    #mdit['{}'.format(tokenn_iid)]['token_id']=tokenn_iid
                    #mdit['{}'.format(tokenn_iid)]['score']=to_to_score
                #print(liistt)
                #sorted(liistt.items(), key=lambda x:x[1],reverse=True)
                #print(liistt)
                #print(mdit)

                #sorted_keys = sorted(mdit, key=lambda x: (mdit[x]['score']),reverse=True)
                #print("============-------------------------")
                #print(sorted_keys)

        #print("===================================================")
        #print(all)
        
        
    '''    for xdb in all:
            client['nftgdp_klaytn_details'][document].insert_one(xdb)
        print(kjbf)
             '''
        
       



