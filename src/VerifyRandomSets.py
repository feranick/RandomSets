#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
**********************************************************
* VerifyRandomSets
* 20200121a
* By: Nicola Ferralis <feranick@hotmail.com>
***********************************************************
'''
print(__doc__)

import numpy as np
import ast, sys, os.path

def main():
    if len(sys.argv) < 1:
        print("usage: VerifyRandomSets roster_2020-01-15_15-49-14.csv")
        return
    else:
        kids = np.genfromtxt(sys.argv[1], delimiter=',').T

    print("Roster:\n", kids)

    print("\n Input criteria for selection in the format:",repr(np.ones((kids.shape[1]-1), dtype=int).tolist()))
    print(" where each element of the array can be 0 or 1, for attribute no and yes respectively,\n or 2, if it's irrelevant to the game")
    print(" type 0 to exit ")
    while True:
        try:
            sel_criteria = ast.literal_eval(input('\nCriteria: '))
            if sel_criteria == 0:
                break
            selected = kids
            for k in range(kids.shape[1]-1):
                if sel_criteria[k] < 2:
                    selected = selected[(selected[:,k+1] == sel_criteria[k])]

            print("\nSelection criteria: ", sel_criteria)
            print("Selected: ", selected)
        except:
            print("wrong format")
            
#************************************
''' Main initialization routine '''
#************************************
if __name__ == "__main__":
    sys.exit(main())

