#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 12:46:35 2019

@author: purvi
"""

from collections import deque


def strStr(haystack: str, needle: str) -> int:
    h = len(haystack)
    n = len(needle)
    
    hq = deque()
    nq = deque()
    
    for i in range(n):
        hq.append(haystack[i])
        nq.append(needle[i])
        
    if hq == nq: return 0 
        
    for i in range(n,h):
        hq.popleft()
        hq.append(haystack[i])
        if hq == nq:
            print(hq,nq)
            return i - n +1
    return -1
    



if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"
    
    print(strStr(haystack, needle))
