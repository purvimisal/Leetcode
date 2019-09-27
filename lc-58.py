#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 13:03:07 2019

@author: purvi
"""

def lengthOfLastWord(s: str) -> int:
     t = s.strip(" ").split(" ")
    
     
     return len(t[-1])
     

     
     
     
     
     
     
if __name__ == "__main__":
    n = "hello world"
    
    print(lengthOfLastWord(n))