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
# dict_armes["Pied de biche"] = [8,-1]
cle_dict_armes = list(dict_armes.keys())
# 0 = néant, 1 = buisson, 2 = petit rocher, 3 = gros rocher, 4 = plaine
# dict_terrain = {}
# dict_terrain[0] = ["Néant",0,0]
# dict_terrain[1] = ["Buisson",25,25]
# dict_terrain[2] = ["Petit rocher",50,50]
# dict_terrain[3] = ["Gros rocher",150,0]
# dict_terrain[4] = ["Plaine",0,100]

# cle_dict_terrain = list(dict_terrain.keys())
# dict_coordonnees = {[0,0,0,0,0,0],
                    # [0,4,4,3,4,0],
                    # [0,4,4,2,1,0],
                    # [0,1,3,2,4,0],
                    # [0,3,2,4,4,0],
                    # [0,0,0,0,0,0]}



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
        self.Actions = 0
#        self.PositionY = dict_coordonnees[Y] // doit contenir la coordonnée Y.
#        self.PositionX = dict_coordonnees[][X] // doit contenir la coordonnée X 


Adversaire = Personnage("Adversaire")
Joueur1 = Personnage("Joueur1")


# def Position(perso): //Cette fonction devra indiquer l'emplacement actuel.
#                      //Elle devra également lire les emplacements situés
#                      //autour (gauche, droite, haut, bas).
    # print(perso.Nom,"est à l'emplacement suivant :",perso.Emplacement)
    # print(perso.Nom,"voit à sa gauche :",perso.PositionX-1)


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
        Adversaire.Cartouches_restantes = Adversaire.Arme[2]
        
        Adversaire.Armure = dict_armures[temp_adversaire_armure].copy()
        Adversaire.Armure.insert(0,temp_adversaire_armure)


def Attaque(attaquant,defenseur):
    for tir in range (attaquant.Arme[3]):
        if attaquant.Cartouches_restantes > 0:
            jet = random.randint(1,100)+(tir*5)
            if jet <= attaquant.Competence-defenseur.Esquive:
                attaquant.Cartouches_restantes -= 1
                
                if attaquant.Arme[1] <= defenseur.Armure[2]:
                    blessure = 0
                elif attaquant.Arme[1] > defenseur.Armure[2]:
                    blessure = attaquant.Arme[1]-defenseur.Armure[2]

                print(attaquant.Nom,"a infligé",blessure,"dégâts à",\
defenseur.Nom)
                defenseur.PV -= blessure

            else:
                attaquant.Cartouches_restantes -= 1
                print(attaquant.Nom,"a râté son attaque !")
        else:
            print("Il ne reste pas de munitions à",attaquant.Nom,"!")
            break


def main():
    print("Bienvenue dans ce simulateur de duel.")
    Equipement(Joueur1.Nom)
    
    print("Voici votre arme :",Joueur1.Arme[0],"Dégâts :",\
Joueur1.Arme[1],"Nombre de cartouches :",Joueur1.Arme[2],"mode de tir :",\
Joueur1.Arme[3])

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
            Joueur1.Actions = 2
            while Joueur1.Actions > 0 and Joueur1.PV > 0:
                print("*" * 5)
                print("Quelle action voulez-vous effectuer ?")
                print("1 - Déplacement. 2 - Observation. 3 - Potion de soin. \
4 - Attaque")
                choix = int(input())
                match choix:
                    case 1:
                        print("Vous vous déplacez.")
                        Deplacement(Joueur1)
                        Joueur1.Esquive = Joueur1.Armure[1]\
                                        +Joueur1.Emplacement[1]
                        localisation_joueur = 0
                        Joueur1.Actions -= 1
                        print("Actions restantes :",Joueur1.Actions)
                    case 2:
                        obs = Observation(Joueur1,Adversaire)
                        Joueur1.Actions -= 1
                        print("Actions restantes :",Joueur1.Actions)
                        if obs == 1 and Joueur1.Actions > 0:
                            localisation_adversaire = 1
                            print("Vous pouvez attaquer.")
                            print("Voulez-vous attaquer ? (oui/non)")
                            choix_attaque = input()
                            if choix_attaque.lower() == "oui":
                                Attaque(Joueur1,Adversaire)
                                Joueur1.Actions -= 1
                            else:
                                print("Vous n'attaquez pas.")
                        else:
                            print("Vous ne pouvez pas attaquer \
pour l'instant.")
                    case 3:
                        print("Vous buvez une potion de soin.")
                        Soin(Joueur1)
                        Joueur1.Actions -= 1
                    case 4:
                        if localisation_adversaire == 1:
                            Attaque(Joueur1,Adversaire)
                            Joueur1.Actions -= 1
                        else:
                            print("Vous n'avez pas encore localisé \
votre adversaire.")
            
            Adversaire.Actions = 2
            while Adversaire.Actions > 0 and Adversaire.PV > 0:
                print("*" * 5)
                if Adversaire.Emplacement[0] != "Petit rocher":
                    print("Votre adversaire se déplace !")
                    Deplacement(Adversaire)
                    Adversaire.Esquive = Adversaire.Armure[1]\
                                    +Adversaire.Emplacement[1]
                    localisation_adversaire = 0
                    Adversaire.Actions -= 1
                elif Adversaire.PV <= 10 and Adversaire.Potion > 0:
                    print("Votre adversaire cherche une potion !")
                    Soin(Adversaire)
                    Adversaire.Actions -= 1
                    Adversaire.Potion -= 1
                elif localisation_joueur == 1:
                    Attaque(Adversaire,Joueur1)
                    Adversaire.Actions -= 1
                else:
                    print("Votre adversaire observe !")
                    adv_obs = Observation(Adversaire,Joueur1)
                    Adversaire.Actions -= 1
                    if adv_obs == 1:
                        localisation_joueur = 1
                        if adv_obs == 1 and localisation_joueur == 1\
and Adversaire.Actions > 0:
                            Attaque(Adversaire,Joueur1)    
                            Adversaire.Actions -= 1

        if Joueur1.PV <= 0:
            print("Vous êtes mort !")
            combat = 0
        else:
            print("Votre adversaire est mort !")
            combat = 0

if __name__ == '__main__':
    main()