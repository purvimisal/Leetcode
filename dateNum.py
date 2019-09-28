#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 16:02:19 2019

@author: purvi
"""

def calcNumber(s):
    x = s.replace('/','')
    y =0
    while(len(s)!=1):
        
        for i in x: 
            print(i)
            y+=int(i)
        x = str(y)
        print(y)
    print(y)
    
    
    
if __name__ == "__main__":
    a = "20/11/1996"
    calcNumber(a)