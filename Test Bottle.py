
import pyodbc
import decimal
import json
import re
from bottle import route, run, template

@route('/<legacyOrderID>')
def index(legacyOrderID):
	try:
		connectToPyODBC()
		fetchDetails(legacyOrderID)
    

run(host='localhost', port=8080)

def connectToPyODBC():
	#Establish iSeries Connection to DB2400 from Python
	connection = pyodbc.connect(DSN='SYSQA DSN',UID='HEGDES',PWD='Apple@124')

def fetchDetails():
	json_dict={}

	counter = 0

	#Lamba Function
	column_head = lambda col_hdng: re.sub('\.+', ' ', col_hdng).strip() if re.search('\.+',col_hdng) else col_hdng.strip()

	with connection.cursor() as c1:
		col_hdng_query = "SELECT CAST(COLUMN_TEXT AS CHAR(50) CCSID 37) AS COL_TEXT FROM QSYS2.SYSCOLUMNS WHERE SYSTEM_TABLE_NAME ='FPOPOR' AND SYSTEM_TABLE_SCHEMA = 'KATHYS'" 
		query = "Select * from KATHYS.FPOPOR where ORDIV = 'MSC' and ORORNO="+legacyOrderID.strip()                                         
		
		c1.execute(col_hdng_query)
		col_hdngs = c1.fetchall()
		col_list = [column_head(col_hdng[0]) for col_hdng in col_hdngs]
		
		c1.execute(query)       
				
		while True:
			row = c1.fetchone()
			
			
			if row is None:
				break
			counter += 1
			json_dict['_id']= counter
			 
			for i in range(len(col_list)):
				for j in range(i,len(row)):
				   
					
					if isinstance(row[j], decimal.Decimal) == True:
						json_dict[col_list[i]]=int(row[j])
					else:
						json_dict[col_list[i]]=row[j].strip()
					break
					
					
			return template('<b>Hello {{name}}</b>!', name=name) json.loads(json_dict)
			json_dict={}
			
		 


