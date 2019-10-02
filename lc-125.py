#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:47:28 2019

@author: purvi
"""

def isPalindrome(s: str) -> bool:
        x = ''
        for i in s: 
            if(i.isalnum()):
                x += i
        s = x.lower()
        print(s)
        s = s.replace(' ', '')
        print(s)
        if( s == "" or s == " " or len(s) == 1): return True
        if (len(s) == 2 and s[0] == s[1]): return True
        if(len(s)%2 == 0):
            s1 = s[:int(len(s)/2)]
            s2 = s[int(len(s)/2):]
            s1 = list(s1)
            s2 = list(s2)
            s2.reverse()
            if(s1 == s2): return True 
            else: return False
        else: 
            s1 = s[:int(len(s)/2)]
            s2 = s[int(len(s)/2)+1:]
            s2 = list(s2)
            s2.reverse()
            a = ''
            for i in s2:
                a += i
            if(a == s1): return True
            else: return False
        return False
            
            

        
        
if __name__ == "__main__":
     s =  "race a car"
     print(isPalindrome(s))
        