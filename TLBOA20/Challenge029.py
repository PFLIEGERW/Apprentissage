#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def vowel_counter(sentence):
    A = 0
    E = 0
    I = 0
    O = 0
    U = 0

    for i in range (len(sentence)):
        if sentence[i].upper() == "A":
            A += 1
        elif sentence[i].upper() == "E":
            E += 1
        elif sentence[i].upper() == "I":
            I += 1
        elif sentence[i].upper() == "O":
            O += 1
        elif sentence[i].upper() == "U":
            U += 1

    print("Voici le décompte des voyelles : ")
    print("A : ",A)
    print("E : ",E)
    print("I : ",I)
    print("O : ",O)
    print("U : ",U)
    
def main():
    sentence = ("Learning programming is similar to learning a musical\
instrument. Both involve practise and making lots of mistakes. \
Both also require perseverance to develop fluency. Keep going!")
    vowel_counter(sentence)
    
if __name__ == '__main__':
    main()