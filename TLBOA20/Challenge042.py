#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def hexatodena(number):
    
    final_number = int(number,16)
    return final_number

def main():
    print("Please enter a number in hexadecimal to be converted in decimal : ")
    number = input()
    X = hexatodena(number)
    print(X)

if __name__ == '__main__':
    main()