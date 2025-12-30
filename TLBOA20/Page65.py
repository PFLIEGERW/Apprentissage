#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def login(username,password):
    newfile = open("Page65_users.txt","r")
    users_2D = eval(newfile.read())
    newfile.close()
    found = False
    for count in range(len(users_2D)):
        if username == users_2D[count][0]:
            found = True
            if password == users_2D[count][1]:
                print("logged in")
            else:
                print("incorrect password")
                login()
    if found==False:
        print("Invalid username")
        login()

def main():
    username = input("What is your username ? ")
    password = input("What is your password ? ")
    login(username,password)

if __name__ == '__main__':
    main()