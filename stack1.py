#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 11:16:07 2019

@author: purvi

Stack data structure 
D
C
B
A

"""

class Stack():
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def get_stack(self):
        return self.items
    
    def is_empty(self):
        return self.items == []
    
    def peak(self):
        if not self.is_empty():
            return self.items[-1]
        


s = Stack()
print(s.is_empty())
s.push("A")
s.push("B")
print(s.get_stack())
s.push("C")
print(s.get_stack())
print(s.pop())
print(s.is_empty())
print(s.get_stack())
print(s.peak())

    