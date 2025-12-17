#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
def diceroll(FaceNumber):
        roll = random.randint(1, FaceNumber)
        return roll

def main():
    print("Merci de bien vouloir indiquer le nombre de faces des dés à \
lancer :")
    try:
        FaceNumber = int(input())
        
        rollsdicttemp = {}
        rollsdict = {}
        rollstemp = {}
        rolls = {}
        for x in range(0,3):
            for i in range(0,2):
                rollsdicttemp["roll{}".format(i)] = diceroll(FaceNumber)
            rollstemp["rollsdict{}".format(x)] = rollsdicttemp
        rolls = rollstemp

        for y, obj in rolls.items():
            print(y)
            
            for y in obj:
                print(y + " : ", obj[y])

    except:
        print("Merci de n'utiliser qu'un nombre entier.")
        return main()
if __name__ == '__main__':
    main()