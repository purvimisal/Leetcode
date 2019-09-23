#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 12:31:11 2019

@author: purvi
"""

def thirdMax(nums) -> int:

    n = list(set(nums[:]))
    n.sort(reverse=True)
    print(n)
    if (len(n)>=3): 
        return n[2]
    else: 
        if(len(n)>=2): return n[0]
        else: return n[0]
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    nums1 = [2, 2, 3, 1]
    nums2 = [3, 2, 1]
    nums3 = [1,2]
    
    print(thirdMax(nums1))