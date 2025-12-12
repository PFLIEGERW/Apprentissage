#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def is_odd(number_in):
    if int(number_in) %2 == 0:
        return False
    else:
        return True

def main():
    again = True
    while again:
        number = input("Enter an integral number or STOP to stop the program : ")
        try:
            if number != "STOP" :
                odd = is_odd(number)
                if odd == True:
                    print("This number is odd.")
                else:
                    print("This number is even.")
            else:
                again = False
        except:
            print("Please only enter an integral number")
            again = True

if __name__ == '__main__':
    main()