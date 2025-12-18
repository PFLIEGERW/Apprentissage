#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main():
    numbers_list = [9, 8, 72, 22, 21, 81, 2, 1]
    numbers_list = sorted(numbers_list, reverse=True)
    print(numbers_list[0])

if __name__ == '__main__':
    main()
    
# Again, si des outils nous sont proposés, utilisons les plutôt que de vouloir
# ré-écrire la roue.