## Igor Benites Moura - 10403462
## Rodrigo Machado de Assis Oliveira de Lima - 10401873

from TGrafoComBusca import Grafo

g = Grafo(5)

g.insereA(0,1)
g.insereA(0,2)
g.insereA(1,3)
g.insereA(3,4)


# Busca em profundidade
print("Busca em profundidade")
g.dfs(0)

# Busca em largura
print("\nBusca em largura")
g.bfs(0)