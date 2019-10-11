#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 11:53:35 2019

@author: purvi
"""

class Stack():
        def __init__(self):
            self.items = []

        def push(self, item):
            self.items.append(item)

        def pop(self):
            return self.items.pop()

        def is_empty(self):
            return self.items == []

        def peak(self):
            return self.items[-1]
    

def div_by_2(num):
    s = Stack()
    
    while num >0:
        remainder = num % 2
        s.push(remainder)
        num = num // 2
        
    binary = ""
    while not s.is_empty():
        binary += str(s.pop())
        
    return binary

print(div_by_2(242))