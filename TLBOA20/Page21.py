#!/usr/bin/env python3
# -*- coding:utf-8 -*-

CONSTANT_PI=3.14159

def circle_area(radius_in):
    area_out = CONSTANT_PI * radius_in**2
    return area_out

def main():
    radius = int(input("Enter the integral radius of the circle: "))
    area = circle_area(radius)
    
    print("The area of the circle is", area)
    
if __name__ == '__main__':
    main()