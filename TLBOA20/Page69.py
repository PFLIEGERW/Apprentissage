#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def shopping():
    item = ' '
    items = []
    while item != 'End':
        item = input('Enter a shopping list item or \
enter "End" to finish your list :').title()
        if item != 'End':
            items.append(item)
        newfile = open("Page69_shopping_list.txt","w")
        newfile.write(str(items))
        newfile.close()


def main():
    shopping()
    
if __name__ == '__main__':
    main()