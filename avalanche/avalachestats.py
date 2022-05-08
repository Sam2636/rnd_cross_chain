# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 14:36:15 2022

@author: User
"""

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
def lambda_handler():
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    # for driver we can download and specifiy the path or we can use the below code
    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
#1-------->aiotydb
    client =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')
    
    #2---------->db2
    #client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')
    my_db=client['nftgdp_avalanche']
    mycol = my_db['avalanche_slug']
    
    infoz=mycol.find({})
    #mycol2 = my_db.collection_stats_by_raritytools
    #mycol3= my_db["nftgdp_coll_details"]
    info=my_db.avalanche_stats
    
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

    fetch_date=str(date.today())

    print(fetch_date)
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

    ditt={}
    for x in infoz:
        #print(i['contract_address'])
        jk=x['contract_address']
    
      
        sd=api_1("https://nftrade.com/_next/data/{}/assets/avalanche/{}.json".format(key1,jk))
        fetch_date=str(date.today())
      
        #sd=api_1("https://nftrade.com/_next/data/tkjn7kaZYdoToTzpydZAy/assets/avalanche/{}.json".format(jk))
        pk=sd['pageProps']['contract']['id']
        vol=api_1("https://api.nftrade.com/api/v1/trades/graph?steps=days&tokenId=&contractId={}".format(pk))
        print(vol[-1])
        one_day_vol=vol[-1]['volume']
        one_day_sales=vol[-1]['sales']
        #print(vol[-1])
        name=sd['pageProps']['contract']['name']
        image=sd['pageProps']['contract']['image']
        cover_image=sd['pageProps']['contract']['cover_image']
        description=sd['pageProps']['contract']['description']
        twitter=sd['pageProps']['contract']['twitter']
        telegram=sd['pageProps']['contract']['telegram']
        discord=sd['pageProps']['contract']['discord']
        website=sd['pageProps']['contract']['website']
        typpe=sd['pageProps']['contract']['type']
        createdat=sd['pageProps']['contract']['createdAt']
        updatedat=sd['pageProps']['contract']['updatedAt']
        totalprice=sd['pageProps']['contract']['totalPrice']
        avgprice=sd['pageProps']['contract']['avgPrice']
        heighestprice=sd['pageProps']['contract']['heighestPrice']
        lowestprice=sd['pageProps']['contract']['lowestPrice']
       
        
        print("hhhhhj",lowestprice)

        dic={
            'slug_name':name, 
            'contract_id':pk,
            'contract_address':jk,
            'image_url':image,
            'description':description,
            'banner_url':cover_image,
            'description':sd,
            'twitter':twitter,
            'telegram':telegram,
            'discord':discord,
            'website':website,
            'type':typpe,
            'created_date':createdat,
            'updated_date':updatedat,
            'total_price':totalprice,
            'average_price':avgprice,
            'height_price':heighestprice,
            'lowest_price':lowestprice,
            'one_day_sale':one_day_sales,
            'one_day_volume':one_day_vol,
            'blockchain':'avalanche',
            
            }
        ditt[name]=dic
        print(ditt)
    #info.insert_one({'date':fetch_date,'items':ditt,'blockchain':'avalanche'}) 
    
driver.close()

lambda_handler()