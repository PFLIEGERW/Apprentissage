#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def options (num):
    if num==1:
        return "Computer Science"
    elif num==2:
        return "Music"
    elif num==3:
        return "Dance"
    elif num==4:
        return "PE"
    else:
        return "Please use a number between 1 and 4"

print("Please choose an activity : 1 - Computer Science, 2 - Music, 3 - Dance, 4 - PE : ")
choice = input()
print(options(choice))
