#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def subtract(num1, num2):
    if num1 > num2:
        out = num1 - num2
    else:
        out = num2 - num1
        
    return out

num1_in = int(input("Enter a number"))
num2_in = int(input("Enter a number"))

difference = subtract(num1_in, num2_in)

print("The difference is", difference)