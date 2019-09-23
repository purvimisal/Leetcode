#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 10:14:52 2019

@author: purvi
"""

def majorityElement(nums) -> int:
    dic = {}
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in dic.keys():
        if(dic[i]>len(nums)/2):
            return i
    
    
    
    
    
if __name__ == "__main__":
     nums = [2,2,1,1,1,2,2]
     print(majorityElement(nums))