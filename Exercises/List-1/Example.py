from numpy  import *
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import math as math

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

ks, Pk = degree_distribution(G)

plt.figure(figsize=(8,5))
fig = plt.subplot(1,1,1)
fig.set_xscale('log')
fig.set_yscale('log')
plt.plot(ks,Pk,'bo')
plt.xlabel("k", fontsize=20)
plt.ylabel("P(k)", fontsize=20)
plt.title("Degree distribution", fontsize=20)
#plt.grid(True)
plt.savefig('degree_dist.eps') #save the figure into a file
plt.show()

def momment_of_degree_distribution(G,m):
    k,Pk = degree_distribution(G)
    M = sum((k**m)*Pk)
    return M

k1 = momment_of_degree_distribution(G,1)
print("Grau médio = ", mean(ks))
print("Primeiro momento da distribuição do grau = ", k1)

k2 = momment_of_degree_distribution(G,2)
print("Segundo momento da distribuição do grau = ", k2)

variance = momment_of_degree_distribution(G,2) - momment_of_degree_distribution(G,1)**2
print("Variância do grau = ", variance)

def shannon_entropy(G):
    k,Pk = degree_distribution(G)
    H = 0
    for p in Pk:
        if(p > 0):
            H = H - p*math.log(p, 2)
    return H

H = shannon_entropy(G)
print("Shannon Entropy = ", "%3.4f"%H)

def normalized_shannon_entropy(G):
    k,Pk = degree_distribution(G)
    H = 0
    for p in Pk:
        if(p > 0):
            H = H - p*math.log(p, 2)
    return H/math.log(len(G),2)

H = normalized_shannon_entropy(G)
print("Normalized Shannon Entropy = ", "%3.4f"%H)

fig, ax = plt.subplots(figsize=(8,5))
ax.boxplot(vk, vert = 0)
ax.set_ylabel('Degree')
plt.show()

CC = (nx.transitivity(G)) 
print("Transitivity = ","%3.4f"%CC)

avc = nx.average_clustering(G)
print("Average clustering:", "%3.4f"%avc)

vcc = []
for i in G.nodes():
    vcc.append(nx.clustering(G, i))
vcc= np.array(vcc)
print('Clustering of all nodes:', vcc)

plt.figure()
plt.hist(vcc, bins  = 10, density=True)
plt.title("Distribution of the clustering coefficient", fontsize=20)
plt.ylabel("P(cc)", fontsize=15)
plt.xlabel("Clustering coefficient (cc)", fontsize=15)
#plt.grid(True)
plt.savefig('clustering.eps') #save the figure into a file
plt.show()

#Average clustering for each degree k
ck = list()
ks = list()
for k in np.arange(np.min(vk), np.max(vk)):
    aux = vk == k
    if(len(vcc[aux]) > 0):
        cm = mean(vcc[aux]) #average clustering among all the nodes with degree k
        ck.append(cm)
        ks.append(k)
plt.loglog(ks,ck,'bo')
plt.title("Clustering coefficient according to degree", fontsize=20)
plt.ylabel("cc(k)", fontsize=15)
plt.xlabel("k", fontsize=15)
#plt.grid(True)
plt.savefig('cck.eps')
plt.show()