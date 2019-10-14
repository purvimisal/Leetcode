#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 18:26:13 2019

@author: purvi
"""

def getHint(secret: str, guess: str) -> str:
    a = 0
    b = 0
        
    dic = {}
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            a += 1
        else:
            if secret[i] not in dic:
                dic[secret[i]] = 1
            else:
                dic[secret[i]] += 1
                
    for i in range(len(secret)):
        if secret[i] != guess[i]:
            if guess[i] in dic and dic[guess[i]] != 0:
                b += 1
                dic[guess[i]] -= 1
                
    return str(a) + 'A' + str(b) + 'B'
        
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    secret = "1123"
    guess = "0111"
    print(getHint(secret, guess))
    
    
