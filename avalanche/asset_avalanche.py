from pydoc import cli
from numpy import place
import pymongo
from datetime import date
from collections import namedtuple
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless") 
# for driver we can download and specifiy the path or we can use the below code
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
#driver = webdriver.Chrome(ChromeDriverManager().install())
#1-------->aiotydb
client =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')

#2---------->db2
#client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')
my_db=client['nftgdp_avalanche']
mycol = my_db['avalanche_slug']
infoz=mycol.find({})
#mycol2 = my_db.collection_stats_by_raritytools
#mycol3= my_db["nftgdp_coll_details"]
#info=my_db.avalanche_slug
my_db_2=client['avalanche_asset']




#listt=["charity-raccoon", "inverseape", "led-punks-classic-club", "bored-octopus-club", "chumbivalleyofficial", "derace-horses", "eva-hoverboard", "crypto-unicorns-market", "baby-otters", "cybee"]

#https://nftrade.com/_next/data/tkjn7kaZYdoToTzpydZAy/assets/avalanche/0x81933ba6ae1bf39eace71519f35fb33fe4d72554.json

driver.set_page_load_timeout(5000)
driver.get("https://nftrade.com/")          
#driver.get("https://howrare.is/shadowysupercoder%22)#---------------%3E single collection details  stats
#driver.get("https://opensea.io/assets?search[categories][0]=art&search[query]=blitmap%22)
driver.maximize_window()
driver.delete_all_cookies()
driver.refresh()
driver.implicitly_wait(2)

elem = driver.find_element_by_xpath("//*")
source_code = elem.get_attribute("outerHTML")


sd=source_code.split("__NEXT_DATA__")[1].split('WEB3_CONNECT_MODAL_ID')[0]
#print(sd)

#/_buildManifest.js" async=""></script><script src="/_next/static/

key=sd.split(' async=""></script><script src="/_next/static/')
key1=key[-1].split('/_ssgManifest.js')[0]
print(key1)

def api_1(url1):
    url = url1
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers)
    #print(response.json())
    return response.json()

hj=[]
jp=[]
for i in infoz:
    #print(i['contract_address'])
    jk=i['contract_address']
    kl=i['contract_id']
    #print("----->",kl)
    hj.append(jk)
    jp.append(kl)
#print(len(hj))
dp=set()
#print(jp)
p=0
setuh=set()
j=0
jk=0
contract_add=hj[12]
print(contract_add)
contract_ID=jp[12]  #------>change according to the collection
#print(contract_ID) #------>change according to the collection
info=my_db_2['avax_avaxgoatz']
while True:
    #print(jk,"ewfafwef")
    # 6969 
    print("justkidding",jk)
    try:
        ap=api_1("https://api.nftrade.com/api/v1/tokens?limit=30&skip={}&contracts[]={}&chains[]=43114".format(jk,contract_ID))
    except:
        time.sleep(3)
        print('case1')
        ap=api_1("https://api.nftrade.com/api/v1/tokens?limit=30&skip={}&contracts[]={}&chains[]=43114".format(jk,contract_ID))

    print("----------------------------------------------------------------------------------------")
    #print("https://api.nftrade.com/api/v1/tokens?limit=30&skip={}&contracts[]={}&chains[]=43114".format(jk,contract_ID))
    if len(ap)==0:
        print("apppppppp",len(ap))
        break
    for i in ap:
        #print("-------->>>>>>",i)
        #print(i['tokenID'])
        #j=1269
        
        pl=i['tokenID']
        setuh.add(pl)
        print('--->>>>>>>>',j)
        j=j+1
        try:
            ap2=api_1("https://nftrade.com/_next/data/{}/assets/avalanche/{}/{}.json".format(key1,contract_add,pl))
        except:
            time.sleep(2)
            print("case2")
            ap2=api_1("https://nftrade.com/_next/data/{}/assets/avalanche/{}/{}.json".format(key1,contract_add,pl))
        #print("https://nftrade.com/_next/data/{}/assets/avalanche/{}/{}.json".format(key1,contract_add,pl))
        #print(ap2['pageProps']['token']['attributes'])
        nft_details=ap2['pageProps']['token']
        contract_add=ap2['pageProps']['token']['contractAddress']
        nft_id=ap2['pageProps']['token']['id']
        contract_name=ap2['pageProps']['token']['contractName']
        token_id=ap2['pageProps']['token']['tokenID']
        token_uri=ap2['pageProps']['token']['tokenURI']
        contract_id=ap2['pageProps']['token']['contractId']
        last_sale=ap2['pageProps']['token']['last_sell']
        current_price=ap2['pageProps']['token']['price']
        image_url=ap2['pageProps']['token']['image']
        image_thumb_url=ap2['pageProps']['token']['thumb']
        image_preview_url=ap2['pageProps']['token']['preview']
        nft_name=ap2['pageProps']['token']['name']
        try:
            li=ap2['pageProps']['token']['attributes']
            dictsmain={}
            for i in range(len(li)):
                ##print("=====================================")
                dictsmain[li[i]['trait_type']]={
                    'trait_type': li[i]['trait_type'], 'value':li[i]['value']
            }
        except:
            li='None'   
            dictsmain='None' 
        permalink="https://nftrade.com/assets/avalanche/{}/{}".format(contract_add,pl)
    
        dfg={
            #'nft_details':nft_details,
            'nft_name':nft_name,
            'token_id':token_id,
            'image_url':image_url,
            'image_thumb_url':image_thumb_url,
            'image_preview':image_preview_url,
            'perma_url':permalink,
            'acc_owner':'None',
            'owner_details':'None',
            'num_sales':'None',
            'traits':dictsmain,
            'nft_id':nft_id,
            'contract_address':contract_add,
            'contract_id':contract_id,
            'contract_name':contract_name,
            'token_uri':token_uri,
            'last_sale':last_sale,
            'current_price':current_price,
            'blockchain':'avalanche'
        }
        #print(dfg)
        info.insert_one(dfg)
        #print(dictsmain)
        #print(acsce)
    
    #print("--->",jk)
    print("--------------------------------------->",p)
    p=p+1
    jk=jk+30
#print("success")
#print(len(setuh))

print("success")
  