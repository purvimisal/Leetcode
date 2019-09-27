#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:06:31 2019

@author: purvi
"""

def romanToInt(s: str) -> int:
    romans = {'M':1000, 'D':500, 'C': 100, 'L':50,'X':10,'V':5,'I':1}
    r = 0
    l = len(s)
    for i in range(0,l-1):
        if romans[s[i]]< romans[s[i+1]]:
            r -= romans[s[i]]
        else:
            r += romans[s[i]]
    return r + romans[s[-1]]
    


if __name__ == "__main__":
    
    
    
    i = "CV"
    print(romanToInt(i))
    