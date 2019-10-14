#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 17:28:24 2019

@author: purvi
"""

def wordPattern(pattern: str, s: str) -> bool:
    dic ={}
    s = s.split(" ")
    pattern = [i for i in pattern]
    if len(pattern)!=len(s):return False
    for i in range(0,len(pattern)):
        if pattern[i] not in dic and s[i] not in dic.values():
            dic[pattern[i]] = s[i]   
    x =[]
    for i in pattern:
        if i in dic:
            x.append(dic[i])
            
    if(x == s): return True
    else: return False 
    #x = [dic[pattern[i]] for i in range(0,len(pattern))]
    #if(s == x):
    #    return True
    #else: return False
    
    
    

    
    
    
if __name__ == "__main__":
    pattern = "abba"
    s = "dog dog dog dog"
    print(wordPattern(pattern,s))