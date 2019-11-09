#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 08:49:12 2019

@author: purvi
"""

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = float('inf')
        min2 = float('inf')
        for i in nums:
            min1 = min(min1,i)
            if i > min1:
                min2 = min(min2,i)
            if i > min2:
                return True
        
        return False
    