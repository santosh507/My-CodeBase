import requests
import json
import urllib.request
import urllib.parse

#resp = requests.get(url="http://localhost:8080/45905726",headers={'User-Agent':'Your Bot 1.0'})
resp = requests.get(url="https://api.chucknorris.io/jokes/random",headers={'User-Agent':'Your Bot 1.0'})
print(json.loads(resp.text)['value'])

values={'category':'dev'}
data = urllib.parse.urlencode(values)
enc_data=data.encode('utf-8')
hand = urllib.request.Request(url="https://api.chucknorris.io/jokes/random",data=enc_data,headers={'User-Agent':'Mozilla/4.0'})
req = urllib.request.urlopen(hand)
print(req.read().decode())