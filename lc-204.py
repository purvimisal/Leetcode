#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 22:28:09 2019

@author: purvi
"""

def primeOrnot(num):
    if num == 2: return True
    for i in range(2,num):
        if(num % i is 0):
            return False
    else:
        return True
    
def countPrimes(n):
    count = 0
    k =1
    if n>4: k = 2
    for i in range(1,n,k):
        if(primeOrnot(i)):
            count += 1
    return count
    

if __name__ == "__main__":
    
    
    print(countPrimes(2))
    
            