#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main():
    animals = [["Charlie", "Dog", 8],["Dolly", "Sheep", 3],\
["Wanda", "Goldfish", 4]]
    for x in range(len(animals)):
        for y in range(0,3):
            print(animals[x][y])
    
    
if __name__ == '__main__':
    main()