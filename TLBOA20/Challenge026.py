#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main():
    y = 0
    for x in range(1,11):
        print("x :",x)
        if x % 2 == 0:
            y = x + 2
            print("y :",y)
        else:
            print("y :",y)
    
if __name__ == '__main__':
    main()