#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 09:52:00 2019

@author: purvi
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        
        a , b = headA, headB
        
        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA
            
        
        if a is None: return b
        else: return a