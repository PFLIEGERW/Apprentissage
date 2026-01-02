#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def binary_to_denary(binary):
    bit1 = int(binary[3])*1
    bit2 = int(binary[2])*2
    bit3 = int(binary[1])*4
    bit4 = int(binary[0])*8
    
    denary_out = bit1 + bit2 + bit3 + bit4
    return denary_out
    
def main():
    binary_in = input("Enter the binary string : ")
    denary = binary_to_denary(binary_in)
    print("The binary value", binary_in, "in denary \
is", denary)

if __name__ == '__main__':
    main()