from unicodedata import category
import requests

#https://marketplaceapi.beyondlife.club/api/v1/dashboard/index?page=1&filter=%7B%22category%22:[%22Digitised+Vintage+Posters%22],%22type%22:[],%22sale_type%22:[],%22keyword%22:null%7D    #sort=recently_listed


#----------------------------------------------------------------------------->ranking   select blockchain
def api_1(url1):
    url = url1
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers)
    print(response.json())
    return response.json()


#category


#category='%22Madhushala%22'      #-------------------------->#1
#category='%22Poster+Signed+Moments%22'    #--------------->  #2
#category='%22BigB+Punks%22'      #-------------------------->#3
#category='%22Chakra+Artpunks%22'    #--------------------->  #4
#category='%22Animated+Living+Comic+Book+Cover%22'    #--------------------->  #5
#category='%22Chakra+Comic+Book+Cover%22'    #--------------------->  #6
#category='%%22Seven+Chakra%27s+Powers%22'    #--------------------->  #7
#category='%22Stan+Lee+B%27day+Special%22'    #--------------------->  #8
#category='%22Stan+Lee+B%27day+Special%22'    #--------------------->  #9
#category='%22Digitised+Vintage+Posters%22'   #---------------------->10
#category='%22Animated+Chakra%22'   #---------------------->11
#category='%22Hindustan+Times+NFT%22'   #---------------------->12





api_1("https://marketplaceapi.beyondlife.club/api/v1/dashboard/index?page=1&filter=%7B%22category%22:[{}],%22type%22:[],%22sale_type%22:[],%22keyword%22:null%7D ".format(category))
