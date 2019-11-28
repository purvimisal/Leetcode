#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 10:07:41 2019

@author: purvi
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        lsort = head = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                lsort.next = l1
                l1 = l1.next
            
            elif l1.val >= l2.val:
                lsort.next = l2
                l2 = l2.next
                
            lsort = lsort.next
        return head.next
            