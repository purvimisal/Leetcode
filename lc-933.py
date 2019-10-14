#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 22:19:56 2019

@author: purvi
"""

from collections import deque

class RecentCounter:

    def __init__(self):
        self.calls = []
        

    def ping(self, t: int) -> int:
        self.calls.insert(0,t)
        
        while t - 3000 > self.calls[len(self.calls)-1]:
            self.calls.pop()
        return len(self.calls)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)