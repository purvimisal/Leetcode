#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 12:15:51 2019

@author: purvi
"""

def threeSum(nums):
    l = len(nums)
    dic = {}
    arr = []
    for i in range(0,l):
        for j in range(0,l):
            if(i!=j):
                dic[nums[i]+nums[j]] = [nums[i],nums[j]]
    for i in dic:
        if 0-i in nums and dic[i][0]!=i and dic[i][1]!=i:
           arr.append((dic[i][0],dic[i][1],-i))
    return [list(i) for i in arr]
    
        
   
        
        
if __name__ == "__main__":
     nums =  [-1, 0, 1, 2, -1, -4]
     print(threeSum(nums))
     
     