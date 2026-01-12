#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import random

#Perso = PV, Armure, Arme, Cartouches restantes,
    #Potion de Soin, Terrain, Visibilité
#Adversaire = PV, Armure, Arme, Cartouches restantes,
    #Potion de Soin, Terrain, Visibilité
#Terrain = Nom, Esquive, Visibilité
#Armures = Nom, Esquive, Armure
#Armes = Nom, Dégâts, Cartouches, mode de tir

dict_terrain = {}
dict_terrain["Gros rocher"] = [150,0]
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
dict_armes["L1A1"] = [15,20,1]
dict_armes["M16"] = [8,30,3]
dict_armes["M9"] = [5,12,1]
cle_dict_armes = list(dict_armes.keys())
# dict_armes["Pied de biche"] = [8,-1]


class Personnage:
    def __init__(self,nom_in):
        self.Nom = nom_in
        self.PV = 20
        self.Armure = ["",0,0]
        self.Potion = 1
        self.Arme = ["",0,0,0]
        self.Cartouches_restantes = 0
        self.Competence = 65
        self.Emplacement = ["Plaine",0,100]
        self.Esquive = 0


Adversaire = Personnage("Adversaire")
Joueur1 = Personnage("Joueur1")


def Soin(perso):
    if perso.Potion > 0:
        perso.PV += 10
        print(perso.Nom,"boit une potion de soin !")
    else:
        print(perso.Nom,"n'a plus de potion à boire !")


def Observation(attaquant,defenseur):
    vue = random.randint(1,100)
    
    if attaquant.Nom == Joueur1.Nom:
        print(attaquant.Nom,"voici votre état de santé :",attaquant.PV)
        print(attaquant.Nom,"vous êtes situé à l'emplacement suivant :",\
        attaquant.Emplacement[0],"Esquive :",attaquant.Emplacement[1],\
        "Visibilité :",attaquant.Emplacement[2])
        print(attaquant.Nom,"Il vous reste",attaquant.Cartouches_restantes,\
        "munitions")
        
        if vue <= defenseur.Emplacement[2]:
            print(defenseur.Nom,"est situé à l'emplacement suivant :"\
            ,defenseur.Emplacement[0])
            print(attaquant.Nom,"voici l'état de",defenseur.Nom,defenseur.PV)
            print(attaquant.Nom,"Voici l'équipement de votre adversaire :",\
            "Armure :",defenseur.Armure[0],"Arme :",defenseur.Arme[0])
            return 1
        else:
            print(defenseur.Nom,"n'est pas visible actuellement.")
            return 0
            
    else:
        if vue <= defenseur.Emplacement[2]:
            return 1
        else:
            return 0


def Deplacement(perso):
    emplacement_temp = random.choice(cle_dict_terrain)
    perso.Emplacement = dict_terrain[emplacement_temp].copy()
    perso.Emplacement.insert(0,emplacement_temp)


def Equipement(perso):
    if perso == Joueur1.Nom:
        print("Veuillez choisir votre arme parmis la liste suivante :",\
cle_dict_armes)
        temp_joueur1_arme = input()
        Joueur1.Arme = dict_armes[temp_joueur1_arme].copy()
        Joueur1.Arme.insert(0,temp_joueur1_arme)
        Joueur1.Cartouches_restantes = Joueur1.Arme[2]
        
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
        attaquant.Cartouches_restantes -= attaquant.Arme[3]
        return 1
    else:
        attaquant.Cartouches_restantes -= attaquant.Arme[3]
        return 0


def Degats(attaquant,defenseur):
    if attaquant.Arme[1] <= defenseur.Armure[2]:
        return 0
    elif attaquant.Arme[1] > defenseur.Armure[2]:
        return attaquant.Arme[1]-defenseur.Armure[2]


def main():
    print("Bienvenue dans ce simulateur de duel.")
    Equipement(Joueur1.Nom)
    
    print("Voici votre arme :",Joueur1.Arme[0],"Dégâts :",\
Joueur1.Arme[1],"Nombre de cartouches :",\
Joueur1.Arme[2])

    print("Voici votre armure :",Joueur1.Armure[0],"Modificateur d'esquive :",\
Joueur1.Armure[1],"Protection :",Joueur1.Armure[2])

    print("Voici votre emplacement :",Joueur1.Emplacement[0],"Esquive :",\
Joueur1.Emplacement[1],"Visibilité :",Joueur1.Emplacement[2])

    print("Votre adversaire se prépare...")
    Equipement(Adversaire.Nom)
    combat = 1
    while combat == 1:
        localisation_adversaire = 0
        localisation_joueur = 0
        while Joueur1.PV > 0 and Adversaire.PV > 0:
            actions_joueur = 2
            while actions_joueur > 0 and Joueur1.PV > 0:
                print("Quelle action voulez-vous effectuer ?")
                print("1 - Déplacement. 2 - Observation.\
3 - Potion de soin. 4 - Attaque")
                choix = int(input())
                match choix:
                    case 1:
                        print("Vous vous déplacez.")
                        Deplacement(Joueur1)
                        Joueur1.Esquive = Joueur1.Armure[1]\
                                        +Joueur1.Emplacement[1]
                        localisation_joueur = 0
                        actions_joueur -= 1
                        print("Actions restantes :",actions_joueur)
                    case 2:
                        obs = Observation(Joueur1,Adversaire)
                        actions_joueur -= 1
                        print("Actions restantes :",actions_joueur)
                        if obs == 1 and actions_joueur > 0:
                            localisation_adversaire = 1
                            print("Vous pouvez attaquer.")
                            print("Voulez-vous attaquer ? (oui/non)")
                            choix_attaque = input()
                            if choix_attaque.lower() == "oui":
                                attaque1 = Touche(Joueur1,Adversaire)
                                if attaque1 == 1:
                                    Blessure = Degats(Joueur1,Adversaire)
                                    print(Joueur1.Nom,"a infligé",Blessure\
                                    ,"dégâts à",Adversaire.Nom)
                                    Adversaire.PV -= Blessure
                                    actions_joueur -= 1
                                    print("Action restante :",\
                                    actions_joueur)
                                elif attaque1 == 0:
                                    print("Vous avez râté votre attaque !")
                                    actions_joueur -= 1
                                    print("Actions restantes :",\
                                    actions_joueur)
                            else:
                                print("Vous n'attaquez pas.")
                        else:
                            print("Vous ne pouvez pas attaquer \
pour l'instant.")
                    case 3:
                        print("Vous buvez une potion de soin.")
                        Soin(Joueur1)
                    case 4:
                        if localisation_adversaire == 1:
                            attaque1 = Touche(Joueur1,Adversaire)
                            if attaque1 == 1:
                                Blessure = Degats(Joueur1,Adversaire)
                                print(Joueur1.Nom,"a infligé",Blessure\
                                ,"dégâts à",Adversaire.Nom)
                                Adversaire.PV -= Blessure
                                actions_joueur -= 1
                                print("Action restante :",\
                                actions_joueur)
                            elif attaque1 == 0:
                                print("Vous avez râté votre attaque !")
                                actions_joueur -= 1
                                print("Actions restantes :",\
                                actions_joueur)
                        else:
                            print("Vous n'avez pas encore localisé \
votre adversaire.")
            
            actions_adversaire = 2
            while actions_adversaire > 0 and Adversaire.PV > 0:

                if Adversaire.Emplacement[0] != "Petit rocher":
                    print("Votre adversaire se déplace !")
                    Deplacement(Adversaire)
                    Adversaire.Esquive = Adversaire.Armure[1]\
                                    +Adversaire.Emplacement[1]
                    localisation_adversaire = 0
                    actions_adversaire -= 1
                elif Adversaire.PV <= 10 and Adversaire.Potion > 0:
                    print("Votre adversaire cherche une potion !")
                    Soin(Adversaire)
                    actions_adversaire -= 1
                    Adversaire.Potion -= 1
                elif localisation_joueur == 1:
                    attaque2 = Touche(Adversaire,Joueur1)
                    if attaque2 == 1:
                        Blessure = Degats(Adversaire,Joueur1)
                        print(Adversaire.Nom,"a infligé",Blessure,\
                        "dégâts à",Joueur1.Nom)
                        Joueur1.PV -= Blessure
                        actions_adversaire -= 1
                    elif attaque2 == 0:
                        print("Votre adversaire a râté son attaque !")
                        actions_adversaire -= 1
                else:
                    print("Votre adversaire observe !")
                    adv_obs = Observation(Adversaire,Joueur1)
                    actions_adversaire -= 1
                    if adv_obs == 1:
                        localisation_joueur = 1
                    if adv_obs == 1 and localisation_joueur == 1\
and actions_adversaire > 0:
                        attaque2 = Touche(Adversaire,Joueur1)
                        if attaque2 == 1:
                            Blessure = Degats(Adversaire,Joueur1)
                            print(Adversaire.Nom,"a infligé",Blessure,\
                            "dégâts à",Joueur1.Nom)
                            Joueur1.PV -= Blessure
                            actions_adversaire -= 1
                        elif attaque2 == 0:
                            print("Votre adversaire a râté son attaque !")
                            actions_adversaire -= 1
        if Joueur1.PV <= 0:
            print("Vous êtes mort !")
            combat = 0
        else:
            print("Votre adversaire est mort !")
            combat = 0

if __name__ == '__main__':
    main()