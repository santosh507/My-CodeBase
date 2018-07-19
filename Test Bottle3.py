import bottle
import pymongo
import json as js

# Model
def connectToMongoDb(OrderNum):
	json_array=[]
	conn = pymongo.MongoClient()
	db = conn.Orders
	json_array=[]
	jsons = db.OrderHeader.find({'ORDER':int(OrderNum)})
	
	for json in jsons:
		json_array.append(js.dumps(json).title())
	
	return json_array

# Controller
@bottle.route('/')
def orderNumberInputPage():
	
	#view
	return bottle.template('Order Request.tpl')

@bottle.post('/newPage')
def OrderNumberResponsePage():
	OrderNum = bottle.request.forms.get('OrderNum')
	return bottle.template('''%for json in request:          
						{{json}}
					%end''',request=connectToMongoDb(OrderNum))

bottle.debug(True)
bottle.run(host='localhost', port=8080)



	
