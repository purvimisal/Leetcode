#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:26:25 2019

@author: purvi
"""

#def plusOne(digits):
#    n = len(digits)
#    arr = digits[:n-1]
#    arr.append(digits[n-1] +1)
#    return arr

def plusOne(digits):
    s = ''
    for n in digits:
        s += str(n)
    res = int(s) +1
    digits = [ int(i) for i in str(res)]
    return digits
    

if __name__ == "__main__":
    dig = [4,3,2,1]
    print(plusOne(dig))