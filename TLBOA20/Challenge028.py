#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def average(numbers_list):
    avg = sum(numbers_list) / len(numbers_list)
    return avg
    

def main():
    print("Please enter the length of the list you want the average of : ")
    list_length = int(input())
    list_numbers = []

    for i in range(list_length):
        print("Please enter a number : ")
        number = float(input())
        list_numbers.append(number)
    list_avg = average(list_numbers)
    print("Your average is : ",list_avg)
    
if __name__ == '__main__':
    main()
    
