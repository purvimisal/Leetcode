#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 13:28:44 2019

@author: purvi
"""

def backspaceCompare(S: str, T: str) -> bool:
    xS = ''
    xT = ''
    for i in range(0,len(S)):
        if (S[i+1] != "#" and S[i] == "#"):
            xS += S[i]
        
    for i in range(0,len(T)):
        if T[i+1] != "#" and T[i] == "#":
            xT += T[i]
            
    print(xS,xT)
    

backspaceCompare("ab#c","ad#c")