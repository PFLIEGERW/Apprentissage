#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def acronym(words):
    acro = ""
    #Convert words into a list of indivudal words
    words_list = words.split()
    #For each word in the words_list
    for word in words_list:
        acro = acro + list(word)[0]
    return acro

def main():

    words = input("Enter words separated by a space to be turned into an \
acronym : ")
    print(acronym(words))

if __name__ == '__main__':
    main()