#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def cubic_volume(length, width, height):
    try:
        volume_out=int(length)*int(width)*int(height)
        return volume_out
    except:
        print("Merci de bien vouloir utiliser uniquement des nombres entiers.")
        return exit()
def main():
    
    print("Merci de bien vouloir entrer une longueur entière : ")
    lenght=input()
    print("Merci de bien vouloir entrer une largeur entière : ")
    width=input()
    print("Merci de bien vouloir entrer une hauteur entière : ")
    height=input()
    
    volume=cubic_volume(lenght, width, height)
    print("Le volume de votre objet est : ",volume)
    
if __name__ == '__main__':
    main()