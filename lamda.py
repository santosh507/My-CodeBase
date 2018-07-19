'''
Created on Apr 25, 2018

@author: hegdes
'''
import sys
import re
from _functools import reduce
n = [4,5,6,7,8]
print(n)
print()
list1 = list(map(lambda x:x**2,n)) 
print(list1)

'''print({x**2 for x in n})


highest = lambda x,y:x if(x>y) else y

print(highest(4,3))'''
print()

    
list2 = list(filter(lambda x:x %2==0,n))
print(list2)


list3 = reduce(sum,n)
print(list3)


def sum(x):
    y=[]
    for id,val in enumerate(n):
        y.append(val*n[id+1])
    return y
#print(sys.version)

'''str = input("Enter the pwd : ")
print(re.findall(^[A-Z],str))

c = myFunc()
print()


def myFunc(self):
    yield "Hello World"
    yield "Monkey"
    yield "rabbit"'''