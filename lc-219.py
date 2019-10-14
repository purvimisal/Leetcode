#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 18:03:25 2019

@author: purvi
"""

def containsNearbyDuplicate(nums,k) -> bool:
    dic = {}
    for i,j in enumerate(nums):
        if j not in dic:
            dic[j] = i
        else:
            if i-dic[j] <=k:
                return True
            else:
                dic[j] = i
    return False
    
    
    
if __name__ == "__main__":
    nums = [1,2,3,1,2,3]
    k = 2
    
    
    print(containsNearbyDuplicate(nums,k))