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
                rollsdict = rollsdicttemp    
                rollstemp["rollsdict{}".format(x)] = rollsdict
            rolls = rollstemp

        for key, obj in rolls.items():
            print(key)
            
            for key in obj:
                print(key + " : ", obj[key])

    except:
        print("Merci de n'utiliser qu'un nombre entier.")
        return main()
if __name__ == '__main__':
    main()