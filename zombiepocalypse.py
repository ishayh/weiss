#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 01:52:37 2017

@author: dunce
"""
import random


def main():
    N = int(input("Enter the total population"))
    k = int(input("Enter the number of initial zombies"))
    M = int(input("Enter the number of simulations of the zombie-pocalypse"))
    s = int(input("Enter seed"))
    pop = { }
    random.seed(s)
    
    for i in range(k):
        pop[i] = 1
    
    for i in range(M):
        while 


if __name__ == '__main__':
    main()