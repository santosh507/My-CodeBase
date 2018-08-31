'''
Created on Jul 25, 2018

@author: hegdes
'''
import os
import sys
import pyodbc
import csv
import time
import decimal
'''
odbcConn = pyodbc.connect(DSN='SYSQA DSN',UID='HEGDES',PWD='Apple@125')
print("Connection Successfull")

with odbcConn.cursor() as curObj:
    col_hdng_query = "SELECT CAST(COLUMN_TEXT AS CHAR(50) CCSID 37) AS COL_TEXT FROM QSYS2.SYSCOLUMNS WHERE SYSTEM_TABLE_NAME ='FPOPOR' AND SYSTEM_TABLE_SCHEMA = 'KATHYS'" 
    query1 = "Select count(*) from KATHYS.FPOPOR"
    query2 = "Select * from KATHYS.FPOPOR"                                         
    
    
    curObj.execute(col_hdng_query)
    col_hdngs = curObj.fetchall()
    #print(col_hdngs)
    colhdngs_list = [col[0].strip() for col in col_hdngs]
    colhdngs_list.insert(0,"_id")
    #print(colhdngs_list)
    #print(col_hdngs)
    with open("OrderHeader.csv", mode="w") as fd:
    
        writeObj = csv.writer(fd)
        writeObj.writerow(colhdngs_list)
        
        counter=0
        row_list=[] 
        curObj.execute(query2)
        start = time.time()
        
        for row in curObj:
        
            if row is None:
                break
            
            counter += 1
            
            for id,val in enumerate(row):   
                
                if isinstance(row[id], decimal.Decimal) == True:
                    row_list.append(int(row[id]))
                else:
                    row_list.append(row[id].strip())
            
            row_list.insert(0,counter)
            #print(row_list)
            writeObj.writerow(row_list)
            row_list=[]
            
            if counter % 100000 == 0:
                print("{0} rows inserted in {1} seconds...".format(counter,time.time()-start))
                
print("CSV created successfully in {} seconds".format(time.time()-start))'''
start = time.time()
os.system('mongoimport -d OrderHistory -c attribdutes -f "C:\\Users\\hegdes\\Documents\\workspace\\Test Py Project\\TestPackage\OrderHeader.csv" --type tsv')
print("Time taken {}".format(time.time()-start))
