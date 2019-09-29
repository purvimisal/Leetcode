#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 19:35:45 2019

@author: purvi
"""
#Twitter problem: Mask email address and phone number in a human friendly way
def maskEmailAdd(s:str):
    t = s.split('@')
    l = len(t[0])
    #x = '*' * int(l-2)
    t[0] = t[0][0] +'*' * 5 + t[0][l-1]
    print('@'.join(t))

def maskPhoneNo(s:str):
    s = s.replace(' ', '')
    
    print(s)
    if '(' in s:
        s = s.replace('(','').replace(')','')
        t = s[0] + '*' *9 + s[-4:]
        print(t)
    else:
        print(2)
    
    
    
    
if __name__ == "__main__":
    s = "purvimisal@gmail.com"
    t = "mahandas1@gmail.com"
    r = "purvi.misal@sjsu.edu"
    
    maskEmailAdd(t)
    maskEmailAdd(r)
    maskPhoneNo("+111 (333) 444-5678")
    