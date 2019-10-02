#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 22:07:12 2019

@author: purvi
"""

def compress(chars) -> int:
        dic = {}
        for i in chars:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        c = len(set(chars))
        j = 0
        while(j<c):
            char[i],char[i+1] = 