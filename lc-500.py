#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:21:59 2019

@author: purvi
"""

def findWords(words):
    res=[]
    dic1={'q','w','e','r','t','y','u','i','o','p','Q','W','E','R','T','Y','U','I','O','P'}
    dic2={'a','s','d','f','g','h','j','k','l','A','S','D','F','G','H','J','K','L'}
    dic3={'z','x','c','v','b','n','m','Z','X','C','V','B','N','M'}
                
    for i in words:
        if set(i) - dic1 == set() or set(i) - dic2 == set()  or set(i) - dic3 == set():
            res.append(i)
    print(res)

    
    
    
    
if __name__ == "__main__":
    findWords(["Hello", "Alaska", "Dad", "Peace"])