#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import random

#Perso = PV, Armure, Arme, Potion de Soin, Terrain, Visibilité
#Adversaire = PV, Armure, Armes, Potion de Soin, Terrain, Visibilité
#Terrain = Nom, Esquive, Visibilité
#Armures = Nom, Esquive, Armure
#Armes = Nom, Dégâts, Cartouches

dict_terrain = {}
dict_terrain["Gros rocher"] = [100,0]
dict_terrain["Plaine"] = [0,100]
dict_terrain["Buisson"] = [25,25]
dict_terrain["Petit rocher"] = [50,50]
cle_dict_terrain = list(dict_terrain.keys())
dict_armures = {}
dict_armures["Lourde"] = [-25,10]
dict_armures["Moyenne"] = [-10,6]
dict_armures["Légère"] = [0,2]
dict_armures["Aucune"] = [5,0]
cle_dict_armures = list(dict_armures.keys())
dict_armes = {}
dict_armes["L1A1"] = [15,20]
dict_armes["M16"] = [10,30]
dict_armes["M9"] = [7,12]
cle_dict_armes = list(dict_armes.keys())
# dict_armes["Pied de biche"] = [8,-1]


def Equipement(perso):
    if perso == Joueur1.Nom:
        print("Veuillez choisir votre arme parmis la liste suivante :",\
cle_dict_armes)
        temp_joueur1_arme = input()
        Joueur1.Arme = dict_armes[temp_joueur1_arme].copy()
        Joueur1.Arme.insert(0,temp_joueur1_arme)
        
        print("Veuillez choisir votre armure parmis la liste suivante : ",\
cle_dict_armures)
        temp_joueur1_armure = input()
        Joueur1.Armure = dict_armures[temp_joueur1_armure].copy()
        Joueur1.Armure.insert(0,temp_joueur1_armure)
    
    else:
        temp_adversaire_arme = random.choice(cle_dict_armes)
        temp_adversaire_armure = random.choice(cle_dict_armures)
        
        Adversaire.Arme = dict_armes[temp_adversaire_arme].copy()
        Adversaire.Arme.insert(0,temp_adversaire_arme)
        
        Adversaire.Armure = dict_armures[temp_adversaire_armure].copy()
        Adversaire.Armure.insert(0,temp_adversaire_armure)

def Touche(attaquant,defenseur):
    jet = random.randint(1,100)
    if jet <= attaquant.Competence-defenseur.Esquive:
        return 1
    else:
        return 0


def Degats(attaquant,defenseur):
    if attaquant.Arme[1] <= defenseur.Armure[2]:
        return 0
    elif attaquant.Arme[1] > defenseur.Armure[2]:
        return attaquant.Arme[1]-defenseur.Armure[2]


class Personnage:
    def __init__(self,nom_in):
        self.Nom = nom_in
        self.PV = 100
        self.Armure = ["",0,0]
        self.Potion = 1
        self.Arme = ["",0,0]
        self.Competence = 65
        self.Emplacement = ["",0,0]
        self.Esquive = self.Armure[1]+self.Emplacement[1]


Adversaire = Personnage("Adversaire")
Joueur1 = Personnage("Joueur1")


def main():
    print("Bienvenue dans ce simulateur de duel.")
    Equipement(Joueur1.Nom)

    Joueur1.Emplacement = (dict_terrain["Plaine"].copy())
    Joueur1.Emplacement.insert(0,"Plaine")
    
    print("Voici votre arme :",Joueur1.Arme[0],"Dégâts :",\
Joueur1.Arme[1],"Nombre de cartouches :",\
Joueur1.Arme[2])

    print("Voici votre armure :",Joueur1.Armure[0],"Modificateur d'esquive :",\
Joueur1.Armure[1],"Protection :",Joueur1.Armure[2])

    print("Voici votre emplacement :",Joueur1.Emplacement[0],"Esquive :",\
Joueur1.Emplacement[1],"Visibilité :",Joueur1.Emplacement[2])

    print("Votre adversaire se prépare...")
    Equipement(Adversaire.Nom)
    
    Adversaire.Emplacement.insert(0,"Plaine")
    Adversaire.Emplacement.extend(dict_terrain["Plaine"].copy())

    print("Votre adversaire a choisi cette arme :",Adversaire.Arme[0],\
"et cette armure :",Adversaire.Armure[0],"Il se situe ici :",\
Adversaire.Emplacement[0],"Esquive :",Adversaire.Emplacement[1],"Visibilité :",\
Adversaire.Emplacement[2])

    while Joueur1.PV > 0 or Adversaire.PV > 0:
        if Joueur1.PV <= 0:
            print("Vous êtes mort.e !")
            break
        elif Adversaire.PV <= 0:
            print("Votre adversaire est mort !")
            break
        else:
            while Joueur1.PV > 0 and Adversaire.PV > 0:
                print("Test combat : ")
                attaque1 = Touche(Joueur1,Adversaire)
                if attaque1 == 1:
                    Blessure = Degats(Joueur1,Adversaire)
                    print(Joueur1.Nom,"a infligé",Blessure,"dégâts à",\
Adversaire.Nom) 
                    Adversaire.PV -= Blessure
                elif attaque1 == 0:
                    print("Vous avez râté votre attaque !")
                    
                attaque2 = Touche(Adversaire,Joueur1)
                if attaque2 == 1:
                    print("Voici l'état de votre adversaire :",\
Adversaire.PV,"PV")
                    Blessure = Degats(Adversaire,Joueur1)
                    print(Adversaire.Nom,"a infligé",Blessure,"dégâts à",\
Joueur1.Nom)
                    Joueur1.PV -= Blessure
                    print("Voici votre état :",Joueur1.PV,"PV")
                elif attaque2 == 0:
                    print("Votre adversaire a râté son attaque !")
                    
                if Adversaire.Emplacement[0] != "Petit rocher":
                    print("Votre adversaire se déplace !")
                    advmove = random.choice(cle_dict_terrain)
                    Adversaire.Emplacement = dict_terrain[advmove].copy()
                    Adversaire.Emplacement.insert(0,advmove)
                    print("Votre adversaire est maintenant à l'emplacement \
suivant :",Adversaire.Emplacement[0])

if __name__ == '__main__':
    main()