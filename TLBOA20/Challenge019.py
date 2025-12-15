#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random

def diceroll(FaceNumber):
    roll = random.randint(1, FaceNumber)
    roll2 = random.randint(1, FaceNumber)
    if roll == roll2 :
        return 1
    
    else:
        return 2

def main(FaceNumber):
    
    if FaceNumber == "":
        print("Merci de bien vouloir entrer le nombre de face des dés à lancer : ")
        try :
            FaceNumber = int(input())
            
            comparison = diceroll(FaceNumber)
        except:
            print("Merci de n'utiliser que des nombres entiers")
            return main(FaceNumber="")

        if comparison == 1:
            print("Game Loading...")
        else:
            input("Please press enter to reroll.")
            return main(FaceNumber)
    
    else:
        comparison = diceroll(FaceNumber)

        if comparison == 1:
            print("Game Loading...")
        else:
            input("Please press enter to reroll.")
            return main(FaceNumber)

if __name__ == '__main__':
    main(FaceNumber="")