from multiprocessing import context
import pymongo
from datetime import date
from collections import namedtuple
import requests
import re
import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time


def f():
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    # for driver we can download and specifiy the path or we can use the below code
    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
    #driver = webdriver.Chrome(ChromeDriverManager().install())

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





    mydb2=client['avalanche_asset']   #--------->to get no of items from database





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
    print(key1)

    p=0
    druv={}
    print(infoz)
    for x in infoz:


        p=p+1
        jk=x['contract_address']
        print("-----",jk)
        df=x['slug_name']
        tp=x['total_nft']
        print(df)
        mycol4 = (mydb2[df]).count()
        print("-------------------")
        sd=api_1("https://nftrade.com/_next/data/{}/assets/avalanche/{}.json".format(key1,jk))

        #print(sd)

        fetch_date=str(date.today())

        #""" sd=api_1("https://nftrade.com/_next/data/tkjn7kaZYdoToTzpydZAy/assets/avalanche/{}.json".format(jk))
        pk=sd['pageProps']['contract']['id']
        print("-----",pk)
        print("https://api.nftrade.com/api/v1/trades/graph?steps=days&tokenId=&contractId={}".format(pk))
        vol=api_1("https://api.nftrade.com/api/v1/trades/graph?steps=days&tokenId=&contractId={}".format(pk))
        
        #print(vol[-1])
        one_day_vol=vol[-1]['volume']
        one_day_sales=vol[-1]['sales']
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
        totalprice=float(sd['pageProps']['contract']['totalPrice'])
        avgprice=float(sd['pageProps']['contract']['avgPrice'])
        heighestprice=float(sd['pageProps']['contract']['heighestPrice'])
        lowestprice=float(sd['pageProps']['contract']['lowestPrice'])
        marketcap=float(lowestprice)*int(tp)



        stats={
            'totalVolume':totalprice,
            'averageprice':avgprice,
            'highest_price':heighestprice,
            'lowest_price':lowestprice,
            'dailySale':one_day_sales,
            'dailyVolume':one_day_vol,
            'marketcap':marketcap,
            'total_nft_db':mycol4,
            'total_nft_actual':int(tp)
        }

        dic={
            'slug':df, 
            'name':name,
            'contract_id':pk,
            'contract_address':jk,
            'img':image,
            'img_preview':cover_image,
            'description':description,
            'twitter':twitter,
            'telegram':telegram,
            'discord':discord,
            'website':website,
            'type':typpe,
            'created_date':createdat,
            'updated_date':updatedat,         
            'stats':stats,
            'blockchain':'avalanche',

            }
        #print(dic)
        druv[df]=dic

        """ if p>10:
            break """
    
    #info.insert_one({'date':fetch_date,'items':druv,'blockchain':'avalanche'})

    driver.close()
while True: #Infinite loop
    f() #Execute the function
    time.sleep(86400)

    #print(l """ambda_handler()) 