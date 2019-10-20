#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:50:36 2019

@author: purvi
"""

def findRestaurant(list1, list2):
        l =[]
        for i in list1:
            if i in list2:
                l.append(i)
        dic = {i: list1.index(i) + list2.index(i) for i in l}
        min_val = min(dic.values())
        print(min_val)
        
        res = []
        for i in dict(dic):
            if dic[i] == min_val:
                res.append(i)
                
        return res
    
    
if __name__ == "__main__":
    a = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    b = ["KFC", "Shogun", "Burger King"]
    findRestaurant(a,b)
    