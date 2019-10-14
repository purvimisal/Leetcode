#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 18:15:30 2019

@author: purvi
"""

def isAnagram(s: str, t: str) -> bool:
    if(len(s)!=len(t)): return False
    
    else:
        t = [i for i in t]
        for i in s:
            if(i in t):
                t.remove(i)
        if(len(t) == 0): return True
        else: return False
    
    
if __name__ == "__main__":
    
    s = "cat"
    t = "tar"
    
    print(isAnagram(s,t))