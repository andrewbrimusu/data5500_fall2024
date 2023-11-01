import requests
import json
import time
import os
from datetime import datetime, timedelta
from itertools import permutations
from itertools import combinations

import networkx as nx
from networkx.classes.function import path_weight

import matplotlib.pyplot as plt




############################################################
# Querying floatrates.com for currency exchange rates
url1 = "http://www.floatrates.com/daily/"
url2 = ".json"

#example rate from "usd" to "eur"
c1 = "usd"
c2 = "eur"

# url to get exchange rate
url = url1 + c1 + url2
print(c1, "to", c2, url)

# Activity Step 1
# request exchange rate information from usd to eur, from floatrates api
req = requests.get(url)
dct1 = json.loads(req.text)

# Activity Step 2
# extract rate from json


#example adding the 2 nodes, and edge between them, to a tuple to be added to a graph
edges.append((c1, c2, rate))



# Activity Step 3
# - loop through permutations of currencies
# - request exchange rate for each pair
# - create a tuple with 2 nodes and an edge
currencies = ["usd", "eur", "gbp"] # , "mxn", "rub", "inr"]

g = nx.DiGraph()
edges = []


# Activity Step 4
# after all the edges are created add them to a graph using the function 
# add_weighted_edges_from


# Activity Step 5
# - loop through all combinations of nodes
# - for each combination call the function all_simple_paths to get all paths from 1 node to another
# - in a nested loop calculate the weight of the path by multiplying the weights of all the edges




