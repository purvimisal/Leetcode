#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:17:37 2019

@author: purvi
"""

def searchInsert(nums, target):
    if(target in nums):
        return nums.index(target)
    else:
        nums.append(target)
        nums.sort()
        return nums.index(target)


if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 2
    
    print(searchInsert(nums, target))