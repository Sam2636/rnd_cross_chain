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
mydb = myclient["klaytn_nft_details"]
mycol = mydb["coll_solona"]
info=mydb["the-meta-kongz"]

driver = webdriver.Chrome(ChromeDriverManager().install())

contra_add='0x5a293a1e234f4c26251fa0c69f33c83c38c091ff'      # contract address of the collection

for i in range(1,10000):
    blockchain="klaytn"
    #i=9887
    print(i)
    driver.set_page_load_timeout(500)
    driver.get("https://opensea.io/assets/{}/{}/{}".format(blockchain,contra_add,i))          
    #driver.get("https://howrare.is/shadowysupercoder%22)#---------------%3E single collection details  stats
    #driver.get("https://opensea.io/assets?search[categories][0]=art&search[query]=blitmap%22)
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.refresh()
    driver.implicitly_wait(2)


    elem = driver.find_element_by_xpath("//*")
    source_code = elem.get_attribute("outerHTML")
    #print(source_code.split('img class="Image--image" src="')[1].split('"')[0])        #image url

    #image
    suy=source_code.split('<img class="Image--image" src="')[1].split('"')[0]



    #header item----------------------------->
    #print(source_code.split('<section class="item--header">')[1].split('</h1></section>')[0])
    sp=source_code.split('<section class="item--header">')[1].split('</h1></section>')[0]

    #print(sp.split('" href="/collection/')[1].split('"')[0])
    #print(sp.split('</a></div></div><div class="item--collection-toolbar-wrapper">')[0])#.split('</a></div></div>')[0])
    kl=sp.split('</a></div></div><div class="item--collection-toolbar-wrapper">')[0]#.split('</a></div></div>')[0])
    #print(kl.split('" href="/collection/')[1].split('">'))     #------>slug name , collection name
    tl=kl.split('" href="/collection/')[1].split('">')   #------>slug name , collection name
    #print(sp.split('class="Blockreact__Block-sc-1xf18x6-0 dBFmez item--title">')[1])           #--------------->nft_name
    #tl=sp.split('class="Blockreact__Block-sc-1xf18x6-0 dBFmez item--title">')[1]           #--------------->nft_name
    nft_name=sp.split('class="Blockreact__Block-sc-1xf18x6-0 dBFmez item--title">')[1]     #--------------->nft_name








    price=source_code.split('<div class="TradeStation--main">')[1].split('<div class="item--frame">')[0]

    #print(price)
    #print(price.split('Current price</div><div class="TradeStation--price-container"><div class="Pricereact__DivContainer-sc-t54vn5-0 iBLrYW Price--main TradeStation--price"><div cursor="pointer" class="Blockreact__Block-sc-1xf18x6-0 kTFrxw"><a class="styles__StyledLink-sc-l6elh8-0 ekTmzq" href="https://scope.klaytn.com/account/0xfd844c2fca5e595004b17615f891620d1cb9bbb2" rel="nofollow noopener" target="_blank"><div size="24" class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexColumnreact__FlexColumn-sc-1wwz3hp-0 VerticalAlignedreact__VerticalAligned-sc-b4hiel-0 CenterAlignedreact__CenterAligned-sc-cjf6mn-0 Avatarreact__AvatarContainer-sc-sbw25j-0 bTIktT jYqxGr ksFzlZ iXcsEj cgnEmv dukFGY"><img alt="WKLAY on Klaytn" class="Blockreact__Block-sc-1xf18x6-0 Avatarreact__ImgAvatar-sc-sbw25j-1 bTIktT hzWBaN" src="https://storage.opensea.io/static/tokens/WKLAY.png" size="24"></div></a></div><div class="Overflowreact__OverflowContainer-sc-7qr9y8-0 jPSCbX Price--amount" tabindex="-1">')[1].split('<span class="Price--raw-symbol">')[0])
    try:
        current_price=price.split('Current price</div><div class="TradeStation--price-container"><div class="Pricereact__DivContainer-sc-t54vn5-0 iBLrYW Price--main TradeStation--price"><div cursor="pointer" class="Blockreact__Block-sc-1xf18x6-0 kTFrxw"><a class="styles__StyledLink-sc-l6elh8-0 ekTmzq" href="https://scope.klaytn.com/account/0xfd844c2fca5e595004b17615f891620d1cb9bbb2" rel="nofollow noopener" target="_blank"><div size="24" class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexColumnreact__FlexColumn-sc-1wwz3hp-0 VerticalAlignedreact__VerticalAligned-sc-b4hiel-0 CenterAlignedreact__CenterAligned-sc-cjf6mn-0 Avatarreact__AvatarContainer-sc-sbw25j-0 bTIktT jYqxGr ksFzlZ iXcsEj cgnEmv dukFGY"><img alt="WKLAY on Klaytn" class="Blockreact__Block-sc-1xf18x6-0 Avatarreact__ImgAvatar-sc-sbw25j-1 bTIktT hzWBaN" src="https://storage.opensea.io/static/tokens/WKLAY.png" size="24"></div></a></div><div class="Overflowreact__OverflowContainer-sc-7qr9y8-0 jPSCbX Price--amount" tabindex="-1">')[1].split('<span class="Price--raw-symbol">')[0]
    except:
        current_price='None'
    #<div class="TradeStation--ask-label">Highest offer</div><div class="TradeStation--price-container"><div class="Pricereact__DivContainer-sc-t54vn5-0 iBLrYW Price--main TradeStation--price TradeStation--price"><div cursor="pointer" class="Blockreact__Block-sc-1xf18x6-0 kTFrxw"><a class="styles__StyledLink-sc-l6elh8-0 ekTmzq" href="https://scope.klaytn.com/account/0xfd844c2fca5e595004b17615f891620d1cb9bbb2" rel="nofollow noopener" target="_blank"><div size="16" class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexColumnreact__FlexColumn-sc-1wwz3hp-0 VerticalAlignedreact__VerticalAligned-sc-b4hiel-0 CenterAlignedreact__CenterAligned-sc-cjf6mn-0 Avatarreact__AvatarContainer-sc-sbw25j-0 iihNrf jYqxGr ksFzlZ iXcsEj cgnEmv dukFGY"><img alt="WKLAY on Klaytn" class="Blockreact__Block-sc-1xf18x6-0 Avatarreact__ImgAvatar-sc-sbw25j-1 iihNrf hzWBaN" src="https://storage.opensea.io/static/tokens/WKLAY.png" size="16"></div></a></div><div class="Overflowreact__OverflowContainer-sc-7qr9y8-0 jPSCbX Price--amount" tabindex="-1">54.687 <span class="Price--raw-symbol"></span></div></div><div class="Pricereact__DivContainer-sc-t54vn5-0 iBLrYW TradeStation--fiat-price TradeStation--fiat-price"><div class="Overflowreact__OverflowContainer-sc-7qr9y8-0 jPSCbX Price--fiat-amount Price--fiat-amount-secondary" tabindex="-1">($61.25)</div></div></div><div class="Blockreact__Block-sc-1xf18x6-0 dBFmez"><div width="100%,100%,100%,50%" class="Blockreact__Block-sc-1xf18x6-0 InlineFlexreact__InlineFlex-sc-9jbsog-0 bpMMRH czWSvr"><button width="100%" type="button" class="Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 kmCSYg gIDfxn"><div aria-hidden="true" class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 cwzTQS jYqxGr"><i value="local_offer" size="24" class="Iconreact__Icon-sc-1gugx8q-0 irnoQt material-icons">local_offer</i></div>Make offer</button></div></div></div></section></div></div>


    #<div class="TradeStation--ask-label">Current price</div><div class="TradeStation--price-container"><div class="Pricereact__DivContainer-sc-t54vn5-0 iBLrYW Price--main TradeStation--price"><div cursor="pointer" class="Blockreact__Block-sc-1xf18x6-0 kTFrxw"><a class="styles__StyledLink-sc-l6elh8-0 ekTmzq" href="https://scope.klaytn.com/account/0xfd844c2fca5e595004b17615f891620d1cb9bbb2" rel="nofollow noopener" target="_blank"><div size="24" class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexColumnreact__FlexColumn-sc-1wwz3hp-0 VerticalAlignedreact__VerticalAligned-sc-b4hiel-0 CenterAlignedreact__CenterAligned-sc-cjf6mn-0 Avatarreact__AvatarContainer-sc-sbw25j-0 bTIktT jYqxGr ksFzlZ iXcsEj cgnEmv dukFGY"><img alt="WKLAY on Klaytn" class="Blockreact__Block-sc-1xf18x6-0 Avatarreact__ImgAvatar-sc-sbw25j-1 bTIktT hzWBaN" src="https://storage.opensea.io/static/tokens/WKLAY.png" size="24"></div></a></div><div class="Overflowreact__OverflowContainer-sc-7qr9y8-0 jPSCbX Price--amount" tabindex="-1">3,500 <span class="Price--raw-symbol"></span></div></div><div class="Pricereact__DivContainer-sc-t54vn5-0 iBLrYW TradeStation--fiat-price"><div class="Overflowreact__OverflowContainer-sc-7qr9y8-0 jPSCbX Price--fiat-amount Price--fiat-amount-secondary" tabindex="-1">($3,920.00)</div></div></div><div display="block,block,block,flex" class="Blockreact__Block-sc-1xf18x6-0 bsPJxM"><div class="Blockreact__Block-sc-1xf18x6-0 dBFmez" style="width: 100%; display: contents;"><div width="[object Object]" class="Blockreact__Block-sc-1xf18x6-0 InlineFlexreact__InlineFlex-sc-9jbsog-0 treHv czWSvr"><button width="100%" type="button" class="Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 kmCSYg fzwDgL"><div aria-hidden="true" class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 cwzTQS jYqxGr"><i value="account_balance_wallet" size="24" class="Iconreact__Icon-sc-1gugx8q-0 irnoQt material-icons">account_balance_wallet</i></div>Buy now</button></div><div width="100%,100%,100%,50%" class="Blockreact__Block-sc-1xf18x6-0 InlineFlexreact__InlineFlex-sc-9jbsog-0 bpMMRH czWSvr"><button width="100%" type="button" class="Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 kmCSYg gIDfxn"><div aria-hidden="true" class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 cwzTQS jYqxGr"><i value="local_offer" size="24" class="Iconreact__Icon-sc-1gugx8q-0 irnoQt material-icons">local_offer</i></div>Make offer</button></div></div></div></div></section></div></div>

    #-------------------->ownedby
    #print(source_code.split('<section class="item--counts">')[1].split('</button></section>')[0])#.split('</section>')[0])
    pl=source_code.split('<section class="item--counts">')[1].split('</button></section>')[0]
    print(pl)
    #print(pl.split('href="/')[1].split('"><span>')[0])
    dfg=pl.split('href="/')[1].split('"><span>')[0]


    #print(source_code.split('<section class="Blockreact__Block-sc-1xf18x6-0 Framereact__Frame-sc-139h1ex-0 dBFmez ihcaBg item--frame item--summary-frame">')[1].split('Blockreact__Block-sc-1xf18x6-0 Textreact__Text-sc-1w94ul3-0 ChainInforeact__ValueText-sc-7gbmjn-1 dBFmez cCfKUE jmAsQO">Polygon</span></div></div></div></div></div></div></div></div></section>')[0])
    try:    
        created=source_code.split('<section class="Blockreact__Block-sc-1xf18x6-0 Framereact__Frame-sc-139h1ex-0 dBFmez ihcaBg item--frame item--summary-frame">')[1].split('</span></div></div></div></div></div></div></div></div></section>')[0]
        creator=created.split('?tab=created"><span>')[1].split('</span></a></div></section></div></div></div></div></div><div class="Panelreact__DivContainer-sc-1uztusg-0 ejFaWs Panel--isClosed Panel--isFramed"')[0]    #-------------->created by
        print(created.split('?tab=created"><span>')[1].split('</span></a></div></section></div></div></div></div></div><div class="Panelreact__DivContainer-sc-1uztusg-0 ejFaWs Panel--isClosed Panel--isFramed"')[0])    #-------------->created by
    except:
        creator='None'
    #details------------------>
    #print(created.split('Details</span>')[1].split('</span></a></div></section></div></div></div></div></div><div class="Panelreact__DivContainer-sc-1uztusg-0 ejFaWs Panel--isClosed Panel--isFramed"')[0])
    details=created.split('Details</span>')[1].split('</section>')[0]
    #print(details)
    #cntract address
    #print(details.split('class="Blockreact__Block-sc-1xf18x6-0 Textreact__Text-sc-1w94ul3-0 ChainInforeact__ValueText-sc-7gbmjn-1 dBFmez cCfKUE jmAsQO"><a class="styles__StyledLink-sc-l6elh8-0 ekTmzq" href="')[1].split('"')[0])
    contract=details.split('class="Blockreact__Block-sc-1xf18x6-0 Textreact__Text-sc-1w94ul3-0 ChainInforeact__ValueText-sc-7gbmjn-1 dBFmez cCfKUE jmAsQO"><a class="styles__StyledLink-sc-l6elh8-0 ekTmzq" href="')[1].split('"')[0]
    #token_id
    #print(details.split('<button class="UnstyledButtonreact__UnstyledButton-sc-ty1bh0-0 TextCopierreact__StyledContainer-sc-ga2cnk-0 btgkrL" type="button">')[1].split('</button>')[0])
    token=details.split('<button class="UnstyledButtonreact__UnstyledButton-sc-ty1bh0-0 TextCopierreact__StyledContainer-sc-ga2cnk-0 btgkrL" type="button">')[1].split('</button>')[0]

    #token_standard   #------------<Schema
    schema=details.split('Token Standard<span class="Blockreact__Block-sc-1xf18x6-0 Textreact__Text-sc-1w94ul3-0 ChainInforeact__ValueText-sc-7gbmjn-1 dBFmez cCfKUE jmAsQO">')[1].split('</span>')[0]
    #print(details.split('Token Standard<span class="Blockreact__Block-sc-1xf18x6-0 Textreact__Text-sc-1w94ul3-0 ChainInforeact__ValueText-sc-7gbmjn-1 dBFmez cCfKUE jmAsQO">')[1].split('</span>')[0])

    #blockcha
    #print(details.split('Blockchain<span class="Blockreact__Block-sc-1xf18x6-0 Textreact__Text-sc-1w94ul3-0 ChainInforeact__ValueText-sc-7gbmjn-1 dBFmez cCfKUE jmAsQO">')[1].split('</span>')[0])
    blockchain=details.split('Blockchain<span class="Blockreact__Block-sc-1xf18x6-0 Textreact__Text-sc-1w94ul3-0 ChainInforeact__ValueText-sc-7gbmjn-1 dBFmez cCfKUE jmAsQO">')[1].split('</span>')[0]


    #properties
    #print(created.split('<div class="Panel--isContentPadded item--properties">')[1].split('class="Panelreact__DivContainer-sc-1uztusg-0 ejFaWs Panel--isClosed Panel--isFramed"')[0].split('<a href='))

    prop=created.split('<div class="Panel--isContentPadded item--properties">')[1].split('class="Panelreact__DivContainer-sc-1uztusg-0 ejFaWs Panel--isClosed Panel--isFramed"')[0].split('<a href=')

    #print(prop)
    #print(type(prop))

    li=[]
    for i in prop[1:]:
        #print("------",i)
        typee=i.split('<div class="Property--type">')[1].split('<')[0]
        #print(typee)
        value=i.split('data-testid="Property--value">')[1].split('<')[0]
        #print(value)
        #<div class="Property--type">
        #data-testid="Property--value">
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
        ##print("=====================================")
        dictsmain[li[i]['_type']]={
            'trait_type': li[i]['_type'], 'value':li[i]['value'], 'rarity_percent': li[i]['rarity_percent']
        }
    pk={
        'owner_name':dfg,
        'owner_address':"https://opensea.io/{}".format(dfg)
    }    

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

    # print(dcp)
    #info.insert_one(dcp)
#class="Property--rarity">

driver.close()