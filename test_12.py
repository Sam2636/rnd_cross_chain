import requests
import json

data = {
  "Device[udid]": "",
  "API_KEY": "",
  "API_SECRET": "",
  "Device[change]": "",
  "fbToken": ""
}

headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
}

url = "https://tofunft.com"

r = requests.get(url, headers=headers)
data = r.json()

print(data)