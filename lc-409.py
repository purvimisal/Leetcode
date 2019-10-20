#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:05:20 2019

@author: purvi
"""

def longestPalindrome(s: str) -> int:
    dic = {}
    count = 0
    for i in s:
        if i in dic:
            dic[i]+=1
        else:
            dic[i] = 1
    print(dic)
    for i in sorted(dic, key=dic.get, reverse=True):
        if dic[i] %2 ==0:
            count+=dic[i]
        if dic[i] %2 !=0:
            count+=dic[i]-1
        if dic[i] ==1:
            count+=1
            return count

        
    
    
    
    
    
    
    
if __name__ == "__main__":
    print(longestPalindrome("abccccdd"))