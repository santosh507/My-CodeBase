'''
Created on May 14, 2018

@author: hegdes
'''
def wrapper(f):
    list = []
    
    def fun(l):
        # complete the function
        # complete the function
        for number in l:
            if len(number) == 10:
                list.append('+91 '+number[0:5]+' '+number[5:])
            elif number[0] == '0':
                list.append('+91 '+number[1:6]+' '+number[6:])
            elif number[0:2] == '91':
                list.append('+91 '+number[2:7]+' '+number[7:])
            elif number[0:3] == '+91':
                list.append('+91 '+number[3:8]+' '+number[8:])
            
        f(list)         
    return fun


@wrapper
def sort_phone(l):
    print(sorted(l), sep='\n')

if __name__ == '__main__':
    l=[]
    for _ in range(int(input())):
        l.append(input())
    print(l)
    sort_phone(l) 