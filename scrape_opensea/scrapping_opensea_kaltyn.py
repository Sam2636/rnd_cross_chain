import pymongo
import time
from selenium import webdriver
import re

from webdriver_manager.chrome import ChromeDriverManager
import pyperclip as pc
myclient = pymongo.MongoClient("mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test")
mydb = myclient["klaytn_nft_details"]
#mycol = mydb["project-spoon-dao"]
info=mydb['project-spoon-dao']

driver = webdriver.Chrome(ChromeDriverManager().install())



#for i in range(6274,10000):
i=8320
print(i)

#driver.get("https://opensea.io")
driver.set_page_load_timeout(5000)
driver.get("https://opensea.io/assets/klaytn/0xc0e6ca567b516a6e64d63023d169ca4e57e62c1c/{}".format(i))          
#driver.get("https://howrare.is/shadowysupercoder%22)#---------------%3E single collection details  stats
#driver.get("https://opensea.io/assets?search[categories][0]=art&search[query]=blitmap%22)
driver.maximize_window()
driver.delete_all_cookies()
driver.refresh()
driver.implicitly_wait(2)

elem = driver.find_element_by_xpath("//*")
source_code = elem.get_attribute("outerHTML")
#print(source_code)
#print(source_code.split('img class="Image--image" src="')[1].split('"')[0])        #image url
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
        suy=source_code.split('<img class="Image--image" src="')[1].split('"')[0]
        print('case<-->',suy)
    except:
        suy=source_code.split('<source src="')[1].split('"')[0]
        print("video<-->",suy)


    #header item----------------------------->
    #print(source_code.split('<section class="item--header">')[1].split('</h1></section>')[0])
    sp=source_code.split('<section class="item--header">')[1].split('</h1></section>')[0]
    #print(sp)
    #print(sp.split('" href="/collection/')[1].split('"')[0])
    #print(sp.split('</a></div></div><div class="item--collection-toolbar-wrapper">')[0])#.split('</a></div></div>')[0])
    kl=sp.split('</a></div></div><div class="item--collection-toolbar-wrapper">')[0]#.split('</a></div></div>')[0])
    #print(kl.split('" href="/collection/')[1].split('">'))     #------>slug name , collection name
    tl=kl.split('" href="/collection/')[1].split('">') 
    try:  #------>slug name , collection name
        print(sp.split('class="Blockreact__Block-sc-1xf18x6-0 dBFmez item--title">')[1])   
        nft_name=sp.split('class="Blockreact__Block-sc-1xf18x6-0 dBFmez item--title">')[1] 
        print('case1------')   #--------------->nft_name
    except:
        print(sp.split('title="')[1].split('">'))             #--------------->nft_name
        #print(sp.split('title="')[1].split('">'))             #--------------->nft_name
        nft_name=sp.split('title="')[1].split('">')[0] 
        print('<case2-->')  #--------------->nft_name
    #tl=sp.split('class="Blockreact__Block-sc-1xf18x6-0 dBFmez item--title">')[1]           #--------------->nft_name


    #<div class="item--collection-info"><div class="item--collection-detail"><div class="CollectionLinkreact__DivContainer-sc-gv7u44-0 jMcPQU"><a class="styles__StyledLink-sc-l6elh8-0 ekTmzq CollectionLink--link" href="/collection/meta-rabbits-official">META RABBITS OFFICIAL V1</a></div></div><div class="item--collection-toolbar-wrapper"><div class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 ButtonGroupreact__StyledButtonGroup-sc-1skvztv-1 dBFmez jYqxGr daKevg"><button class="Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 bhqEJb jdSrqf ButtonGroupreact__StyledButton-sc-1skvztv-0 
    #eztnHW" type="button"><div aria-hidden="true" class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 jClwup jYqxGr"><i value="refresh" size="24" class="Iconreact__Icon-sc-1gugx8q-0 irnoQt material-icons">refresh</i></div></button><a class="styles__StyledLink-sc-l6elh8-0 ekTmzq Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 bhqEJb jdSrqf ButtonGroupreact__StyledButton-sc-1skvztv-0 eztnHW" href="http://linktr.ee/MetaRabbitClub" rel="nofollow noopener" target="_blank"><div aria-hidden="true" class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 jClwup jYqxGr"><i value="open_in_new" size="24" class="Iconreact__Icon-sc-1gugx8q-0 irnoQt material-icons">open_in_new</i></div></a><button class="Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 bhqEJb jdSrqf ButtonGroupreact__StyledButton-sc-1skvztv-0 eztnHW" type="button" aria-expanded="false"><div aria-hidden="true" class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 jClwup jYqxGr"><i value="share" size="24" class="Iconreact__Icon-sc-1gugx8q-0 irnoQt material-icons">share</i></div></button><button aria-label="More" class="Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 bhqEJb jdSrqf ButtonGroupreact__StyledButton-sc-1skvztv-0 eztnHW" type="button" aria-expanded="false"><div aria-hidden="true" class="Blockreact__Block-sc-1xf18x6-0 
    #Flexreact__Flex-sc-1twd32i-0 jClwup jYqxGr"><i value="more_vert" size="24" class="Iconreact__Icon-sc-1gugx8q-0 irnoQt material-icons">more_vert</i></div></button></div></div></div><h1 class="Blockreact__Block-sc-1xf18x6-0 dBFmez item--title" title="Meta Rabbit #8941">Meta Rabbit #8941







    #-------------------->ownedby
    #print(source_code.split('<section class="item--counts">')[1].split('</button></section>')[0])#.split('</section>')[0])
    pl=source_code.split('<section class="item--counts">')[1].split('</button></section>')[0]
    print(pl.split('href="/')[1].split('"><span>')[0])
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
    try:
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
            try:
                rarity=i.split('class="Property--rarity">')[1].split('% have this trait<')[0]
            except:
                rarity='None'
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
    except:
        dictsmain='None'

    dcp={
        'token_id':token,
        'nft_name':nft_name,
        'nft_image_url':suy,
        'slug':tl[0],
        'collection_name':tl[1],
        'owned_by':dfg,
        'created_by':creator,
        'contract_address':contract,
        'schema':schema,
        'blockchain':blockchain,
        'traits':dictsmain
    }

    print(dcp)
info.insert_one(dcp)
#class="Property--rarity">

