#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 12:50:59 2019

@author: purvi
"""

def generate(numRows: int):
    tri = []
    x = []
    for i in range(1,numRows+1):
        for j in range(0,i):
            x.append(j)
            print(x)
        print("tri: ",tri, "n:", j)
        tri.append(x)
    return tri

if __name__ == "__main__":
    print(generate(4))
    