#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def subject_shortener(subject):
    shorty=subject[0:3]
    return shorty

def main():
    print("Merci de bien vouloir entrer une matière à raccourcir : ")
    subject=input()
    print(subject_shortener(subject))

if __name__ == '__main__':
    main()