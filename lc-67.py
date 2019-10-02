#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:13:34 2019

@author: purvi
"""

def addBinary(a: str, b: str) -> str:
    a = int(a,2)
    b = int(b,2)
    sum = bin(a+b)
    s = sum[2:]
    return str(s)
    
    
    
if __name__ == "__main__":
    a = "101011010011"
    b = "1011110011"
    
    addBinary(a,b)