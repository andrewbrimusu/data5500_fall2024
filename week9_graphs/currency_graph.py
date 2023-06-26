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


currencies = ["usd", "eur", "gbp", "mxn", "rub", "inr"]

g = nx.DiGraph()
edges = []

############################################################
# Querying floatrates.com for currency exchange rates
url1 = "http://www.floatrates.com/daily/"
url2 = ".json"
for c1, c2 in permutations(currencies,2):
    url = url1 + c1 + url2
    print(c1, "to", c2, url)
    
    req = requests.get(url)
    dct1 = json.loads(req.text)
    rate = dct1[c2]["rate"]
    edges.append((c1, c2, rate))
    
g.add_weighted_edges_from(edges) 



############################################################
# Saving Graph Visual
curr_dir = os.path.dirname(__file__) # get the current directory of this file
graph_visual_fil = curr_dir + "/" + "currencies_graph_visual.png"

pos=nx.circular_layout(g) # pos = nx.nx_agraph.graphviz_layout(G)
nx.draw_networkx(g,pos)
labels = nx.get_edge_attributes(g,'weight')
nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)

plt.savefig(graph_visual_fil)
