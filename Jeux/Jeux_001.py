#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#Perso = PV, Armure, Arme, Potion de Soin, Terrain, Visibilité
#Adversaire = PV, Armure, Armes, Potion de Soin, Terrain, Visibilité
#Terrain = Nom, Esquive, Visibilité
#Armures = Nom, Esquive, Armures
#Armes = Nom, Dégâts, Cartouches

Dict_Terrain = {}
Dict_Terrain["Gros rocher"] = [100,0]
Dict_Terrain["Plaine"] = [0,100]
Dict_Terrain["Buisson"] = [25,25]
Dict_Terrain["Petit rocher"] = [50,50]
Dict_Armures = {}
Dict_Armures["Lourde"] = [-25,10]
Dict_Armures["Moyenne"] = [-10,6]
Dict_Armures["Légère"] = [0,2]
Dict_Armures["Aucune"] = [5,0]
Dict_Armes = {}
Dict_Armes["L1A1"] = [15,20]
Dict_Armes["M16"] = [10,30]
Dict_Armes["M9"] = [7,12]
Dict_Armes["Pied de biche"] = [8,-1]

class Personnage:
    PV = 100
    Armure = 0
    Potion = 1
    Arme = 0
    Esquive = 0
    
Joueur1 = Personnage()

def main():
    print("Bienvenue dans ce simulateur de duel.")
    print("Veuillez choisir votre arme : ")
    ChoixArme=input()
    Joueur1.Arme = ChoixArme
    print("Veuillez choisir votre armure : ")
    ChoixArmure=input()
    Joueur1.Armure = ChoixArmure
    print("Voici votre arme :",Joueur1.Arme,"Dégâts :",\
Dict_Armes[Joueur1.Arme][0],"Nombre de cartouches :",\
Dict_Armes[Joueur1.Arme][1])
    print("Voici votre armure :",Joueur1.Armure,"Modificateur d'esquive :",\
Dict_Armures[Joueur1.Armure][0],"Protection :",Dict_Armures[Joueur1.Armure][1])

if __name__ == '__main__':
    main()