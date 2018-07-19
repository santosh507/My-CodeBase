import pymongo
import json as js
from bottle import route, run, template,debug



def connectToMongoDb(OrderNum):
	json_array=[]
	conn = pymongo.MongoClient()
	db = conn.Orders
	json_array=[]
	jsons = db.OrderHeader.find({'ORDER':int(OrderNum)})
	
	for json in jsons:
		json_array.append(js.dumps(json))
	
	return json_array
	

@route('/<OrderNum>')
def myFunc(OrderNum):
	return template('''%for json in request:          
						{{json}}
					%end''',request=connectToMongoDb(OrderNum))

debug(True)
run(host='localhost', port=8080)


	
