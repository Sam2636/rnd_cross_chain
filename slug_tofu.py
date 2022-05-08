import requests
import re
import pymongo


client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')
my_db=client2['nftgdp_tofu_slug']
#infoz=my_db.acclimatedmooncats
#my_db=client2['nftgdp_bsc_slug']
info=my_db.polygon_slug



def api_1(url1):
    url = url1
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers)
    #print(response.json())
    return response.json()


def api_2(url2):
    url = url2
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',"Accept": "application/json","X-Requested-With" : "XMLHttpRequest"}
    response = requests.request("GET", url, headers=headers)
    #print(response.text)
    return response.text    





#___________________________________________________api key station__________________________________________________#

#tofu_key="syUZXJVkvIzvV8fojZxjA" #-------------------->last modified on 5.30 pm 25/1/2022
#tofu_key="iuHeaHuCksmWLdVLqo239"  #------->changing frequently
#tofu_key="dblU_ga3iDxEC4e9QxKdV"  #------->changing frequently
#tofu_key="-sZLbZ9KAQ7jT_5-wOdaA"  #------->changing frequently



api_key=api_2("https://tofunft.com/bundle/bsc/OLwgg")
name_pattern = re.compile(r'src="/_next/static/([A-Za-z0-9\-\_]+)/_buildManifest.js').findall(api_key)
print("tofu_api_key---->",name_pattern[0])
tofu_key=name_pattern[0]



#______________________________________________________api_works_tofu___________________________________________________#


#-------------------->select blockchain and run   ,  change the tofu_key
blockchain="polygon" 
#blockchain="bsc"
#blockchain="avax"


#rank=api_1("https://tofunft.com/_next/data/{}/en/ranking.json?network={}".format(tofu_key,blockchain))         #----------------->ranking
rank=api_1("https://tofunft.com/_next/data/{}/en/ranking.json?network={}".format(tofu_key,"137"))         #----------------->ranking  polygon
#print(rank)
#https://tofunft.com/_next/data/-sZLbZ9KAQ7jT_5-wOdaA/en/ranking.json?network=polygon

#print(rank['pageProps']['rates']['MATIC'])
for lkl in range(len(rank['pageProps']['items'])): 
    #print(rank['pageProps']['items'][lkl]['nft_contract']['name'])
    if rank['pageProps']['items'][lkl]['nft_contract']['slug']==None:

        pass
    else:
        print("--------->",rank['pageProps']['items'][lkl]['nft_contract']['slug'])
        slug=rank['pageProps']['items'][lkl]['nft_contract']['slug']
        pk=api_1("https://tofunft.com/_next/data/{}/en/collection/{}/items.json?slug={}".format(tofu_key,slug,slug))
        #print(pk['pageProps']['data']['bundle']['contract'])
        if pk['pageProps']['data']['contract']['rarity_meta']==None:
            #print(slug=rank['pageProps']['items'][lkl]['nft_contract']['slug'])
            vp=[]
            op=[]
            for lp in range(len(pk['pageProps']['data']['esMapping'])):
                df=pk['pageProps']['data']['esMapping'][lp]['es_key']
                if pk['pageProps']['data']['esMapping'][lp]['es_key'].find('meta_text')!=-1:
                    jkl=pk['pageProps']['data']['esMapping'][lp]['name']
                    jkl_list=op.append(pk['pageProps']['data']['esMapping'][lp]['name'])
                    key=pk['pageProps']['data']['esMapping'][lp]['es_key']
                    #print(pk['pageProps']['data']['esMapping'][lp]['name'])
                    #print(key)
                    #print(pk['pageProps']['data']['searchOptions'][key])#['options']['name'])
                    #value=pk['pageProps']['data']['searchOptions'][key]#['options']['name'])
                    value=vp.append(pk['pageProps']['data']['searchOptions'][key])#['options']['name'])

            # using naive method
            # to convert lists to dictionary
            res = {}
            for key in op:
                for value in vp:
                    res[key] = value
                    vp.remove(value)
                    break  
            
            # Printing resultant dictionary 
            print ("Resultant dictionary is : " +  str(res))        

            dpc={
                'slugname':slug,
                'attribute':'None',
                'blockchain':'polygon',
                'true_attr':res,
                
            }
            print(dpc)
            #info.insert_one(dpc)
                    
                #print(pk['pageProps']['data']['searchOptions'][df]['options'])


            #break
            
        #print(pk['pageProps']['data']['contract']['rarity_meta'])
        slp=pk['pageProps']['data']['contract']['rarity_meta']

        pic={
            'slug_name':slug,
            'attributes':slp,
            'blockchain':'polygon',
            'true_attr':'None'
            
        } 
        info.insert_one(pic)

    #"https://tofunft.com/_next/data/-sZLbZ9KAQ7jT_5-wOdaA/en/collection/unusdao/items.json?slug=unusdao"
