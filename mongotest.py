'''
Created on May 4, 2018

@author: hegdes
'''
import json

with open('C:\data\db\ORDHIS1_3K.js','r') as fd:
    json_data = ' '.join(fd.readlines())
    json_dict = json.loads(json_data)
    print(json_dict)
    
    
    
