
import requests

url = "https://api.opensea.io/api/v1/assets?token_ids=6993&asset_contract_addresses=0x1a92f7381b9f03921564a437210bb9396471050c&order_direction=desc&offset=0&limit=20"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    "Accept": "application/json",
    #"X-API-KEY": " 5ca9ad56f654460c95f7c1aa25cbcd13"
}

response = requests.request("GET", url, headers=headers)

print(response.json())