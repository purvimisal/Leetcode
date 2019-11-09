#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 08:49:53 2019

@author: purvi
"""

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if not s: return s
        i, j = 0, k-1
        chars = [c for c in s]
        while i < len(s):
            x, y = i, min(j, len(s)-1)
            while x < y:
                chars[x], chars[y] = chars[y], chars[x]
                x, y = x + 1, y - 1
            i, j = i + 2*k, j + 2*k
        return ''.join(chars)