#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 09:16:01 2019

@author: purvi
"""

def twoSum(numbers, target):
    dic = {}
    for i, j in enumerate(numbers):
        if(target-j in dic):
             [x,y] = [dic[target-j], i]
        dic[j] = i
    return [x+1,y+1]    
    
    
    
if __name__ == "__main__":
    numbers = [2,7,11,15]
    target = 9
    print(twoSum(numbers, target))
    
    
