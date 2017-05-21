# -*- coding: utf-8 -*-
import numpy as np
import scipy as sp

File = "greek_verbs.txt"

fin = open(File, "r")
verbs = [line.rstrip('\n') for line in fin]
fin.close()

print(verbs)

input_verb = "πειρά"


#Begin Greedy Algorithm
pos_letter = 0
temp = len(verbs)
ii = 0

while pos_letter < len(input_verb)-1:
    while ii < len(verbs):
        if verbs[ii][pos_letter] != input_verb[pos_letter]:
            verbs.remove(verbs[ii])
        ii += 1
    pos_letter += 1
    ii = 0
print((verbs)) 
    
    
    
