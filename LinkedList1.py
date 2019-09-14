#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 08:06:22 2019

@author: purvi
"""

#Simple linked list operations

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def printList(self):
            temp = self.head
            while(temp):
                print(temp.data)
                temp = temp.next
            print("-------")
                
    
    def push(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
    
    def insertAfter(self, prevnode, data):
        if (prevnode == None):
            print("Node should exist in linked list")
            return
        newnode = Node(data)
        newnode.next = prevnode.next
        prevnode.next = newnode
        
        
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = new_node
        
        

if __name__ == "__main__":
    
    ll = LinkedList()
    ll.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    ll.head.next = second
    second.next = third
    
    ll.printList()
    ll.push(6)
    ll.printList()
    ll.insertAfter(ll.head, 44)
    ll.printList()
    ll.append(33)
    ll.printList()