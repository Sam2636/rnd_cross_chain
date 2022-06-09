# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 16:51:08 2022

@author: User
"""
import json
import requests
from web3 import Web3
from web3._utils.events import get_event_data
import requests

def main1():
    url="https://api.etherscan.io/api?module=account&action=tokennfttx&contractaddress=0x23581767a106ae21c074b2276D25e5C3e136a68b&page=1&offset=5&startblock=0&endblock=27025780&sort=desc&apikey=HRNRSG6M94RNXEVTD8ZY6A247E2WJX3HM7"
    response=requests.get(url)
    out=response.json()
    response=out['result']
    print(response)
    
    infura= "https://mainnet.infura.io/v3/bd9f073d0a47405486102f47b634c1d4" #---------------eth
    w3 =Web3(Web3.HTTPProvider(infura))
    trans_hash=[]
    trans_history=[]
    for i in response:
        #print(i['hash']) 
        hash1=i['hash']
        #print("jjjjjjjjjjjj",hash1)
        
        timestamp=i['timeStamp']
        contract_address=i['contractAddress']
        token_id=i['tokenID']
        token_name=i['tokenName']
        trans_hash.append(hash1)
        log=w3.eth.getTransaction(hash1)
        print("...............",log)
        a=log['value']
        dic={
        'from':log['from'],
        'to':log['to'],
        'block':log['blockNumber'],
        'hash':hash1,
        'gsaPrice':log['gasPrice'],
        'timestamp':timestamp,
        'contractaddress':contract_address,
        'token_id':token_id,
        'token_name':token_name,
        'eth_value':log['value']
        }
        #print(dic)
        trans_history.append(dic)
    print(trans_history)
    #print("hash",trans_hash)
main1()
        
        
        #print("iiiiiiiii",log['value'])
       
        
       