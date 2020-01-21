#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
**********************************************************
* CreateRandomSet
* 20200121a
* By: Nicola Ferralis <feranick@hotmail.com>
***********************************************************
'''
print(__doc__)

import numpy as np
import ast, sys
from datetime import datetime, date

def main():
    if len(sys.argv) < 2:
        print("usage: CreateRandomSets <number of students> <probabilities in array form - [.5, .3, .6, ...]>")
        return
    
    prob_q = ast.literal_eval(sys.argv[2])
    print("Attributes:",len(prob_q))
    print("Probabilities:", prob_q,"\n")
    print("Number of Students:",int(sys.argv[1]))

    saved_roster = "roster"+str(datetime.now().strftime('_%Y-%m-%d_%H-%M-%S.csv'))

    for i in range(int(sys.argv[1])):
        kid = [i+1]
        for j in range(len(prob_q)):
            kid = np.hstack((kid, np.random.choice(np.arange(0,2),p=[prob_q[j],1-prob_q[j]])))
        try:
            kids = np.vstack((kids, kid))
        except:
            kids = kid
    
    print("Roster:\n", kids)
    with open(saved_roster, "a") as file:
        np.savetxt(file, kids, delimiter=',', fmt='%i')
    print("\nRoster saved in:", saved_roster)
    
    
#************************************
''' Main initialization routine '''
#************************************
if __name__ == "__main__":
    sys.exit(main())



