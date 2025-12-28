#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def average_2DList(cs_scores):
    total = 0
    for student in range(len(cs_scores)):
        for exam in range(1,4):
            total = total + int(cs_scores[student][exam])
            average = "{:.2f}".format(total / 3)
        print("average",cs_scores[student][0],"=",average)
        total = 0

def main():
    cs_scores = [["Karman","45","60","72"],["Daniel","55","65","70"],\
["Parker","71","78","78"],["Jessica","68","79","80"],["Edie","98","85","91"]]
    print("Here is the average score for each student :")
    average_2DList(cs_scores)
    
if __name__ == '__main__':
    main()