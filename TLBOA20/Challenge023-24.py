#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def passwordstrength(password):
    obvious = ["password", "qwerty", "hello123", "letmein", "123456"]
    minlength = 8
    symbols = ("&", "%", "@", "*", "#", "$", "€", "£")
    strength = 0
    
    for i in obvious:
        if password == i:
            return "WEAK"
    
    if len(password) < 8:
        return "LONG"
    
    for i in password:
        if i in symbols:
            break
    else:
        return "SYMB"

    for k in password:
        if k.islower():
            break
    else:
        return "min"
    
    for l in password:
        if l.isupper():
            break
    else:
        return "MAJ"
        
    for m in password:
        if m.isnumeric():
            break
    else:
        return "NUM"
        
    return strength

def main():
    print("Merci de bien vouloir entrer votre mot de passe : ")
    password=input()
    passstrength = passwordstrength(password)
    
    if passstrength == "WEAK":
        print("Votre mot de passe est faible.")
        print("Il fait partie des pires possibles.")
        print("Merci de bien vouloir en changer.")
    elif passstrength != 0:
        print(passstrength)
        print("Votre mot de passe est faible.")
        print("Merci de bien vouloir en changer.")
    else:
        print("Votre mot de passe est suffisamment fort")

if __name__ == '__main__':
    main()