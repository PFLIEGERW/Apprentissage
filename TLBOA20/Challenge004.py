#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def options (number):
    if number != '1' and number != '2' and number != '3' and number != '4':
        return "Please use a number between 1 and 4"
    else:
        number=int(number)
        if number==1:
            return "Computer Science"
        elif number==2:
            return "Music"
        elif number==3:
            return "Dance"
        elif number==4:
            return "PE"

print("Please choose a GCSE option : 1 - Computer Science, 2 - Music, 3 - Dance, 4 - PE. ")
choice = input()
print(options(choice))
