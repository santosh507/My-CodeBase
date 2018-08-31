'''
Created on May 11, 2018

@author: hegdes
'''
import time
import logging

def time_it_decorator(func):
    def wrapper(*args,**kwargs):
        logger.debug("Harmless debug Message")
        start = time.clock()
        print(func(*args,**kwargs))
        end = time.clock()
        print(func.__name__+" took {0} ms".format((end-start) * 1000))
        
    return wrapper   

@time_it_decorator      
def square(x):
    return [i**2 for i in range(1,x+1)]

@time_it_decorator
def cube(y): 
    return [i**3 for i in range(1,y+1)]

def init_logger():
    #Create and configure logger
    logging.basicConfig(filename="newlogfile.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')
    
if __name__ == '__main__':
    init_logger()
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    square(1000)
    print()
    cube(1000)