#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def notes(Note):
    ExamNotes = [["A", "90"],["B", "83",],["C", "72"],["D", "60"],["E", "49"],\
["F", "30"]]
    
    Found = False
    for count in range(len(ExamNotes)):
        if Note == ExamNotes[count][0]:
            Found = True
            besoin = ExamNotes[count][1]
            return besoin
    if Found == False:
        return -1
        

def main():
    print("Merci de bien vouloir entrer la note que vous souhaitez obtenir :\
A, B, C, D, E ou F")
    Note = input()
    score = notes(Note)
    if score == -1:
        print("Nous n'avons pas pu trouver la note recherchée.")
    else:
        print("Le score nécessaire à l'obtention de la note",Note,"est :"\
,score)
    
if __name__ == '__main__':
    main()