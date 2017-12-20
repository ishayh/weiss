#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import random

NUM_CARDS = 52
suit = {'H', 'S', 'D', 'C'}
typeOfCard = {"2","3","4","5","6","7", 
   "8","9","10","J","Q","K","A"}
value = {2,3,4,5,6,7,8,9,10,10,10,10,11}

"""
* Should permute the deck of cards, effectively shuffling it.
 * You must use the Fisher-Yates / Durstenfeld shuffle algorithm
 *  described in the assignment writeup.
"""
def shuffle(cards):
    return

"""
* Prints the card in a "pretty" format:   "type-suit"
 *  Examples:  K-C  (King of clubs), 2-H (2 of hearts)
 *  Valid Types are: 2,3,4,5,6,7,8,9,10,J,Q,K,A
 *  Valid Suits are: H, D, C, S
"""
def printCard(id):
    return

"""
 * Returns the numeric value of the card.
 *  Should return 11 for an ACE and can then
 *  be adjusted externally based on the sum of the score.
"""
def cardValue(id):
    return

"""
 * Should print out each card in the hand separated by a space and
 * then print a newline at the end.  
 * Should use printCard() to print out each card.
"""
def printHand(hand, numCards):
    return



"""
 * Should return the total score of the provided hand.  
 * ACES should be treated as 11s to make the highest possible hand
 *  and only being reduced to 1s as needed to avoid busting.
"""
def getBestScore(hand, numCards):
    return



    
def main():
    if len(sys.argv) < 2:
        print ('Error - Please provide the seed value.')
        return 0
    seed = int(sys.argv[1])
    random.seed(seed)
    
    cards = []
    dhand = []
    phand = []
    
    
    
    return 0

if __name__ == "__main__":
    main()