import bottle
import pyodbc
import json as js
import re
import decimal

# Model
def connectToPyODBC(OrderNum):
	doc=[]
	json_dict={}
	counter=0
	
	conn = pyodbc.connect(DSN='SYSQA DSN',UID='HEGDES',PWD='Apple@124')
	column_head = lambda col_hdng: re.sub('\.+', ' ', col_hdng).strip() if re.search('\.+',col_hdng) else col_hdng.strip()
	
	with conn.cursor() as cur:
		col_hdng_query = "SELECT CAST(COLUMN_TEXT AS CHAR(50) CCSID 37) AS COL_TEXT FROM QSYS2.SYSCOLUMNS WHERE SYSTEM_TABLE_NAME ='FPOPOR' AND SYSTEM_TABLE_SCHEMA = 'KATHYS'" 
		query = "Select * from KATHYS.FPOPOR where ORORNO="+OrderNum                                         
        
        
		cur.execute(col_hdng_query)
		col_hdngs = cur.fetchall()
		col_list = [column_head(col_hdng[0]) for col_hdng in col_hdngs]
       
		cur.execute(query)       
	
		while True:
			row = cur.fetchone()
            #print(row)
            
			if row is None:
				break
			counter += 1
             
			for i in range(len(col_list)):
				for j in range(i,len(row)):

					if isinstance(row[j], decimal.Decimal) == True:
						json_dict[col_list[i].title()]=int(row[j])
					else:
						json_dict[col_list[i].title()]=row[j].strip()
					break
            
			doc.append(js.dumps(json_dict))
			json_dict={}
            
	return doc
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
					%end''',request=connectToPyODBC(OrderNum))

bottle.debug(True)
bottle.run(host='localhost', port=8080)



	
