#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 13:39:47 2019

@author: purvi
"""

def removeOuterParentheses(S: str) -> str:
    count = 0
    i = 0
    j =0
    res = ""
    while(j<len(S)):
        
        if(S[j] == "("):
            count += 1
        elif(S[j] == ")"):
            count -= 1
        print(count)
        if(count == 0):
            res += S[i+1:j]
            print(res)
            i = j +1
        j = j + 1
    return res
        
    
    
    
    
if __name__ == "__main__":
    print("hi")
    print("ans:", removeOuterParentheses("(()())(())"))
    
    
    
    
    
