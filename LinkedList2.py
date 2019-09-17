#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 08:37:58 2019

@author: purvi
"""

#Generate linked list from array 
#delete value from a linked list 
#delete node at a position


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
    
    def deleteValueNode(self, value):
        temp = self.head
        if(temp is not None):
            if(temp.data == value):
                self.head = temp.next
                temp = None
                return
        while(temp is not None):
            if (temp.data == value):
                break
            prev = temp
            temp = temp.next
            
        if(temp == None):
            return 
        prev.next = temp.next
        temp = None
        
    def deleteAtPos(self, pos):
        temp = self.head
        counter = 0
        if(temp is not None):
            if(counter == pos):
                self.head = temp.next
                temp = None
                return
        while(temp is not None):
            if(counter == pos):
                break
            prev = temp
            temp = temp.next
            counter += 1
        if(temp == None):
            return
        prev.next = temp.next
        temp = None
                
        
if __name__ == "__main__":
    
    ll = LinkedList()
    arr = [1,2,3,4,5]
    ll.addArray(arr)
    ll.printList()
    ll.deleteValueNode(4)
    ll.printList()
    ll.deleteAtPos(2)
    ll.printList()
    
    