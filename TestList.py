'''
Created on Jun 6, 2018

@author: hegdes
'''
import time

def methodTime(func):
    def wrapper():
        start = time.clock()
        func()
        end=time.clock()
        print("Time Taken in sec :",end-start)
    return wrapper

@methodTime
def countListItems():
    name = ['Apple','Mango','Banana','Apple','grape','Orange','Apple','Banana']
    myDict = {}
    for fruit in name:    
        if fruit in name:
            myDict[fruit] = name.count(fruit)
        else:
            myDict[fruit] = 1  
    
    return myDict
   
        
if __name__ == "__main__":
    
    
    print(countListItems())
