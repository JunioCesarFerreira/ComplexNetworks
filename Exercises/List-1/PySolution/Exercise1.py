# Exercício 1 Lista 1 de Sistemas Dinâmicos em Redes Complexas
# Objetivo do exercício:
# Para a rede do livro "Os miseráveis" (base lesmis), calcule o terceiro e quarto momento do grau.
from numpy  import *
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

#G= nx.read_edgelist("data/lesmis.txt", nodetype=int, data=(('weight',float),))
# Abre arquivo de rede
G= nx.read_gml("data/lesmis.gml") # Read the network

# Transforma o grafo em rede sem direção
G = G.to_undirected()
G.remove_edges_from(nx.selfloop_edges(G))

# Seleciona apenas a maior componente conexa
Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
G = G.subgraph(Gcc[0])

# Transforma labels em numeros inteiros
G = nx.convert_node_labels_to_integers(G, first_label=0)

# Graus dos vértices
vk = dict(G.degree()).values()
vk = np.array(list(vk))

# Grau médio da rede
md = mean(vk)

# Cálcula momentos
def nth_moment(g,n):
    degree_np = np.array(list(dict(g.degree).values()))
    return (sum(degree_np**n)/len(g))

print('Terceiro momento de k:', "%5.0f"%nth_moment(G,3))
print('Quarto momento de k:  ', "%5.0f"%nth_moment(G,4))
