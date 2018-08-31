'''
Created on May 15, 2018

@author: hegdes
'''
import pyodbc
import decimal
import pymongo
import time
import re
import sys


#try:
#Establish iSeries Connection to DB2400 from Python
#connection = pyodbc.connect(DSN='SYSQA DSN',UID='HEGDES',PWD='Apple@125')
connection = pyodbc.connect(DSN='MYDSN',UID='$HEGDES',PWD='qwerty@125')
doc=[]
json_dict={}

counter = 0
print("Connection succesfull...")
column_head = lambda col_hdng: re.sub('\.+', ' ', col_hdng).strip() if re.search('\.+',col_hdng) else col_hdng.strip().title()

with connection.cursor() as c1:
    col_hdng_query = "SELECT CAST(COLUMN_TEXT AS CHAR(50) CCSID 37) AS COL_TEXT FROM QSYS2.SYSCOLUMNS WHERE SYSTEM_TABLE_NAME ='FPOPOR' AND SYSTEM_TABLE_SCHEMA = 'KATHYS'"
    #col_hdng_query = "SELECT CAST(COLUMN_TEXT AS CHAR(50) CCSID 37) AS COL_TEXT FROM QSYS2.SYSCOLUMNS WHERE SYSTEM_TABLE_NAME ='FPOPOR' AND SYSTEM_TABLE_SCHEMA = 'JUSRDTA'"
    query1 = "Select count(*) from KATHYS.FPOPOR"
    #query1 = "Select count(*) from JUSRDTA.FPOPOR"
    query2 = "Select * from KATHYS.FPOPOR"
    #query2 = "Select * from JUSRDTA.FPOPOR"
    
    
    c1.execute(col_hdng_query)
    col_hdngs = c1.fetchall()
    col_list = [column_head(col_hdng[0]) for col_hdng in col_hdngs]
    #print(col_hdngs)
    
    c1.execute(query1)       
    
    
    row_count = c1.fetchone()[0]
    print(row_count)
    div = int(row_count/1000)
    rem = row_count % 1000
    print(row_count,div,rem)

    c1.execute(query2)
    start1 = time.time() 
     
    while True:
        
        try:  
                    
            for row in c1:   
                start = time.time()

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
                
                doc.append(json_dict)
                json_dict={}
                
                if ((counter % 1000 == 0) & (counter <= (div * 1000))) | (counter > div * 1000):
                    #end = time.time()
                    #print("SQL Fetch Took {} seconds".format(end-start))
                    print(str(counter)+" records Processed...")
                    py_conn = pymongo.MongoClient()
                    db = py_conn.SysqaOrders
                    start = time.time()
                    db.OrderHeader.insert_many(doc)
                    print("Documents inserted Succesfully in {} seconds".format(time.time()-start))
                    doc=[]
            
            if row is None:
                break
            
        except KeyboardInterrupt:
            try:
                response = input('\nPausing...  (Hit ENTER to continue, type quit to exit.)')
                if response == 'quit':
                    break
                print ('Resuming...')
            except KeyboardInterrupt:
                print ('Resuming...')
                continue
        print("Total time taken is {} seconds..".format(time.time()-start1))