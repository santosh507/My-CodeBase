'''
Created on Jul 31, 2018

@author: hegdes
'''
import time


while True:
    try:
        print("Hello World!!...\n")
        time.sleep(10)
    except KeyboardInterrupt:
        print()
        
        try:
            if (input('Hit Enter to Resume...or quit to exit').lower() == 'quit'):
                break;
        except KeyboardInterrupt:
            print("Resuming..")
            continue;
             