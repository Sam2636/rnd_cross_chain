from email.mime import image
import pymongo
import time
from selenium import webdriver
import re
import requests

from webdriver_manager.chrome import ChromeDriverManager
import pyperclip as pc
myclient = pymongo.MongoClient("mongodb+srv://prabhat:aiotylabs2020!@cluster0.qgqw9.mongodb.net/test")
mydb = myclient["sol"]
mycol = mydb["slug_solona"]
info=mydb.nft_solona_slug







#how rare api extracty data     ------------------->https://howrare.is/api/v0.1/collections/shadowysupercoder








def api_1(url1):
    url = url1
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers)
    
    return response.json()





driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://howrare.is/")#--------------->coll stats
#driver.get("https://opensea.io/assets?search[categories][0]=art&search[query]=blitmap")
driver.maximize_window()
driver.delete_all_cookies()
driver.refresh()
driver.implicitly_wait(2)



#-------------------------------------------------------------------------------->list of collcetion slug
""" ap=[]
obj = driver.find_elements_by_xpath("//div[@class='all_coll_col']/a")
link_slug=set()
for w in obj:
    link_src=w.get_attribute("href").split('/')[3]
    if(link_src.find("?")==-1):
        link_slug.add(link_src) 
    #if link_slug=='?':
     #   ap.append(link_slug)  

print(link_slug)
print(len(link_slug))  """

pl=['dogsontheblock', 'antisocialrobotclub', 'blockassetlegends_ovechkin', 'hokkaidofrogz', 'solanapenguins', 'junglecats', 'meerkatmillionaires', 'titanzseries2', 'thepandas', 'copsgame', 'spacesharks', 'newworldmonkes', 'skatercatsociety', 'habibtisofarabpunkz', 'drakosunchained', 'eternalbeings', 'alphagorillas', 'skyline', 'panzerdogs', 'transdimensional_fox_federation', 'mixmob', 'thesteves', 'boneworld', 'modernmice', 'pandafraternity', 'solderlandbunnies', 'solbears', 
'magicsolanashit', 'gmgroundhogs', 'boryokulizardz', 'psynetworkplanetz', 'angryoctos', 'gamekidz', 'pandacrew', 'xindragons', 'belugies', 'solsunsets', 'smb', '888anonclub', 'spookyz', 'solarmy2d', 'cartel', 'cyberfrogs', 'phanbots', 'metasmoothbrainclub', 'cryptopets', 'hazyhippos', 'turtles', 'solanasurfers', 'raredon', 'solsantaschristmasescape', 'ruderhinosclub', 'solsisters', 'fancyfrenchies', 'seraphs', 'quantumtraders', 'cartelkittens', 'solcatcoin', 'shibafamily', 'blockassetlegends_rooney', 'solamanders', 'solanadroidbusiness', 'foxyfennecsgang', 'solamids', 'wildwestverse', 'lifinityflares', 'thekrooks', 'freakyfoxfamily', 'blockassetlegends_exiledlomu', 'nogoalfaces', 'babywukongs', 'catcartel', 'solslugs', 'dinodawgkingdom', 'souldogscity', 'soulkombat', 'solanaoctopusbusiness', 'solsnatchers', 'theelementies', 'arabpunkz', 'piggysolgang', 'lostlynxsociety', 'cryptoastronuts', 'thesolciety', 'kaizencorps', 'whalesnation', 'forgebots', 'talesfromtheattic', 'unknownpixelplants', 'sharkbros', 'soldads', '0xdrip', 'copycats', 'jellybeasts', 'sollamas', 'waifudaogamingguild', 'stealthninjas', 'babyapes', 'shkarysharks', 'thelioncats', 'akumanoneko', 'asgardarmy', 'thenastyboys', 'unitedaliens', 'poshdolphs', 'aurory', 'daringdragons', 'pixelracers', 'pawnshopgnomies', 'dogecapital', 'infamousmonkes', 'angrybunnyclub', 'sollyfish', 'lazyheroes', 'sollions', 'supersols', 'solanadogenft', 'deadogs', 'blockassetlegends_lomu', 'skeletoncrew', 'metamounts', 'megam1', 'grimsyndicate', 'theacesnft', 'famousfoxfederation', 'panzerdogstanks', 'shibasolgang', 'brobots', 'bountyhunterspaceguild', 'suckers', 'botborgs', 'kaiju', 'gloompunkclub', 'solarians', 'solanahavanacigarclub', 'bitbrawl', 'nekoverse', 'abstratica', 'civilians', 'boldbadgers', 'chinesepunkz', 'danukidojo', 'dollsociety', 'gmoot', 'wcgshearedsheep', 'divinedragonz', 'solanadogenftgen2', 'jambomambo', 'solbricks', 'derivativelions', 'solanasquirrels', 'thepantheraclub', 'solpatrol', 'solgalaxy', 'culturevultures', 'dragonslayerz', 'monkeyball', 'sneks3d', 'solarnauts', 'solninjas', 'solarmy3d', 'catalinawhalemixer', 'woofers', 'mekkafroggo', 'finefillies', 'soloths', 'solsteads', 'trippybunnytribe', 'drippypenguins', 'niftynanas', 'cryptocubmutants', 'mysterycrabs', 'peskypenguinclub', 'solsouls', 'dicecasino', 'cyberkatz', 'prickly_petes_platoon_ewcollection', 'zillaznft', 'dangervalleyducks', 'nyanheroes', 'panthersinthemetaverse', 'thesneks', 'rarewojak', 'shroomz', 'nftreessolana', 'doggos', 'degenapes', 'solanadonkeybusiness', 'bossbullsclub', 'cyberpharmacy', 'blockassetlegends_bisping', 'madtrooper', 'nfteepee', 'thegeishaclan', 'babyapesocialclub', 'danerob', 'santaminers', 'ubik', 
'artpunks', 'solsweeps', 'solanimals', 'nakedmeerkats', 'wintertinytigers', 'lonelyghose', 'kam1', 'mysteryman', 'gloriousgeckos', 'sisterverse', 'thedeer', 'cassets', 'prickly_petes_platoon_og_cactoon_series', 'solchicks', 'cybertrollsgen2', 'solaghosts', 'artmonkees', 'solanabananas', 'corruptcatz', 'theneighborhood', 'dilltheseal', 'solstein', 'luckykittens', 'psyshrooms', 'gooneytoons', 'spookeletons', 'phenomphoenixes', 'solsphere', 'nastynerds', 'stylishstuds', 'diamond_baepes_by_monkey_kingdom', 'billionairebens', 'chimpfrens', 'pixelpuffins', 'flunkdonkeys', 'balloonlabzdogz', 'goatcollection', 'framesnft', 'cryptocavemenclub', 'dirtypanda', 'degenlizzy', 'piggygirlgang', 'solseats', 'noiaducks', 'invokersnft', 'skellies', 'oinkclubnft', 'cryptocubs', 'kaidostempest', 'blockassetlegends_ali', 'soulless', 'miniroyalenations', 'suchshibas', 'solcapys', 'tinytigers', 'theinfungibles', 'groovyafterlife', 'vampiresofsol', 'exiled_degenapes', 'cutelilphant', 'brokenrobotburgerbar', 'rudegolems', 'shibalady', 'gapesonsol', 'solgods', 'venussoltraps', 'stonedapecrew', 'hoodratsnft', 'gapettesonsol', 'kiddomonkeys', 'chainmyth', 'cybertrolls', 'meremarbles', 'metabaes', 'degods', 'alphadragons', 'taiyorobotics', 'boryokudragonz', 'hippofamily', 'cybersamurai', 'litjesus', 'orcracingclub', 'skulldivision', 'chickenmafia', 'soulofox', 'solsocks', 'shadowysupercoder', 'thedegens', 'eyeballz', 'howlywolfies', 'solanamonkeyuniversity', 'camocrocs', '65millionyears', 'woolcapitalgroup', 'eitbitapes', 'titanzseries1', 'autonomousscoopshop', 'saibagang', 'coolbeans', 'theinfamousthugbirdz', 'mightyorc', 'dopeapes', 'solantis', 'roguesharks', 'redpandasquad', 'neopetsmetaverse', 'solmatch', 'elysia', 'solanamonkettebusiness', 'solanauts', 'cozycubs', 'solaticforce', 'pandastreet', 'mindfolkcabins', 'sighducks', 'thejungle', 'mutantpenguins', 'kaidotrainers', 'theframeboyjourney', 'cyberapeage', 'peeps', 'solanafelinebusiness', 'monkeybabybusiness', 'eggplantparty', 'kyra', 'perkypandaclub', 'soldough', 'bitbaddies', 'solanavalley', 'fortunecookies', 'thehellions', 'undeadsols', 'thugbirdz', 'dazedducks', 'solcats', 'mechsofsolana', 'legionpunks', 'braincaseunique', 'bobosofwar', 'punktee', 'baebots', 'toastyturts', 'angomon', 'solanageckobusiness', 'solanaswinegang', 'mindfolk', 'bitboat', 'robotmafiaclub', 'boredapesocialclub', 'playgroundwaves' ]

print(len(pl)) 
#print(cwervwrvw)
#print(ap)


#solona Data------------------>Api https://howrare.is/api/v0.1/collections/shadowysupercoder
''' for i in link_slug:
    print(i)
    s=api_1("https://howrare.is/api/v0.1/collections/{}".format(i))
    print(len(s['result']['data']['items']))
    for jk in range(len(s['result']['data']['items'])):
        print(s['result']['data']['items'][jk])
 '''



'''
elem = driver.find_element_by_xpath("//*")
source_code = elem.get_attribute("outerHTML")
 '''
#time.sleep(5)
''' source=source_code.split("<div class='stat'>")[0]

print(source) '''
''' fav =re.compile(r'<div class="stat">(.*?)</div>')     #favorite bug fix
z = fav.findall(source_code) '''

#print(z) 
#print(z)
''' elem = driver.find_element_by_xpath("//*")
source_code = elem.get_attribute("outerHTML")
 '''
#-----------------------> collection stats
''' pk=[]
secti= driver.find_elements_by_xpath("//div[@class='all_coll_row']")
for i in secti:
    heade=i.text.splitlines()
    pk.append(heade)
    #print(heade)
    #print("<------>")

print(pk) '''





'''
#//div[@class='all_coll_col']/a/img

obj = driver.find_elements_by_xpath("//div[@class='all_coll_col']/a/img")
img=[]
for w in obj:
    link_src=w.get_attribute("src")
    img.append(link_src)

print(img)


#time.sleep(3)
li=['Shadowy Super Coder','Degen Ape Academy','Aurory','Thugbirdz','Nyan Heroes','Solchicks','Solsteads','SolanaMonkeyBusiness (SMB)','Pesky Penguin Club','Stylish Studs','Sol Patrol']

print(pk[1][0])
print(img[0])



for i in range(len(pk)):
    for j in li:      
        if pk[i][0]==j:  
            dic={
            'NAME':pk[i][0],
            'FLOOR PRICE':pk[i][1],
            'ITEMS':pk[i][2],
            'HOLDERS':pk[i][3],
            'ON SALE':pk[i][4],
            'ON SALE %':pk[i][5],
            'FLOOR MC (USD)':pk[i][6],
            'img':img[i-1],
            'slug':img[i-1].split(".jpg")[0].split("logo/")[1]
            #'Image link':img[i],
            #'slug':slug
        
            }
            print("<-------->")
            print(dic) 

    
driver.implicitly_wait(1)
 '''

#solona Data------------------>Api https://howrare.is/api/v0.1/collections/shadowysupercoder
for ip in pl:
    #ip="solamids"
    print(ip)
    driver.get("https://howrare.is/{}".format(ip))#---------------> single collection details  stats
    driver.set_page_load_timeout(1000)

    elem = driver.find_element_by_xpath("//*")
    source_code = elem.get_attribute("outerHTML")

    #         id="form_filters"
    source_code=source_code.replace("\n","")#.replace(" ","")

    source_code=source_code.split('id="form_filters">')[1]
    # <div class="checkboxes">
    source_code=source_code.split('class="checkboxes">')[0]

    lst=source_code.split("<label for")



    #print(source_code)
    #print(lst)
    final_trait=[]
    for itemzz in lst[1:]:
        #print(itemzz)
        
        titleuh=itemzz.split('>')[1].split('</label')[0]
        # <div class="checkboxes">
        #titleuh=titleuh
        #print(titleuh)
        #print("---------")

        fun=itemzz.split('</option')
        #print(fun)
        segm=[]
        for seg in fun[1:len(fun)-1]:
            #print(fdgd)
            cdf=seg.split(">")[2].split("(")
            #print(cdf)
            ttname=cdf[0].strip()
            #print(ttname)
            ttcount=cdf[1].split(")")[0]
            segm.append([ttname,ttcount])
            #print(">>>>>>>>>")
        single_trait={"name":titleuh,"t_items":segm}
        final_trait.append(single_trait)
    #print(final_trait)
    ''' pk=[]  #------------------------------------------>attributes of the collection traits. for score calculation
    secti= driver.find_elements_by_xpath("//div[@id='form_filters']")
    for i in secti:
        heade=i.text#.replace("\n",",").replace(" ","").replace(",,",",").replace('Pleaseselect','[')#.split(",")
        pk.append(heade)
        #print(heade)
        print("<------>") '''

    gh={
        'slug':ip,
        'attributes':final_trait,
        'blockchain':'sol'
    }
    info.insert_one(gh)
    print(gh)
    #print(Aewa)
    #print(cwcaca)

    #print(pk)
#time.sleep(3) 
driver.implicitly_wait(1) 

#print(len(l))
#driver.close()