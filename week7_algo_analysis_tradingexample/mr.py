import numpy as np
import os
# os.system("pip3 install numpy") 

import os


# load all the prices from the file, into a Python List
# stock prices file
curr_dir = os.path.dirname(__file__) # get the current directory of this file

tkr = "wmt"
stock_fil = curr_dir + "/data/" + tkr + ".txt" # dirname and __file__ (this file) returns the current folder
file = open(stock_fil, "r")

prcs = [float(x) for x in file.readlines()]
print(prcs)


buy = 0
profit = 0.0
i = 0
days = 5

for p in prcs:
    file = open(stock_fil)
    prcs = [float(x) for x in file.readlines()] # need this line?

    if i >= days:
        avg = np.mean(prcs[i-days:i])
        
        if p < avg * .96 and buy == 0: # buy
            buy = p
            print("buying: ", p)
        elif p > avg * 1.04 and buy != 0: # sell
            profit += p - buy
            buy = 0
            print("selling at: ", p)
            
        else:
            pass
        
    i += 1
    
print("total profit: ", profit)
print(prcs[0])
print("returns: ", profit/prcs[0])
