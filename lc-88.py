#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:58:51 2019

@author: purvi
"""
#
#def merge(nums1, m, nums2, n): 
#        count = 0
#        n1 = [i for i in nums1 if i!= 0]
#        for i in nums1: 
#            if(i ==0): count+=1
#        if (m>= n):
#            nums1[:] = n1 +nums2
#            nums1.sort()
#        elif(count>=n):
#            nums1[:] = nums2 


def merge(nums1, m, nums2, n):
    nums1[m:m+n] = nums2
    nums1.sort()

if __name__ == "__main__":
    nums1 = [0]
    m = 0
    nums2 = [1]  
    n = 1
    
    merge(nums1, m, nums2, n)
    print(nums1)