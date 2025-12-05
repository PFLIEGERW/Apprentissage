#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def highest_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

Firstnum = int(input("Enter first number: "))
Secondnum = int(input("Enter second number: "))
Thirdnum = int(input("Enter third number: "))

Highnum = highest_number(Firstnum, Secondnum, Thirdnum)

print("The highest number is  " +str(Highnum))
