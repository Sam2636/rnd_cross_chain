import requests
import re
import pymongo


client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')
my_db=client2['nftgdp_tofu_slug']
#infoz=my_db.acclimatedmooncats
#my_db=client2['nftgdp_bsc_slug']
info=my_db.polygon_slug_stats




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
blockchain="137"    #polygon
#blockchain="bsc"
#blockchain="avax"

#https://tofunft.com/_next/data/-sZLbZ9KAQ7jT_5-wOdaA/en/ranking.json?network=137

rank=api_1("https://tofunft.com/_next/data/{}/en/ranking.json?network={}".format(tofu_key,blockchain))         #----------------->ranking

#print(rank['pageProps']['rates']['MATIC'])
pk=[]
for lkl in range(len(rank['pageProps']['items'])): 

    #print(rank['pageProps']['items'][lkl]['nft_contract']['name'])
    #print(rank['pageProps']['items'][lkl]['nft_contract']['slug'])
    #rint(rank['pageProps']['items'][lkl]['nft_contract']['contract'])
    #print(rank['pageProps']['items'][lkl]['nft_contract']['icon_url'])
    #print(rank['pageProps']['items'][lkl]['volume'])
    #print(rank['pageProps']['items'][lkl]['change_7d'])
    #print(rank['pageProps']['items'][lkl]['change_1d'])
    #print(rank['pageProps']['items'][lkl]['item_count'])
    #print(rank['pageProps']['items'][lkl]['owner_count'])
    #print(rank['pageProps']['rates']['MATIC'])    #matic in usd


    name=rank['pageProps']['items'][lkl]['nft_contract']['name']
    slug_name=rank['pageProps']['items'][lkl]['nft_contract']['slug']
    #slg.append(rank['pageProps']['items'][lkl]['nft_contract']['slug'])
    contract_address=rank['pageProps']['items'][lkl]['nft_contract']['contract']
    image_url=rank['pageProps']['items'][lkl]['nft_contract']['icon_url']
    volume=rank['pageProps']['items'][lkl]['volume']
    convert_usd_volume=rank['pageProps']['items'][lkl]['volume']
    seven_day_change=rank['pageProps']['items'][lkl]['change_7d']
    one_day_change=rank['pageProps']['items'][lkl]['change_1d']
    total_supply=rank['pageProps']['items'][lkl]['item_count']
    num_owners=rank['pageProps']['items'][lkl]['owner_count']
    floor_price=rank['pageProps']['items'][lkl]['floor_price']['value']
    usd_value=rank['pageProps']['rates']['MATIC']    #matic in usd
    usd_vol=usd_value*convert_usd_volume

    #print("converted_usd_volume",usd_value*convert_usd_volume)

    dicpk={
        'name':name,
        'slug_name':slug_name,
        'contract_address':contract_address,
        'image_url':image_url,
        'total_volume':volume,
        'total_volume_usd':usd_vol,
        'seven_day_change':seven_day_change,
        'one_day_change':one_day_change,
        'total_supply':total_supply,
        'num_owners':num_owners,
        'floor_price':floor_price,
    }
    pk.append(dicpk)



dcp={
    'nft_collection':pk
}
print(dcp)
info.insert_one(dcp)
    #print(rank['pageProps']['items'][lkl]['nft_contract']['info'])

#_______________________________________________________collectin_stats__________________________________________________________#


