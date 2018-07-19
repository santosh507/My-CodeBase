'''
Created on May 11, 2018

@author: hegdes
'''

def myFunc(*msg,**name):
    def child1 ():
        
        return ("Inside Child1") 
    
    def child2():
        return ("Inside Child2") 
    
    return child2
    return msg,name


print(myFunc("Hello World",first_name="Santosh",last_name="Hegde")())

