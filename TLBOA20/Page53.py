#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main():
#Àl'intérieur de cs_scores, ["Jo","45","60","72"] correspond à cs_scores[0].
#"Jo", correspond à cs_scores[0][0]
#Donc, lors de la lecture d'une liste de liste, alors [][] correspond à l'entrée
#dans une liste puis à la lecture d'un indice dans cette liste.

    cs_scores=[["Jo","45","60","72"],["Zi","55","65","70"],\
["Ellie","71","78","78"],["Jessica","68","79","80"],\
["Taseen","65","70","71"]]

    print("We will try to find the result for a given \
student's exam")
    name = input("Enter a student name: ")
    exam_number = int(input("Enter the exam number (1,2,3) : "))
    found = False
    for count in range(len(cs_scores)):
        if name == cs_scores[count][0]:
            found = True
            result = cs_scores[count][exam_number]
            print(name+ "'s result for exam", exam_number,\
"was", result )
    if found == False:
        print(name, "cannot be found")
    
if __name__ == '__main__':
    main()