#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:13:31 2019

@author: purvi
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        if( len(nums) <3): return []
        if len(nums) ==3:
            if(nums[0] + nums[1] + nums[2] ==0): return [nums]
        for i in range(0,len(nums)-3):
            start = i +1
            end = len(nums) -1
            while(start<end):
                sum = nums[i] +nums[start] +nums[end]
                if(sum ==0):
                    if [nums[i],nums[start],nums[end]] not in result: result.append([nums[i],nums[start],nums[end]])
                if(sum<0):
                    currS = start
                    while(currS == start and start<end): start = start +1
                else:
                    currE = end
                    while(currE == end and start<end): end = end -1
        return result