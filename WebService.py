import bottle
import json
import pymongo
import pyodbc
import socket

def findOrder(order_num):
    mongo_conn = pymongo.MongoClient()
    db = mongo_conn.Orders
    docs = db.OrderHeader.find({'Order': int(order_num)})
    response=[]
    for doc in docs:
        response.append(json.dumps(doc))
    '''if doc == None || doc = '':
        connection = pyodbc.connect(DSN='SYSQA DSN', UID='HEGDES', PWD='Apple@125')'''

    return response

@bottle.get('/<order_num>')
def controller(order_num):
    return findOrder(order_num)

bottle.debug(True)
#bottle.run(host='localhost',port='8080')
bottle.run(host=socket.gethostbyname(socket.gethostname()))
#findOrder(45905726)