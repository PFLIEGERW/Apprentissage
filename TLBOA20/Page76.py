#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main():
    denary = int(input("Enter the denary number between \
0 and 15 : "))
    binary = ["0","0","0","0"]
    if denary > 15:
        print("error")
    if denary >=8 and denary <=15:
        binary[0] = "1"
        denary = denary - 8
    if denary >=4 and denary <=15:
        binary[1] = "1"
        denary = denary - 4
    if denary >=2 and denary <=15:
        binary[2] = "1"
        denary = denary - 2
    if denary >=1 and denary <=15:
        binary[3] = "1"
    for count in range(len(binary)):
        print(binary[count],end="")
if __name__ == '__main__':
    main()