#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 16:29:36 2019

@author: purvi
"""


class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode: