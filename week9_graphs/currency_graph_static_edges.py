'''
This program takes the currency exchange rates in a 2D list
and creates a graph with the currencies as nodes, and exchange rates as edges
'''

import requests
import json
import time
from datetime import datetime, timedelta
from itertools import combinations

import networkx as nx
from networkx.classes.function import path_weight


###########################################
# 2D list of currency exchange rates 
# 1st row is Polish Zolty, PLN
# to go from PLN to PLN, exchange rate is 1.0
# to go from PLN to EUR, exchange rate is 0.23
# Meaning 1 PLN gets you 0.23 Euros
# to go from PLN to RUB (Russian Ruble), exchange rate is 16.43
# Meaning 1 PLN gets your 16.43  Rubles
currencies = ('PLN', 'EUR', 'USD', 'RUB', 'INR', 'MXN')

rates = [
    [1, 0.23, 0.25, 16.43, 18.21, 4.94],
    [4.34, 1, 1.11, 71.40, 79.09, 21.44],
    [3.93, 0.90, 1, 64.52, 71.48, 19.37],
    [0.061, 0.014, 0.015, 1, 1.11, 0.30],
    [0.055, 0.013, 0.014, 0.90, 1, 0.27],
    [0.20, 0.047, 0.052, 3.33, 3.69, 1],
]



###########################################
# Creating graph by iterating through list of exchange rates
# and adding each each, 2 currency nodes, and the exchange rate in between
g = nx.DiGraph()
edges = []
i = 0
for c1 in currencies:
    j = 0
    for c2 in currencies:
        if c1 != c2:
            edges.append((c1, c2, rates[i][j]))
            print("adding edge: ", c1, c2, rates[i][j])
        j +=1
    i += 1
g.add_weighted_edges_from(edges) 

print(g.nodes)



###########################################
# Traversing the Graph
# Going through each of the paths from one currency to the others
# combination function returns all possible currency pairs
# calculating path weight from one currency to another
# then back again
for n1, n2 in combinations(g.nodes,2):
    print("All paths from ", n1, "to", n2, "---------------")
    
    for path in nx.all_simple_paths(g, source=n1, target=n2):
        print("Path To", path)
    
        path_weight = 1.0
        # calculating the path weight from the first currency to the second
        for i in range(len(path) - 1):
            path_weight *= g[path[i]][path[i+1]]['weight']
        print("path_weight: ", path_weight)
    
        # Reversing the path, so calculate the path weight returning 
        path.reverse()
        print("Path From", path)
        
        path_weight = 1.0
        # calculating the path weight from the first currency to the second
        for i in range(len(path) - 1):
            path_weight *= g[path[i]][path[i+1]]['weight']
        print("path_weight: ", path_weight)
    
    print("---------------\n")
    
input("press enter")
