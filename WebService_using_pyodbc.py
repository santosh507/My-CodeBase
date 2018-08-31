import bottle
import json
import pyodbc
import socket
import re
import decimal

def findOrder(order_num):
    connection = pyodbc.connect(DSN='SYSQA DSN', UID='HEGDES', PWD='Apple@125')
    doc = []
    json_dict = {}
    column_head = lambda col_hdng: re.sub('\.+', ' ', col_hdng).strip() if re.search('\.+',
                                                                                     col_hdng) else col_hdng.strip()

    with connection.cursor() as c1:
        col_hdng_query = "SELECT CAST(COLUMN_TEXT AS CHAR(50) CCSID 37) AS COL_TEXT FROM QSYS2.SYSCOLUMNS WHERE SYSTEM_TABLE_NAME ='FPOPOR' AND SYSTEM_TABLE_SCHEMA = 'KATHYS'"
        # col_hdng_query = "SELECT CAST(COLUMN_TEXT AS CHAR(50) CCSID 37) AS COL_TEXT FROM QSYS2.SYSCOLUMNS WHERE SYSTEM_TABLE_NAME ='FPOPOR' AND SYSTEM_TABLE_SCHEMA = 'JUSRDTA'"
        query2 = "Select * from KATHYS.FPOPOR where ORORNO="+order_num
        # query2 = "Select * from JUSRDTA.FPOPOR"

        c1.execute(col_hdng_query)
        col_hdngs = c1.fetchall()
        col_list = [column_head(col_hdng[0]) for col_hdng in col_hdngs]

        c1.execute(query2)
        #row = c1.fetchall()

        for row in c1:

            if row is None:
                break

            for i in range(len(col_list)):
                for j in range(i, len(row)):

                    if isinstance(row[j], decimal.Decimal) == True:
                        json_dict[col_list[i]] = int(row[j])
                    else:
                        json_dict[col_list[i]] = row[j].strip()
                    break

            doc.append(json.dumps(json_dict))
            json_dict = {}
        return doc

@bottle.get('/<order_num>')
def controller(order_num):
    return findOrder(order_num)

bottle.debug(True)
#bottle.run(host='localhost',port='8080')
bottle.run(host=socket.gethostbyname(socket.gethostname()))
#findOrder(45905726)