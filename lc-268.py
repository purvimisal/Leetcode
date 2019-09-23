#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 10:42:56 2019

@author: purvi
"""

def missingNumber(nums) -> int:
    nums.sort()
    s = set(nums)
    t = set(range(0,len(nums)+1))
    k = t.difference(s)
    
    return k.pop()
    
    
    
    
    
if __name__ == "__main__":
    nums1 = [3,0,1]
    nums2= [9,6,4,2,3,5,7,0,1]
    nums3 = [0,1,2]
    print(missingNumber(nums2))
    
    