#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import random

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
Cle_Dict_Terrain = list(Dict_Terrain.keys())
Dict_Armures = {}
Dict_Armures["Lourde"] = [-25,10]
Dict_Armures["Moyenne"] = [-10,6]
Dict_Armures["Légère"] = [0,2]
Dict_Armures["Aucune"] = [5,0]
Cle_Dict_Armures = list(Dict_Armures.keys())
Dict_Armes = {}
Dict_Armes["L1A1"] = [15,20]
Dict_Armes["M16"] = [10,30]
Dict_Armes["M9"] = [7,12]
Cle_Dict_Armes = list(Dict_Armes.keys())
# Dict_Armes["Pied de biche"] = [8,-1]
Blessure = 0

def combat(Attaquant,Defenseur):
    if Dict_Armes[Attaquant.Arme][0] <= Dict_Armures[Defenseur.Armure][1]:
        return 0
    elif Dict_Armes[Attaquant.Arme][0] > Dict_Armures[Defenseur.Armure][1]:
        return Dict_Armes[Attaquant.Arme][0]-Dict_Armures[Defenseur.Armure][1]

class Personnage:
    PV = 100
    Armure = []
    Potion = 1
    Arme = []
    Esquive = 0
    Nom = ""
    
Joueur1 = Personnage()
Adversaire = Personnage()

def main():
    print("Bienvenue dans ce simulateur de duel.")
    Joueur1.Nom = "Joueur1"
    Adversaire.Nom = "Adversaire"
    print("Veuillez choisir votre arme parmis la liste suivante :",\
Cle_Dict_Armes)
    Joueur1.Arme = input()
    
    print("Veuillez choisir votre armure parmis la liste suivante : ",\
Cle_Dict_Armures)
    Joueur1.Armure=input()
    
    print("Voici votre arme :",Joueur1.Arme,"Dégâts :",\
Dict_Armes[Joueur1.Arme][0],"Nombre de cartouches :",\
Dict_Armes[Joueur1.Arme][1])

    print("Voici votre armure :",Joueur1.Armure,"Modificateur d'esquive :",\
Dict_Armures[Joueur1.Armure][0],"Protection :",Dict_Armures[Joueur1.Armure][1])

    print("Votre adversaire se prépare...")
    Adversaire.Arme = random.choice(Cle_Dict_Armes)
    Adversaire.Armure = random.choice(Cle_Dict_Armures)
    print("Votre adversaire a choisi cette arme :",Adversaire.Arme,\
"et cette armure :",Adversaire.Armure)
    
    print("Test combat : ")
    Blessure = combat(Joueur1,Adversaire)
    print(Joueur1.Nom,"a infligé",Blessure,"à",Adversaire.Nom)
    Adversaire.PV -= Blessure

if __name__ == '__main__':
    main()