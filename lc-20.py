#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 11:53:18 2019

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
    
def is_match(p1,p2):
        if p1 == "(" and p2 == ")":
            return True
        elif p1 == "{" and p2 == "}":
            return True
        elif p1 == "[" and p2 == "]":
            return True
        else:
            return False

class Solution:
    
    
    def isValid(self, paren_string: str) -> bool:
        s = Stack()
        is_balanced = True
        index = 0

        while index <len(paren_string) and is_balanced:
            paren = paren_string[index]
            if paren in "[{(":
                s.push(paren)
            else:
                if s.is_empty():
                    is_balanced = False
                else:
                    top = s.pop()
                    if not is_match(top, paren):
                        is_balanced = False
            index += 1
        if s.is_empty() and is_balanced:
            return True
        else: return False