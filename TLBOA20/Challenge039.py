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
    
def PSSWGEN(longeur):
    import random

    LETTRES = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P",\
"Q","R","S","T","U","V","W","X","Y","Z"]
    lettres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',\
'q','r','s','t','u','v','w','x','y','z']
    chiffres = ["0","1","2","3","4","5","6","7","8","9"]
    Special = ["@","#","-","","%","*","‰","€","$","£","µ","?","^"]
    PSSW = [""]
    PSSW_final = ""


    while (len(PSSW) < longeur):
        a = random.choice(LETTRES)
        PSSW += a
        c = random.choice(chiffres)
        PSSW += c
        d = random.choice(Special)
        PSSW += d
        b = random.choice(lettres)
        PSSW += b
    else:
        random.shuffle(PSSW)
        for i in PSSW:
            PSSW_final += i
        return PSSW_final
        
def add_account(X,Y):
    file = open("Challenge039_users.txt","r")
    items = eval(file.read())
    file.close()
    items.append(X)
    items.append(Y)
    newfile = open("Challenge039_users.txt","w")
    newfile.write(str(items))
    newfile.close()

def main():
    name = ""
    first_name = ""
    
    name = input("Veuillez entrer votre nom de famille : ")
    first_name = input("Veuillez entrer votre prénom : ")
    
    X = LOGIN_GEN(name,first_name)
    print(X)
    
    longeur = int(input("Veuillez entrer le nombre de caractères \
souhaités pour votre mot de passe : "))
    print(f"Ce générateur de mot de passe créera des chaînes de {longeur} \
caractères.")
    Y = PSSWGEN(longeur)
    add_account(X,Y)
    
    print("Votre compte est maintenant enregistré avec le login :",X)
    
if __name__ == '__main__':
    main()