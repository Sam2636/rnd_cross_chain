""" import requests

url = "https://api.opensea.io/api/v1/events?collection_editor=boredapeyachtclub"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    "Accept": "application/json",
    "X-API-KEY": "5ca9ad56f654460c95f7c1aa25cbcd13"
}

response = requests.request("GET", url, headers=headers)

print(response.text) """

import requests

url = "https://api.opensea.io/api/v1/asset/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d/8520/offers?limit=20"

headers = {
    "Accept": "application/json",
    "X-API-KEY": "5ca9ad56f654460c95f7c1aa25cbcd13"
}

response = requests.request("GET", url, headers=headers)

print(response.text)