#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 10:18:25 2019

@author: purvi
"""

class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, value):
        if value <= self.data :
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)
    
    def contains(self, value):
        if value == self.data:
            return True
        elif value <= self.data:
            if self.left == None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right == None:
                return False
            else:
                return self.right.contains(value)
            
    
    def printInOrder(self):
        if self.left is not None:
            self.left.printInOrder()
        print(self.data)
        if self.right is not None:
            self.right.printInOrder()
            
    
    
            
            
            
if __name__ == "__main__":
    
    INT_MIN = float('-inf')
    INT_MAX = float('inf')
    
    def checkBST(Node):
        return isBST(Node, INT_MIN, INT_MAX)
    
    def isBST(node, imin, imax):
        if node is None: return True
        
        if node.data < imin or node.data > imax:
            return False
        
        return (isBST(node.left,imin,node.data-1) and isBST(node.right, node.data+1, imax))
    
    x = Node(8)
    x.insert(2)
    x.insert(10)
    x.insert(7)
    x.printInOrder()
    print(x.contains(11))
    print(checkBST(x))       
            
                
                
    
    