#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 18:40:26 2019

@author: purvi
"""

def reverseString(s) -> None:
    #s[:] = [s[len(s)+i-1] for i in range(-len(s),0) ]
    s[:] = [s[len(s)-1 -i] for i in range(0,len(s)) ]
    
    
if __name__ == "__main__":
    s =  ["h","e","l","l","o"]
    print(s)
    reverseString(s)
    print(s)