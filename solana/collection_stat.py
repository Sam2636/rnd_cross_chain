from operator import le
import requests

def api_1(url1):
    url = url1
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers)
    return response.json()

url = "https://qzlsklfacc.medianetwork.cloud/get_collections" 
headers = {"Accept": "application/json"}
response = requests.request("GET", url, headers=headers)
s=[]
setp=[]
lll=[]
#------------------------------------------------------------------------------------------------------------------>solonart
#setuh=set()                                       ----------------------------->solona art
''' for i in range(len(response.json())):
    #print(response.json()[i]['url'])
    ds=response.json()[i]['url']
    setp.append(ds)

    s=api_1("https://qzlsklfacc.medianetwork.cloud/get_attributes_floor_price?collection={}".format(ds))
    dp={
        "name":ds,
        "attributes":s,
        }
    print(dp)
print(len(setp))
#https://qzlsklfacc.medianetwork.cloud/get_attributes_floor_price?collection=degenape   '''


#------------------------------------------------------------------------------------------------------------------->magic eiden
s=api_1("https://api-mainnet.magiceden.io/all_collections")  #---------------------->magic edien
for j in range(len(s["collections"])):
    fd=s["collections"][j]["symbol"]
    setp.append(fd)
    #setuh.add(fd)
    #https://api-mainnet.magiceden.io/all_collections                    #--------------------------->all collection slug
    #https://api-mainnet.magiceden.io/rpc/getCollectionEscrowStats/parks        #----------------------->attributes api
    er=api_1("https://api-mainnet.magiceden.io/rpc/getCollectionEscrowStats/{}".format(fd))
    pk=er['results']['availableAttributes']
    df={
        "name":fd,
        "attributes":pk   
        }

    print(df)


#https://magiceden.io/item-details/GyxQzg8Lqub19fUPDH5nf7hE4KAWFr7yqGDKDysuDe3C     #------------------->




'''     if fd in setp:
        lll.append(fd)
print("------")
print("len:",len(lll)) '''
#print("union",len(setuh))

#----------------------------------------------------------------------------------------------------->how rare
'''     #print(s["collections"][j]["symbol"])
s=api_1("https://howrare.is/api/v0.1/collections")               #------------------------>how rare
for j in ((s["result"]["data"])):
    fl=j["url"].replace("/","")
    setp.append(fl)
    #setuh.add(fd)

#print("union",len(setuh))
#print(s["collections"][j]["symbol"])
print(len(response.json()))
#print(len(s["collections"]))
print(len(setp))
print(setp)
'''
''' for t in s:
    if t not in setp:
        print(t)
        s.append(t)

print(len(s)) '''
''' print("union",len(setuh))
print(setuh) '''


#print(len(response.json()))
#solona art 
#https://qzlsklfacc.medianetwork.cloud/get_attributes_floor_price?collection=degenape   -----> attribtes for score calculation
#https://qzlsklfacc.medianetwork.cloud/query_volume_all  --------------> first page ranking details
#https://qzlsklfacc.medianetwork.cloud/get_collections ------------->get collection deetails

''' import requests

url="https://api.opensea.io/api/v1/assets?token_ids=19501&token_ids=19502&token_ids=19503&token_ids=19504&token_ids=19505&token_ids=19506&token_ids=19507&token_ids=19508&token_ids=19509&token_ids=1951&token_ids=19510&token_ids=19511&token_ids=19512&token_ids=19513&token_ids=19514&token_ids=19515&token_ids=19516&token_ids=19517&token_ids=19518&token_ids=19519&order_direction=desc&offset=0&limit=21"
#url="https://api.opensea.io/api/v1/assets?token_ids=19519&order_direction=desc&offset=0&limit=21"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',"Accept": "application/json"}
response = requests.request("GET", url, headers=headers)
print(response.json()) '''