
import pymongo
from datetime import date
from collections import namedtuple
import requests

#1-------->aiotydb
client =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')

#2---------->db2
#client2 =pymongo.MongoClient('mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test')
my_db=client['nft_trade_polygon']
""" mycol = client['nftgdp']["nftslugname"]
mycol2 = my_db.collection_stats_by_raritytools
mycol3= my_db["nftgdp_coll_details"] """
info=my_db.poly_slug

#listt=["charity-raccoon", "inverseape", "led-punks-classic-club", "bored-octopus-club", "chumbivalleyofficial", "derace-horses", "eva-hoverboard", "crypto-unicorns-market", "baby-otters", "cybee"]

#https://nftrade.com/_next/data/tkjn7kaZYdoToTzpydZAy/assets/avalanche/0x81933ba6ae1bf39eace71519f35fb33fe4d72554.json

""" listt=["0x81933ba6ae1bf39eace71519f35fb33fe4d72554",
        "0x4db152a1ffb71918eaf10c0baebd5da535a51932",
        "0xf70576a5255fccfe6551f3ec8de74c9e002e1a82",
        "0x3155cd3c00fbbfe9c767465e1ec8365a9c29d639",
        "0xf0229b39a278ce003f852b1965fdb624602496ca",
        "0xfe8fcf6b03407fe7f4bf916e1649a662d1b2ee5d",
        "0x260d5af5b1c9f2c8ba129d0405a4db4b1e98d6bd",
        "0xe400fe01e57ddadb7ad21b1ef1d5952032c0208a",
        "0xfabe4d57a1248a1ba4bb45b7863900a6d5d04db6",
        "0x8372530bc1c3ef2739213059b113c76e143bc25d",] """

lip=["0x9498274b8c82b4a3127d67839f2127f2ae9753f4"]
lp="poly_PolygonPunks"
def api_1(url1):
    url = url1
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers)
    #print(response.json())
    return response.json()
for i in lip:
    sd=api_1("https://nftrade.com/_next/data/2ogRZydkZ4eA_SP433X2d/assets/polygon/{}.json".format(i))
    print(sd)
    pk=sd['pageProps']['contract']['id']
    name=sd['pageProps']['contract']['name']

    print(pk)

    dic={
        'slug_name':lp,
        'name':name, 
        'contract_id':pk,
        'contract_address':i,
        'blockchain':'polygon'

    }
    print(dic)

    info.insert_one(dic)

print("qasds-->yes")