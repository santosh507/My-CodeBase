'''
Created on Jul 30, 2018

@author: hegdes
'''

import pymongo
from random import Random

conn = pymongo.MongoClient()
sampleCollection = conn.SampleDb


if __name__ == '__main__':
    x = Random()
    print(Random.random(x)*100)
    #sampleCollection.find_one()