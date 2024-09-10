# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 14:23:05 2023

@author: icalc
"""
from grafoMatriz import Grafo
from TGrafoND import GrafoND

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

# vertice 0 é fonte?
print(f"vertice 0 é fonte? {g.isVSource(0)}")

# vertice 3 é sorvedouro?
print(f"vertice 3 é sorvedouro? {g.isVSink(3)}")

# remove vertice 0
g.removeV(1)
g.showMin()

print(f"Grafo é completo? {g.isComplete()}")
print(f"Grafo complementar: {g.Complementary()}")

#Grafo nao direcionado com peso
nd = GrafoND(4, isWeighted=True)

nd.insereA(0,1,20) # insere aresta 0->1 com peso 20
nd.insereA(0,2,30)
nd.insereA(2,1,21)

nd.show()
nd.showMin()