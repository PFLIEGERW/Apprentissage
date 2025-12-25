#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def vowel_counter(Sentence):
    Vowel_List=[["A",0],["E",0],["I",0],["O",0],["U",0],["Y",0]]
    
    for Lettre in Sentence:
        for Sublist in Vowel_List:
            if Sublist[0] == Lettre.upper():
                Sublist[1] += 1
    else:
        return Vowel_List
        
def main():
    Sentence = "Learning programming is similar to learning a musical \
instrument. Both involve practise and making lots of mistakes. \
Both also require perseverance to develop fluency. Keep going!"
    print("Voici les voyelles composant la phrase : ",Sentence)
    Vowel_List_Out = vowel_counter(Sentence)
    print(Vowel_List_Out)
    
if __name__ == '__main__':
    main()