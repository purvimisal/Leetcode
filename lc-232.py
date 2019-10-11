#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 18:07:18 2019

@author: purvi
"""

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.items.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        temp = []
        while self.items: temp.append(self.items.pop())
        r = temp.pop()
        while temp: self.items.append(temp.pop())
        return r
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        temp = []
        while self.items: temp.append(self.items.pop())
        r = temp[-1]
        while temp: self.items.append(temp.pop())
        return r
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.items == []        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()