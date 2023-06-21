import networkx as nx
from igraph import Graph

# Lê o arquivo de arestas do grafo
G = nx.read_edgelist("data/jazz.txt", nodetype=int)

# Converte o grafo para não direcionado
G = G.to_undirected()

# Remove arestas de auto-loop
G.remove_edges_from(nx.selfloop_edges(G))

# Obtém a componente conexa gigante
Gcc = max(nx.connected_components(G), key=len)
G = G.subgraph(Gcc)

# Converte os rótulos dos nós para inteiros começando de 0
mapping = dict(zip(G.nodes(), range(len(G))))
G = nx.relabel_nodes(G, mapping)

# Converte o grafo para o formato esperado pelo python-igraph
g = Graph.Adjacency((nx.to_numpy_array(G) > 0).tolist(), mode="UNDIRECTED")

# Executa o algoritmo de Multilevel para detecção de comunidades
communities = g.community_multilevel()

# Obtém a atribuição de comunidades para cada nó
membership = communities.membership

# Calcula a modularidade
modularity = g.modularity(membership)

print("Modularidade = ", modularity)