'''
Created on May 7, 2018

@author: hegdes
'''
import tweepy
 
# Consumer keys and access tokens, used for OAuth
consumer_key = 'CJmW0VI3FZvwTGFNPXRJAAEnu'
consumer_secret = 'uTC6Cqo2CjSDhUisR87hnIzQPGTpuFaKviAyWOF6uuSEqOA5aL'
access_token = '607987247-1SenFYhQShsxVPOE9V6TGjUuWpQBG8MOVGUUqcCR'
access_token_secret = 'lkWiD7Cp2P1rnldZRxQQQqHLCUPqQwiuarNQAgUBwz58S'
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

for elem in dir(api.search):
    print(elem)
# Sample method, used to update a status
'''for elem in search_results:
    print(elem)'''