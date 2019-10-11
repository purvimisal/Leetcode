#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 18:06:18 2019

@author: purvi
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        

    def push(self, x: int) -> None:
        self.items.append(x)

    def pop(self) -> None:
        if self.items: self.items.pop()

    def top(self) -> int:
        if self.items: return self.items[-1]

    def getMin(self) -> int:
        if self.items:
            return min(self.items)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()