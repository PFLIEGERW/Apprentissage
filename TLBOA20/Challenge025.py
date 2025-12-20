#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random

def penalty(tir):
    goal=random.randint(0,2)

    if goal == tir:
        print("Tir arrêté.")
        return 0
    else:
        print("BUT !")
        return 1
def main():
    print("Bienvenue à ce tir au but.")
    tirs_restant = 5
    but = 0
    while tirs_restant != 0:
        print("Merci de bien vouloir entrer la direction dans laquelle vous \
souhaitez tirer : 0. Gauche, 1. Centre, 2. Droite.")
        tir = int(input())
        tentative = penalty(tir)
        tirs_restant -= 1
        if tentative == 1:
            but += 1
        else:
            continue
    print(f"Tirs au but : {but}")
    tirs_arrêtés = 5-but
    print(f"Tirs arrêtés : {tirs_arrêtés}")
    if but < tirs_arrêtés:
        print("Le Goal a gagné !")
    else:
        print("Le Tireur a gagné !")

if __name__ == '__main__':
    main()