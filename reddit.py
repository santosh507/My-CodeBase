'''
Created on Aug 1, 2018

@author: hegdes
'''
import urllib.request as UT
import json
import requests
import re
import pymongo


'''headers={}
headers['User-agent']='our bot 0.1'
req = UT.Request(url="https://api.chucknorris.io/jokes/random",headers=headers)
print(type(req))
resp = UT.urlopen(req)
print(resp.read())'''

req = UT.Request(url="https://api.chucknorris.io/jokes/categories",headers={'User-agent':'My Bot 1.0'})
resp = UT.urlopen(req)
category_str = resp.read().decode('utf-8')
category = re.findall(r'"([A-Za-z]*)"', category_str)

for each_cat in category:
    req = UT.Request(url="https://api.chucknorris.io/jokes/random?category="+each_cat,headers={'User-agent':'My Bot 1.0'})
    resp = UT.urlopen(req)
    data =  resp.read().decode()
    print(json.loads(data))
    
    


#resp = requests.get("https://api.chucknorris.io/jokes/random",headers = {'User-agent': 'your bot 0.1'})
#print(resp.json())
#print(json.loads(resp.text))