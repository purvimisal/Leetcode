#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 18:07:00 2019

@author: purvi
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
        
        def top(self):
            l = len(self.items)
            return self.items[l-1]



class Solution:
        
    def removeDuplicates(self, S: str) -> str:
        s = Stack()
        for i in S:
            if(s.is_empty() or s.top() != i):
                s.push(i)
            elif(s.top() == i):
                s.pop()
        l = ''
        for i in s.get_stack(): l+= i
        return l