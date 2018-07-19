'''
Created on May 6, 2018

@author: hegdes
'''
import pymongo
import json
conn = pymongo.MongoClient()
db = conn.mongojson
result = db.zips
for each in dir(result):
    print(each)
for doc in result.find({}):
    print(doc)
    print(json.dumps(doc,indent=4,sort_keys=True))

