from numpy import block
import pymongo
import time
from selenium import webdriver
import re

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pyperclip as pc
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
#driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)

myclient = pymongo.MongoClient("mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test")
mydb = myclient["polygon_nft_details"]
#mycol = mydb["coll_solona"]
info=mydb["inverseape"]

driver = webdriver.Chrome(ChromeDriverManager().install())

contra_add='0x3c8ba6955d5e69cf853d421bf197939da2631595'      # contract address of the collection
def scrap(i):
  
    blockchain="matic"
    #i=9887
    print(i)
    driver.set_page_load_timeout(500)
    driver.get("https://opensea.io/assets/{}/{}/{}".format(blockchain,contra_add,i))          
    
    driver.maximize_window()
    driver.delete_all_cookies()
    #driver.refresh()
    driver.implicitly_wait(2)


    elem = driver.find_element_by_xpath("//*")
    source_code = elem.get_attribute("outerHTML")
    
    try:
        error=source_code.split('<div class="error--')[1].split('">')[0]
        print(error,"---->",i)
    except:
        error='200'
    if error=='404':
        pass
    else:

        #image
    
        try:
            try:
                suy=source_code.split('<img class="Image--image" src="')[1].split('"')[0]
            except:  
                time.sleep(4)
                suy=source_code.split('<img class="Image--image" src="')[1].split('"')[0]  
                #print('case<-->',suy)
        except:
            try :
                suy=source_code.split('<source src="')[1].split('"')[0]
            except :
                time.sleep(4)
                suy=source_code.split('<source src="')[1].split('"')[0]
                # print("video<-->",suy)


    
        sp=source_code.split('<section class="item--header">')[1].split('</h1></section>')[0]

    
        kl=sp.split('</a></div></div><div class="item--collection-toolbar-wrapper">')[0]
    
        tl=kl.split('" href="/collection/')[1].split('">')   
    
        
        try:
            #print(sp.split('class="BlockreactBlock-sc-1xf18x6-0 dBFmez item--title">')[1])
            nft_name=sp.split('class="BlockreactBlock-sc-1xf18x6-0 dBFmez item--title">')[1] 
            #print('case1------')   #--------------->nft_name
        except:
            #print(sp.split('title="')[1].split('">'))             #--------------->nft_name
            
            nft_name=sp.split('title="')[1].split('">')[0] 
            #print('<case2-->')  #--------------->nft_name

        try :
            price=source_code.split('<div class="TradeStation--main">')[1].split('<div class="item--frame">')[0]
        except :
            pass
    
        try:
            current_price=price.split('Current price</div><div class="TradeStation--price-container"><div class="Pricereact__DivContainer-sc-t54vn5-0 iBLrYW Price--main TradeStation--price"><div cursor="pointer" class="Blockreact__Block-sc-1xf18x6-0 kTFrxw"><a class="styles__StyledLink-sc-l6elh8-0 ekTmzq" href="https://scope.klaytn.com/account/0xfd844c2fca5e595004b17615f891620d1cb9bbb2" rel="nofollow noopener" target="_blank"><div size="24" class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexColumnreact__FlexColumn-sc-1wwz3hp-0 VerticalAlignedreact__VerticalAligned-sc-b4hiel-0 CenterAlignedreact__CenterAligned-sc-cjf6mn-0 Avatarreact__AvatarContainer-sc-sbw25j-0 bTIktT jYqxGr ksFzlZ iXcsEj cgnEmv dukFGY"><img alt="WKLAY on Klaytn" class="Blockreact__Block-sc-1xf18x6-0 Avatarreact__ImgAvatar-sc-sbw25j-1 bTIktT hzWBaN" src="https://storage.opensea.io/static/tokens/WKLAY.png" size="24"></div></a></div><div class="Overflowreact__OverflowContainer-sc-7qr9y8-0 jPSCbX Price--amount" tabindex="-1">')[1].split('<span class="Price--raw-symbol">')[0]
        except:
            current_price='None'
    

        pl=source_code.split('<section class="item--counts">')[1].split('</button></section>')[0]
        #print(pl)
    
        dfg=pl.split('href="/')[1].split('"><span>')[0]


    
        try:    
            created=source_code.split('<section class="Blockreact__Block-sc-1xf18x6-0 Framereact__Frame-sc-139h1ex-0 dBFmez ihcaBg item--frame item--summary-frame">')[1].split('</span></div></div></div></div></div></div></div></div></section>')[0]
            creator=created.split('?tab=created"><span>')[1].split('</span></a></div></section></div></div></div></div></div><div class="Panelreact__DivContainer-sc-1uztusg-0 ejFaWs Panel--isClosed Panel--isFramed"')[0]    #-------------->created by
            #print(created.split('?tab=created"><span>')[1].split('</span></a></div></section></div></div></div></div></div><div class="Panelreact__DivContainer-sc-1uztusg-0 ejFaWs Panel--isClosed Panel--isFramed"')[0])    #-------------->created by
        except:
            creator='None'
    
        details=created.split('Details</span>')[1].split('</section>')[0]
    
        contract=details.split('class="Blockreact__Block-sc-1xf18x6-0 Textreact__Text-sc-1w94ul3-0 ChainInforeact__ValueText-sc-7gbmjn-1 dBFmez cCfKUE jmAsQO"><a class="styles__StyledLink-sc-l6elh8-0 ekTmzq" href="')[1].split('"')[0]
    
        token=details.split('<button class="UnstyledButtonreact__UnstyledButton-sc-ty1bh0-0 TextCopierreact__StyledContainer-sc-ga2cnk-0 btgkrL" type="button">')[1].split('</button>')[0]

    
        schema=details.split('Token Standard<span class="Blockreact__Block-sc-1xf18x6-0 Textreact__Text-sc-1w94ul3-0 ChainInforeact__ValueText-sc-7gbmjn-1 dBFmez cCfKUE jmAsQO">')[1].split('</span>')[0]
    

    
        blockchain=details.split('Blockchain<span class="Blockreact__Block-sc-1xf18x6-0 Textreact__Text-sc-1w94ul3-0 ChainInforeact__ValueText-sc-7gbmjn-1 dBFmez cCfKUE jmAsQO">')[1].split('</span>')[0]


     
        try :
            prop=created.split('<div class="Panel--isContentPadded item--properties">')[1].split('class="Panelreact__DivContainer-sc-1uztusg-0 ejFaWs Panel--isClosed Panel--isFramed"')[0].split('<a href=')

            

            li=[]
            for i in prop[1:]:
                #print("------",i)
                typee=i.split('<div class="Property--type">')[1].split('<')[0]
                #print(typee)
                value=i.split('data-testid="Property--value">')[1].split('<')[0]
                #print(value)
                
                rarity=i.split('class="Property--rarity">')[1].split('% have this trait<')[0]
                #print(rarity)
            # print("----------")

                dic={
                    '_type':typee,
                    'value':value,
                    'rarity_percent':rarity
                }

                li.append(dic)
            dictsmain={}
            for i in range(len(li)):
                
                dictsmain[li[i]['_type']]={
                    'trait_type': li[i]['_type'], 'value':li[i]['value'], 'rarity_percent': li[i]['rarity_percent']
                }

            pk={
                'owner_name':dfg,
                'owner_address':"https://opensea.io/{}".format(dfg)
            }  
        except :
            pk={
            'owner_name':dfg,
            'owner_address':"https://opensea.io/{}".format(dfg)
            } 
            dictsmain="None"    

        dcp={
            'token_id':token,
            'nft_name':nft_name,
            'image_url':suy,
            'perma_url':"https://opensea.io/assets/matic/{}/{}".format(contract,token),
            'slug':tl[0],
            'collection_name':tl[1],
            'owned_by':dfg,
            'created_by':creator,
            'contract_address':contract,
            'owner_details':pk,
            'schema':schema,
            'blockchain':blockchain,
            'current_price':current_price,
            'traits':dictsmain
        }
        #info.insert_one(dcp)        

for i in range(3646,10001):
    try:
        scrap(i)
    except IndexError:
        print("----case504--pass")
        driver.refresh()
        continue
            
driver.close()