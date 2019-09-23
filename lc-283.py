#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 12:05:36 2019

@author: purvi
"""

def moveZeroes(nums) -> None:
#    dic = {}
#    for i,j in enumerate(nums):
#        if(j): dic[i] = j
    x = len(nums)
    nums[:] = [i for i in nums if i != 0]
    nums.extend([0] * (x-len(nums)))
    
    
if __name__ == "__main__":
    nums = [0,1,0,3,12]
    print(nums)
    moveZeroes(nums)
    print('after:',nums)
        