#!/usr/bin/env python3

def print_fibonacci(length):
    a,b =0,1
    result=[]
    while length>0:
        result.append(a)
        a,b = b, a + b
        length -=1
    print(result)    
print_fibonacci(9)   