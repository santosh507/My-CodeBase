'''
Created on Aug 3, 2018

@author: hegdes
'''
import time
import datetime
import requests
import urllib

struct = time.localtime()
print(struct)

print(datetime.datetime.now())

print(datetime.datetime.now().strftime('%Y/%m/%d %A %B %C %y %F %H:%M').encode('utf8'))

#res = requests.get(url="https://www.pythonforbeginners.com")
res = requests.get(url="http://localhost:8080/45905726",headers={'User-Agent':'My Bot 1.0'})
print(res.text)