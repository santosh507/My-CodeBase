audit = '''
Created on May15,2018
Jun13,2018
@author: hegdes
@author: suhas
@author: pritam
@author: prashant
@author: Bro's
'''
import re

def vol (a,b,c):
    return a*b*c

def vol (a,b,c):
    return float(a*b*c)

print(re.sub('(Cookie){2}','T', 'CookieCookie in a Cookie jar '))

print(re.findall(r'[A-Za-z][a-z]{2}\s?\d{2},\s?\d{4}', audit))

print(re.findall(r'@author:\s.+', audit))


#people = [input().split() for i in range(int(input()))]
#print(people)
#print(sorted(people,key=lambda x:x[2]))

print(vol(1,2,3))


