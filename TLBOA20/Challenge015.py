#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def is_multiple(x_in, y_in):
    if x_in % y_in == 0:
        return True

    else:
        return False

def main():
    print("A program to check if x is a multiple of y")
    try:
        x = int(input("Enter a number to check if it is a multiple : "))
        y = int(input("Enter a number to divide by : "))
        status = is_multiple(x, y)
        if status == True:
            print(x, "is a multiple of ", y)
        else:
            print(x, "is not a multiple of ", y)
    except:
        print("Please only enter integral numbers")
    
if __name__ == '__main__':
    main()