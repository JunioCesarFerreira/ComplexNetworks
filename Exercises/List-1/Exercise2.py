# Exercício 2 de Sistemas Dinâmicos em Redes Complexas
# Objetivo do exercício:
# Implementar uma rotina para calcular a medida de complexidade. Qual o valor da complexidade
# para a rede de energia elétrica dos EUA (Base powergrid).
from numpy  import *
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import math as math

# Abre arquivo 
G= G=nx.read_edgelist("data/powergrid.txt", nodetype=int) # read data file has only two columns

# Transforma o grafo em rede sem direção
G = G.to_undirected()
G.remove_edges_from(nx.selfloop_edges(G))

# Seleciona apenas a maior componente conexa
Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
G = G.subgraph(Gcc[0])

# Cálcula momentos
def nth_moment(g,n):
    degree_np = np.array(list(dict(g.degree).values()))
    return (sum(degree_np**n)/len(g))

# Cálcula coeficiente de complexidade
C = nth_moment(G,2)/nth_moment(G,1)

print("Coeficiente de complexidade = ","%3.2f"%C)