# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 08:24:20 2023

@author: Hannah
"""

def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    #Building the base case
    if n==1:
        #recursively calling the function
        print ("Move disk 1 from rod", from_rod, "to rod", to_rod)
        return 
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod) #moving the disk from the first rod (source) to the second rod (destination)
    print ("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)

#testing it
TowerOfHanoi(3, 'A', 'C', 'B')  