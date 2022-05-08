import requests
import re




def api_1(url1):
    url = url1
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers)
    print(response.json())
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
#blockchain="polygon" 
blockchain="bsc"
#blockchain="avax"


api_1("https://tofunft.com/_next/data/{}/en/ranking.json?network={}".format(tofu_key,blockchain))         #----------------->ranking



api_1("https://tofunft.com/_next/data/{}/en/{}.json?network={}".format(tofu_key,blockchain,blockchain))  #-------------->no_of collection



contract_address ='0xDD86Cbc9465257917B32B5d25706E237B6285A2C'
token_id='328'
api_1("https://tofunft.com/_next/data/{}/en/nft/{}/{}/{}.json?".format(tofu_key,blockchain,contract_address,token_id))   #------------->specific details  api