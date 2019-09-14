#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 08:37:58 2019

@author: purvi
"""

#Generate linked list from array 

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
    
    def addArray(self, arr):
        arr.reverse()
        for i in arr:
            self.push(i)
            
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":
    
    ll = LinkedList()
    arr = [1,2,3,4,5]
    ll.addArray(arr)
    ll.printList()
    
    
    