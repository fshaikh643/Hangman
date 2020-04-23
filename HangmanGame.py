#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 09:41:42 2020

@author: firozshaikh
"""


import random
import sys

#create the hangman segments to loop through when an incorrect guess is made
hanger = []
for j in range(15):
    hanger.append("")

hanger[0] = "    ________"
 
for i in range(1,5):
    hanger[i] = "   |        |"
hanger[5]= "    0       |"    
hanger[6] =" --+--      |"
hanger[7]="/  |  \\     |"
hanger[8]="   |        |"
hanger[9]="  / \\       |"
hanger[10]=" /   \\      |"

for k in range(11,14):
    hanger[k]="            |"

hanger[14]="_____________"

h=len(hanger)

#two categories of words for the player to choose from
animals = ["giraffe", "monkey", "rhinoceros", "alligator", "whale", 
           "shark", "horse"]
flowers = ["daffodil","rose", "dahlia","tulip", "poppy","bluebell"]

#to exit game any time - press 0
def esc(g):
    if g == "0":
        print("\nExit from game.")
        sys.exit()

#player can press 1 or 2 to select  category and 0 to exit anytime
c = "" 
while c not in ["0", "1", "2"]:
    c = input("Press '1' for Animals '2' for Flowers or '0' to "
              "exit anytime \n")
    esc(c)

#map the choise to the cateogry
dict = {"1":animals, "2": flowers}
#pick a  random word from the category
word = random.choice(dict[c]).upper()


#formulate the word as a list to compare the guesses with
wordlist = list(word.upper())
l = len(word)

#create a space to store the guesses and print out later (like e.g W*LF )
guess = []
for i in range(l):
    guess.append('*')

#a placeholder for wrong guesses
errs =[]   
#record number of matches and incorrect guesses
hit = 0
miss = 0
print("There are",l, "letters: ", *guess)
while hit < l:
    g = input("\nGuess a letter...   ").upper()
    esc(g)
    if g.isalpha() == False:
        print("Please type a letter or 0 to exit:")
        continue  
     #check the letter has not  already been selected, if so ask for another   
    if g in guess:
        print("You've selected this letter already. Try another..")
        continue
#if a correct guess is made
    if g in wordlist:   
        for i in range(l): 
#otherwise record a match and place the letter in our guess list
            if wordlist[i] == g:
                guess[i] = g
                hit += 1        
        print("Great guess!")        
    else:  
#let player know of a incorrect letter tried already (no miss count is recorded)          
        if g in errs:
                print("Letter was already incorrectly guessed")
                continue
#for incorrect guesses record a miss            
        else:
            errs.append(g)        
        print("Sorry wrong guess..\n")
        miss +=1     
#print the hangman for the number of misses        
    for n in range(miss):
        print(hanger[n])    
#print the word with the correct guesses e.g W*LF       
    print("\nWord: ", *guess)
#list all the incorrect guesses                       
    print("\nMisses:", *errs)
#if enough wrong guesses are made we have man is hung        
    if miss == len(hanger):
        print("\nSorry you lose...the answer was", word)
        break
#if all the letters have been guessed the player has won      
    if hit == l:  
        print("\nYou've won!")
        break
    
        
        
        
