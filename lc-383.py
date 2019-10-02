#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 19:15:37 2019

@author: purvi
"""

def canConstruct(ransomNote: str, magazine: str) -> bool:
    i = 0
    s = []
    k = len(magazine)
    m = list(magazine)
    print(magazine)
    while(i<len(ransomNote)):
        if ransomNote[i] in list(magazine):
                m.pop(magazine.index(ransomNote[i]))
        print(s)
        i += 1
    print(m)
    if(k - len(m) == len(ransomNote)):
        return True
    else:
        return False
    
    

    
    
print(canConstruct("aa", "aab"))    