#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 12:41:47 2019

@author: purvi
"""

def maxProduct(nums) -> int:
    max = nums[0]
    prev = 1
    for i in nums:
        if(prev*i > i):
            prev *=i
        else: prev = i
        if(max<prev): max = prev
    return max
    
    
if __name__ == "__main__":
    nums = [-3,3,-4]
    
    print(maxProduct(nums))