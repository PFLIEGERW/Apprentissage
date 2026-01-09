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

def Touche(Attaquant,Defenseur):
    jet = random.randint(1,100)
    if jet <= Attaquant.Competence-Defenseur.Esquive:
        return 1
    else:
        return 0

def Degats(Attaquant,Defenseur):
    if Attaquant.Arme[1] <= Defenseur.Armure[2]:
        return 0
    elif Attaquant.Arme[1] > Defenseur.Armure[2]:
        return Attaquant.Arme[1]-Defenseur.Armure[2]

class Personnage:
    def __init__(self,Nom_in):
        self.Nom = Nom_in
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

    Joueur1.Emplacement = (Dict_Terrain["Plaine"].copy())
    Joueur1.Emplacement.insert(0,"Plaine")
    
    print("Voici votre arme :",Joueur1.Arme[0],"Dégâts :",\
Joueur1.Arme[1],"Nombre de cartouches :",\
Joueur1.Arme[2])

    print("Voici votre armure :",Joueur1.Armure[0],"Modificateur d'esquive :",\
Joueur1.Armure[1],"Protection :",Joueur1.Armure[2])

    print("Voici votre emplacement :",Joueur1.Emplacement[0],"Esquive :",\
Joueur1.Emplacement[1],"Visibilité :",Joueur1.Emplacement[2])

    print("Votre adversaire se prépare...")
    TempAdversaireArme = random.choice(Cle_Dict_Armes)
    TempAdversaireArmure = random.choice(Cle_Dict_Armures)
    
    Adversaire.Arme = Dict_Armes[TempAdversaireArme].copy()
    Adversaire.Arme.insert(0,TempAdversaireArme)
    
    Adversaire.Armure = Dict_Armures[TempAdversaireArmure].copy()
    Adversaire.Armure.insert(0,TempAdversaireArmure)
    
    Adversaire.Emplacement.insert(0,"Plaine")
    Adversaire.Emplacement.extend(Dict_Terrain["Plaine"].copy())

    print("Votre adversaire a choisi cette arme :",Adversaire.Arme,\
"et cette armure :",Adversaire.Armure,"Il se situe ici :",\
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
                Attaque1 = Touche(Joueur1,Adversaire)
                if Attaque1 == 1:
                    Blessure = Degats(Joueur1,Adversaire)
                    print(Joueur1.Nom,"a infligé",Blessure,"dégâts à",\
Adversaire.Nom) 
                    Adversaire.PV -= Blessure
                elif Attaque1 == 0:
                    print("Vous avez râté votre attaque !")
                    
                Attaque2 = Touche(Adversaire,Joueur1)
                if Attaque2 == 1:
                    print("Voici l'état de votre adversaire :",\
Adversaire.PV,"PV")
                    Blessure = Degats(Adversaire,Joueur1)
                    print(Adversaire.Nom,"a infligé",Blessure,"dégâts à",\
Joueur1.Nom)
                    Joueur1.PV -= Blessure
                    print("Voici votre état :",Joueur1.PV,"PV")
                elif Attaque2 == 0:
                    print("Votre adversaire a râté son attaque !")
                    
                if Adversaire.Emplacement[0] != "Petit rocher":
                    print("Votre adversaire se déplace !")
                    Advmove = random.choice(Cle_Dict_Terrain)
                    Adversaire.Emplacement = Dict_Terrain[Advmove].copy()
                    Adversaire.Emplacement.insert(0,Advmove)
                    print("Votre adversaire est maintenant à l'emplacement \
suivant :",Adversaire.Emplacement[0])

if __name__ == '__main__':
    main()