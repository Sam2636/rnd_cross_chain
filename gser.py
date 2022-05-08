import requests

url = "https://api.opensea.io/api/v1/assets?token_ids=5217&token_ids=5218&asset_contract_addresses=0xdc0479cc5bba033b3e7de9f178607150b3abce1f&order_direction=desc&offset=0&limit=20"

#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',"Accept": "application/json","X-API-KEY": " 5ca9ad56f654460c95f7c1aa25cbcd13"}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',"Accept": "application/json","X-API-KEY":"5ca9ad56f654460c95f7c1aa25cbcd13"} 
                
response = requests.request("GET", url, headers=headers)

print(response.json())


''' import requests

url = "https://axie-infinity.p.rapidapi.com/get-battle-log/0xc6aaba4d4ede6c5cbc1bb9fd863701726ed63d2e"

headers = {
    'x-rapidapi-host': "axie-infinity.p.rapidapi.com",
    'x-rapidapi-key': "SIGN-UP-FOR-KEY"
    }

response = requests.request("GET", url, headers=headers)

print(response.text) '''

""" import requests

url = "https://api.opensea.io/api/v1/assets?token_ids=5587&asset_contract_addresses=0x3c8ba6955d5e69cf853d421bf197939da2631595&order_direction=desc&offset=0&limit=20"

headers = {
    "Accept": "application/json",
    "X-API-KEY": " 5ca9ad56f654460c95f7c1aa25cbcd13"
}

response = requests.request("GET", url, headers=headers)

print(response.text) """