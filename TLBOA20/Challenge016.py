#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def div(num1_in, num2_in):
#    out = (num1_in+num2_in) // 10
    out = (num1_in // num2_in)
    return out

def main():
    try:
        num1 = int(input("Enter your first number : "))
        num2 = int(input("Enter your second number : "))
        floor = div(num1,num2)
        print(floor)
    except:
        print("Please only use integral numbers.")
    
if __name__ == '__main__':
    main()