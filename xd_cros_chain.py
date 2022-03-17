import streamlit as st
from web3 import Web3
import requests



st.title('Cross chain')

r=st.text_input('contract Address')
#print(r)
t=st.text_input('Token_id')
#print(t)


y=st.selectbox('Pick Blockchain', ['eth', 'polygon','avax','bsc'])
if st.button('submit') is True:
    print(r,t,y)
#st.image('C:/Users/user/scopeX/web scraping/blockchain_web3_check/none.jpeg')



#contract_Add=input("enter the contract address:")
#token_id=input("enter the token id:")
    contract_Add=r
    token_id=t
    #contract_Add="0x67f4732266c7300cca593c814d46bee72e40659f" 
    #token_id=186132
    chain=y
    print("scanning......")

    #"0xf70576a5255fccfe6551f3ec8de74c9e002e1a82" 
    #8201
    
    def control(contract_Add,token_id):
        w3 =Web3(Web3.HTTPProvider(infura))

        ck_token_addr = contract_Add   # boredape
        token_add=token_id
        #acc_address = "0xf70576a5255fccfe6551f3ec8de74c9e002e1a82"      # CryptoKitties Sales Auction

        api_key="IY8CI532S53SWPTFX7FDA6G6NYI7UQC7DA"

        def api_1(url1):
            url = url1
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',"Accept": "application/json"}
            response = requests.request("GET", url, headers=headers)
            #print(response.json())
            return response.json()


        # This is a simplified Contract Application Binary Interface (ABI) of an ERC-721 NFT Contract.
        # It will expose only the methods: balanceOf(address), name(), ownerOf(tokenId), symbol(), totalSupply()

        df=api_1("https://api.etherscan.io/api?module=contract&action=getabi&address={}&apikey={}".format(ck_token_addr,api_key))
        

        simplified_abi = [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"owner","type":"address"},{"indexed":True,"internalType":"address","name":"approved","type":"address"},{"indexed":True,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"owner","type":"address"},{"indexed":True,"internalType":"address","name":"operator","type":"address"},{"indexed":False,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":True,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":True,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"claim","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"contractURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"creatorAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"generateMetadata","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCurrency","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getCurrencyAmount","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_owner","type":"address"},{"internalType":"address","name":"_operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"isOperator","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"ownerClaim","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"rand","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenOfOwnerByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"withdrawBalance","outputs":[],"stateMutability":"payable","type":"function"}]



        #ck_contract = w3.eth.contract(address=w3.toChecksumAddress(ck_token_addr), abi=simplified_abi)#+contracabi)
        #ck_contract = w3.eth.contract(address=w3.toChecksumAddress(ck_token_addr), abi=simplified_abi)#+contracabi)
        try:
            ck_contract = w3.eth.contract(address=w3.toChecksumAddress(ck_token_addr), abi=df['result'])#+contracabi)
            print(ck_contract)
        except:
            ck_contract = w3.eth.contract(address=w3.toChecksumAddress(ck_token_addr), abi=simplified_abi)
            contract = w3.eth.contract(address=w3.toChecksumAddress(ck_token_addr), abi=simplified_abi)
            #print (contract,"contract")

            #transferEvent = contract.eventFilter('Transfer', {'fromBlock': 0,'toBlock': 'latest'});
            #print (transferEvent, "transferEvent")

            #eventlist = transferEvent.get_all_entries()
            #print(eventlist, "eventlist")
        #+contracabi)
        #ck_contract1 = w3.eth.contract(address=w3.toChecksumAddress(ck_token_addr), abi=simplified_abi)
        #print(ck_contract)

        name = ck_contract.functions.name().call()
        symbol = ck_contract.functions.symbol().call()
        
        try:
            owner=ck_contract.functions.owner().call()
            print("owner_contract_Addr--->",owner)

        except:
            pass
        print(name)
        #st.header("collection")
        st.subheader(name)
        try:
            totalsupply = ck_contract.functions.totalSupply().call()
            st.subheader("totalSupply:")
            st.write(totalsupply)          
        except:
            pass


        try:
            st.header("Contract Owner")
            st.subheader(owner)
        except:
            pass    
        print(symbol) 
        #print(df)
        print(f"Fetching NFT #{token_add}")
        

        try:
            owner_of=ck_contract.functions.ownerOf(int(token_add)).call()
            er2=w3.eth.get_balance(owner)
            print("<------->",er2)
            a=w3.fromWei(er2, 'ether')    #--->contract
            print("-----val",a)
            st.subheader("wallet Balance")
            st.write(a)
            print("owner_token_Addr---->",owner_of)
            st.header('Token Owner')
            st.subheader(owner_of)
            balance=ck_contract.functions.balanceOf(owner_of).call()
            print("no_of_nft_bal",balance)
            er=w3.eth.get_balance(owner_of)
            print("----------",er)   #---->token
            s=w3.fromWei(er, 'ether')    #--->token
            print("value",s)
            st.subheader("wallet balance Token")
            st.write(s)
    
        except:
            pass    


        
        print(token_add)
        dataa = ck_contract.functions.tokenURI(int(token_add)).call()
        try:
            de=api_1(dataa)
            print(de)
            print(dataa)

            st.image(de['image'])
            
            try:
                if de['name'] == True:
                    st.title(de['name'])
            except:
                pass   
            try:
                if de['animation_url'] == True:
                    st.video(de['animation_url'])
            except:
                pass   
            try:
                s=de['description']
                st.subheader(s)
                #st.write(de['description'])
            except:
                pass   
            try: 
                if de['attributes'] !=True:
                    st.title("Attributes")
                    for i in de['attributes']:
                        for key, value in i.items():
                            #print (key, value)
                            st.subheader(key)
                            st.write(value)
            except:
                pass   
            try:
                if de['properties'] != True:
                    st.title("Attributes")
                    for i in de['properties']:
                        for key, value in i.items():
                            #print (key, value)
                            st.subheader(key)
                            st.write(value)
            except:
                pass           

        except:
            de=api_1(dataa.replace("ipfs:/","https://ipfs.io/ipfs"))
            print(de)
            print(dataa)
            #st.write("## Image example:- ")

            #img = Image.open("dogs.jpeg")
            try:
                st.image(de['image'])
            except:
                pass    
            try:
                if de['animation_url'] == True:
                    st.video(de['animation_url'])
            except:
                pass 
            print(de['image'].replace("ipfs:/","https://ipfs.io/ipfs"))
            st.image(de['image'].replace("ipfs:/","https://ipfs.io/ipfs"))
            try:
                if de['name'] == True:
                    st.title(de['name'])
            except:
                pass 
            
            #st.subheader("Description")
            try:
                if de['description'] == True:
                    st.subheader(de['description'])
            except:
                pass        

            try:
                if de['attributes']!= True:
                    st.title("Attributes")
                    for i in de['attributes']:
                        for key, value in i.items():
                            #print (key, value)
                            st.subheader(key)
                            st.write(value)
            except:
                pass            
            try:
                if de['properties'] != True:
                    st.title("Attributes")
                    for i in de['properties']:
                        for key, value in i.items():
                            #print (key, value)
                            st.subheader(key)
                            st.write(value)
            except:
                pass

            #st.write(de['attributes'])
            
        

        #print(f"{name} [{symbol}] NFTs in totalsupply: {totalsupply}")

        try:

            event_signature = w3.sha3(text="Transfer(address,address,uint256)").hex()

            logs = w3.eth.getLogs({
                "fromBlock": w3.eth.blockNumber - 120,
                "address": w3.toChecksumAddress(ck_token_addr),
                "topics": [event_signature]
            })


            for log in logs:
                print("------------------------------------------------------->",w3.eth.getTransaction(log['transactionHash']))
                print(log)
        except:
            pass        

    if chain=="eth":
        infura= "https://mainnet.infura.io/v3/bd9f073d0a47405486102f47b634c1d4" #---------------eth
        control(contract_Add,token_id)
    elif chain=="polygon":
        #infura="https://polygon-mainnet.g.alchemy.com/v2/73RCBi2WZ1JYX-lT0Xjrd3pD46AuDTp6"  #----------------polygon
        infura="https://polygon-rpc.com"  #----------------polygon
        control(contract_Add,token_id)
    elif chain=="avax":
        #infura= "https://rpc.ankr.com/avalanche" #-----------------------------------------------avax
        infura= "https://avalancherpc.com" #-----------------------------------------------avax
        control(contract_Add,token_id)
    else:
        infura= "https://bsc-dataseed.binance.org/" #---------------------------------------------bsc
        control(contract_Add,token_id)
