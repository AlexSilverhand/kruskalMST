# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 23:58:10 2024

@author: diego
"""
import networkx as nx
import matplotlib.pyplot as plt
import random

# Crear un objeto de grafo
G = nx.Graph()

# Agregar nodos
G.add_nodes_from(['A','B','C','E','F','G','H','I'])

# Agregar varias aristas a la vez mediante una lista
edges = [('A', 'B'), 
         ('A', 'D'), 
         ('A', 'G'), 
         ('B', 'C'), 
         ('B', 'E'), 
         ('B', 'H'), 
         ('C', 'H'), 
         ('D', 'E'), 
         ('E', 'F'), 
         ('F', 'I'),
         ('F', 'G'),
         ('G', 'H'),
         ('G', 'I'),
         ('H', 'I'),
         ('C', 'F'),
         ('A', 'C'),     
         ('B', 'D'),     
         ('E', 'J'),     
         ('F', 'J'),     
         ('H', 'J'),     
         ('I', 'J')]     

for edge in edges:
    G.add_edge(edge[0], edge[1], weight=random.randint(1, 15))
    
# Aplicar el algoritmo de Kruskal
T = nx.minimum_spanning_tree(G)

# Visualizar el árbol de expansión mínima
pos = nx.spring_layout(G)
plt.figure(figsize=(10, 5))

# Dibujar el grafo original
nx.draw(G, pos)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Sobreponer el árbol de expansión mínima
nx.draw(T, pos, with_labels=True, node_color='red', node_size=600, font_size=15, edge_color='salmon', width=3)

plt.title("Kruskal")
plt.show()



