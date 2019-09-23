#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 10:25:48 2019

@author: purvi
"""

def rotate(nums, k) -> None:
    l = len(nums)
    nums[:] = nums[l-k:l] + nums[:l-k] 

    
    
    
if __name__== "__main__":
    
    nums = [1,2,3,4,5,6,7]
    k = 3
    k = k % len(nums)
    print(k)
    print(nums)
    
    rotate(nums,k)
    print('after: ',nums)
    