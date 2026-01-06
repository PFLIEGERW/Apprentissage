#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import random

#Perso = PV, Armure, Arme, Potion de Soin, Terrain, Visibilité
#Adversaire = PV, Armure, Armes, Potion de Soin, Terrain, Visibilité
#Terrain = Nom, Esquive, Visibilité
#Armures = Nom, Esquive, Armure
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

def combat(Attaquant,Defenseur):
    if Attaquant.Arme[1] <= Defenseur.Armure[2]:
        return 0
    elif Attaquant.Arme[1] > Defenseur.Armure[2]:
        return Attaquant.Arme[1]-Defenseur.Armure[2]

class Personnage:
    def __init__(self,Nom_in):
        self.Nom = Nom_in
        self.PV = 100
        self.Armure = []
        self.Potion = 1
        self.Arme = []
        self.Esquive = 0

def main():
    print("Bienvenue dans ce simulateur de duel.")
    
    Joueur1 = Personnage("Joueur1")
    
    print("Veuillez choisir votre arme parmis la liste suivante :",\
Cle_Dict_Armes)
    TempJoueur1Arme = input()
    Joueur1.Arme = Dict_Armes[TempJoueur1Arme].copy()
    Joueur1.Arme.insert(0,TempJoueur1Arme)
    
    print("Veuillez choisir votre armure parmis la liste suivante : ",\
Cle_Dict_Armures)
    TempJoueur1Armure = input()
    Joueur1.Armure = Dict_Armures[TempJoueur1Armure].copy()
    Joueur1.Armure.insert(0,TempJoueur1Armure)
    
    print("Voici votre arme :",Joueur1.Arme[0],"Dégâts :",\
Joueur1.Arme[1],"Nombre de cartouches :",\
Joueur1.Arme[2])

    print("Voici votre armure :",Joueur1.Armure[0],"Modificateur d'esquive :",\
Joueur1.Armure[1],"Protection :",Joueur1.Armure[2])

    print("Votre adversaire se prépare...")
    Adversaire = Personnage("Adversaire")
    TempAdversaireArme = random.choice(Cle_Dict_Armes)
    TempAdversaireArmure = random.choice(Cle_Dict_Armures)
    
    Adversaire.Arme = Dict_Armes[TempAdversaireArme].copy()
    Adversaire.Arme.insert(0,TempAdversaireArme)
    
    Adversaire.Armure = Dict_Armures[TempAdversaireArmure].copy()
    Adversaire.Armure.insert(0,TempAdversaireArmure)

    print("Votre adversaire a choisi cette arme :",Adversaire.Arme,\
"et cette armure :",Adversaire.Armure)

    while Joueur1.PV > 0 and Adversaire.PV > 0:
        print("Test combat : ")
        Blessure = combat(Joueur1,Adversaire)
        print(Joueur1.Nom,"a infligé",Blessure,"à",Adversaire.Nom)
        Adversaire.PV -= Blessure
        print("Voici l'état de votre adversaire :",Adversaire.PV,"PV")
        Blessure = combat(Adversaire,Joueur1)
        print(Adversaire.Nom,"a infligé",Blessure,"à",Joueur1.Nom)
        Joueur1.PV -= Blessure
        print("Voici votre état :",Joueur1.PV,"PV")
    
    if Joueur1.PV == 0:
        print("Vous êtes mort.e !")
    else:
        print("Votre adversaire est mort !")
        
if __name__ == '__main__':
    main()