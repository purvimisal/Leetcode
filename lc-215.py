#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 12:40:43 2019

@author: purvi
"""

def findKthLargest(nums, k) -> int:
    nums.sort()
    print(nums)
    return nums[len(nums)-k]
    
    
    
        
if __name__ == "__main__":
    nums = [3,2,1,5,6,4]
    k = 2
    print(findKthLargest(nums, k))
    