#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def user_name(forename, last_name, year):
    #on commence par l'indice zéro, INCLUS, puis on termine par le 4, EXCLUS.
    username_out = year[2:4] + forename[0] + last_name
    
    print("Your user name is " + username_out)
    
first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
joined = input("Enter the year you joined the school: ")

user_name(first_name,surname,joined)