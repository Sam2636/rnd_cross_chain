import pymongo
from datetime import date
from collections import namedtuple
import requests
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

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
info=my_db.avalanche_slug

driver.set_page_load_timeout(5000)
driver.get("https://nftrade.com/")          
#driver.get("https://howrare.is/shadowysupercoder%22)#---------------%3E single collection details  stats
#driver.get("https://opensea.io/assets?search[categories][0]=art&search[query]=blitmap%22)
driver.maximize_window()
driver.delete_all_cookies()
driver.refresh()
driver.implicitly_wait(2)


#listt=["charity-raccoon", "inverseape", "led-punks-classic-club", "bored-octopus-club", "chumbivalleyofficial", "derace-horses", "eva-hoverboard", "crypto-unicorns-market", "baby-otters", "cybee"]

#https://nftrade.com/_next/data/tkjn7kaZYdoToTzpydZAy/assets/avalanche/0x81933ba6ae1bf39eace71519f35fb33fe4d72554.json


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



elem = driver.find_element_by_xpath("//*")
source_code = elem.get_attribute("outerHTML")

sd=source_code.split("__NEXT_DATA__")[1].split('WEB3_CONNECT_MODAL_ID')[0]
#print(sd)

#/_buildManifest.js" async=""></script><script src="/_next/static/

key=sd.split(' async=""></script><script src="/_next/static/')
key1=key[-1].split('/_ssgManifest.js')[0]

p=0
for i in infoz:
   
    print('----------------------------------')
    print(i)
    print(p)
    p=p+1

    print(i['contract_address'])

    jk=i['contract_address']

  
    sd=api_1("https://nftrade.com/_next/data/{}/assets/avalanche/{}.json".format(key1,jk))
    pk=sd['pageProps']['contract']['id']
    name=sd['pageProps']['contract']['name']
    image=sd['pageProps']['contract']['image']
    cover_image=sd['pageProps']['contract']['cover_image']
    description=sd['pageProps']['contract']['description']
    twitter=sd['pageProps']['contract']['twitter']
    telegram=sd['pageProps']['contract']['telegram']
    discord=sd['pageProps']['contract']['discord']  
    website=sd['pageProps']['contract']['website']
    typpe=sd['pageProps']['contract']['type']

    #print(pk)

    dic={
        'slug_name':name, 
        'contract_id':pk,
        'contract_address':jk,
        'image_url':image,
        'banner_url':cover_image,
        'description':sd,
        'twitter':twitter,
        'telegram':telegram,
        'discord':discord,
        'website':website,
        'type':typpe,


        'blockchain':'avalanche'
    }
    #print(dic) 
'''     if p>10:
        break '''

driver.close()