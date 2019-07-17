#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 21:04:45 2019

@author: awesome_k
"""

def collatz(num):
    while num != 1:
        if (num % 2 == 0):
            num = num // 2
            print (num)
        
        elif (num % 2 == 1):
            num = ((num * 3) +1)
            print (num)
            
try:
    print ('Enter an integer value ')
    collatz(int(input()))
except:
    print ('Re-enter an integer value only!')