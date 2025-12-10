#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def initials_only(first, middle, last):
    initials = first[0]+middle[0]+last[0]
    return initials

def main():
    print("Merci de bien vouloir entrer votre prénom: ")
    first=input()
    print("Merci de bien vouloir entrer votre surnom ou deuxième prénom : ")
    middle=input()
    print("Merci de bien vouloir entrer votre nom de famille : ")
    last=input()
    print(initials_only(first, middle, last))

if __name__ == '__main__':
    main()