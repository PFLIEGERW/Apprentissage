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
    for x in (0,3):
        for i in (1,3):
            rolls["roll{0}".format(i)] = diceroll(FaceNumber)
        print(rolls["1"], "+", rolls["2"], "=", rolls["1"]+rolls["2"])

#    except:
    print("Merci de n'utiliser qu'un nombre entier.")
    return main()
if __name__ == '__main__':
    main()