#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 10:19:42 2019

@author: purvi
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        l = head
        while l:
            while l.next and l.val == l.next.val:
                l.next = l.next.next
            l = l.next
        return head