#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def add(num1, num2):
    sum=num1+num2
    return sum

def main():
    num1_in = int(input("Enter a number : "))
    num2_in = int(input("Enter another number : "))
    
    total = add(num1_in,num2_in)
    
    print("The sum of the two numbers is : " + str(total))

if __name__ == '__main__':
    main()