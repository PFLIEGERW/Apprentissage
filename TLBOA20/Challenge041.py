#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def test_email(email):
    Found = False
    file = open ("Challenge041_users.txt","r")
    users = eval(file.read())
    file.close()
    
    for count in range(len(users)):
        if email == users[count][0]:
            Found = True
            return Found

    return Found

def main():

    email = input("Enter a username : ")
    print(test_email(email))
    
    
if __name__ == '__main__':
    main()