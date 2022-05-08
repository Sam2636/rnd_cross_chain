
import requests
import re
url= "https://tofunft.com/bundle/bsc/OLwgg"

headers = {"Accept": "application/json",'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
           "X-Requested-With" : "XMLHttpRequest",}


response = requests.get(url, headers=headers)

xhr = response.text

#([A-Za-z0-9\-\_]+)
name_pattern = re.compile(r'src="/_next/static/([A-Za-z0-9\-\_]+)/_buildManifest.js').findall(xhr)
print(name_pattern[0])


#print(xhr)
