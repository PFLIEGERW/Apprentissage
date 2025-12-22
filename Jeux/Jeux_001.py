#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#Perso = PV, Armure, Armes, Potion de Soin, Terrain, Visibilité
#Adversaire = PV, Armure, Armes, Potion de Soin, Terrain, Visibilité
#Terrain = Nom, Esquive, Visibilité
#Armures = Nom, Esquive, Armures
#Armes = Nom, Dégâts, Cartouches

Dict_Perso = {PV[100],Armure[""],Armes[""],Potion[1]}
Dict_Terrain = {Gros rocher[100,0],Plaine[0,100],Buisson[25,25],\
Petit rocher[50,50]]}
Dict_Armures = {Lourde[-25,10],Moyenne[-10,6],Légère[0,2],Aucune[5%,0]}
Dict_Armes = {L1A1[15,20],M16[10,30],M9[7,12],Pied de biche[8,-1]}


def main():
    print("Bienvenue dans ce simulateur de duel.")
    print("Veuillez choisir votre arme : ")
    ChoixArme=int(input())

if __name__ == '__main__':
    main()