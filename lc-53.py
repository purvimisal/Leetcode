#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 12:11:19 2019

@author: purvi
"""

def maxSubArray(nums) -> int:
    maxsum = nums[0]
    min = 0
    for i in nums:
        if(min+i>i): min+=i
        else:  min = i
        if(min>maxsum):
            maxsum = min
    return maxsum
    
    
    
    
    
#    maxSum = nums[0]
#        prevMaxSum = 0
#		
#        if not nums:
#            return None
#        
#        if len(nums) == 1:
#            return nums[0] 
#        
#        for num in nums:
#            prevMaxSum = max(prevMaxSum + num, num)
#            maxSum = max(prevMaxSum, maxSum)
    
    
    
if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    
    maxSubArray(nums)