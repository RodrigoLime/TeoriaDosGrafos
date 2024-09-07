# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 14:23:05 2023

@author: icalc
"""
from grafoMatriz import Grafo

g = Grafo(4)
#insere as arestas do grafo
#A={(0,1),(0,2),(2,1),(2,3),(1,3)}
g.insereA(0,1)
g.insereA(0,2)
g.insereA(2,1)
g.insereA(2,3)
g.insereA(1,3)
# mostra o grafo preenchido
g.show()
g.showMin()

# grau de entrada do vertice 3:
print(f"grau de entrada do vertice 3: {g.inDegree(3)}")

# grau de saida do vertice 0:
print(f"grau de saida do vertice 0: {g.outDegree(0)}")
