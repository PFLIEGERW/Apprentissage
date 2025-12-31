#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def add_shopping():
    item = ' '
    file = open("Page70_shopping_list.txt","r")
    items = eval(file.read())
    file.close()
    while item != 'End':
        item = input('Enter a shopping list item or \
enter "End" to finish your list : ').title()
        if item != 'End':
            items.append(item)
    newfile = open("Page70_shopping_list.txt","w")
    newfile.write(str(items))
    newfile.close()

def main():
    add_shopping()
if __name__ == '__main__':
    main()