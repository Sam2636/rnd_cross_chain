import requests

def api_1(url1):
    url = url1
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',"Accept": "application/json",'X-API-Key': 'nTn7bQFYVjxOPyb3rLhdDkahNUPnwHbzbeMzuJ1S0ST7D0xdK5kBPXnzPAEC9p15'}
    response = requests.request("GET", url, headers=headers)
    #print(response.json())
    return response.json()


#pp= api_1("https://deep-index.moralis.io/api/v2/0xef764bac8a438e7e498c2e5fccf0f174c3e3f8db?chain=eth")    
pp= api_1("https://deep-index.moralis.io/api/v2/nft/0x495f947276749ce646f68ac8c248420045cb7b5e/25904909721345378695781540710917280912424441640456853830352847639701723545601/metadata/resync?chain=eth&flag=uri")    
print(pp)