
import networkx as nx
import numpy as np
import random
# create a undirected graph
def create_graph(n,p)    :                                   # number of nodes, probability of edge creation
    G = nx.Graph()
    G.add_nodes_from(range(1, n+1))                         # add nodes to the graph
# add edges to the graph with the given probability
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if random.random() < p:
               G.add_edge(i, j)
    return G

def random_walk(Graph, start_node, end_node):  
  path = [start_node]      
  ### START CODE HERE ###
  current_node = start_node
  len_nodes = len(Graph)
  times = 2 * (len_nodes) ** 3
  print(end_node)
  for i in range(times):
      neighbors = Graph[current_node]
      #convierte el dict en list
      neighbors_list = list(neighbors)
      #eleccion random de los nodes conectados a current_node
      next_node = random.choice(neighbors_list)
      #añade el next node al path
      if current_node == end_node:
        print("there is a path.")
        break
      if current_node != end_node and i == times:
        print("there is no path.")
      path.append(next_node)
      current_node = next_node


  ### END CODE HERE ###      
  return path


# test graph
G = create_graph(50,0.2)

# visualize the graph
from matplotlib.pyplot import figure
figure(figsize=(20, 6), dpi=80)
nx.draw(G, with_labels=True,font_size=10,font_color= 'white', node_color='blue',node_size=350,width=0.2)

path=random_walk(G, 1, 19)
path

path_graph=nx.path_graph(path)

figure(figsize=(20, 6), dpi=80)
nx.draw(path_graph, with_labels=True,font_size=10,font_color= 'white', node_size=400,width=0.2)
