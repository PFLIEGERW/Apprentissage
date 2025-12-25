#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#Perso = PV, Armure, Arme, Potion de Soin, Terrain, Visibilité
#Adversaire = PV, Armure, Armes, Potion de Soin, Terrain, Visibilité
#Terrain = Nom, Esquive, Visibilité
#Armures = Nom, Esquive, Armures
#Armes = Nom, Dégâts, Cartouches

Dict_Terrain = {}
Dict_Terrain["Gros_rocher"] = [100,0]
Dict_Terrain["Plaine"] = [0,100]
Dict_Terrain["Buisson"] = [25,25]
Dict_Terrain["Petit_rocher"] = [50,50]
# Dict_Armures = {"Lourde"[-25,10],"Moyenne"[-10,6],"Légère"[0,2],"Aucune"[5,0]}
# Dict_Armes = {"L1A1"[15,20],"M16"[10,30],"M9"[7,12],"Pied_de_biche"[8,-1]}

class Personnage:
    PV = 100
    Armure = 0
    Potion = 1
    Arme = 0
    Esquive = 0
    
    # Joueur = Personnage()

def main():
    print("Bienvenue dans ce simulateur de duel.")
    # print("Veuillez choisir votre arme : ")
    # ChoixArme=int(input())
    print(Dict_Terrain)

if __name__ == '__main__':
    main()