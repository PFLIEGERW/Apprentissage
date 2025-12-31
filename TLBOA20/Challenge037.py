#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def LOGIN_GEN(name,first_name):
    login = ""
    name = name
    first_name = first_name.lower()
    login = (name.title()+first_name[0].upper())
    
    users_file = open("Challenge037_users.txt","r")
    usernames = eval(users_file.read())
    users_file.close()
    
    for count in range(len(usernames)):
        if usernames[count][0] == login:
            login = login+"#"
    return login

def main():
    name = ""
    first_name = ""
    
    name = input("Veuillez entrer votre nom de famille : ")
    first_name = input("Veuillez entrer votre prénom : ")
    
    X = LOGIN_GEN(name,first_name)
    print(X)
    
if __name__ == '__main__':
    main()