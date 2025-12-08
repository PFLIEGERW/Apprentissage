#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def mystery_number(num):
    if num == 3:
        print(1)
    elif num < 5:
        print(8)
    else:
        print(num)

num_in = int(input("Enter a number: "))
mystery_number(num_in)