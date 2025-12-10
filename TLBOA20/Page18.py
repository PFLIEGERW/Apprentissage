#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def user_name(forename, last_name, year):
    
    username_out = year[2:4] + forename[0] + last_name
    
    return username_out

def main():
    first_name = input("Enter your first name: ")
    surname = input("Enter your surname: ")
    year = input("Enter the year you joined the school: ")
    
gen_user_name = user_name(first_name, surname, year)
print("Your user name is " + gen_user_name)

if __name__ == '__main__':
    main()
    
#La main devrait être utilisée pour appeler d'autres fonctions et gérer les entrées-sorties du programme.
#Cette convention permet entre autre chose, de générer un code plus propre, en centralisant les actions du programme.
#Il est également fréquent de voir la main être le point de départ du programme pour un OS.