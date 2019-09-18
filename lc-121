#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:30:53 2019

@author: purvi
"""

def maxProfit(prices):
    max = 0
    min = prices[0]
    arr = prices[:]
    arr.sort(reverse=True)
    if(arr == prices):
        return 0
    for i in range(0,len(prices)):
        if(min>prices[i]): min = i
        print(min)
        if(max<prices[i]-min): max = prices[i]-min
        print(max)
    return max 
    
    
    
    
    
    
    
    
    
    
#    prof ={}
#    if(len(prices) == 0 or len(prices) == 1):
#        return 0
#    if(len(prices) == 2 and prices[1]>prices[0]):
#        return prices[1]-prices[0]
#    else:
#        temp = prices[0]
#        for i in range(1,len(prices)):
#            if(temp<prices[i]):
#                prof[i] = prices[i] - temp
#            else: temp = prices[i]
#        print(prof)
#    max = 0
#    min = prices[0]
#    for i in range(1,len(prices)):
#        if(min>prices[i]): min = i
#        if(max<prices[i]-min): max = prices[i]-min
#    return max  
        
        

    
    
    
    
if __name__ == "__main__":
    arr = [3,2,6,5,0,3]
    
    print(maxProfit(arr))
    
    
    
    
    
    
    
