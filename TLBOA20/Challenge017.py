#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def acronym(word):
    word = word[0]
    return word

def main():
    
    sentinel = "XXX" #The sentinel value
    word = ""
    acro = ""

    while word != sentinel:
        word = input("Enter a word or 'XXX' to finish : ")
        if word != sentinel:
            acro = acro + acronym(word)

    print(acro)

if __name__ == '__main__':
    main()