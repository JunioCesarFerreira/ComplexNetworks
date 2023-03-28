# Exercício 3 Lista 1 de Sistemas Dinâmicos em Redes Complexas
# Objetivo do exercício:
# Implementar uma rotina para calcular a entropia de Shannon e calcular essa medida
# para a base de estradas da Europa (base euroroad)
from numpy  import *
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import math as math

# Abre arquivo 
G= G=nx.read_edgelist("data/euroroad.txt", nodetype=int) # read data file has only two columns

# Transforma o grafo em rede sem direção
G = G.to_undirected()
G.remove_edges_from(nx.selfloop_edges(G))

# Seleciona apenas a maior componente conexa
Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
G = G.subgraph(Gcc[0])

def degree_distribution(G):
    vk = dict(G.degree())
    vk = list(vk.values())  # we get only the degree values
    vk = np.array(vk)
    maxk = np.max(vk)
    mink = np.min(vk)
    kvalues= np.arange(0,maxk+1) # possible values of k
    Pk = np.zeros(maxk+1) # P(k)
    for k in vk:
        Pk[k] = Pk[k] + 1
    Pk = Pk/sum(Pk) # the sum of the elements of P(k) must to be equal to one
    return kvalues,Pk

def shannon_entropy(G):
    k,Pk = degree_distribution(G)
    H = 0
    for p in Pk:
        if(p > 0):
            H = H - p*math.log(p, 2)
    return H

H = shannon_entropy(G)
print("Shannon Entropy = ", "%3.2f"%H)