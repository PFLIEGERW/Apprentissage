#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main():
    discounts = [["summer10",0.1],["welcome",0.15],["refer20",0.2],\
["loyalty25",0.25]]
    discount = 0
    
    total = float(input("What is the order total: £"))
    
    discount_in = input("Do you have a discount code?").lower()
    
    if discount_in == "yes":
        discountcode = input("Enter a discount code").lower()
        valid = False
        for count in range(len(discounts)):
            if discountcode == discounts[count][0]:
                discount = discounts[count][1]
                valid = True
        if valid == False:
            print("Invalid discount code")

    total = total - (total*discount)
    print("Your total is £%.2f" %total)

if __name__ == '__main__':
    main()