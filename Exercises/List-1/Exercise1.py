from numpy  import *
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Exercício 1 de Sistemas Dinâmicos em Redes Complexas
# Objetivo do exercício:
# Para a rede do livro "Os miseráveis" (base lesmis), calcule o terceiro e querto momento do grau.

#G= nx.read_edgelist("data/lesmis.txt", nodetype=int, data=(('weight',float),))
G= nx.read_gml("data/lesmis.gml") # Read the network
# If the data file has only two columns, use this:
#G= G=nx.read_edgelist("data/powergrid.txt", nodetype=int)


# Transforma o grafo em rede sem direção
G = G.to_undirected()
G.remove_edges_from(nx.selfloop_edges(G))

# Seleciona apenas a maior componente conexa
Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
G = G.subgraph(Gcc[0])

# Transforma labels em numeros inteiros
G = nx.convert_node_labels_to_integers(G, first_label=0)

# Número de vértices e arestas
N = len(G)
M = G.number_of_edges()
print('Number of nodes:', N)
print('Number of edges:', M)

# Graus dos vértices
vk = dict(G.degree()).values()
vk = np.array(list(vk))
print('Degree', vk)

# Grau médio da rede
md = mean(vk)
print('Grau médio: ', md)

# Cálcula momentos
def momment(G,m):
    M = 0
    N = len(G)
    for i in G.nodes:
        M = M + G.degree(i)**m
    M = M/N
    return M

print('Primeiro momento de k:', momment(G,1))
print('Segundo momento de k:', momment(G,2))
print('Terceiro momento de k:', momment(G,3))
print('Quarto momento de k:', momment(G,4))
print('Variância de k:', np.var(vk))
print('Mediana de k:', np.median(vk))

# Exibe a rede
plt.figure(figsize=(12,10))
pos = nx.spring_layout(G)
nx.draw(G, pos, node_color="lightgray", node_size=400, with_labels=True) 
plt.show()