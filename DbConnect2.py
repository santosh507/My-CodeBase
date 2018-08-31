'''
Created on May 15, 2018

@author: hegdes
'''
import pyodbc
import decimal
import pymongo
import time
import re

try:
    #Establish iSeries Connection to DB2400 from Python
    connection = pyodbc.connect(DSN='MYDSN',UID='$HEGDES',PWD='qwerty@124')
    doc=[]
    json_dict={}
    
    counter = 0
    print("Connection succesfull...")
    column_head = lambda col_hdng: re.sub('\.+', ' ', col_hdng).strip().title() if re.search('\.+',col_hdng) else col_hdng.strip().title()
    
    with connection.cursor() as c1:
        col_hdng_query = "SELECT CAST(COLUMN_TEXT AS CHAR(50) CCSID 37) AS COL_TEXT FROM QSYS2.SYSCOLUMNS WHERE SYSTEM_TABLE_NAME ='FPOPOR' AND SYSTEM_TABLE_SCHEMA = 'KATHYS'" 
        query = "Select * from KATHYS.FPOPOR where ORDIV = 'MSC'"
        
        
        c1.execute(col_hdng_query)
        col_hdngs = c1.fetchall()
        col_list = [column_head(col_hdng[0]) for col_hdng in col_hdngs]
        #print(col_hdngs)
        
        c1.execute(query)       
        start = time.clock()
        #rows = c1.fetchall()
        end =  time.clock()       
        while True:
            row = c1.fetchone()
            #print(row)
            
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
            
            #print(json_dict)
            
        #Iterate throw list of tuples to get Data into a new Dictinionary
        '''for i in range(0,len(rows)):
            counter += 1
            json_dict['_id']= counter
            
            for k in range(len(col_list)):
                for j in range(k,len(rows[i])):
                    
                    if isinstance(rows[i][j], decimal.Decimal) == True:
                        json_dict[col_list[k]]=int(rows[i][j])
                    else:
                        json_dict[col_list[k]]=rows[i][j].strip()
                    break
                    
            doc.append(json_dict)
            print(json_dict)
            json_dict={}'''
            
    #Iterate throw list of tuples to get Column Headings in a new List
    '''for row in c1.fetchall():
        #doc.append(dict(zip(col_list, row)))
        doc.append(dict(zip(col_list, row)))
    print(doc)'''    
     
    ''' for tuple in tuples: 
          json_dict = collections.OrderedDict()
          counter += 1
          json_dict['_id']= counter
          json_dict['COMPANY']= tuple.COMPANY'''
    
    
        
        #print(doc)
        

        #if counter = 100:         

                
    end = time.clock()
    print("SQL Fetch Took {} seconds".format(end-start))
    print(counter)

except TypeError as exp:
    print(exp)
except pyodbc.InterfaceError as pyexp:
    print(pyexp)
