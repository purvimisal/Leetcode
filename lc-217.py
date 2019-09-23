#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 10:37:22 2019

@author: purvi
"""

def containsDuplicate(nums) -> bool:
    s = set(nums)
    if(len(s)<len(nums)):
        return True
    else:
        return False
    
    
if __name__=="__main__":
    
    
    nums1 = [1,2,3,1]
    nums2 = [1,2,3,4]
    
    print(containsDuplicate(nums2))
        