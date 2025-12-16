#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
def diceroll(FaceNumber):
        roll = random.randint(1, FaceNumber)
        return roll

def main():
    print("Merci de bien vouloir indiquer le nombre de faces des dés à \
lancer :")
#    try:
    FaceNumber = int(input())
    rolls = {}
    rollscopy = {}
    for x in range(0,3):
        for i in range(0,2):
            rollscopy["roll{}".format(i)] = diceroll(FaceNumber)
        rolls=rollscopy
        print(rolls["roll0"]," + ",rolls["roll1"]," = ",\
rolls["roll0"]+rolls["roll1"])

#    except:
#    print("Merci de n'utiliser qu'un nombre entier.")
#    return main()
if __name__ == '__main__':
    main()